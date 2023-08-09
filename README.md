## Version 0.1.1
> ⚠️ This is the initial version 0.1.0 and is currently in the alpha stage. It is not recommended for professional production use.

---

**Welcome to FlaskDeta Docs!**

Flask-Deta is a Python library that simplifies the integration of your [DetaSpace](https://deta.space/) collection of database and/or drive files with [Flask](https://flask.palletsprojects.com/en/2.3.x/) framework. 

With Flask-Deta, you can store and manage data with `DetaBase` and handle file storage operations with `DetaDrive`, all within the context of your Flask application. This robust combination allows you to leverage the secure and scalable cloud infrastructure of [DetaSpace](https://deta.space/), making data and file management for your web projects convenient. 

In this documents, we will provide you with an in-depth overview of Flask-Deta and help you get started using this extraordinary tool.

> We'd like to inform you that not all DetaSpace functionalities are currently integrated, both in Drive and Base. However, we are working on gradually incorporating them to create a robust integration package between Flask and DetaSpace. Our aim is to enhance your development experience by leveraging the full potential of this integration.
# Install
```shell
pip install flask-deta
```

# QuickStart

1. **Create a Flask App:** Begin by creating an instance of the Flask app in your Python code.

2. **Set Configuration Parameters:** Set the required parameters, such as your Deta project key, Base name, and Drive name.

3. **Create DetaBase and DetaDrive Instances:** Create instances of DetaBase and DetaDrive using your Flask `app` as an argument.


## DetaBase
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

For comprehensive details on the usage and available methods, refer to our documentation: [DetaBase](./docs/DetaBase/base.md) & [DetaDrive](./docs/DetaDrive/drive.md).