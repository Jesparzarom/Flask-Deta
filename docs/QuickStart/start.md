# QuickStart

1. **Create a Flask App:** Begin by creating an instance of the Flask app in your Python code.

2. **Set Configuration Parameters:** Set the required parameters, such as your Deta project key, Base name, and Drive name.

3. **Create DetaBase and DetaDrive Instances:** Create instances of DetaBase and DetaDrive using your Flask `app` as an argument.


## DetaBase
```python
from flask import Flask
from deta_flask import DetaBase

app = Flask(__name__)

# Set the DetaSpace project key and database name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["DETA_DB_NAME"] = "products" # DetaSpace Base for data 

# Create instance of DetaBase
db = DetaBase(app)
```


## DetaDrive
```python
from flask import Flask
from deta_flask import DetaDrive

app = Flask(__name__)

# Set the DetaSpace project key and drive name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["DETA_DRIVE_NAME"] = "brands" # DetaSpace Drive for files

# Create instances of DetaDrive
dd = DetaDrive(app)

```


## DetaBase + DetaDrive
```python
from flask import Flask
from deta_flask import DetaBase, DetaDrive

app = Flask(__name__)

# Set the DetaSpace project key and drive name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["DETA_DB_NAME"] = "products" # DetaSpace Base for data 
app.config["DETA_DRIVE_NAME"] = "brands" # DetaSpace Drive for files

# Create instances of DetaDrive
db = DetaBase(app)
dd = DetaDrive(app)

```