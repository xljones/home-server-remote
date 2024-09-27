import os

import pytest

from service.app import HomeServerRemote


def test_app_errors_no_config() -> None:
    with pytest.raises(
        FileNotFoundError,
        match="Configuration file .*/no_file.py not found",
    ):
        os.environ["FLASK_ENV"] = "no_file"
        _ = HomeServerRemote()
