from deta import Deta
from .__deta_setup import DetaTemplate


class DetaBase(DetaTemplate):
    # ========== SETUPS ==========
    def __get_config_name__(self):
        return "DETA_DB_NAME"

    def __get_type_name__(self):
        return "Base"

    def __get_deta_instance__(self):
        return Deta().Base

    # ========== OPERATIONS ==========
    def push(
        self,
        data: dict[dict | list | tuple | int | str | bool],
        key=None,
        expire_in=None,
        expire_at=None,
    ):
        """
        push (method) Store data in the Deta database.

        Args:
        *** data: Data to be stored. Can be a dictionary,
            a list, a string, an integer, or a boolean.
            Overrides an item if key already exists.

        *** key: (Optional) The key associated with the data.
            Could be provided as function argument or a field in the data dict

        *** expire_in: (Optional) Time in seconds until the data expires.

        *** expire_at: (Optional) Unix timestamp or datetime when the data expires.

        Returns:
            The result of the storage operation or None if the database
            is not available or an error occurs.

        Example:
        ```
        >>> app = Flask(__name__)
        >>> app.config['DETA_SECRET_KEY'] = 'yourKey'
        >>> app.config['DETA_DATABASE'] = 'nameOfDatabase'
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
            self.__app__.logger.error(f"Error creating record: {e}")
            return None

    def get(self, key: str):
        """Retrieves data from the Deta BASE database using the provided key.

        Args:
            key (str): The key associated with the data to be retrieved. Equivalent to id or a primary key

        Returns:
            Any | None: The retrieved data or None if the database is not available or an error occurs.

        Example:
            >>> app = Flask(__name__)
            >>> app.config['DETA_SECRET_KEY'] = 'yourKey'
            >>> app.config['DETA_DATABASE'] = 'nameOfDatabase'
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
            self.__app__.logger.error(f"Error getting record: {e}")
            return None

    def get_all(self):
        """Retrieves all data from the Deta database.

        Returns:
            list | None: A list containing all the data from the database
            or None if the database is not available or an error occurs.

        Example:
            >>> app = Flask(__name__)
            >>> app.config['DETA_SECRET_KEY'] = 'yourKey'
            >>> app.config['DETA_DATABASE'] = 'nameOfDatabase'
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
            all_data = self.BASE.fetch().items
            return all_data
        except Exception as e:
            self.__app__.logger.error(f"Error fetching records: {e}")
            return None

    def edit(self, key: str, data: dict[dict | list | tuple | int | str | bool]):
        """Edit and updates data in the Deta BASE database using the provided key.

        Args:
            key (str): The key associated with the data to be updated. Equivalent to id or a primary key
            data (dict[dict | list | str | int | bool]): The updated data.

        Returns:
            Any | None: The result of the database update operation or None if the database is not available or an error occurs.

        Example:
            >>> app = Flask(__name__)
            >>> app.config['DETA_SECRET_KEY'] = 'yourKey'
            >>> app.config['DETA_DATABASE'] = 'nameOfDatabase'
            >>>
            >>> db = DetaBase(app)
            >>>
            >>> key = "1122334455"
            >>> data = {"name": "John", "age": 30}
            >>> db.update(key, data)
        """
        if not self.BASE:
            return None
        try:
            return self.BASE.update(data, key=key)
        except Exception as e:
            self.__app__.logger.error(f"Error updating record: {e}")
            return None

    def remove(self, key: str):
        """Remove/Deletes data from the Deta BASE database using the provided key.

        Args:
            key (str): The key associated with the data to be deleted. Equivalent to id or a primary key

        Returns:
            Any | None: The result of the database delete operation or None if the database is not available or an error occurs.

        Example:
            >>> app = Flask(__name__)
            >>> app.config['DETA_SECRET_KEY'] = 'yourKey'
            >>> app.config['DETA_DATABASE'] = 'nameOfDatabase'
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
            self.__app__.logger.error(f"Error deleting record: {e}")
            return None
