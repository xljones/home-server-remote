from flask import Blueprint, render_template, jsonify, Response
from service.application_services.status_service import StatusService

bp = Blueprint("main", __name__, url_prefix="")


@bp.get("/")
def home() -> str:
    status_service = StatusService()
    status: dict = status_service.get_status()

    return render_template(
        "index.html",
        status=status,
    )


@bp.get("/ping")
def ping() -> tuple[Response, int]:
    return jsonify({"message": "pong"}), 200
