
## *class* DetaDrive [DEPRECATED]
> `flask_deta.DetaDrive(app : Flask, project_key: str, name: str, host: Optional[str])`

- Attributes:
    * `app (Flask)`: Flash app to contextualize class methods and attributes.
    * `project_key  (str)`: The DetaSpace Project key used for authentication.
        The argument can be passed manually, if the argument is empty, an attempt
        is made to find it if it was defined as `app.config['DETA_PROJECT_KEY] = DETA_PROJECT_KEY.
    * `name (str)`: The name of your DetaSpace Drive.The argument can be passed manually, if the argument is empty, an attempt is made to find it if it was defined as `app.config['DRIVE_NAME'] = DRIVE_NAME`.
    * Optional:
        * `host (Optional[str])`:
        Host URL for API requests. This URL specifies the Deta server where
        the requests will be sent. The default Deta **drive** host URL will be used;
        host = "https://drive.deta.sh". It can be defined as 
        `app.config['DRIVE_HOST'] = "https://mydrivehost.host"`

### Basic instance
```python
from flask import Flask
from flask_deta import DetaDrive

app = Flask(__name__)

# Set the DetaSpace project key and drive name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["DRIVE_NAME"] = "store1" # DetaSpace Drive for files

# Create instances of DetaDrive
drive = DetaDrive(app)
```
---

### init_app instance

**Instance**
```python
from flask import Flask
from flask_deta import DetaDrive

app = Flask(__name__)

# Set the DetaSpace project key and drive name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["DRIVE_NAME"] = "store1" # DetaSpace Drive for files

# Create instance of DetaDrive
drive = DetaDrive()

# ....

drive.init_app(app)
```

---

### Methods
* [init_app](#init_app) -> Initializes the extension and binds it to a Flask application instance.

* [all_files](#all_files) -> Fetches all files stored in the Deta Drive.

* [get_file](#get_file) -> Fetches a specific file from the Deta Drive.

* [put_file](#put_file) -> Saves a file in the Deta Cloud Drive.

* [delete_file](#delete_file) -> Removes a file from the Deta Drive.

* [detete_many](#delete_many) -> Removes multiple files from the Deta Drive..

---

Building upon the previous instantiation example, wherein the Flask-Deta instance is assigned to a variable named `drive` using `drive = DetaDrive()`, the following methods can be subsequently employed:

---

<!------------------------------INIT_APP----------------------------------->
### init_app
```python
drive.init_app(app: Flask)
```
Initializes the extension and binds it to a Flask application instance.

- Args
    * `app`: Flask app

_Example_
```python
# DetaDrive Instance
drive = DetaDrive()

# Define a view or blueprint to retrieve all files
@app.route("/files")
def files():
    return drive.all_files()

# Initialize the DetaBase instance with the Flask app
drive.init_app(app)
```


<!------------------------------ALL FILES----------------------------------->
### all_files
```python
drive.all_files(limit: int=1000, prefix: str=None )
```
Fetches all files stored in the Deta Drive.

- Args
    * `limit (optional[int])`: Specifies the maximum number of files to be retrieved.
    * `prefix (optional[str])`:  Prefix that file names must start with to be returned 

- Returns
    A list containing names of all files or Exception if an error occurs.

_Example_
```python
drive = DetaDrive(app)
logos = drive.all_files()
```

---

<!---------------------------------GET FILE----------------------------------->
### get_file
```python
drive.get_file(name: str)
```
Fetches a specific file from the Deta Drive.

- Args:
    `name (str)`: The name of the file to fetch or Exception if an error occurs.

- Returns
    the content of the file as bytes or Exceptions if the file does not exist or an error occurs.

_Example_
```python
descriptions = "descriptions.txt"
file_content = drive.get_file(descriptions)
```

---

<!------------------------------PUT FILE----------------------------------->
### put_file
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

- Returns True if the file is saved successfully or Exceptions if an error occurs.

_Example_
```python
name = "electronics.txt"
data = "Hello, Electronics!"
drive.put_file(name=name, data=data, type="text/plain")
```

> ⚠ Note: you can find all MIME types in: 
> [MIME_Types](https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_Types)
   

--- 

<!------------------------------ DELETE FILE ----------------------------------->
### delete_file
```python
drive.delete_file(name: str)
```
Removes a file from the Deta Drive.

- Args:
    * `name (str)`: The name of the file to be removed.

- Returns the name of the removed file or Exeption if the file does not exist or an error occurs.

_Example_
```python
file_to_remove = "example.txt"
drive.delete_file(file_to_remove)
```

---

<!------------------------------DELETE_MANY---------------------------------->
### delete_many
```python
drive.delete_many(names: list[str])
```
Remove multiple files from the Deta Drive.

- Args
    * `names: (list[str])`: Remove multiple files from the Deta Drive.

- Returns the names of the removed files or Exeption if the files does not exists or an error occurs.

_Example_ 
```python
to_delete = [
    "clients.txt",
    "hotsale.png",
    "drinks.csv"
]

drive.delete_many(to_delete)
```
