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
            self.logger.info(f"[BEFORE] power_button_device  = {self._power_button_device}")
            self._power_button_device.on()
            self.logger.info(f"[AFTER]  power_button_device  = {self._power_button_device}")
        except Exception as exc:
            self.logger.error(f"Failed to power on: {exc}")

    def off(self) -> None:
        try:
            self.logger.info(f"[BEFORE] power_button_device  = {self._power_button_device}")
            self._power_button_device.off()
            self.logger.info(f"[AFTER]  power_button_device  = {self._power_button_device}")
        except Exception as exc:
            self.logger.error(f"Failed to power off: {exc}")
