# BLOG_API

BLOG_API is a web application that allows users to create, read, update, and delete blog posts. It provides a RESTful API for managing blogs and comments, allowing users to perform CRUD (Create, Read, Update, Delete) operations on blog posts and associated comments.

The application is built using Flask, a lightweight Python web framework, and utilizes a repository pattern to interact with the data storage. It provides endpoints for creating new blogs, retrieving blogs by ID, updating existing blogs, and deleting blogs. Additionally, users can add comments to specific blog posts, retrieve comments for a blog post, update comments, and delete comments.

This project is designed to showcase the implementation of a basic blog API using Flask and best practices for building RESTful APIs. It can serve as a starting point for developing more advanced blog applications or as a learning resource for Flask and web API development.
Please note that in a production environment, it is recommended to use databases such as PostgreSQL, MySQL, or MongoDB for data storage. This project uses in-memory data storage as a simplified development approach.


## Installation

1. Clone the repository:

```shell
   git clone https://github.com/mdamatoc/blog_api.git
```


2. Navigate to the project directory:
```shell
cd blog_api
```

3. Create a virtual environment (optional but recommended):
```shell
python3 -m venv env
source env/bin/activate
```

4. Install the dependencies:
```shell
pip install -r requirements.txt
```

5. Usage
Start the application:

```shell
python app.py
```
