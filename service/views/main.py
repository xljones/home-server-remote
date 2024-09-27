from flask import Blueprint, render_template

bp = Blueprint("main", __name__, url_prefix="")


@bp.get("/")
def home() -> str:
    return render_template(
        "index.html",
    )
