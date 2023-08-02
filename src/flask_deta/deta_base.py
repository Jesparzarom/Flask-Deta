from deta import Deta
from .deta_setup import DetaTemplate

class DetaBase(DetaTemplate):
    def __get_config_name__(self):
        return "DETA_DB_NAME"

    def __get_type_name__(self):
        return "Base"

    def __get_deta_instance__(self):
        return Deta().Base
    
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
        >>> app.config['DETA_SECRET_KEY'] = 'yourKey'
        >>> app.config['DETA_DATABASE'] = 'nameOfDatabase'
        >>> db = DetaSpace(app)

        # Usage 1: Passing individual arguments
        >>> data = {"name" : John, "age" : 30}
        >>> db.push(data, key="custom_key")

        # Usage 2: Passing all arguments in a dictionary
        >>> data = {"name" : John, "age" : 30}
        >>> args_dict = {
        ...     'data': data,
        ...     'key': "custom_key",
        ...     'expire_in': 300,
        ...     'expire_at'=datetime.fromisoformat("2023-01-01T00:00:00")
        ... }
        >>> db.push(**args_dict)

        ```
        """

        if not self.BASE:
            return None

        try:
            return self.BASE.put(
                data=data, key=key, expire_in=expire_in, expire_at=expire_at
            )
        except Exception as e:
            self.app.logger.error(f"Error creating record: {e}")
            return None

    def get(self, key):
        if not self.BASE:
            return None
        try:
            return self.BASE.get(key)
        except Exception as e:
            self.app.logger.error(f"Error getting record: {e}")
            return None

    def edit(self, key, data):
        if not self.BASE:
            return None
        try:
            return self.BASE.update(data, key=key)
        except Exception as e:
            self.app.logger.error(f"Error updating record: {e}")
            return None

    def remove(self, key):
        if not self.BASE:
            return None
        try:
            return self.BASE.delete(key)
        except Exception as e:
            self.app.logger.error(f"Error deleting record: {e}")
            return None

    def get_all(self):
        if not self.BASE:
            return None
        try:
            all_data = self.BASE.fetch().items
            return all_data
        except Exception as e:
            self.app.logger.error(f"Error fetching records: {e}")
            return None