# Blog

This is a full-stack blog application with a CMS admin panel, user rights, article management, comments, tags, and search.

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

*   Python 3.x
*   pip

### Installation

1.  Clone the repo
    ```sh
    git clone https://github.com/leopixel1/your_repository_.git
    ```
2.  Install PIP packages
    ```sh
    pip install -r requirements.txt
    ```
3.  Apply migrations
    ```sh
    python manage.py migrate
    ```
4.  Run the development server
    ```sh
    python manage.py runserver
    ```

### Running the Frontend

1.  Navigate to the `frontend` directory
    ```sh
    cd frontend
    ```
2.  Install NPM packages
    ```sh
    npm install
    ```
3.  Run the development server
    ```sh
    npm start
    ```

## Tech Stack

*   **Backend:** Django, Django REST Framework
*   **Frontend:** React
*   **Database:** SQLite (for development)