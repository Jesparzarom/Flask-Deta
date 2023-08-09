# QuickStart

1. **Create a Flask App:** Begin by creating an instance of the Flask app in your Python code.

2. **Set Configuration Parameters:** Set the required parameters, such as your Deta project key, Base name, and Drive name.

3. **Create DetaBase and DetaDrive Instances:** Create instances of DetaBase and DetaDrive using your Flask `app` as an argument.


## DetaBase

Explore the complete usage and available methods in our [**DetaBase** documentation](../detabase/base.md)

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



## DetaDrive

Explore the complete usage and available methods in our [**DetaDrive** documentation](../detadrive/drive.md)

```python
from flask import Flask
from flask_deta import DetaDrive

app = Flask(__name__)

# Set the DetaSpace project key and drive name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["DRIVE_NAME"] = "icons" # DetaSpace Drive for files

# Create instances of DetaDrive
dd = DetaDrive(app)

```


## DetaBase + DetaDrive

Integrate the features of DetaBase and DetaDrive seamlessly into your Flask application with. These components enable efficient storage and management of data and files within your project using DetaSpace.

For comprehensive details on the usage and available methods, refer to our documentation: [DetaBase](../detabase/base.md) & [DetaDrive](../detadrive/drive.md).

```python
from flask import Flask
from flask_deta import DetaBase, DetaDrive

app = Flask(__name__)

# Set the DetaSpace project key and drive name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["BASE_NAME"] = "products" # DetaSpace Base for data 
app.config["DRIVE_NAME"] = "icons" # DetaSpace Drive for files

# Create instances of DetaDrive
db = DetaBase(app)
dd = DetaDrive(app)

```