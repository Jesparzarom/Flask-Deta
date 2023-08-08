from abc import ABC
from typing import Optional
from flask import Flask, abort
from deta import Deta


class DetaConnect(ABC):
    """
    Abstract base class for connecting to DetaSpace.

    This class provides a foundation for connecting to DetaSpace using DetaBase or DetaDrive.
    It handles the initialization of connection parameters and abstracts the connection logic.

    ### Args:
        * `app (Flask, optional)`: The Flask app instance. Defaults to None.
        * `project_key (str, optional)`: The Deta project key. Defaults to None.
        * `type (str, optional)`: The type of connection ("Base" or "Drive"). Defaults to None.

    ### Attributes:
        * `_app (Flask)`: The Flask app instance.
        * `_project_key (str)`: The Deta project key.
        * `_type (str)`: The type of connection ("Base" or "Drive").
        * `_name (str)`: The name of DetaBase or DetaDrive.
    """

    def __init__(
        self,
        app: Flask = None,
        project_key: Optional[str] = None,
        name: Optional[str] = None,
        type: str = None,
        config_key: str = None,
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
                self._app.logger.error(
                    f"[Deta-Flask]: No DetaSpace Project Key provided for Deta connection"
                )
            raise ValueError(
                f"[Deta-Flask]: No DetaSpace Project Key provided for Deta connection"
            )

        if not self._name:
            if self._app:
                self._app.logger.error(
                    f"[Deta-Flask]:No {self._type} Name provided for Deta connection"
                )
            raise ValueError(
                f"[Deta-Flask]: No {self._type} Name provided for Deta connection"
            )

        if not self._type:
            raise ValueError(
                f"[Deta-Flask]: No {self._type} name provided for Deta connection"
            )

    def _connect(self):
        """DetaSpace connection manager"""
        try:
            deta = Deta(self._project_key)

            if self._type == "Base":
                connection = deta.Base(self._name)
            elif self._type == "Drive":
                connection = deta.Drive(self._name)
            else:
                return None

            setattr(self, self._type, connection)
            return connection

        except Exception as e:
            error_message = f"Error connecting to {self._type} in Flask-Deta => deta.{self._type}(): {e}"
            if self._app:
                self._app.logger.error(error_message)

            setattr(self, self._type, None)
            return None
