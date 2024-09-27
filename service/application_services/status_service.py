from gpiozero import DigitalInputDevice
from datetime import datetime, UTC
from dataclasses import dataclass
from service.application_services import BaseService, BaseInputCapture


POWER_LED_PIN = 17
POWER_BUTTON_PIN = 27
RESET_BUTTON_PIN = 22
GND_PIN = 6


@dataclass
class CPUStatus(BaseInputCapture):
    temperature: float | None = None
    last_update: datetime = datetime.now(tz=UTC)

    def __init__(self) -> None:
        super().__init__()

    def update(self) -> None:
        # self.temperature = CPUTemperature().temperature
        self.temperature = 42.0
        self.last_update = datetime.now(tz=UTC)
        self.logger.info(f"Updated CPU temperature: {self.temperature}")


@dataclass
class RemoteComputerStatus(BaseInputCapture):
    power: bool | None = None
    last_update: datetime = datetime.now(tz=UTC)

    def __init__(self) -> None:
        super().__init__()

    def update(self) -> None:
        try:
            # power_id: DigitalInputDevice = DigitalInputDevice(POWER_LED_PIN)
            # self.power = bool(power_id.value)
            # self.logger.info("Power value: %s", power_id.value)
            self.power = True
            self.last_update = datetime.now(tz=UTC)
            self.logger.info(f"Updated power status: {self.power}")
        except Exception as exc:
            self.logger.info(f"Error updating power status: {exc}")


class StatusService(BaseService):
    def __init__(self) -> None:
        super().__init__()
        self.cpu: CPUStatus = CPUStatus()
        self.rcs: RemoteComputerStatus = RemoteComputerStatus()

    def get_status(self) -> dict:
        try:
            self.cpu.update()
            self.rcs.update()
        except Exception as exc:
            self.logger.info(f"Error updating status: {exc}")

        return {
            "cpu": self.cpu.__dict__,
            "rcs": self.rcs.__dict__,
        }
