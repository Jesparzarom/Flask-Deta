
# Quickstart

1. **Install** Flask-Deta. See more in [installation](./install.md)

2. **Create a Flask App:** Begin by creating an instance of the Flask app in your Python code.

3. **Set Configuration Parameters:** Set the required parameters, such as your Deta project key, Base name, and Drive name. See more in [configurations](./config.md)

4. **Create DetaBase and DetaDrive Instances:** You can easily create instances of DetaBase and DetaDrive by using your Flask app as an argument, either directly or by utilizing the `init_app(app)` method.

**Install**
```shell
pip install flask-deta
```

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