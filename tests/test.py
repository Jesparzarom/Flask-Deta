from flask import Flask, redirect, url_for, send_file
from src.Flask_Deta import DetaBase, DetaDrive

app = Flask(__name__)

# Set the DetaSpace project key and drive name
app.config["DETA_PROJECT_KEY"] = "e0zjojm64a9_ytQ518tbqJJyJUucmMsn5bhKQCzuuPEs"
app.config["BASE_NAME"] = "users"  # DetaSpace Base for data
app.config["DRIVE_NAME"] = "profilepics"  # DetaSpace Drive for files

# Create instances of DetaDrive
db = DetaBase(app)
dd = DetaDrive(app)


# ============== DETABASE CRUD TEST ===================


@app.route("/")
def home():
    return "<h1 style='text-align: center'>WELCOME TO DETA-FLASK TEST</h1>"


@app.route("/base/all")
def all():
    items = db.get_all()
    if items:
        return items
    else:
        return {"ERROR": "NO SE PUDO CONECTAR"}


@app.route("/base/one")
def one():
    item = db.get("juanesparza2023")
    print(item)
    if item:
        return item
    else:
        return {"ERROR": "NO SE PUDO CONECTAR"}


@app.route("/base/add/<index>")
def add(index):
    items = [
        {
            "apellido": "Pérez",
            "apodos": ["Pepe", "Perrito"],
            "dni": "78901234",
            "edad": "30",
            "esMayor": True,
            "nombre": "Juan",
        },
        {
            "apellido": "Ramos",
            "key": "ramitos2023",
            "apodos": ["Rami", "Rama"],
            "dni": "95555200",
            "edad": "20",
            "esMayor": True,
            "nombre": "Carlos",
        },
        {
            "apellido": "López",
            "apodos": ["Lopi", "Lopecito"],
            "dni": "45678901",
            "edad": "28",
            "esMayor": True,
            "nombre": "Luis",
            "otros": {"cumple": "05/10/1995"},
        },
    ]

    if int(index) >= 2:
        db.push(items[int(index)])
        return redirect(url_for("all"))
    else:
        return {"ERROR": "NO SE PUDO ENVIAR EL REGISTRO"}


@app.route("/base/addlist")
def add_all():
    items = [
        {
            "apellido": "González",
            "apodos": ["Gonza", "Gonzalito"],
            "dni": "12345678",
            "edad": "25",
            "esMayor": True,
            "nombre": "Laura",
        },
        {
            "apellido": "Rodríguez",
            "apodos": ["Rodri", "Rodrigo"],
            "dni": "98765432",
            "edad": "35",
            "esMayor": True,
            "nombre": "Pedro",
        },
        {
            "apellido": "Sánchez",
            "apodos": ["Sanche", "San"],
            "dni": "54321678",
            "edad": "40",
            "esMayor": True,
            "nombre": "Marta",
        },
        {
            "apellido": "Fernández",
            "apodos": ["Fer", "Fernandito"],
            "dni": "87654321",
            "edad": "18",
            "esMayor": False,
            "nombre": "Lucía",
        },
        {
            "apellido": "Gómez",
            "apodos": ["Gomi", "Gomita"],
            "dni": "13579246",
            "edad": "22",
            "esMayor": False,
            "nombre": "Alejandro",
        },
    ]
    if items:
        db.push_all(items, expire_in=60)
        return redirect(url_for("all"))
    else:
        return {"ERROR": "NO SE PUDO ENVIAR LA LISTA"}
    
@app.route("/base/del/<id>")
def del_one(id):
    if id:
        db.remove(id)
        return redirect(url_for("all"))
    else:
        return {"ERROR" : "NO SE PUDO BORRAR"}
    

@app.route("/base/edit/<key>/<ix>")
def edit(key, ix):
    updates = [
        {"apellido": "Martínez", "apodos": ["Marti", "Martincito"], "dni": "56789012", "edad": "22", "esMayor": False, "nombre": "Ana"},
        {"nombre": "Alejandro", "apellido": "Gómez", "apodos": ["Alex", "Ale"], "dni": "13579246", "edad": "22", "esMayor": False,},
        {"nombre": "Emily", "apellido": "Pérez", "apodos": ["Emi", "Emma"], "dni": "24681357", "edad": "28", "esMayor": True,},
        {"nombre": "Pierre", "apellido": "Martínez", "apodos": ["Pierrot", "Petit"], "dni": "24680135", "edad": "32", "esMayor": True,},
        {"nombre": "Anastasia", "apellido": "López", "apodos": ["Ana", "Nastya"], "dni": "13579135", "edad": "25", "esMayor": True,},
        {"nombre": "Sasha", "apellido": "González", "apodos": ["Sas", "Shura"], "dni": "80135791", "edad": "19", "esMayor": False,},
        {"nombre": "Isabelle", "apellido": "Sánchez", "apodos": ["Isa", "Isabelita"], "dni": "79135780", "edad": "26", "esMayor": True,}, 
    ]
    if key and id:
        db.edit(key, updates[int(ix)])
        return redirect(url_for("all"))
    else:
        return {"ERROR" : "NO SE PUDO BORRAR"}



# ============== DETADRIVE CRUD TEST ===================
@app.route("/drive/list")
def list_files():
    files = dd.get_all_files()
    if files:
        return files
    else:
        return {"NO FILES FOUND"}
    
@app.route("/drive/file/<name>")
def file(name):
    file = dd.get_file(name)
    if file:
        return send_file(file, mimetype="image/png")
    else:
        return {"NO FILE FOUND"}
    

@app.route("/drive/save/<name>")
def save(name):

    path=f"./tests/imgs/{name}"
    data = "This is a gift free icon logo"

    if dd.push_file(filename=name, data=data, type="img/png"):
        return redirect(url_for("list_files"))
    else:
        return {"NO FILES FOUND"}
    

@app.route("/drive/del/<name>")
def del_file(name):
    delete = dd.remove_file(name)
    if delete:
        return redirect(url_for("list_files"))
    else:
        return {"NO FILES FOUND"}


# ============== RUN THE APP ===================
if __name__ == "__main__":
    app.run(debug=True)
