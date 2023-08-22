# Change Log

_All notable changes to this project will be documented in this file._

_The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)._

## Unreleased
- none

## Version 0.2.0
<small>Release in 2023-08-22</small>

**Added**

- Added the "init_app" method to DetaBase and DetaDrive to support Flask modularity.
  
- Separated the connection logic; connection logic is now internal to each class (DetaBase and DetaDrive) for simplicity.

- Added an optional "limit" parameter to the "get_all" method in DetaBase, allowing customization of the number of elements to retrieve.

- Added an optional "limit" parameter to the "all_files" method in DetaDrive, allowing customization of the number of files to retrieve.

- Introduced a "verify_setups" function in "validator.py," which verifies DetaSpace configuration and connection setups. It checks for the presence of keys and names and their existence. This function works for both DetaDrive and DetaBase.

**Changed**

- Renamed files containing "DetaDrive" to "deta_drive.py" and "DetaBase" to "deta_base.py."

**Removed**

- Removed unnecessary and/or empty files.

**Fixed**

- Implemented general and specific error handling in both classes within the Flask context.

**Updated**

- Updated the documentation.

## Version 0.1.1
<small>Release in 2023-08-09</small>

- Initial release of Flask-Deta.
