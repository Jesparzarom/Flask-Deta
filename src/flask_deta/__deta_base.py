from typing import Optional, Union
from datetime import datetime
from flask import Flask, abort
from .__deta_setup import DetaConnect


# SUBCLASS
class DetaBase(DetaConnect):

    """
    ## Class DetaBase
    Represents a DetaSpace Base that allows you to store and manage data.

    ### Attributes:
        * `app (Flask)`: Flash app to contextualize class methods and attributes.

        * `project_key  (str)`: The DetaSpace Project key used for authentication.
            The argument can be passed manually, if the argument is empty, an attempt
            is made to find it if it was defined as `app.config['DETA_PROJECT_KEY] = "myKey"`.

        * `name (str)`: The name of your DetaSpace Base.The argument can be passed manually,
                      if the argument is empty, an attempt is made to find it if it was defined
                      as `app.config['Base_NAME'] = "coolBase"`.

    ### Methods:
        *   `get_all()`:Fetches all data stored in the Deta Base.

        *   `get(filename: str)`: Fetches a specific file from the Deta Base.

        *   `put(filename: str, data: dict[str|bytes|io.TextIOBase|io.BufferedIOBase|io.RawIOBase] = None, file_path: str = None, type: str = None)`:
            Saves a file in the Deta Cloud Base.

        *   `put_all(items: list[dict], expire_in: int = None, expire_at: int | float | datetime = None,)`:
            Store a list whit your dict[data] in the Deta database.

        *   `update(self, key: str, updates: dict[dict, list, tuple, int, str, bool])`: Saves a file in the DetaSpace database.

        *   `remove(name: str)`: Removes a file from the Deta Base.
    """

    def __init__(
        self,
        app: Flask = None,
        project_key: str | None = None,
        name: str | None = None,
    ):
        super().__init__(
            app, project_key=project_key, name=name, type="Base", config_key="BASE_NAME"
        )

        # Connection:
        self._BASE = self._connect()

    def put(
        self,
        data: dict[Union[dict, list, tuple, int, str, bool]],
        key: Optional[str] = None,
        expire_in: Optional[int] = None,
        expire_at: Optional[Union[int, float, datetime]] = None,
    ):
        """
        Store data in the Deta database.

        ### Args:
            *   `data`: Data to be stored. Can be a dictionary,
                a list, a string, an integer, or a boolean.
                Overrides an item if key already exists.

            *   `key`: (Optional) The key associated with the data.
                Could be provided as function argument or a field in the data dict

            *   `expire_in`: (Optional) Time in seconds until the data expires.

            *   `expire_at`: (Optional) Unix timestamp or datetime when the data expires.

        ### Returns:
            The result of the storage operation or None if the database
            is not available or an error occurs.

        ### Example:
        ```
        >>> app = Flask(__name__)
        >>> app.config['DETA_PROJECT_KEY'] = 'yourKey'
        >>> app.config['BASE_NAME'] = 'nameOfDatabase'
        >>>
        >>> db = DetaBase(app)
        >>>
        >>> data = {"name" : John, "age" : 25}
        >>> db.put(data, key="custom_key", expire_in=300)
        ```
        """

        if not self._BASE:
            return None

        try:
            crud = self._BASE.put(
                data=data, key=key, expire_in=expire_in, expire_at=expire_at
            )
            
            if crud:
                return crud
            
            else:
                abort(404, f"Error creating record")

        except Exception as e:
            self._app.logger.error(f"Error creating record: {e}")
            return None

    def put_all(
        self,
        items: list[dict],
        expire_in: Optional[int] = None,
        expire_at: Optional[int | float | datetime] = None,
    ):
        """
        Store a list whit your data in the Deta database.

        ### Args:
            *   `items`: list whit items to be stored. Can be a list whit dictionaries,
                lists, strings, integers, or booleans.

            *   `expire_in`: (Optional) Time in seconds until the data expires.

            *   `expire_at`: (Optional) Unix timestamp or datetime when the data expires.

        ### Returns:
            The result of the storage operation or None if the database
            is not available or an error occurs.

        ### Examples:
            >>> app = Flask(__name__)
            >>> app.config['DETA_PROJECT_KEY'] = 'yourKey'
            >>> app.config['BASE_NAME'] = 'nameOfDatabase'
            >>>
            >>> db = DetaBase(app)
            >>>
            >>> records = [
            ...     {"name" : "John", "age" : 30},
            ...     {"name" : "Tim", "age" : 45},
            ...     {"name" : "Guido", "age" : 52},
            ... ]
            >>>
            >>> db.put_all(records)
        """

        if not self._BASE:
            return None

        try:
            crud = self._BASE.put_many(items=items, expire_in=expire_in, expire_at=expire_at)
            if crud:
                return crud
            else:
                abort(404, "Error creating multiple records")

        except Exception as e:
            self._app.logger.error(f"Error creating multiple records: {e}")
            return None

    def get(self, key: str) -> Optional[dict]:
        """
        Retrieves data from the Deta Base database using the provided key.

        ### Args:
            *   key (str): The key associated with the data to be retrieved. Equivalent to id or a primary key

        ### Returns:
            *   Any | None: The retrieved data or None if the database is not available or an error occurs.

        ### Example:
            >>> app = Flask(__name__)
            >>> app.config['DETA_PROJECT_KEY'] = 'yourKey'
            >>> app.config['BASE_NAME'] = 'nameOfDatabase'
            >>>
            >>> db = DetaBase(app)
            >>>
            >>> key = "1122334455"
            >>> result = db.get(key)
        """
        if not self._BASE:
            return None
        try:
            record = self._BASE.get(key)
            if record:
                return record
            else:
                abort(404, f"{key} record not found")

        except Exception as e:
            self._app.logger.error(f"Error getting record: {e}")
            return None

    def get_all(self) -> Optional[list[dict]]:
        """
        Retrieves all data from the Deta database.

        ### Returns:
            list | None: A list containing all the data from the database
            or None if the database is not available or an error occurs.

        ### Example:
            >>> app = Flask(__name__)
            >>> app.config['DETA_PROJECT_KEY'] = 'yourKey'
            >>> app.config['BASE_NAME'] = 'nameOfDatabase'
            >>>
            >>> db = DetaBase(app)
            >>>
            >>> all_data = db.get_all()
        """

        if not self._BASE:
            return None
        try:
            fetch_records = self._BASE.fetch(desc=True).items
            if fetch_records:
                return fetch_records
            else: 
                abort(404, f"Error fetching records")
        except Exception as e:
            self._app.logger.error(f"Error fetching records: {e}")
            return None

    def update(
        self,
        key: str,
        updates: dict[Union[dict, list, tuple, int, str, bool]],
        expire_in: Optional[int] = None,
        expire_at: Optional[Union[int, float, datetime]] = None,
    ):
        """
        update and updates data in the Deta Base database using the provided key.

        ### Args:
            *   `key (str)`: The key associated with the data to be updated. Equivalent to id or a primary key
            *   `data (dict[dict | list | str | int | bool])`: The updated data.

        ### Returns:
            Any | None: The result of the database update operation or None if the database is not available or an error occurs.

        ### Example:
            >>> app = Flask(__name__)
            >>> app.config['DETA_PROJECT_KEY'] = 'yourKey'
            >>> app.config['BASE_NAME'] = 'nameOfDatabase'
            >>>
            >>> db = DetaBase(app)
            >>>
            >>> id_key = "1122334455"
            >>> update = {"name": "John", "age": 30}
            >>> expire_in = 60 # seconds
            >>> db.update(key=id_key, updates=update, expire_in=expire_in)
        """
        if not self._BASE:
            return None
        try:
            crud = self._BASE.update(
                updates=updates, key=key, expire_in=expire_in, expire_at=expire_at
            )

            if crud:
                return crud
            else:
                abort(404, f"Error updating record {crud}" )

        except Exception as e:
            self._app.logger.error(f"Error updating record: {e}")
            return None

    def delete(self, key: str) -> Optional[bool]:
        """
        Deletes data from the Deta BASE database using the provided key.

        ### Args:
            *   key (str): The key associated with the data to be deleted. Equivalent to id or a primary key

        ### Returns:
            Any | None: The result of the database delete operation or None if the database is not available or an error occurs.

        ### Example:
            >>> app = Flask(__name__)
            >>> app.config['DETA_PROJECT_KEY'] = 'yourKey'
            >>> app.config['BASE_NAME'] = 'nameOfDatabase'
            >>>
            >>> db = DetaBase(app)
            >>>
            >>> key = "1122334455"
            >>> db.delete(key)
        """
        if not self._BASE:
            return None
        try:
            crud = self._BASE.delete(key)
            if crud:
                return crud
            else:
                abort(404, f"Error deleting record: {key}")
        except Exception as e:
            self._app.logger.error(f"Error deleting record: {e}")
            return None
