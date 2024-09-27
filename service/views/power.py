from flask import Blueprint, redirect
from service.application_services import (
    get_power_service,
    PowerService,
)

bp = Blueprint("power", __name__, url_prefix="/power")


@bp.get("/on")
def on() -> str:
    ps: PowerService = get_power_service()
    ps.on()

    return redirect("/")


@bp.get("/off")
def off() -> str:
    ps: PowerService = get_power_service()
    ps.off()

    return redirect("/")
