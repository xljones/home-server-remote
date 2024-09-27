from service.application_services.status_service import StatusService
from service.application_services.power_service import PowerService
from service.const import POWER_LED_PIN, POWER_BUTTON_PIN
from gpiozero import DigitalInputDevice, DigitalOutputDevice


POWER_BUTTON_DEVICE = DigitalOutputDevice(POWER_BUTTON_PIN)
POWER_LED_DEVICE = DigitalInputDevice(POWER_LED_PIN)


def get_status_service(
    power_led_device: DigitalInputDevice | None = None,
    power_button_device: DigitalOutputDevice | None = None,
) -> StatusService:
    return StatusService(
        power_led_device=power_led_device or POWER_LED_DEVICE,
        power_button_device=power_button_device or POWER_BUTTON_DEVICE,
    )

def get_power_service(
    power_button_device: DigitalOutputDevice | None = None,
) -> PowerService:
    return PowerService(
        power_button_device=power_button_device or POWER_BUTTON_DEVICE,
    )
