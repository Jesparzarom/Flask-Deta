import io
from abc import ABC
from typing import Optional

from flask import Flask
from deta import Deta


class DetaTemplate(ABC):
    def __init__(
        self,
        app: Flask = None,
        project_key: Optional[str] = None,
        name: Optional[str] = None,
    ):
        self.instance = self.__get_deta_instance__()
        self.config = self.__get_config_name__()
        self.type = self.__get_type_name__()

        self.app = app

        self.project_key = project_key or (app and app.config.get("DETA_PROJECT_KEY"))

        self.name = name or (app and app.config.get(self.config))

        if not self.project_key:
            raise ValueError(f"No project key provided for {self.type}")

        if not self.name:
            raise ValueError(f"No {self.type.lower()} name provided for {self.type}")

        try:
            self.deta = Deta(self.project_key)
            setattr(
                self,
                self.type.upper(),
                self.instance(self.name),
            )
        except Exception as e:
            if self.app:
                self.app.logger.error(
                    f"Error connecting to {self.type.lower()} in Flask-Deta => deta.{self.type}(): {e}"
                )
            setattr(self, self.type.upper(), None)

    @classmethod
    def __get_config_name__(cls):
        pass

    @classmethod
    def __get_type_name__(cls):
        pass

    @classmethod
    def __get_deta_instance__(cls):
        pass
