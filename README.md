# TourCRM Backend

This repository contains the backend services for the TourCRM application, built entirely with Django. It provides the necessary APIs to manage tours, customers, bookings, and other related functionalities for a customer relationship management system tailored for tour operators.

## Features

-   User authentication and authorization
-   Tour management (create, read, update, delete tours)
-   Customer management
-   Booking management
-   Reporting and analytics

## Technologies Used

*   **Language:** Python
*   **Framework:** Django
*   **Database:** MySql
*   **ORM:** Django ORM
*   **Other Libraries/Tools:** [e.g., Django REST Framework, Celery, Redis, Docker, Testing Frameworks like Pytest/unittest]

## Folder Structure

This project follows a standard Django project structure with an `apps` directory for modular applications and a `config` directory for project-wide settings.

```
.
├── apps/                 # Contains individual Django applications
│   ├── accounts/         # User authentication, authorization, organizations, roles
│   │   ├── migrations/   # Database schema changes for the accounts app
│   │   ├── models/       # Django models for users, organizations, roles, invites
│   │   ├── serializers/  # Django REST Framework serializers for API data
│   │   ├── services/     # Business logic and service functions
│   │   ├── views/        # API view logic
│   │   ├── admin.py      # Django admin configurations
│   │   ├── apps.py       # App configuration
│   │   ├── urls.py       # URL routing for the accounts app
│   │   └── tests.py      # Unit and integration tests
│   └── # ... other Django apps (e.g., tours, bookings)
├── config/               # Project-level configuration
│   ├── settings/         # Environment-specific settings (base, dev, prod)
│   │   ├── base.py       # Base settings common to all environments
│   │   ├── dev.py        # Development-specific settings
│   │   ├── prod.py       # Production-specific settings
│   ├── asgi.py           # ASGI configuration for async applications
│   ├── urls.py           # Main URL dispatcher for the project
│   └── wsgi.py           # WSGI configuration for synchronous applications
├── manage.py             # Django's command-line utility for administrative tasks
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Prerequisites

Before you begin, ensure you have met the following requirements:

*   Python 3.x installed (e.g., Python 3.9+)
*   [Your chosen database] installed and running (e.g., PostgreSQL)
*   `pip` (Python package installer)

## Installation

Follow these steps to set up the project locally:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/tourcrm-backend.git
    cd tourcrm-backend
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Setup:**

    *   Ensure your database server is running.
    *   Create a database named `TRavel_crm` (or as configured in your `.env` file).
    *   Run database migrations to apply the schema:

        ```bash
        python manage.py migrate
        ```

    *   (Optional) Create a superuser to access the Django admin:

        ```bash
        python manage.py createsuperuser
        ```

    *   (Optional) Seed the database with initial data (if you have a management command for it):

        ```bash
        # Example command, if available
        python manage.py seed_data
        ```

## Configuration

Environment variables are used for sensitive information and configuration settings. Create a `.env` file in the root of the project based on a `.env.example` (you might need to create this file if it doesn't exist, mirroring the variables in `config/settings/base.py`, `dev.py`, etc.):

```
# Example .env.example content (adjust based on your actual settings)
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@host:port/tourcrm_db
# Add other environment variables as needed, e.g., for email, API keys
```

*   **`SECRET_KEY`**: A unique and unpredictable secret key for Django. **Crucial for security in production.**
*   **`DEBUG`**: Set to `True` for development, `False` for production.
*   **`DATABASE_URL`**: Your database connection string.
*   [List any other crucial environment variables and their purpose.]

## Running the Application

To start the Django development server:

```bash
python manage.py runserver
```

The application should now be running at `http://localhost:8000/`. You can access the Django admin panel at `http://localhost:8000/admin/`.

## API Endpoints

The backend exposes a RESTful API. For detailed information on available endpoints, request/response formats, and authentication, please refer to the API documentation (if available) or explore the `urls.py` files within each app.

### Example Endpoints (based on your `accounts` app):

*   `POST /api/v1/accounts/register/` - User registration
*   `POST /api/v1/accounts/login/` - User login
*   `GET /api/v1/accounts/organizations/` - Get organization details (example, adjust as per your views)
*   [Add more endpoints as your project grows, e.g., for tours, bookings, etc.]

## Running Tests

To run the project's test suite:

```bash
python manage.py test
```

## Contributing

We welcome contributions! Please follow these steps to contribute:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes and ensure they adhere to Django's coding conventions and best practices.
4.  Write comprehensive tests for your changes.
5.  Commit your changes (`git commit -m 'feat: Add new feature X'`).
6.  Push to the branch (`git push origin feature/your-feature-name`).
7.  Open a Pull Request.

## License

This project is licensed under the [Specify License, e.g., MIT License] - see the [LICENSE.md](LICENSE.md) file for details.
