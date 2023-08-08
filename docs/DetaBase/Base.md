

## *Class* DetaBase
> `flask_deta.DetaBase(app : Flask, project_key: str, name: str)`

- Attributes:
    - `app (Flask)`: 
    Flash app to contextualize deta.
    
    - `project_key  (str)`: 
    The DetaSpace Project key used for authentication.
        The argument can be passed manually, if the argument is empty, an attempt
        is made to find it if it was defined as `app.config['DETA_PROJECT_KEY] = DETA_PROJECT_KEY`.
    
    - `name (str)`: 
    The name of your DetaSpace Base.The argument can be passed manually,
    if the argument is empty, an attempt is made to find it if it was defined
    as `app.config['BASE_NAME'] = BASE_NAME`.

### Instance
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

---
## Methods:

Building upon the previous instantiation example, wherein the Flask-Deta instance is assigned to a variable named `base` using `base = DetaBase(app)`, the following methods can be subsequently employed:

###  get_all

```python
base.get_all()
```
Retrieves all data stored from the Deta database.

- Returns:
    * list | None: A list containing all the data from the database
     or None if the database is not available or an error occurs.

**Example**
```python
all_data = base.get_all()
```

---

### get 
```python
base.get(key: str):
```
Retrieves data from the Deta Base database using the provided key.

- Args
    * ``key (str)`: The key associated with the data to be retrieved. Equivalent to id or a primary key

- Returns
    * Any | None: The retrieved data or None if the database is not available or an error occurs.

**Example**
```python
key = "1122334455"
result = base.get(key)
```
---

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
    * `data:` Data to be stored. Can be a dictionary,
    a list, a string, an integer, or a boolean.
    Overrides an item if key already exists.
    
    * `key: (Optional)` The key associated with the data.
    Could be provided as function argument or a field in the data dict
    
    * `expire_in: (Optional)` Time in seconds until the data expires.
    
    * `expire_at: (Optional)` Unix timestamp or datetime when the data expires.

- Returns
    * The result of the storage operation or None if the database
    is not available or an error occurs.

**Example** 
```python
data = {"name" : John, "age" : 25}

base.put(data, key="custom_key", expire_in=300)
```
---

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
    * `items`: list whit items to be stored. Can be a list whit dictionaries,
        lists, strings, integers, or booleans.

    * `expire_in`: (Optional) Time in seconds until the data expires.

    * `expire_at`: (Optional) Unix timestamp or datetime when the data expires.

- Returns:
    * The result of the storage operation or None if the database
    is not available or an error occurs.

**Examples**:
```python
records = [
    {"name" : "John", "age" : 30},
    {"name" : "Tim", "age" : 45},
    {"name" : "Guido", "age" : 52},
]

db.put_all(records)
```

---

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
    * `updates(dict[dict | list | str | int | bool])`: The updated data.
    * `expire_in optional(int)`:Defaul value is None,
    * `expire_at optional(int|float|datetime)`: Default value is None

- Returns:
    Any | None: The result of the database update operation or None if the database is not available or an error occurs.

**Example**
```python
id_key = "1122334455"
update = {"name": "John", "age": 30}
expire_in = 60 # seconds

db.update(key=id_key, updates=update, expire_in=expire_in)
```

### delete
```python
base.delete(key: str):
```
Deletes data from the Deta BASE database using the provided key.

- Args:
    * `key (str)`: The key associated with the data to be deleted. Equivalent to id or a primary key

- Returns:
    Any | None: The result of the database delete operation or None if the database is not available or an error occurs.

**Example**
```python
key = "1122334455"
base.delete(key)
```