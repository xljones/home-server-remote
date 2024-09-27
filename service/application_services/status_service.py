from gpiozero import CPUTemperature, DigitalInputDevice, DigitalOutputDevice
from datetime import datetime, UTC
from dataclasses import dataclass
from service.application_services.base import BaseService


@dataclass
class HostStatus:
    temperature: float
    last_update: datetime = datetime.now(tz=UTC)


@dataclass
class RemoteStatus():
    power: bool
    power_button: bool
    last_update: datetime = datetime.now(tz=UTC)


class StatusService(BaseService):
    host_status: HostStatus
    remote_status: RemoteStatus

    def __init__(
        self,
        power_led_device: DigitalInputDevice,
        power_button_device: DigitalOutputDevice,
    ) -> None:
        super().__init__()
        self._power_led_device = power_led_device
        self._power_button_device = power_button_device

    def get_status(self) -> dict:
        try:
            self.logger.info(f"power_led_device  = {self._power_led_device}")
            self.logger.info(f"power_button_device  = {self._power_button_device}")
            self.host_status = HostStatus(
                temperature=CPUTemperature().temperature
            )
            self.remote_status = RemoteStatus(
                power=bool(self._power_led_device.value),
                power_button=bool(self._power_button_device.value),
            )
        except Exception as exc:
            self.logger.info(f"Error updating status: {exc}")

        return {
            "host": self.host_status.__dict__,
            "remote": self.remote_status.__dict__,
        }
