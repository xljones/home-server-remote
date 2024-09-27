from flask.testing import FlaskClient


def test_main(app: FlaskClient, captured_templates: list) -> None:
    resp = app.get("/")

    assert resp.status_code == 200
    assert len(captured_templates) == 1

    template, context = captured_templates[0]
    assert template.name == "index.html"
    assert context == {}