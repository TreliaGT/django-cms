# Headless CMS (Work in Progress)

This project is a **work in progress** aimed at creating a **headless CMS** built with Django.

## Overview

The goal is to build a flexible, scalable content management system that serves content via APIs without being tied to any frontend framework — perfect for modern web apps, mobile apps, and more.

## Current Status

- Core architecture is being developed
- Basic app structure in place (`pages`, `adminpanel`, etc.)
- Context processors and template setup underway
- Headless API endpoints to be implemented soon


## How To start

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    ```

    - On **Windows**, activate with:

      ```bash
      env\Scripts\activate
      ```

    - On **macOS/Linux**, activate with:

      ```bash
      source env/bin/activate
      ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

**Install npm dependencies:**

    ```bash
    npm install
    ```

7. **Build frontend assets (if applicable):**

    ```bash
    npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
    ```

8. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

9. **Access the site:**

    Open your browser and go to:  
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## Generate Defaults 
python manage.py setup_posttypes_and_roles
