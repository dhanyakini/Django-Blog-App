# MyBlog - A Django Blog Application

## Project Overview
**MyBlog** is a Django-based blog application that enables users to create, edit, and manage blog posts. This app provides a simple interface for CRUD (Create, Read, Update, Delete) operations on blog posts, making it easy for users to share their thoughts, stories, or any content they like.

## Features
- **Create, Edit, and Delete Blog Posts**: Users can add new blog posts, update existing ones, and delete posts.
- **List View**: Displays all blog posts in a list format for easy browsing.
- **Details View**: Provides a detailed view of each blog post.
- **User Authentication** (if implemented): Supports login and registration for secure access.
- **Responsive Design**: Optimized for desktop and mobile viewing.

## Tech Stack
- **Django**: Back-end framework for building web applications in Python.
- **HTML, CSS**: Front-end technologies for structure and styling.
- **SQLite** (default, or specify if you’ve changed it): Database for storing blog post data.

## Project Structure
```
MyBlog/
│
├── blog/                   # Main app for blog functionalities
│   ├── migrations/         # Database migrations
│   ├── static/             # Static files (CSS, JavaScript, images)
│   ├── templates/          # HTML templates for the blog
│   ├── views.py            # Views for handling user requests
│   ├── models.py           # Database models for blog posts
│   ├── urls.py             # URL routing for the blog app
│   ├── forms.py            # Forms for creating and editing posts
│   └── admin.py            # Admin interface configuration
│
├── MyProject/              # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL configuration for the project
│   └── wsgi.py             # WSGI entry-point for deployment
│
├── manage.py               # Django command-line utility
└── requirements.txt        # List of dependencies
```

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dhanyakini/my-blog-app.git
   cd my-blog-app
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For MacOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the app**:
   - Open your browser and go to `http://127.0.0.1:8000/` to view the application.

## Usage
- **Creating Posts**: Navigate to the "New Post" section to create a new blog post.
- **Editing and Deleting Posts**: Use the Edit and Delete buttons in the details view of a post.
- **Viewing Posts**: Browse the homepage to see a list of all posts and click on each to view details.

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Any contributions are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
