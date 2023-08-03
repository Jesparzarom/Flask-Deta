import io
from typing import Optional, Union
from deta import Deta
from .__deta_setup import DetaTemplate


class DetaDrive(DetaTemplate):
    """
    Represents a Deta Drive that allows you to store and manage files.
    """
        
    def __get_config_name__(self):
        return "DETA_DRIVE_NAME"

    def __get_type_name__(self):
        return "Drive"

    def __get_deta_instance__(self):
        return Deta().Drive

    def all_files(self) -> Optional[dict]:
        """
        Fetches all files stored in the Deta Drive.

        Returns:
            dict: A dictionary containing information about all the files, or None if an error occurs.
        """
        if not self.DRIVE:
            return None
        try:
            all_data = self.DRIVE.list()
            return all_data
        except Exception as e:
            self.__app__.logger.error(f"Error fetching records: {e}")
            return None

    def file(self, filename: str) -> Optional[bytes]:
        """
        Fetches a specific file from the Deta Drive.

        Args:
            filename (str): The name of the file to fetch.

        Returns:
            bytes: The content of the file as bytes, or None if the file does not exist or an error occurs.
        """

        if not self.DRIVE:
            return None
        try:
            file = self.DRIVE.get(filename)
            return file
        except Exception as e:
            self.__app__.logger.error(f"Error fetching record: {e}")
            return None

    def save(
        self,
        filename: str,
        data: Union[str, bytes, io.TextIOBase, io.BufferedIOBase, io.RawIOBase] = None,
        file_path: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Optional[bool]:
        """
        Saves a file in the Deta Drive.

        Args:
            filename (str): The name of the file to be saved.
            data (Union[str, bytes, io.TextIOBase, io.BufferedIOBase, io.RawIOBase], optional):
                The content of the file. It can be a string, bytes, or file-like object. Defaults to None.
            file_path (str, optional): The path of the file to be saved. Defaults to None.
            type (str, optional): The content type of the file. Defaults to None.

        Returns:
            bool: True if the file is saved successfully, or None if an error occurs.
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
            self.DRIVE.put(**config)
            return True
        except Exception as e:
            self.__app__.logger.error(f"Error saving file: {e}")
            return None

    def remove(self, name: str) -> Optional[str]:
        """
        Removes a file from the Deta Drive.

        Args:
            name (str): The name of the file to be removed.

        Returns:
            str: The name of the removed file, or None if the file does not exist or an error occurs.
        """
        if not self.DRIVE:
            return None
        try:
            self.DRIVE.delete(name)
            return name
        except Exception as e:
            self.__app__.logger.error(f"Error deleting record: {e}")
            return None
