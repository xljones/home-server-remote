from gpiozero import DigitalOutputDevice
from service.application_services.base import BaseService


class PowerService(BaseService):
    def __init__(
        self,
        power_button_device: DigitalOutputDevice,
    ) -> None:
        super().__init__()
        self._power_button_device = power_button_device

    def on(self) -> None:
        try:
            self._power_button_device.on()
        except Exception as exc:
            self.logger.error(f"Failed to power on: {exc}")

    def off(self) -> None:
        try:
            self._power_button_device.off()
        except Exception as exc:
            self.logger.error(f"Failed to power off: {exc}")
