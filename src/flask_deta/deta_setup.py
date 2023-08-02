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
        self.__instance__ = self.__get_deta_instance__()
        self.__config__ = self.__get_config_name__()
        self.__type__ = self.__get_type_name__()

        self.__app__ = app

        self.__project_key__ = project_key or (app and app.config.get("DETA_PROJECT_KEY"))

        self.__name = name or (app and app.config.get(self.__config__))

        if not self.__project_key__:
            raise ValueError(f"No project key provided for {self.__type__}")

        if not self.__name:
            raise ValueError(f"No {self.__type__.lower()} name provided for {self.__type__}")

        try:
            self.__deta__ = Deta(self.__project_key__)
            setattr(
                self,
                self.__type__.upper(),
                self.__instance__(self.__name),
            )
        except Exception as e:
            if self.__app__:
                self.__app__.logger.error(
                    f"Error connecting to {self.__type__.lower()} in Flask-Deta => deta.{self.__type__}(): {e}"
                )
            setattr(self, self.__type__.upper(), None)

    @classmethod
    def __get_config_name__(cls):
        pass

    @classmethod
    def __get_type_name__(cls):
        pass

    @classmethod
    def __get_deta_instance__(cls):
        pass
