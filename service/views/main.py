from flask import Blueprint, render_template, jsonify

bp = Blueprint("main", __name__, url_prefix="")


@bp.get("/")
def home() -> str:
    return render_template(
        "index.html",
    )


@bp.get("/ping")
def ping() -> tuple[str, int]:
    return jsonify({"message": "pong"}), 200
