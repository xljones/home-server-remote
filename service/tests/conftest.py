from typing import Any, Iterator

import pytest
from flask import template_rendered
from flask.testing import FlaskClient

from service.app import flask_app, hsr


@pytest.fixture
def app() -> Iterator[FlaskClient]:
    """Provide a testing Flask application for view testing."""
    with hsr.flask_app.test_client() as client:
        yield client


@pytest.fixture
def captured_templates() -> Iterator[list]:
    recorded = []

    def record(sender: Any, template: Any, context: Any, **extra: Any) -> None:
        recorded.append((template, context))

    template_rendered.connect(record, flask_app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, flask_app)
