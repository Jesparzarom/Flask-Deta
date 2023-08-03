from deta import Deta
import io


class DetaBase:
    """Connect to a Deta database using provided parameters in two ways.

    Parameters:
        app (Flask app, optional): The Flask app instance.
        If provided, 'project_key' and 'database' will be read
        from the app.config dictionary. Default is None.

        project_key (str, optional): The Deta project key. Required if 'app' is not provided.
        database (str, optional): The name of the Deta database.Required if 'app' is not provided.

    Examples:
        Connect using app.config parameters:
        ```python
        app.config['DETA_SECRET_KEY'] = 'yourKey'
        app.config['DETA_DATABASE'] = 'nameOfDatabase'
        db = DetaSpace(app)
        ```

        Connect using direct parameters:
        ```python
        db = DetaSpace(
            project_key='yourKey',
            database='nameOfDatabase',
        )
        ```
    """

    def __init__(self, app=None, project_key=None, deta_base=None):
        self.app = app
        self.project_key = project_key or (app and app.config.get("DETA_PROJECT_KEY"))
        self.deta_base = deta_base or (app and app.config.get("DETA_DB_NAME"))

        if not self.project_key:
            raise ValueError("No project key provided")

        if not self.deta_base:
            raise ValueError("No Drive or Database name provided")

        try:
            self.deta = Deta(self.project_key)
            self.BASE = self.deta.Base(self.deta_base)

        except Exception as e:
            if self.app:
                self.app.logger.error(f"Error connecting to database: {e}")
            self.BASE = None

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


class DetaDrive:
    def __init__(self, app=None, project_key=None, deta_drive=None, drive_host=None):
        self.app = app

        self.project_key = project_key or (app and app.config.get("DETA_PROJECT_KEY"))
        self.deta_drive = deta_drive or (app and app.config.get("DETA_DRIVE_NAME"))

        if not self.project_key:
            raise ValueError("No project key provided")

        if not self.deta_drive:
            raise ValueError("No Drive name provided")

        try:
            self.deta = Deta(self.project_key)
            self.DRIVE = self.deta.Drive(self.deta_drive)

        except Exception as e:
            if self.app:
                self.app.logger.error(f"Error connecting to database: {e}")
            self.DRIVE = None

    def all_files(self):
        if not self.DRIVE:
            return None
        try:
            all_data = self.DRIVE.list()
            return all_data
        except Exception as e:
            self.app.logger.error(f"Error fetching records: {e}")
            return None

    def get(self, filename: str):
        if not self.DRIVE:
            return None
        try:
            file = self.DRIVE.get(filename)
            return file
        except Exception as e:
            self.app.logger.error(f"Error fetching records: {e}")
            return None

    def save(
        self,
        filename: str,
        data: str | bytes | io.TextIOBase | io.BufferedIOBase | io.RawIOBase = None,
        file_path: str = None,
        type: str = None,
    ):
        if not self.DRIVE:
            return None
        try:
            config = {
                "name": filename,
                "data": data,
                "path": file_path,
                "content_type": type,
            }
            self.DRIVE.put(**config)
            return True
        except Exception as e:
            self.app.logger.error(f"Error saving file: {e}")
            return None


from src.flask_deta import det
