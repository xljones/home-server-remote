from flask import Blueprint

from service.api.ip import bp as ip_bp
from service.api.services import bp as services_bp
from service.views.main import bp as main_bp

VIEW_BLUEPRINTS: list[Blueprint] = [ip_bp, services_bp, main_bp]
