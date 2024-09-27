from flask import Blueprint
from service.views.main import bp as main_bp
from service.views.power import bp as power_bp

VIEW_BLUEPRINTS: list[Blueprint] = [main_bp, power_bp]
