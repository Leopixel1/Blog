# Full-Stack Blog Application

This is a full-stack blog application built with a Django backend and a React frontend. It includes a CMS admin panel, user rights, article management, comments, tags, and search functionality.

## Project Structure

This project is organized into two main parts: a Django backend and a React frontend.

-   `blog/`: A Django app that contains the models, views, and other logic for the blog functionality.
-   `blog_project/`: The main Django project folder. It contains project-level settings, URL configurations, and the WSGI entry point. This is a standard convention in Django projects.
-   `frontend/`: A React application created with Create React App, which serves as the user interface.
-   `manage.py`: A command-line utility for interacting with the Django project.
-   `db.sqlite3`: The SQLite database file used for development.

## Tech Stack

-   **Backend:** Django, Django REST Framework
-   **Frontend:** React
-   **Database:** SQLite (for development)

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

-   Python 3.x
-   Node.js and npm
-   pip

### Backend Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/leopixel1/your_repository_.git
    cd your_repository_
    ```

2.  **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

4.  **Run the Django development server:**
    ```sh
    python manage.py runserver
    ```

    The backend API will be available at `http://127.0.0.1:8000/`.

### Frontend Setup

1.  **Navigate to the frontend directory** (in a new terminal):
    ```sh
    cd frontend
    ```

2.  **Install Node.js dependencies:**
    ```sh
    npm install
    ```

3.  **Run the React development server:**
    ```sh
    npm start
    ```

    The frontend application will be available at `http://localhost:3000`.

## Available Frontend Scripts

In the `frontend` directory, you can run:

-   `npm start`: Runs the app in development mode.
-   `npm test`: Launches the test runner in interactive watch mode.
-   `npm run build`: Builds the app for production into the `build` folder.

For more information, you can refer to the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).
