from flask import Blueprint
from service.views.main import bp as main_bp

VIEW_BLUEPRINTS: list[Blueprint] = [main_bp]
