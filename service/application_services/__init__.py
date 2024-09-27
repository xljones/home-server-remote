from service.application_services.status_service import StatusService
from service.application_services.power_service import PowerService

def get_status_service() -> StatusService:
    return StatusService()

def get_power_service() -> PowerService:
    return PowerService()
