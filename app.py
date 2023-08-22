from flask import Flask, render_template
from src.flask_deta import DetaBase, DetaDrive


app = Flask(__name__)

# Set the DetaSpace project key and drive name
app.config["DETA_PROJECT_KEY"] = "e03pugxae2g_mJzHnruUs5vCrwdW28C5YXUDu552CMZN"
app.config["BASE_NAME"] = "users"  # DetaSpace Base for data
app.config["DRIVE_NAME"] = "icons"  # DetaSpace Drive for files

# Create instances of DetaDrive and DetaBase
base = DetaBase()
drive = DetaDrive()


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


# DetaBase instance
@app.route("/data")
def all_records():
    data = base.get_all()
    return data

# DetaDrive instance
@app.route("/files")
def all_files():
    files = drive.all_files()
    return files


base.init_app(app)
drive.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
