# Usage

---

This is a simple guide on how to integrate Deta with your Flask application using the `flask-deta` package. DetaSpace is a cloud-based backend service that allows you to store and manage data in a scalable and efficient manner.

## Prerequisites

Before you begin, make sure you have the following:

1. Python installed on your system.
2. A Deta account. You can sign up for a free account at https://deta.sh/.

## Installation

1. Install `flask-deta` package using pip:

```bash
pip install flask-deta
```

2. Create a new Flask project or open your existing Flask project.

3. Import the necessary modules:

```python
from flask import Flask, request, jsonify
from flask_deta import DetaSpace
```

## Initialization

1. Create a new Flask app:

```python
app = Flask(__name__)
```

2. Set the Deta configuration using your secret key and database name:

```python
app.config["DETA_SECRET_KEY"] = "YOUR_SECRET_KEY"
app.config["DETA_DB_NAME"] = "YOUR_DATABASE_NAME"
```

## DetaSpace Integration

1. Initialize the `DetaSpace` class with your Flask app:

```python
db = DetaSpace(app=app)
```

The `DetaSpace` class will handle the connection to the Deta backend using your provided secret key and database name.

## Usage

You can now use the `db` instance to interact with your Deta database.

### Creating a Record

To create a new record in the database, use the `create` method:

```python
@app.route("/create", methods=["POST"])
def create_record():
    data = request.get_json()
    result = db.create(data)
    if result:
        return {"success": True}
    else:
        return {"success": False}, 500
```

### Fetching All Records

To fetch all records from the database, use the `get_all` method:

```python
@app.route("/view_all", methods=["GET"])
def view_all_records():
    records = db.get_all()
    records_list = []  # Initialize an empty list to store the records
    for record in records.iterall():
        records_list.append(record)  # Append each record to the list
    return jsonify(records_list)
```

## Run the App

Finally, run your Flask app:

```bash
python app.py
```

Your Flask app is now integrated with Deta, and you can start creating and fetching records from the database.

Remember to handle error cases and implement additional features as needed for your specific use case.

That's it! You've successfully integrated Deta with your Flask application using `flask-deta`. Enjoy building scalable and efficient applications with Deta's powerful backend service!