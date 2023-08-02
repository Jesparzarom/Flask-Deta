from flask import Flask, request, redirect, url_for, Response, flash
from src.flask_deta import DetaBase, DetaDrive
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DETA_PROJECT_KEY= os.getenv("DETA_PROJECT_KEY")
DETA_DB_NAME = os.getenv("DETA_DB_NAME")
DETA_DRIVE_NAME = os.getenv("DETA_DRIVE_NAME")


app.config["SECRET_KEY"] = SECRET_KEY
app.config["DETA_PROJECT_KEY"] = DETA_PROJECT_KEY
app.config["DETA_DB_NAME"] = DETA_DB_NAME
app.config['DETA_DRIVE_NAME'] = DETA_DRIVE_NAME

db = DetaBase(app)
dd = DetaDrive(app)


@app.route("/", methods=["GET", "POST"])
def home():
    return redirect(url_for("get_all"))


@app.route("/add", methods=["GET", "POST"])
def add():
    content = {
        "apellido": "Hernandez",
        "apodos": "",
        "dni": "45552232",
        "edad": 15,
        "esMayor": False,
        "nombre": "Francisco",
        "otros": "",
    }
    try:
        result = db.push(content)
        if result:
            print({"success": True})
            return redirect(url_for("get_all"))
        else:
            return {"success": False}, 500
    except Exception as e:
        print(f"error {e}")

@app.route("/users", methods=["GET"])
def get_all():
    records = db.get_all()
    if records:
        return records
    else:
        return {"message": "No records found"}
    

@app.route("/users/<user>", methods=["GET"])
def get_one(user):
    record = db.get(user)  
    if record:
        return record
    else:
        return {"message": "No records found"}


def edit():
    data_key = ""
    new_values = ""
    update = db.edit(data_key, new_values)







@app.route("/pics", methods=["GET"])
def all_pics():
    pics_list = dd.all_files() 
    if pics_list:
        flash(message="RESPONSE IS OK", category="success")
        return pics_list
    else:
        return {"message": "No files found"}


@app.route("/pics/<user>", methods=["GET"])
def user_pic(user):
    pic = dd.get(user).read()
    response = Response(pic, content_type="image/png")
    if pic:
        return response
    else:
        return {"message": "No file found"}


@app.route("/save/<filename>", methods=["GET"])
def save(filename):
    PATH = f"C:/Users/fames/Pictures/programmacion/{filename}"
    file_path = PATH
    type = "image/png"
    save_pic = dd.save(filename, file_path=file_path, type=type) 
    if save_pic:
        return redirect(url_for("all_pics"))
    else:
        return {"message": "No file found"}



if __name__ == "__main__":
    app.run(debug=True)
