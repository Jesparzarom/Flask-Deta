## OVERVIEW
<a href="/">
    <img src="images/flaskdeta.png" width=100%/>
</a>


# ⚠️ Deprecation Notice

**Important:** This project is now deprecated and no longer maintained due to the discontinuation of Deta Base, which is a critical dependency.

### Reason for Deprecation
Deta, the platform supporting the database used by this module, has announced that they will cease operations for their services as of **October 17, 2024**. Starting from that date, all hosted apps, installed apps, horizons, websites, and data will be removed.

> "Space will keep running for 45 days until October 17, 2024. We will then start removing all apps (hosted or installed), horizons, websites and data.
>
> You can continue to login until sunset. We've built tools to export your data (and code for developers)."

For more details on Deta's announcement, please refer to their [official statement](https://flask-deta.readthedocs.io/en/stable/).

### Recommended Actions
- **Backup your data**: Ensure you have exported any necessary data and code before October 17, 2024, using the tools provided by Deta.
- **Explore Alternatives**: Consider migrating to other database solutions that align with your project's needs.

We appreciate your understanding and thank you for your support.

---

## Version 0.2.1
> ⚠️ This is the initial version 0.2.1 and is currently in the alpha development stage. It is not recommended for production use.

---

**Welcome to FlaskDeta Docs!**
[DEPRECATED]

Flask-Deta is a Python library that simplifies the integration of your [DetaSpace](https://deta.space/) collection of database and/or drive files with [Flask](https://flask.palletsprojects.com/en/2.3.x/) framework. 

With Flask-Deta, you can store and manage data with `DetaBase` and handle file storage operations with `DetaDrive`, all within the context of your Flask application. This robust combination allows you to leverage the secure and scalable cloud infrastructure of [DetaSpace](https://deta.space/), making data and file management for your web projects convenient. 

In this documents, we will provide you with an in-depth overview of Flask-Deta and help you get started using this extraordinary tool.

> We'd like to inform you that not all DetaSpace functionalities are currently integrated, both in Drive and Base. However, we are working on gradually incorporating them to create a robust integration package between Flask and DetaSpace. Our aim is to enhance your development experience by leveraging the full potential of this integration.

- [x] To learn more about DetaSpace visit the [DetaSpace documentation](https://deta.space/docs/en/).
- [x] To learn more about Flask visit the [Flask documentation](https://flask.palletsprojects.com/en/2.3.x/).

<!----------------------------USER GUIDE----------------------------------->
## User Guide
For comprehensive information on how to use Flask-Deta, please refer to our User Guide, which covers the following topics: 

- #####  Getting started
    * [Installation (DEPRECATED)](./guide/install.md)
    * [Configurations (DEPRECATED)](./guide/config.md)
    * [Quickstart (DEPRECATED)](./guide/start.md)
- ##### Api reference (DEPRECATED)
    * [DetaBase](./detabase/base.md)
    * [DetaDrive](./detadrive/drive.md)
- ##### About
    * [License](./about/LICENSE.md)
    * [Changes](./about/CHANGELOG.md)
    


<!----------------------------FEATURES----------------------------------->
## Key Advantages
- **Seamless Interaction:** Flask-Deta provides an intuitive and user-centric framework that seamlessly facilitates interactions with Deta Base and Deta Drive.

- **Comprehensive Versatility:** Unleash the capabilities of Flask-Deta to effortlessly store, retrieve, upload, download, and manage data through Deta Base, while also handling file management tasks using Deta Drive.

- **Effortless Integration:** Configuring Flask-Deta within your Flask application is a swift and straightforward process, allowing you to dedicate your efforts to the core development of your project.

<!----------------------------SOURCE CODE----------------------------------->
## Source Code

The **[source code](https://github.com/Jesparzarom/Flask-Deta)** of this project is available on GitHub and is open-source under the _BSD 3-Clause License_. We invite developers and contributors to explore the codebase. 

> The codebase relies on the Flask and Deta libraries, which are essential components driving the functionality of this project.

<!----------------------------ISSUES----------------------------------->

## Issues

If you find any issues or have ideas for improvements, feel free to open an issue on [GitHub Repo/issues](https://github.com/Jesparzarom/Flask-Deta/issues/new).

<!-----------------------------CHANGES---------------------------------->
## Changes
The changes can be found in the project [changelog](./about/CHANGELOG.md)

<!----------------------------lICENSE----------------------------------->
## License

Flask-Deta is licensed under the BSD 3-Clause License. See [LICENSE](./about/LICENSE.md) for more details.

By using this project, you agree to abide by the terms of the BSD 3-Clause License. We encourage you to review the license for more details. This license ensures that this project remains open-source and freely accessible to the community, fostering collaboration and innovation.



<!----------------------------AUTHOR/S----------------------------------->
## Authors

J.P. Esparza | [jesparzarom](https://github.com/Jesparzarom)



<!----------------------------SPONSORSHIP----------------------------------->
## Support this Project
If you value Deta-Flask and its continued growth, consider backing the project. Your support helps developers enhance the library, fix issues, and add features.

By backing Deta-Flask, you ensure a reliable tool for integrating DetaSpace's functionalities with Flask.

Your support is appreciated and fuels the project's success. Together, we can enhance Deta-Flask further!


<!----------------------------LOGO----------------------------------->
---
<a href="https://www.python.org/" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width=60/>
</a>
<a href="https://flask.palletsprojects.com/en/2.3.x/" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width=60/>
</a>
<a href="https://deta.space/" target="_blank">
    <img src="https://deta.space/landing-page/assets/logo.20539aa2.svg" width=235/>
</a>


> Our sincere thanks to the creators and maintainers of the Flask and Deta libraries, as well as the Python community.

---
