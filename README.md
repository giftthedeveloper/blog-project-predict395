# Django Blog Project

This is a simple blog application built with Django. The application allows users to create, edit, delete, and view blog posts.

## Features

- List all blog posts
- View details of a single blog post
- Create new blog post
- Edit existing blog post
- Delete a blog post

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed on your system:

- Python (>= 3.9)
- pip (Python package installer)
- Virtualenv (recommended)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/giftthedeveloper/blog-project-predict365.git
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    You will be provided with a `.env` file containing necessary environment variables. Place this file in the root directory of your project.

### Database Setup

1. **Apply the migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

2. **Create a superuser to access the admin interface:**

    ```sh
    python manage.py createsuperuser
    ```

### Running the Server

1. **Start the development server:**

    ```sh
    python manage.py runserver
    ```

2. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.

### Testing the Application

To test the functionalities of the application:

1. **List Blog Posts:**
    - Go to `http://127.0.0.1:8000/blog/`
    - You should see a list of all blog posts. If there are no posts, create a new one.

2. **View Blog Post Detail:**
    - Click on any blog post title from the list to view its details.

3. **Create a New Blog Post:**
    - Click on the "New Post" button.
    - Fill in the form and click "Save".
    - You will be redirected to the blog post detail page of the newly created post.

4. **Edit a Blog Post:**
    - From the blog post list or detail view, click the "Edit" button on a post.
    - Modify the post details and click "Save".
    - You will be redirected to the updated blog post detail page.

5. **Delete a Blog Post:**
    - From the blog post list or detail view, click the "Delete" button on a post.
    - The post will be deleted and you will be redirected to the blog post list.

### Deployment

To deploy the application to a production environment, consider the following:

- Use a production-ready database such as PostgreSQL.
- Set up a web server such as Gunicorn.
- Use a reverse proxy such as Nginx.
- Ensure static files are correctly served.
- Secure the application with HTTPS.

### License


### Contact



