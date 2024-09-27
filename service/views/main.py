from flask import Blueprint, render_template, jsonify, Response
from service.application_services import get_status_service, StatusService
from datetime import datetime, UTC
import os

bp = Blueprint("main", __name__, url_prefix="")


@bp.get("/")
def home() -> str:
    status_service: StatusService = get_status_service()
    status: dict = status_service.get_status()

    return render_template(
        "index.html",
        server={
            "datetime": datetime.now(tz=UTC),
            "GPIOZERO_PIN_FACTORY": os.environ.get("GPIOZERO_PIN_FACTORY", "not set"),
        },
        status=status,
    )


@bp.get("/ping")
def ping() -> tuple[Response, int]:
    return jsonify({"message": "pong"}), 200
