# Flask-Deta Configuration

Define the required configuration keys, such as your Deta project key, Base name, and Drive name.

Example:
```python
# Imports
from flask import Flask
from flask_deta import DetaBase, DetaDrive

# Flask app instance
app = Flask(__name__)

# Configuration keys
app.config["DETA_PROJECT_KEY"] = "MyKey123"
app.config["BASE_NAME"] = "products" # For DetaBase
app.config["DRIVE_NAME"] = "icons" # For DetaDrive
```

## Configuration Keys

---

### flask_deta.config.DETA_PROJECT_KEY

*This key is used to set your Deta project key, which is required for connecting to your Deta account.

```python
# Usage
app.config["DETA_PROJECT_KEY"] = "MyKey123"
```

---

### flask_deta.config.BASE_NAME

This key is used to set the base name when working with DetaBase. It identifies the specific DetaBase you want to interact with.

```python
# Usage
app.config["BASE_NAME"] = "products" # For DetaBase
```

---

### flask_deta.config.DRIVE_NAME

This key is used to set the drive name when working with DetaDrive. It specifies the DetaDrive instance you want to work with.

```python
# Usage
app.config["DRIVE_NAME"] = "icons" # For DetaDrive
```