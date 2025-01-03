
# Toyama API Wrapper

`toyama` is a Python library that provides an API wrapper for controlling Toyama switches. It enables discovering, monitoring, and interacting with Toyama smart devices via Zeroconf and HTTP requests. This library is designed to be used as part of a custom integration for Home Assistant.

## Features

- **Gateway Discovery**: Automatically discovers the gateway using Zeroconf.
- **Device Interaction**: Send commands to control device states and request device statuses.
- **Callback Integration**: Allows handling device updates through user-defined callback functions.
- **Asynchronous**: Built with `asyncio` for efficient, non-blocking operations.

## Installation

To install the library, you can use pip:

```bash
pip install toyama
```

Or you can install it directly from the repository:

```bash
pip install git+https://github.com/prasannareddych/toyama.git
```

## Usage

### Discovering a Gateway

```python
from toyama.gateway import GatewayDiscovery

async def discover_gateway():
    gateway_data = await GatewayDiscovery.discover(timeout=10.0)
    print(f"Discovered gateway: {gateway_data}")
```

### Controlling Devices

```python
from toyama.gateway import Gateway
from toyama.device import Device

async def control_device():
    gateway = Gateway(callback_func=handle_device_update)
    await gateway.initialize()

    device = Device(board_id="board_id", button_id="button_id")
    await gateway.update_device_state(device, new_state=1)

async def handle_device_update(update):
    print(f"Device update: {update}")
```

