import io
from typing import Optional, Union
from deta import Deta
from .__deta_setup import DetaTemplate


class DetaDrive(DetaTemplate):
    """
    Represents a DetaSpace Drive that allows you to store and manage files.

    Attributes:
        DETA_PROJECT_KEY (str): The Deta Project key used for authentication.
        DETA_DRIVE_NAME (str): The name of the DetaSpace Drive for files.

    Methods:
        get_all_files() -> Optional[dict]:
            Fetches all files stored in the Deta Drive.

            Returns:
                dict: A dictionary containing information about all the files, or None if an error occurs.

        get_file(filename: str) -> Optional[bytes]:
            Fetches a specific file from the Deta Drive.

            Args:
                - filename (str): The name of the file to fetch.

            Returns:
                bytes: The content of the file as bytes, or None if the file does not exist or an error occurs.


        push_file(
            filename: str,
            data: Optional[str|bytes|io.TextIOBase|io.BufferedIOBase|io.RawIOBase] = None,
            file_path: Optional[str] = None,
            type: Optional[str] = None
        ) -> Optional[bool]:

            Saves a file in the Deta Cloud Drive.

            Args:

                filename (str): The name of the file to be saved.

                data:The content of the file. It can be a string, bytes, or file-like object. Defaults to None.

                file_path (str, optional): The path of the file to be saved. Defaults to None.

                type (str, optional): The content type of the file. Defaults to None.

            Returns:
                bool: True if the file is saved successfully, or None if an error occurs.

        remove_file(name: str) -> Optional[str]:
            Removes a file from the Deta Drive.

            Args:
                name (str): The name of the file to be removed.

            Returns:
                str: The name of the removed file, or None if the file does not exist or an error occurs.
    """

    def __get_config_name__(self):
        return "DETA_DRIVE_NAME"

    def __get_type_name__(self):
        return "Drive"

    def __get_deta_instance__(self):
        return Deta().Drive

    def get_all_files(self) -> Optional[dict]:
        """
        Fetches all files stored in the Deta Drive.

        Returns:
            dict or None: A dictionary containing information about all the files, or None if an error occurs.

        Usage:
        ```python
        app = Flask(__name__)
        app.config["DETA_PROJECT_KEY"] = "MyKey12345"
        app.config["DETA_DRIVE_NAME"] = "brands" # DetaSpace Drive for files

        dd = DetaDrive(app)
        logos = dd.get_all_files()
        ```
        """
        if not self.DRIVE:
            return None
        try:
            all_files = self.DRIVE.list()
            return all_files
        except Exception as e:
            self.__app__.logger.error(f"Error fetching records: {e}")
            return None

    def get_file(self, filename: str) -> Optional[bytes]:
        """
        Fetches a specific file from the Deta Drive.

        Args:
            `filename (str)`: The name of the file to fetch.

        Returns:
            bytes or None: The content of the file as bytes, or None if the file does not exist or an error occurs.

        Usage:
        ```python
        >>> app = Flask(__name__)
        >>> app.config["DETA_PROJECT_KEY"] = "MyKey12345"
        >>> app.config["DETA_DRIVE_NAME"] = "brands" # DetaSpace Drive for files
        >>> dd = DetaDrive(app)
        >>>
        >>> descriptions = "descriptions.txt"
        >>> file_content = dd.get_file(descriptions)
        ```
        """

        if not self.DRIVE:
            return None
        try:
            file = self.DRIVE.get(filename)
            return file
        except Exception as e:
            self.__app__.logger.error(f"Error fetching record: {e}")
            return None

    def push_file(
        self,
        filename: str,
        data: Union[str, bytes, io.TextIOBase, io.BufferedIOBase, io.RawIOBase] = None,
        file_path: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Optional[bool]:
        """
        Saves a file in the Deta Drive.

        Args:
            `filename (str)`: The name of the file to be saved.

            `data (str| bytes|io.TextIOBase|io.BufferedIOBase|io.RawIOBase, optional)`:
                The data content of the file. Defaults to None.

            `file_path (str, optional)`: The local path of the file to be saved. Defaults to None.

            `type (str, optional)`: The content type (MIME style => "type/subtype") of the file. Defaults to None.

        Returns:
            bool or None: True if the file is saved successfully, or None if an error occurs.

        Usage:
        ```python
        >>> app = Flask(__name__)
        >>> app.config["DETA_PROJECT_KEY"] = "MyKey12345"
        >>> app.config["DETA_DRIVE_NAME"] = "categories" # DetaSpace Drive for files
        >>> dd = DetaDrive(app)
        >>>
        >>> filename = "electronics.txt"
        >>> data = "Hello, Electronics!"
        >>> dd.push_file(filename, data=data, type="text/plain")
        ```

        Notes:
            you can find all MIME types in:
              https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_Types
        """
        if not self.DRIVE:
            return None
        try:
            config = {
                "name": filename,
                "data": data,
                "path": file_path,
                "content_type": type,
            }

            return self.DRIVE.put(**config)

        except Exception as e:
            self.__app__.logger.error(f"Error saving file: {e}")
            return None

    def remove_file(self, name: str) -> Optional[str]:
        """
        Removes a file from the Deta Drive.

        Args:
            name (str): The name of the file to be removed.

        Returns:
            str or None: The name of the removed file, or None if the file does not exist or an error occurs.

        Usage:
        ```python
        >>> app = Flask(__name__)
        >>> app.config["DETA_PROJECT_KEY"] = "MyKey12345"
        >>> app.config["DETA_DRIVE_NAME"] = "categories" # DetaSpace Drive for files
        >>> dd = DetaDrive(app)
        >>>
        >>> filename_to_remove = "example.txt"
        >>> dd.delete_file(filename_to_remove)
        ```
        """
        if not self.DRIVE:
            return None
        try:
            return self.DRIVE.delete(name)
        except Exception as e:
            self.__app__.logger.error(f"Error deleting record: {e}")
            return None
