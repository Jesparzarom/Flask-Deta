## Version 0.2.1
> ⚠️ This is the initial version 0.2.1 and is currently in the alpha stage. It is not recommended for production use.

---

**Welcome to FlaskDeta README!**

**For a more detailed use, I recommend you to visit the [Flask-Deta documentation](https://flask-deta.readthedocs.io/en/latest/)**

Flask-Deta is a Python library that simplifies the integration of your [DetaSpace](https://deta.space/) collection of database and/or drive files with [Flask](https://flask.palletsprojects.com/en/2.3.x/) framework. 

With Flask-Deta, you can store and manage data with `DetaBase` and handle file storage operations with `DetaDrive`, all within the context of your Flask application. This robust combination allows you to leverage the secure and scalable cloud infrastructure of [DetaSpace](https://deta.space/), making data and file management for your web projects convenient. 

In this documents, we will provide you with an in-depth overview of Flask-Deta and help you get started using this extraordinary tool.

> We'd like to inform you that not all DetaSpace functionalities are currently integrated, both in Drive and Base. However, we are working on gradually incorporating them to create a robust integration package between Flask and DetaSpace. Our aim is to enhance your development experience by leveraging the full potential of this integration.

- To learn more about DetaSpace visit the [DetaSpace documentation](https://deta.space/docs/en/).
- To learn more about Flask visit the [Flask documentation](https://flask.palletsprojects.com/en/2.3.x/).

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

# DetaBase.get_all()
@app.route("/data")
def all_records():
    data = base.get_all()
    return data

if __name__ == "__main__":
    app.run(debug=True)
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
drive = DetaDrive(app)

# DetaDrive.all_files()
@app.route("/files")
def all_files():
    files = drive.all_files()
    return files

if __name__ == "__main__":
    app.run(debug=True)
```

## DetaDrive + DetaBase
```python
from flask import Flask
from flask_deta import DetaBase, DetaDrive

app = Flask(__name__)

# Set the DetaSpace project key, database name and drive name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["BASE_NAME"] = "products" # DetaSpace Base for data 
app.config["DRIVE_NAME"] = "icons" # DetaSpace Drive for files

# Create instances of DetaDrive and DetaBase
base = DetaBase(app)
drive = DetaDrive(app)

# DetaBase.get_all()
@app.route("/data")
def all_records():
    data = base.get_all()
    return data

# DetaDrive.all_files()
@app.route("/files")
def all_files():
    files = drive.all_files()
    return files

if __name__ == "__main__":
    app.run(debug=True)
```

## Using `init_app()`
To ensure modularity and easy integration, the `init_app()` method is provided for initializing both DetaBase and DetaDrive separately. This approach allows you to configure and associate the extensions with your Flask application in a standardized manner.

### DetaBase.`init_app`
```python
from flask import Flask
from flask_deta import DetaBase

app = Flask(__name__)

# Set the DetaSpace project key and database name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["BASE_NAME"] = "products" # DetaSpace Base for data 

# Create an instance of DetaBase
base = DetaBase()

@app.route("/all")
def all_data():
    data = base.get_all()
    return data

base.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
```

### DetaDrive.`init_app`
```python
from flask import Flask
from flask_deta import DetaDrive

app = Flask(__name__)

# Set the DetaSpace project key and drive name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["DRIVE_NAME"] = "icons" # DetaSpace Drive for files

# Create an instance of DetaDrive
drive = DetaDrive()

@app.route("/files")
def files():
    files = drive.all_files()
    return files

drive.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
```

### DetaBase.init_app + DetaDrive.init_app
```python
app = Flask(__name__)

# Set the DetaSpace project key and drive name
app.config["DETA_PROJECT_KEY"] = "MyKey12345"
app.config["BASE_NAME"] = "products"  # DetaSpace Base for data
app.config["DRIVE_NAME"] = "icons"  # DetaSpace Drive for files

# Create instances of DetaDrive and DetaBase
base = DetaBase()
drive = DetaDrive()

# Home
@app.route("/")
def home():
    links = """
    <head>
        <title>Flask-Deta</title>
        <style>
            body {
                background: antiquewhite;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
            }

            h1 {
                color: darkslateblue;
            }

            a {
                display: block;
                margin: 10px auto;
                padding: 10px;
                width: 200px;
                background-color: deepskyblue;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s ease-in-out;
            }

            a:hover {
                background-color: dodgerblue;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Flask-Deta</h1>
        <div>
            <a href="/data" target="_blank">
                Get all data list
            </a>
            <a href="/files" target="_blank">
                Get all files list
            </a>
        </div>
    </body>
    """
    return links


# DetaBase.get_all()
@app.route("/data")
def all_records():
    data = base.get_all()
    return data

# DetaDrive.all_files()
@app.route("/files")
def all_files():
    files = drive.all_files()
    return files


base.init_app(app)
drive.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
```

Visit the [Flask-Deta documentation](https://flask-deta.readthedocs.io/en/latest/)