from typing import Optional, Union
from datetime import datetime
from flask import Flask
from .__deta_setup import DetaConnect


# SUBCLASS
class DetaBase(DetaConnect):

    """
    Represents a DetaSpace Base that allows you to store and manage data.

    Attributes:
        `app (Flask)`: Flash app to contextualize class methods and attributes.

        `project_key  (str)`: The DetaSpace Project key used for authentication.
            The argument can be passed manually, if the argument is empty, an attempt
            is made to find it if it was defined as `app.config['DETA_PROJECT_KEY] = "myKey"`.

        `name (str)`: The name of your DetaSpace Base.The argument can be passed manually, if the argument is empty, an attempt is made to find it if it was defined as `app.config['Base_NAME'] = "coolBase"`.

    Methods:
        get_all():
            Fetches all data stored in the Deta Base.

            Returns:
                dict: A dictionary containing information about all the data, or None if an error occurs.

                
        get(filename: str):
            Fetches a specific file from the Deta Base.

            Args:
                - filename (str): The name of the file to fetch.

            Returns:
                bytes: The content of the file as bytes, or None if the file does not exist or an error occurs.


                
        push(
            filename: str,
            data: dict[str|bytes|io.TextIOBase|io.BufferedIOBase|io.RawIOBase] = None,
            file_path: str = None,
            type: str = None
        ):

            Saves a file in the Deta Cloud Base.

            Args:

                filename (str): The name of the file to be saved.

                data:The content of the file. It can be a string, bytes, or file-like object. Defaults to None.

                file_path (str, optional): The path of the file to be saved. Defaults to None.

                type (str, optional): The content type of the file. Defaults to None.

            Returns:
                bool: True if the file is saved successfully, or None if an error occurs.

                

        push_all(
            self,
            items: list[dict],
            expire_in: int = None,
            expire_at: int | float | datetime = None,
        ):
        
        push_all (method) Store a list whit your dict[data] in the Deta database.

        Args:
            items: list whit items to be stored. Can be a list whit dictionaries,
                lists, strings, integers, or booleans.

            expire_in: (Optional) Time in seconds until the data expires.

            expire_at: (Optional) Unix timestamp or datetime when the data expires.

        Returns:
            The result of the storage operation or None if the database
            is not available or an error occurs.



        edit(self, key: str, updates: dict[dict, list, tuple, int, str, bool]):

            Saves a file in the DetaSpace database.

            Args:
                key: The key associated with the data to be updated.

                updates:The content of the update.

                file_path (str, optional): The path of the file to be saved. Defaults to None.

                type (str, optional): The content type of the file. Defaults to None.

            Returns:
                bool: True if the file is saved successfully, or None if an error occurs.


        remove(name: str):
            Removes a file from the Deta Base.

            Args:
                name (str): The name of the file to be removed.

            Returns:
                str: The name of the removed file, or None if the file does not exist or an error occurs.
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
        self.BASE = super().connect()

    def push(
        self,
        data: dict[Union[dict, list, tuple, int, str, bool]],
        key: Optional[str] = None,
        expire_in: Optional[int] = None,
        expire_at: Optional[Union[int, float, datetime]] = None,
    ):
        """
        push (method) Store data in the Deta database.

        Args:
            data: Data to be stored. Can be a dictionary,
                a list, a string, an integer, or a boolean.
                Overrides an item if key already exists.

            key: (Optional) The key associated with the data.
                Could be provided as function argument or a field in the data dict

            expire_in: (Optional) Time in seconds until the data expires.

            expire_at: (Optional) Unix timestamp or datetime when the data expires.

        Returns:
            The result of the storage operation or None if the database
            is not available or an error occurs.

        Example:
        ```
        >>> app = Flask(__name__)
        >>> app.config['DETA_PROJECT_KEY'] = 'yourKey'
        >>> app.config['BASE_NAME'] = 'nameOfDatabase'
        >>>
        >>> db = DetaBase(app)

        # Usage 1: Passing individual arguments
        >>> data = {"name" : John, "age" : 25}
        >>> db.push(data, key="custom_key", expire_in=300)

        # Usage 2: Passing all arguments in a dictionary
        >>> data = {"name" : John, "age" : 25}
        >>> config = {
        ...     'data': data,
        ...     'key': "1122334455",
        ...     'expire_in': 300, #seconds
        ...     'expire_at'=datetime.fromisoformat("2023-01-01T00:00:00")
        ... }
        >>> db.push(**config)

        ```
        """

        if not self.BASE:
            return None

        try:
            return self.BASE.put(
                data=data, key=key, expire_in=expire_in, expire_at=expire_at
            )
        except Exception as e:
            self._app.logger.error(f"Error creating record: {e}")
            return None

    def push_all(
        self,
        items: list[dict],
        expire_in: Optional[int] = None,
        expire_at: Optional[int | float | datetime] = None,
    ):
        
        """
        push_all (method) Store a list whit your dict[data] in the Deta database.

        Args:
            items: list whit items to be stored. Can be a list whit dictionaries,
                lists, strings, integers, or booleans.

            expire_in: (Optional) Time in seconds until the data expires.

            expire_at: (Optional) Unix timestamp or datetime when the data expires.

        Returns:
            The result of the storage operation or None if the database
            is not available or an error occurs.

        Examples:
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
            >>> db.push_all(records)
        """
        
        if not self.BASE:
            return None

        try:
            return self.BASE.put_many(
                items=items, expire_in=expire_in, expire_at=expire_at
            )
        
        except Exception as e:
            self._app.logger.error(f"Error creating record: {e}")
            return None

    def get(self, key: str) -> Optional[dict]:
        """Retrieves data from the Deta Base database using the provided key.

        Args:
            key (str): The key associated with the data to be retrieved. Equivalent to id or a primary key

        Returns:
            Any | None: The retrieved data or None if the database is not available or an error occurs.

        Example:
            >>> app = Flask(__name__)
            >>> app.config['DETA_PROJECT_KEY'] = 'yourKey'
            >>> app.config['BASE_NAME'] = 'nameOfDatabase'
            >>>
            >>> db = DetaBase(app)
            >>>
            >>> key = "1122334455"
            >>> result = db.get(key)
            >>> print(result)
        """
        if not self.BASE:
            return None
        try:
            return self.BASE.get(key)
        except Exception as e:
            self._app.logger.error(f"Error getting record: {e}")
            return None

    def get_all(self) -> Optional[list[dict]]:
        """Retrieves all data from the Deta database.

        Returns:
            list | None: A list containing all the data from the database
            or None if the database is not available or an error occurs.

        Example:
            >>> app = Flask(__name__)
            >>> app.config['DETA_PROJECT_KEY'] = 'yourKey'
            >>> app.config['BASE_NAME'] = 'nameOfDatabase'
            >>>
            >>> db = DetaBase(app)
            >>>
            >>> all_data = db.get_all()
            >>> for data in all_data:
            ...     print(data)
        """
        if not self.BASE:
            return None
        try:
            fetch_records = self.BASE.fetch(desc=True).items
            return fetch_records
        except Exception as e:
            self._app.logger.error(f"Error fetching records: {e}")
            return None

    def edit(
        self,
        key: str,
        updates: dict[Union[dict, list, tuple, int, str, bool]],
        expire_in: Optional[int] = None,
        expire_at: Optional[Union[int, float, datetime]] = None,
    ) -> Optional[bool]:
        """Edit and updates data in the Deta Base database using the provided key.

        Args:
            key (str): The key associated with the data to be updated. Equivalent to id or a primary key
            data (dict[dict | list | str | int | bool]): The updated data.

        Returns:
            Any | None: The result of the database update operation or None if the database is not available or an error occurs.

        Example:
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
        if not self.BASE:
            return None
        try:
            return self.BASE.update(
                updates=updates, key=key, expire_in=expire_in, expire_at=expire_at
            )
        except Exception as e:
            self._app.logger.error(f"Error updating record: {e}")
            return None

    def remove(self, key: str) -> Optional[bool]:
        """Remove/Deletes data from the Deta BASE database using the provided key.

        Args:
            key (str): The key associated with the data to be deleted. Equivalent to id or a primary key

        Returns:
            Any | None: The result of the database delete operation or None if the database is not available or an error occurs.

        Example:
            >>> app = Flask(__name__)
            >>> app.config['DETA_PROJECT_KEY'] = 'yourKey'
            >>> app.config['BASE_NAME'] = 'nameOfDatabase'
            >>>
            >>> db = DetaBase(app)
            >>>
            >>> key = "1122334455"
            >>> db.delete(key)
        """
        if not self.BASE:
            return None
        try:
            return self.BASE.delete(key)
        except Exception as e:
            self._app.logger.error(f"Error deleting record: {e}")
            return None
