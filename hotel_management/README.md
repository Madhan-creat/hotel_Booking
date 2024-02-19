# HOTEL_MANEGEMENT

## Prerequisites

Make sure you have the following installed:

- Python (3.x recommended)
- pip (Python package installer)
- virtualenv (optional but recommended)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```Terminal
    cd hotel_management
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    virtualenv hotel_env
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        hotel_env\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source hotel_env/bin/activate
        ```

5. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser for the Django admin (follow the prompts):

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

The project should now be running at http://127.0.0.1:8000/.


