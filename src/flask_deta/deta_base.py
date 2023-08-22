from datetime import datetime
from typing import Optional, Union

from flask import current_app
from .validator import verify_setups


class DetaBase:
    """## Class DetaBase
    Represents a DetaSpace Base that allows you to store and manage data.

    ### Attributes:
        * `app (Flask)`: Flash app to contextualize class methods and attributes.

        * `project_key  (str)`: The DetaSpace Project key used for authentication.
            The argument can be passed manually, if the argument is empty, an attempt
            is made to find it if it was defined as 
            
            ```python
            app.config['DETA_PROJECT_KEY] = "myKey123"
            ```

        * `name (str)`: The name of your DetaSpace Base.The argument can be passed manually,
            if the argument is empty, an attempt is made to find it if it was defined as

            ```python
            app.config['BASE_NAME'] = "data"
            ```

        * `host (str)`: Optional host URL for API requests. This URL specifies the Deta server where
                    the requests will be sent. The default Deta host URL will be used.
                    `host = "https://database.deta.sh"` -> app.config['BASE_HOST']

    ### Methods:
        *  `init_app(app: Flask)`: Initializes the extension and binds it to a Flask application instance.

        *   `get_all(limit: int = 1000)`:Fetches all data stored in the Deta Base. By default it returns 1000 or 1MB.

        *   `get(key: str)`: Fetches a specific file from the Deta Base.

        *   `put(data: dict[str|bytes|io.TextIOBase|io.BufferedIOBase|io.RawIOBase] = None, key: str = None, expire_in: int = None, expire_at: int|float|datetime = None)`:
            Saves a file in the Deta Cloud Base.

        *   `put_all(items: list[dict], expire_in: int = None, expire_at: int | float | datetime = None,)`:
            Store a list whit your dict[data] in the Deta database.

        *   `update(key: str, updates: dict[dict, list, tuple, int, str, bool], expire_in: int = None, expire_at: int | float | datetime = None)`: Saves a file in the DetaSpace database.

        *   `delete(key: str)`: Removes a file from the Deta Base.
    """

    def __init__(self, app=None, project_key=None, name=None, host=None):
        self.project_key = project_key
        self.name = name
        self.host = host

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initializes the extension and binds it to a Flask application instance.

        #### Args
        * `app` : The Flask application instance to which the extension will be bound.

        #### Example
        ```python
        >>> # DetaBase Instance
        >>> base = DetaBase()
        >>>
        >>> # Define a view or blueprint to retrieve all data
        >>> @app.route("/all")
        >>> def all_data():
        ...    return base.get_all()
        >>>
        >>> # Initialize the DetaBase instance with the Flask app
        >>> base.init_app(app)
        ```
        """

        self.project_key = app.config.get("DETA_PROJECT_KEY", self.project_key)
        self.name = app.config.get("BASE_NAME", self.name)
        self.host = app.config.get("BASE_HOST", self.host)

        self.instance = verify_setups(self.project_key, self.name, self.host, "Base")

        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["flask_deta"] = {"base": self}

    def put(
        self,
        data: dict[Union[dict, list, tuple, int, str, bool]],
        key: Optional[str] = None,
        expire_in: Optional[int] = None,
        expire_at: Optional[Union[int, float, datetime]] = None,
    ):
        """Store data in the Deta database.

        ### Args:
            *   `data`: Data to be stored. Can be a dictionary,
                a list, a string, an integer, or a boolean.
                Overrides an item if key already exists.

            *   `key`: (Optional) The key associated with the data.
                Could be provided as function argument or a field in the data dict

            *   `expire_in`: (Optional) Time in seconds until the data expires.

            *   `expire_at`: (Optional) Unix timestamp or datetime when the data expires.

        ### Returns:
            The result of the storage operation or TypeError.

        ### Example:
        ```
        >>> data = {"name" : John, "age" : 25}
        >>> db.put(data, key="custom_key", expire_in=300)
        ```
        """

        try:
            crud = self.instance.put(
                data=data, key=key, expire_in=expire_in, expire_at=expire_at
            )
            return crud
        except:
            msg = """Error in 'DetaBase.put()' while storing data in the database.
                Possible causes include:"
                   - Incorrect data format provided."
                   - Key must be a string."
                   - Incorrect format for expiration parameters (expire_in or expire_at)."
                   - Other unknown issues."
            """
            raise TypeError(msg)

    def put_all(
        self,
        items: list[dict],
        expire_in: Optional[int] = None,
        expire_at: Optional[int | float | datetime] = None,
    ):
        """Store a list whit your data in the Deta database.

        ### Args:
            * `items`: list whit items to be stored. Can be a list whit dictionaries,
                lists, strings, integers, or booleans.

            * `expire_in`: (Optional) Time in seconds until the data expires.

            * `expire_at`: (Optional) Unix timestamp or datetime when the data expires.

        ### Returns:
            The result of the storage operation or `TypeError`.

        ### Examples:
            >>> records = [
            ...     {"name" : "John", "age" : 30},
            ...     {"name" : "Tim", "age" : 45},
            ...     {"name" : "Guido", "age" : 52},
            ... ]
            >>>
            >>> db.put_all(records)
        """

        try:
            crud = self.instance.put_many(
                items=items, expire_in=expire_in, expire_at=expire_at
            )
            return crud
        except:
            msg = "Error in 'DetaBase.put_all()' while storing multiple items in the database."
            current_app.logger.error(msg)
            raise TypeError(msg)

    def get(self, key: str) -> dict:
        """Retrieves data from the Deta Base database using the provided key.

        ### Args:
            * key (str): The key associated with the data to be retrieved. Equivalent to id or a primary key

        ### Returns:
            * The retrieved data`or `TypeError`.

        ### Example:
            >>> key = "1122334455"
            >>> result = db.get(key)
        """
        record = self.instance.get(key)
        if record:
            return record
        else:
            msg = f"Error in 'DetaBase.get()' while getting '{key}'. Record not found due to incorrect identification key."
            current_app.logger.error(msg)
            raise TypeError(msg)

    def get_all(self, limit: int = 1000) -> list[dict]:
        """Retrieves all data from the Deta database.

        ### Returns:
            A list containing all the data from the database or `TypeError`.

        ### Args
            limit (optional): Specifies the maximum number of records to be retrieved.
            By default it returns 1000 or 1MB.

        ### Example:
            >>> all_data = db.get_all() # All records
            >>> five_records = db.get_all(limit=5) # limit=n records
        """
        try:
            fetch = self.instance.fetch(limit=limit).items
            return fetch
        except Exception as e:
            msg = f"Error in 'DetaBase.get_all()' while retrieving data from the database."
            current_app.logger.error(f"{msg} => {e}")
            raise TypeError(msg)

    def update(
        self,
        key: str,
        updates: dict[Union[dict, list, tuple, int, str, bool]],
        expire_in: Optional[int] = None,
        expire_at: Optional[Union[int, float, datetime]] = None,
    ):
        """update and updates data in the Deta Base database using the provided key.

        ### Args:
            *   `key (str)`: The key associated with the data to be updated. Equivalent to id or a primary key
            *   `updates (dict[dict | list | str | int | bool])`: The updated data.
            *   `expire_in`: (Optional) Time in seconds until the data expires.
            *   `expire_at`: (Optional) Unix timestamp or datetime when the data expires.

        ### Returns:
            The result of the database update operation or `TypeError`.

        ### Example:
            >>> id_key = "1122334455"
            >>> update = {"name": "John", "age": 30}
            >>> expire_in = 60 # seconds
            >>> db.update(key=id_key, updates=update, expire_in=expire_in)
        """

        try:
            crud = self.instance.update(
                updates=updates, key=key, expire_in=expire_in, expire_at=expire_at
            )
            return crud

        except:
            msg = f"""Error in 'DetaBase.update()' while updating record '{key}'. This could be due to:
            - The provided key does not correspond to an existing record.
            - An issue with the database connection.
            - Incorrect data format for updates.
            - Expiration parameters (expire_in or expire_at) not set correctly.
            - Other unknown issues.
            """
            current_app.logger.error(msg)
            raise TypeError(msg)

    def delete(self, key: str):
        """Deletes data from the Deta BASE database using the provided key.

        ### Args:
            *   key (str): The key associated with the data to be deleted. Equivalent to id or a primary key

        ### Returns:
            The result of the database delete operation or `TypeError`.

        ### Example:
            >>> key = "1122334455"
            >>> db.delete(key)
        """

        crud = self.instance.delete(key)
        if crud:
            return crud
        else:
            msg = f"Error in 'DetaBase.delete()' while deleting '{key}'. Record not found due to incorrect identification key."
            current_app.logger.error(msg)
            raise TypeError(msg)
