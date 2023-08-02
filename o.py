import io
from abc import ABC, abstractmethod
from typing import Optional
from deta import Deta


class DetaTemplate(ABC):
    def __init__(self, app=None, project_key: Optional[str] = None, name: Optional[str] = None):
        self.app = app
        self.project_key = project_key or (app and app.config.get(self.get_config_name()))
        self.name = name or (app and app.config.get(self.get_config_name()))

        if not self.project_key:
            raise ValueError(f"No project key provided for {self.get_type_name()}")

        if not self.name:
            raise ValueError(f"No {self.get_name_type().lower()} name provided for {self.get_type_name()}")

        try:
            self.deta = Deta(self.project_key)
            setattr(self, self.get_type_name().upper(), self.get_deta_instance()(self.name))
        except Exception as e:
            if self.app:
                self.app.logger.error(f"Error connecting to {self.get_name_type().lower()} in {self.get_type_name()}: {e}")
            setattr(self, self.get_type_name().upper(), None)

    @abstractmethod
    def __get_config_name(self):
        pass

    @abstractmethod
    def __get_name_type(self):
        pass

    @abstractmethod
    def __get_deta_instance(self):
        pass


class DetaBase(DetaTemplate):
    def __get_config_name(self):
        return "DETA_DB_NAME"

    def __get_name_type(self):
        return "Base"

    def __get_deta_instance(self):
        return Deta().Base


class DetaDrive(DetaTemplate):
    def __get_config_name(self):
        return "DETA_DRIVE_NAME"

    def __get_name_type(self):
        return "Drive"

    def __get_deta_instance(self):
        return Deta().Drive
