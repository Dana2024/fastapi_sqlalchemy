# React FastAPI SQLAlchemy Project

This project showcases a simple one-page React app that allows users to submit their favorite flavor. 
The flavor data is collected through the React frontend, sent to the FastAPI backend, and stored in a SQLite database using SQLAlchemy. 
Users can also retrieve all the saved flavors through the API.

## Prerequisites

I had the following software installed:

- [Node.js](https://nodejs.org/) - JavaScript runtime environment for the frontend.
- [Python](https://www.python.org/) - Programming language for the backend.
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast (high-performance) web framework for building APIs.
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and Object-Relational Mapping (ORM) library.
- [SQLite](https://www.sqlite.org/) - Self-contained, serverless, zero-configuration, transactional SQL database.

### Usage
Access the React frontend at http://localhost:3000.

Submit your favorite flavor through the provided input form on the webpage. 
The flavor data will be sent to the FastAPI backend and stored in the database.

To retrieve all flavors saved in the database, make a GET request to http://localhost:8000/flavors.

### Frontend page
![ice-cream-shop](https://github.com/Dana2024/fastapi_sqlalchemy/assets/130597970/366d2d90-0717-48ff-bbcb-be84015cf4c3)

### Fast API GET endpoint returning all the saved items
![fastapi-get](https://github.com/Dana2024/fastapi_sqlalchemy/assets/130597970/d35e203a-b739-4e11-8963-814ae5d607f0)



