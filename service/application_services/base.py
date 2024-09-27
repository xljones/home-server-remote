from flask import current_app


class BaseService:
    def __init__(self) -> None:
        self.logger = current_app.logger
