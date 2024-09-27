from gpiozero import DigitalOutputDevice
from service.application_services.base import BaseService
from service.const import POWER_BUTTON_PIN


class PowerService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def on(self) -> None:
        try:
            dod = DigitalOutputDevice(POWER_BUTTON_PIN)
            dod.on()
        except Exception as exc:
            self.logger.error(f"Failed to power on: {exc}")

    def off(self) -> None:
        try:
            dod = DigitalOutputDevice(POWER_BUTTON_PIN)
            dod.off()
        except Exception as exc:
            self.logger.error(f"Failed to power off: {exc}")
