from gpiozero import CPUTemperature, DigitalInputDevice, DigitalOutputDevice
from datetime import datetime, UTC
from dataclasses import dataclass
from service.application_services.base import BaseService


@dataclass
class HostStatus:
    temperature: float | None
    last_update: datetime = datetime.now(tz=UTC)


@dataclass
class RemoteStatus():
    power: bool | None
    power_button: bool | None
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
            self.host_status = self._get_host_status()
            self.remote_status = self._get_remote_status()
        except Exception as exc:
            self.logger.info(f"Error updating status: {exc}")

        return {
            "host": self.host_status.__dict__,
            "remote": self.remote_status.__dict__,
        }

    def _get_host_status(self) -> HostStatus:
        try:
            host_status = HostStatus(
                temperature=CPUTemperature().temperature
            )
        except Exception as exc:
            self.logger.error(f"Error getting host status: {exc}")
            host_status = HostStatus(temperature=None)
        return host_status

    def _get_remote_status(self) -> RemoteStatus:
        try:
            remote_status = RemoteStatus(
                power=bool(self._power_led_device.value),
                power_button=bool(self._power_button_device.value),
            )
        except Exception as exc:
            self.logger.error(f"Error getting remote status: {exc}")
            remote_status = RemoteStatus(power=None, power_button=None)
        return remote_status
