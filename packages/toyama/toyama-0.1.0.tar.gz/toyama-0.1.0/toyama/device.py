from dataclasses import dataclass
from enum import Enum


class DeviceType(str, Enum):
    MASTER = "master"
    FAN = "dimmer"
    SWITCH = "onoff"

@dataclass
class Device:
    """Toyama device."""

    id: int
    button_id: int
    name: str
    type: DeviceType
    state: int
    gateway: str
    gateway_id: int
    zone: str
    zone_id: int
    room: str
    room_id: int
    board: str
    board_id: int

    def __repr__(self) -> str:
        return f"Device(room='{self.room}' name='{self.name}' type={DeviceType(self.type).name})"

    @property
    def nice_name(self):
        return f"{self.room} {self.name}"

    @property
    def unique_id(self) -> str:
        unique_id = f"{self.room}_{self.board_id}_{self.button_id}"
        return unique_id.replace(" ","_").replace("-","_")
    
    @property
    def is_device(self) -> bool:
        return self.type != DeviceType.MASTER
    
    @property
    def is_master(self) -> bool:
        return self.type == DeviceType.MASTER
    
    @property
    def is_fan(self) -> bool:
        return self.type == DeviceType.FAN
    
    @property
    def is_switch(self) -> bool:
        return self.type == DeviceType.SWITCH