import asyncio
import json
import socket
from typing import Any, Callable, Dict, Optional

import aiohttp
from loguru import logger
from zeroconf import ServiceBrowser, ServiceInfo, ServiceListener, Zeroconf

from .device import Device


class GatewayDiscoveryError(Exception):
    """Gateway Discovery Error"""


class GatewayListener(ServiceListener):
    def __init__(self) -> None:
        self.data: Optional[Dict[str, Any]] = None

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        logger.debug(f"Service removed: {name}")

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        logger.debug(f"Service added: {name}")
        info: Optional[ServiceInfo] = zc.get_service_info(type_, name)
        if info:
            self.data = {
                "name": info.name,
                "address": ".".join(map(str, info.addresses[0])),
                "port": info.port,
                "properties": {
                    k.decode().lower(): (v.decode() if v is not None else None)
                    for k, v in info.properties.items()
                },
            }
            logger.debug(f"Service info: {self.data}")


class GatewayDiscovery:
    @classmethod
    async def discover(cls, timeout: float = 10.0) -> Dict[str, Any]:
        """
        Discovers services using Zeroconf.

        Args:
            timeout (float): Maximum time (in seconds) to wait for a service.

        Returns:
            Dict[str, Any]: Discovered service information.

        Raises:
            GatewayDiscoveryError: If no service is found within the timeout or an error occurs.
        """
        zeroconf: Zeroconf = Zeroconf()
        listener: GatewayListener = GatewayListener()
        service_type: str = "_toyama._tcp.local."
        browser: ServiceBrowser = ServiceBrowser(zeroconf, service_type, listener)

        try:
            logger.debug("Starting mDNS discovery with Zeroconf")
            start_time = asyncio.get_running_loop().time()

            while True:
                if listener.data:
                    return listener.data

                elapsed_time = asyncio.get_running_loop().time() - start_time
                if elapsed_time >= timeout:
                    raise GatewayDiscoveryError("No services found within the timeout")

                await asyncio.sleep(0.1)  # Polling interval

        except Exception as e:
            logger.error(f"Error during Zeroconf discovery: {e}")
            raise GatewayDiscoveryError(f"Unexpected error: {e}")

        finally:
            browser.cancel()
            zeroconf.close()


class Gateway:
    """Gateway class"""

    gateway_ip: Optional[str] = None

    def __init__(self, callback_func: Optional[Callable[[Dict[str, Any]], Any]] = None) -> None:
        """
        Initialize the Gateway instance.

        Args:
            callback_func (Optional[Callable[[Dict[str, Any]], Any]]): 
                An optional callback function for handling device updates. 
                The function should accept a single parameter of type Dict[str, Any].
        """

        self.callback_func = callback_func

    async def discover_gateway_loop(self) -> None:
        """
        Continuously discovers and monitors the gateway IP.

        If the gateway IP is not found, it attempts to discover one.
        If the gateway IP is found, it periodically checks its reachability.
        """
        while True:
            if not self.gateway_ip:
                try:
                    data = await GatewayDiscovery.discover()
                    self.gateway_ip = data.get("address")
                    logger.debug(f"Found gateway ip: {self.gateway_ip}")
                except Exception:
                    self.gateway_ip = None
            else:
                try:
                    async with aiohttp.ClientSession(timeout=3) as session:
                        async with session.get(f"http://{self.gateway_ip}:8900") as resp:
                            if (await resp.text()).strip() != '0':
                                self.gateway_ip = None
                except:
                    logger.debug(f"Lost gateway ip: {self.gateway_ip}")
                    self.gateway_ip = None
            await asyncio.sleep(10)

    async def initialize(self) -> None:
        """
        Initializes the gateway by starting the discovery loop and, if a callback function is provided,
        creates a task to listen for device updates.
        """
        self.loop = asyncio.get_running_loop()
        self.loop.create_task(self.discover_gateway_loop())
        if self.callback_func:
            self.loop.create_task(self.listen_device_updates())
            await self.request_all_devices_status()

    async def send_request(self, payload: Dict[str, Any]) -> bool:
        """
        Sends an HTTP POST request to the gateway.

        Args:
            payload (Dict[str, Any]): The payload to be sent.

        Return:
            bool: True if the request succeeds, otherwise False.
        """
        if not self.gateway_ip:
            return False
        async with aiohttp.ClientSession() as session:
            try:
                resp = await session.post(f"http://{self.gateway_ip}:8900/operate", json=payload)
                result = await resp.text()
                return result == 'ok'
            except:
                self.gateway_ip = None
                return False

    async def update_device_state(self, device: Device, new_state: int) -> bool:
        """
        Updates the state of a given device.
        Args:
            device (Device): The device to update.
            new_state (int): The new state to set.

        Returns:
            bool: True if the update succeeds, otherwise False.
        """

        payload: Dict[str, Any] = {
            "type": "swcmd",
            "data": [
                {
                    "addr": [device.board_id],
                    "nodedata": {
                        "cmdtype": "operate",
                        "subid": int(device.button_id)+16,
                        "cmd": new_state
                    }
                }
            ]
        }
        try:
            logger.debug(f"updating: {device.nice_name}, {new_state}")
            return await self.send_request(payload)
        except Exception as e:
            logger.error(f"Failed to update the state for {device}: {e}")
        return False

    async def request_all_devices_status(self) -> bool:
        """
        Requests the status of all devices.

        Returns:
            bool: True if the request succeeds, otherwise False.
        """
        payload: Dict[str, Any] = {
            "type": "swcmd",
            "data": [
                {
                    "addr": [
                        "ffffffffffff"
                    ],
                    "nodedata": {
                        "cmdtype": "getstatus"
                    }
                }
            ]
        }
        try:
            return await self.send_request(payload)
        except Exception as e:
            logger.error(f"Failed to request all device status: {e}")
            return False

    async def listen_device_updates(self) -> None:
        """
        Listens for updates from devices and calls the callback function if provided.
        Rebinds the socket if the network changes.
        """
        def create_socket() -> socket.socket:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(('0.0.0.0', 56000))
            sock.setblocking(False)
            return sock

        sock = create_socket()
        logger.info("Listening for device updates on port 56000...")

        try:
            while True:
                try:
                    data, _ = await asyncio.wait_for(self.loop.sock_recvfrom(sock, 1024), timeout=5)
                    update = json.loads(data.decode('utf-8'))
                    logger.debug(f"Device update: {update}")
                    if self.callback_func:
                        await self.callback_func(update)
                except asyncio.TimeoutError:
                    pass
                except OSError as e:
                    # Handle potential socket errors due to network changes
                    logger.warning(f"Socket error detected: {e}. Rebinding the socket.")
                    sock.close()
                    sock = create_socket()
                except Exception as e:
                    logger.error(f"Unexpected error: {e}")
                await asyncio.sleep(0.1)
        finally:
            sock.close()
            logger.info("Socket closed.")
