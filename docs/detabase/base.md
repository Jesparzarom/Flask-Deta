
## *class* DetaBase
> `flask_deta.DetaBase(app : Flask, project_key: str, name: str, host: Optional[str])`

- Attributes:
    - `app (Flask)`: 
    Flash app to contextualize deta.
    
    - `project_key  (str)`: 
    The DetaSpace Project key used for authentication.
        The argument can be passed manually, if the argument is empty, an attempt
        is made to find it if it was defined as `app.config['DETA_PROJECT_KEY'] = DETA_PROJECT_KEY`.
    
    - `name (str)`: 
    The name of your DetaSpace Base.The argument can be passed manually,
    if the argument is empty, an attempt is made to find it if it was defined
    as `app.config['BASE_NAME'] = BASE_NAME`.
    
    - Optional:
        - `host (Optional[str])`:
        Host URL for API requests. This URL specifies the Deta server where
        the requests will be sent. The default Deta **database** host URL will be used;
        host = "https://database.deta.sh". It can be defined as 
        `app.config['BASE_HOST'] = "https://mybasehost.host"`



### Basic instance
> Represents a DetaSpace Base that allows you to store and manage data.
```python
from flask import Flask
from flask_deta import DetaBase

app = Flask(__name__)

# Set the DetaSpace project key and database name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["BASE_NAME"] = "products" # DetaSpace Base for data 

# Create instance of DetaBase
base = DetaBase(app)
```

### init_app instance

**Instance**
```python
from flask import Flask
from flask_deta import DetaBase

app = Flask(__name__)

# Set the DetaSpace project key and database name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["BASE_NAME"] = "products" # DetaSpace Base for data 

# Create instance of DetaBase
base = DetaBase()

# ....

base.init_app(app)
```

---
### Methods

* [init_app](#init_app) -> Initializes the extension and binds it to a Flask application instance.

* [get_all](#get_all) -> Fetches all data stored in the Deta Base.

* [get](#get) -> Fetches a specific file from the Deta Base.

* [put](#put) -> Saves a file in the Deta Cloud Base.

* [put_all](#put_all) -> Store a list whit your dict[data] in the Deta database.

* [update](#update) -> Saves a file in the DetaSpace database.

* [delete](#delete) -> Removes a file from the Deta Base.

---

Building upon the previous instantiation example, wherein the Flask-Deta instance is assigned to a variable named `base` using `base = DetaBase()`, the following methods can be subsequently employed:

---

<!------------------------------INIT_APP----------------------------------->
### init_app
```python
base.init_app()
```
Initializes the extension and binds it to a Flask application instance.

- Args
    * `app`: Flask app

_Example_
```python
# DetaBase Instance
base = DetaBase()

# Define a view or blueprint to retrieve all data
@app.route("/all")
def all_data():
    return base.get_all()

# Initialize the DetaBase instance with the Flask app
base.init_app(app)
```

---

<!------------------------------GET_ALL----------------------------------->
###  get_all
```python
base.get_all()
```
Retrieves all data stored from the Deta database.

- Args
    *  `limit (Optional[int])`: Specifies the maximum number of records to be retrieved.
    By default it returns 1000 or 1MB

- Returns: A list containing all the data from the database or `TypeError`.

_Example_
```python
all_data = base.get_all()
some_data = base.get_all(limit=50)
```

---

<!------------------------------GET----------------------------------->
### get 
```python
base.get(key: str):
```
Retrieves data from the Deta Base database using the provided key.

- Args
    * `key (str)`: The key associated with the data to be retrieved. Equivalent to id or a primary key

- Returns: The retrieved data or `TypeError`.

_Example_
```python
key = "1122334455"
result = base.get(key)
```
---

<!------------------------------PUT----------------------------------->
### put
```python
base.put(
    data: dict[dict|list|tuple|int|str|bool],
    key: str = None,
    expire_in: int = None,
    expire_at: int|float|datetime = None,
):
```
Store a record in the Deta's Cloud Base.

- Args
    * `data (dict[dict|list|tuple|int|str|bool])`: Data to be stored. Can be a dictionary,
    a list, a string, an integer, or a boolean.
    Overrides an item if key already exists.  
    * `key (Optional[str])`: The key associated with the data.
    Could be provided as function argument or a field in the data dict 
    * `expire_in (Optional[int])`:Time in seconds until the data expires.
    * `expire_at (Optional[int|float|datetime])`:Unix timestamp or datetime when the data 

- Returns
    * The result of the storage operation or `TypeError`.

_Example_
```python
data = {
    "name" : John, 
    "age" : 25
}

base.put(
    data, 
    key="custom_key", 
    expire_in=300
)
```
---

<!------------------------------PUT_ALL----------------------------------->
### put_all
```python
base.put_all(
    items: list[dict],
    expire_in: int = None,
    expire_at: int | float | datetime = None,
):
```
Store a list whit your data in the Deta database.

- Args:
    * `items (list)`: list whit items to be stored. Can be a list whit dictionaries,
        lists, strings, integers, or booleans.
    * `expire_in (Optional[int])`:Time in seconds until the data expires.
    * `expire_at (Optional[int|float|datetime])`:Unix timestamp or datetime when the data expires.

- Returns:
    * The result of the storage operation or `TypeError`.

_Example_:
```python
records = [
    {"name" : "John", "age" : 30},
    {"name" : "Tim", "age" : 45},
    {"name" : "Guido", "age" : 52},
]

base.put_all(records)
```

---

<!------------------------------UPDATE----------------------------------->
### update
```python
base.update(
    key: str,
    updates: dict[dict|list|tuple|int|str|bool],
    expire_in: int = None,
    expire_at: int|float|datetime = None,
):
```
update and updates data in the Deta Base database using the provided key.

- Args:
    * `key (str)`: The key associated with the data to be updated. Equivalent to id or a primary key
    * `updates (dict[dict | list | str | int | bool])`: The updated data.
    * `expire_in (Optional[int])`:Time in seconds until the data expires.
    * `expire_at (Optional[int|float|datetime])`:Unix timestamp or datetime when the data expires.

- Returns:
    The result of the database update operation.

**Example**
```python
id_key = "1122334455"
updates = {"name": "John", "age": 30}
expire_in = 60 # seconds

base.update(key=id_key, updates=updates, expire_in=expire_in)
```

---


<!------------------------------DELETE----------------------------------->
### delete
```python
base.delete(key: str):
```
Deletes data from the Deta BASE database using the provided key.

- Args:
    * `key (str)`: The key associated with the data to be deleted. Equivalent to id or a primary key

- Returns:
    The result of the database delete operation.

**Example**
```python
key = "1122334455"
base.delete(key)
```