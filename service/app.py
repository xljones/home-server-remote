"""Setup the Flask application and all the required infrastructure."""

import logging
import os

from flask import Blueprint, Flask

from service.views import VIEW_BLUEPRINTS


class HomeServerRemote:
    def __init__(
        self,
        template_folder: str = "templates",
        static_folder: str = "static",
    ) -> None:
        """Setup all the relevant parts of a Flask application."""
        self.flask_app = Flask(
            __name__,
            template_folder=template_folder,
            static_folder=static_folder,
        )
        self.logger = self._setup_logger()
        self.env = os.environ["FLASK_ENV"]
        config_file = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                os.pardir,
                "config",
                "flask",
                f"{self.env}.py",
            )
        )
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Configuration file {config_file} not found.")
        self.logger.info(f"Loading configuration from {config_file}")
        self.flask_app.config.from_pyfile(str(config_file))

    def _setup_logger(self) -> logging.Logger:
        """Create a logger for the application."""
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.INFO)
        gunicorn_logger = logging.getLogger("gunicorn.error")
        self.flask_app.logger.handlers = gunicorn_logger.handlers
        self.flask_app.logger.setLevel(gunicorn_logger.level)

        return logger

    def register_blueprints(self, blueprints: list[Blueprint]) -> None:
        """Register Blueprints for a Flask application.

        Args:
            blueprints: List of Blueprint objects to register.
        """
        for bp in blueprints:
            self.flask_app.register_blueprint(bp)


hsr = HomeServerRemote()
hsr.register_blueprints(VIEW_BLUEPRINTS)

# Store a reference to the Flask application so gunicorn can access it.
flask_app = hsr.flask_app
