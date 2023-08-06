from abc import ABC
from typing import Optional
from flask import Flask
from deta import Deta
from colorama import Fore

# SUPERCLASS
class DetaConnect(ABC):

    def __init__(
        self,
        app: Flask = None,
        project_key: Optional[str] = None,
        name: Optional[str] = None,
        type: str = None,
        config_key: str = None
    ):
        # Flask Instance
        self._app = app

        # Deta Project Key
        self._project_key = project_key or (app and app.config.get("DETA_PROJECT_KEY"))

        # Name of Drive/Base. Retrieve it from the app or enter it manually.
        self._name = name or (app and app.config.get(config_key))

        # Type of connection: Base or Drive
        self._type = type

        if not self._project_key:
            if self._app:
                self._app.logger.error(f"[Deta-Flask]: No DetaSpace Project Key provided for Deta connection")
            raise ValueError(f"[Deta-Flask]: No DetaSpace Project Key provided for Deta connection")

        if not self._name:
            if self._app:
                self._app.logger.error(f"[Deta-Flask]:No {self._type} Name provided for Deta connection")
            raise ValueError(f"[Deta-Flask]: No {self._type} Name provided for Deta connection")

        if not self._type:
            raise ValueError(f"[Deta-Flask]: No {self._type} name provided for Deta connection")

    def connect(self):
        """ DetaSpace connection manager """
        try:
            # DetaBase
            if self._type == "Base":
                deta = Deta(self._project_key)
                base = deta.Base(self._name)
                return base
            
            # DetaDrive
            elif self._type == "Drive":
                deta = Deta(self._project_key)
                drive = deta.Drive(self._name)
                return drive

        except Exception as e:
            if self._app:
                self._app.logger.error(
                    Fore.RED + f"Error connecting to {self._type} in Flask-Deta => deta.{self._type}(): {e}" + Fore.RESET
                )
            setattr(self, self._type, None)
            return None
