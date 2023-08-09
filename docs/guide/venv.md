
# How to Create a Virtual Environment

Before installing any Python package, it is a good practice to create and activate a virtual environment for your project to isolate its dependencies. You can choose one of the following methods to create a virtual environment:

## Creating

### With virtualenv
```bash
# Install virtualenv if you haven't already
pip install virtualenv

# Create a virtual environment
virtualenv enviroment_name
```

### With python -m venv
```bash
# Create a virtual environment named 'myenv'
python -m venv enviroment_name
```
Don't forget to substitute "environment_name" with a fitting name for your project. Usually, virtual environments are named "venv" or "env" as a common practice.


## Activating

### Activate in Windows
```shell
.\enviroment_name\Scripts\activate
```

### Activate in macOS / Linux
```bash
source enviroment_name/bin/activate
```









Creating a virtual environment allows you to keep your project dependencies separate from the global Python installation, providing a clean and isolated environment for your project. It is highly recommended to use virtual environments for Python projects to avoid conflicts between different packages and versions. Once the virtual environment is activated, you can proceed with the installation of Flask-Deta and other packages specific to your project.