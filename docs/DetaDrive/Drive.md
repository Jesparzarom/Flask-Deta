
Represents a DetaSpace Drive that allows you to store and manage files.
## *class* DetaDrive
> `flask_deta.DetaDrive(app : Flask, project_key: str, name: str)`

- Attributes:
    * `app (Flask)`: Flash app to contextualize class methods and attributes.
    
    * `project_key  (str)`: The DetaSpace Project key used for authentication.
        The argument can be passed manually, if the argument is empty, an attempt
        is made to find it if it was defined as `app.config['DETA_PROJECT_KEY] = "myKey"`.
    
    * `name (str)`: The name of your DetaSpace Drive.The argument can be passed manually, if the argument is empty, an attempt is made to find it if it was defined as `app.config['DRIVE_NAME'] = "coolDrive"`.

#### Instance
```python
from flask import Flask
from flask_deta import DetaDrive

app = Flask(__name__)

# Set the DetaSpace project key and drive name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["DRIVE_NAME"] = "icons" # DetaSpace Drive for files

# Create instances of DetaDrive
drive = DetaDrive(app)
```
---

### Methods:
* [all_files](#all_files) -> Fetches all files stored in the Deta Drive.

* [get_file](#get_file) -> Fetches a specific file from the Deta Drive.

* [put_file](#put_file) -> Saves a file in the Deta Cloud Drive.

* [delete_file](#delete_file) -> Removes a file from the Deta Drive.

---

Building upon the previous instantiation example, wherein the Flask-Deta instance is assigned to a variable named `drive` using `drive = DetaBase(app)`, the following methods can be subsequently employed:

<!------------------------------ALL FILES----------------------------------->
#### all_files
```python
drive.all_files()
```
Fetches all files stored in the Deta Drive.

- Returns
    dict or None: A dictionary containing information about all the files, or None if an error occurs.

> Example
```python
drive = DetaDrive(app)
logos = drive.all_files()
```

---

<!---------------------------------GET FILE----------------------------------->
#### get_file
```python
drive.get_file(name: str)
```
Fetches a specific file from the Deta Drive.

- Args:
    `name (str)`: The name of the file to fetch.

- Returns
    bytes or None: The content of the file as bytes, or None if the file does not exist or an error occurs.

> Example
```python
descriptions = "descriptions.txt"
file_content = drive.get_file(descriptions)
```

---

<!------------------------------PUT FILE----------------------------------->
#### put_file
```python
drive.put_file(
    name: str,
    data: str| bytes|io.TextIOBase|io.BufferedIOBase|io.RawIOBase = None,
    path: str = None,
    type: str = None,
)
```
Saves a file in the Deta Drive.

- Args:
    * `name (str)`: The name of the file to be saved.

    * `data (str| bytes|io.TextIOBase|io.BufferedIOBase|io.RawIOBase, optional)`:
        The data content of the file. Defaults to None.

    *  `path (str, optional)`: The local path of the file to be saved. Defaults to None.

    *  `type (str, optional)`: The content type (MIME style => "type/subtype") of the file. Defaults to None.

- Returns:
    * bool or None: True if the file is saved successfully, or None if an error occurs.

> Example
```python
name = "electronics.txt"
data = "Hello, Electronics!"
drive.put_file(name=name, data=data, type="text/plain")
```

> ⚠ Note: you can find all MIME types in: 
> [MIME_Types](https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_Types)
   

--- 

<!------------------------------ DELETE FILE ----------------------------------->
#### delete_file
```python
drive.delete_file(name: str)
```
Removes a file from the Deta Drive.

- Args:
    * `name (str)`: The name of the file to be removed.

- Returns
    str or None: The name of the removed file, or None if the file does not exist or an error occurs.

> Example
```python
file_to_remove = "example.txt"
drive.delete_file(file_to_remove)
```
