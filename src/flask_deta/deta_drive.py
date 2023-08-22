import io
from typing import Optional, Union

from .validator import verify_setups


class DetaDrive:
    """
    ## Class DetaDrive
    Represents a DetaSpace Drive that allows you to store and manage files.

    ### Attributes:
        *   `app (Flask)`: Flash app to contextualize class methods and attributes.

        *   `project_key  (str)`: The DetaSpace Project key used for authentication.
            The argument can be passed manually, if the argument is empty, an attempt
            is made to find it if it was defined as 

            ```python
            >>> app.config['DETA_PROJECT_KEY] = "myKey123".
            ```

        *   `name (str)`: The name of your DetaSpace Drive.The argument can be passed manually, 
            if the argument is empty, an attempt is made to find it if it was defined as 
            
            ```python
            >>> app.config['DRIVE_NAME'] = "files".
            ```

        * `host (str)`: Optional host URL for API requests. This URL specifies the Deta server where
                    the requests will be sent. The default Deta host URL will be used.
                    `host = "https://drive.deta.sh"` -> app.config['DRIVE_HOST']


    ### Methods:
        * `init_app(app: Flask)`: Initializes the extension and binds it to a Flask application instance.

        * `all_files(limit: int=1000, prefix: str=None)`: Gets all files stored on the Deta drive. By default it returns 1000 or 1MB.

        * `get_file(name: str)`: Fetches a specific file from the Deta Drive.

        * `put_file(name: str, data: dict[str|bytes|io.TextIOBase|io.BufferedIOBase|io.RawIOBase] = None, path: str = None, type: str = None): `
            Saves a file in the Deta Cloud Drive.

        * `delete_file(name: str)`:Removes a file from the Deta Drive.

        * `delete_many(names: str)`: Remove multiple files from the Deta Drive..
    """

    def __init__(self, app=None, project_key=None, name=None, host=None):
        self.project_key = project_key
        self.name = name
        self.host = host

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.project_key = app.config.get("DETA_PROJECT_KEY", self.project_key)
        self.name = app.config.get("DRIVE_NAME", self.name)
        self.host = app.config.get("DRIVE_HOST", self.host)

        self.instance = verify_setups(self.project_key, self.name, self.host, "Drive")

        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["flask_deta"] = {"drive": self.instance}

    def all_files(
        self, limit: Optional[int] = 1000, prefix: Optional[str] = None
    ) -> Optional[list]:
        """
        Fetches all files stored in the Deta Drive.

        ### Returns:
            list: A list containing names of all files.

        ### Args
            limit (optional): Specifies the maximum number of files to be retrieved.
            prefix (optional):  Prefix that file names must start with to be returned

        ### Examples:
        ```python
        >>> logos = drive.all_files() # All files
        >>> five_logos = drive.all_files(limit=5) # 5 Files
        >>> burger_logos = drive.all_files(prefix="burger") # Files starting with "Burger".
        ```
        """

        try:
            files = self.instance.list(limit=limit, prefix=prefix)
            if files["names"]:
                return files["names"]
            else:
                raise ValueError("List of files is empty")
        except Exception as e:
            raise Exception(f"Error in 'DetaDrive.all_files()' method => {e}")

    def get_file(self, name: str) -> bytes:
        """
        Fetches a specific file from the Deta Drive.

        ### Args:
            `name (str)`: The name of the file to fetch.

        ### Returns:
            The file

        ### Examples:
        ```python
        >>> descriptions = "descriptions.txt"
        >>> file_content = drive.get_file(descriptions)
        ```
        """
        if name:
            file = self.instance.get(name)
            if name in set(self.instance.list()["names"]):
                return file
            else:
                raise Exception(
                    "Error in 'DetaDrive.get_file()' method => 404 File not found"
                )
        else:
            raise Exception(
                "Error in 'DetaDrive.get_file()' method => The name has not been provided"
            )

    def put_file(
        self,
        name: str,
        data: Union[str, bytes, io.TextIOBase, io.BufferedIOBase, io.RawIOBase] = None,
        path: Optional[str] = None,
        type: Optional[str] = None,
    ) -> str:
        """
        Saves a file in the Deta Drive.
        IMPORTANT: You must pass either `data` or `path` but not both, otherwise an error will be generated.

        ### Args:
            *   `name (str)`: The name of the file to be saved.

            *   `data (str| bytes|io.TextIOBase|io.BufferedIOBase|io.RawIOBase, optional)`:
                The data content of the file. Defaults to None.

            *   `path (str, optional)`: The local path of the file to be saved. Defaults to None.

            *   `type (str, optional)`: The content type (MIME style => "type/subtype") of the file. Defaults to None.

        ### Returns:
            bool or None: True if the file is saved successfully, or None if an error occurs.

        ### Examples:
        ```python
        >>> name = "electronics.txt"
        >>> data = "Hello, Electronics!"
        >>> drive.put_file(name, data=data, type="text/plain")
        ```

        ####    Notes:
            you can find all MIME types in:
              https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_Types
        """

        try:
            to_save = self.instance.put(
                name=name, data=data, path=path, content_type=type
            )
            if name:
                return to_save
            else:
                raise ValueError("Drive name is not provided")
        except Exception as e:
            raise Exception(f"Error in 'DetaDrive.put_file()' method => {e}")

    def delete_file(self, name: str) -> str:
        """
        Removes a file from the Deta Drive.

        ### Args:
            *   name (str): The name of the file to be removed.
        
        - Returns the name of the removed file or Exeption if the file does not exist or an error occurs.

        ### Examples:
        ```python
        >>> file_to_remove = "example.txt"
        >>> drive.delete_file(file_to_remove)
        ```
        """

        try:
            del_file = self.instance.delete(name)
            if del_file:
                return del_file
            else:
                if del_file not in set(self.instance.list()):
                    raise ValueError(
                        f"The file '{name}' could not be deleted because it does not exist."
                        + "Please check the arguments entered."
                    )
                raise Exception(
                    f"An error occurred trying to delete the '{name}' file."
                )
        except Exception as e:
            raise Exception(f"Error in 'DetaDrive.delete_file()' method => {e}")

    def delete_many(self, names: list[str]):
        """
        Remove multiple files from the Deta Drive.

        This method allows you to remove multiple files from the Deta Drive at once.

        ### Args:
            names (list[str]): A list of names of the files to be removed.

        - Returns the names of the removed files or Exeption if the file does not exist or an error occurs.

        ### Examples:
            >>> files_to_remove = ["example.txt", "data.csv"]
            >>> drive.delete_many(files_to_remove)
        """
        
        try:
            if isinstance(names, list):
                return self.instance.delete_many(names)
            else:
                raise ValueError("List of names has not been provided or is not a list")
        except Exception as e:
            raise Exception(f"Error in 'DetaDrive.delete_many()' method => {e}")
