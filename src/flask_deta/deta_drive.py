import io
from deta import Deta
from .deta_setup import DetaTemplate

class DetaDrive(DetaTemplate):
    def __get_config_name__(self):
        return "DETA_DRIVE_NAME"

    def __get_type_name__(self):
        return "Drive"

    def __get_deta_instance__(self):
        return Deta().Drive
    
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
                "name" : filename,
                "data" : data,
                "path" : file_path,
                "content_type" : type
            }
            self.DRIVE.put(**config)
            return True
        except Exception as e:
            self.app.logger.error(f"Error saving file: {e}")
            return None






