**`README.md`**

```markdown
# Job Search App Backend

This is the backend for a job search web application built with FastAPI, MongoDB, and JWT authentication. It includes endpoints for user registration, login, logout, and job search functionality.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/job-search-backend.git
   cd job-search-backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install MongoDB:**

   Follow the instructions to install MongoDB from the [official documentation](https://docs.mongodb.com/manual/installation/).

5. **Run MongoDB:**

   ```bash
   brew services start mongodb/brew/mongodb-community  # For macOS with Homebrew
   mongod  # Alternatively, start the MongoDB server
   ```

## Configuration

1. **Create a `.env` file in the root directory and add the following environment variables:**

   ```env
   MONGODB_URI=mongodb://localhost:27017/job_search
   SECRET_KEY=your_jwt_secret_key
   ```

## Running the Application

1. **Run the import script to load job data into MongoDB:**

   ```bash
   python import_jobs.py
   ```

2. **Start the FastAPI server:**

   ```bash
   uvicorn app.main:app --reload
   ```

   The server will be running at `http://localhost:8000`.

## API Endpoints

### Auth Endpoints

- **`POST /api/auth/signup`**

  Registers a new user.

  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```

- **`POST /api/auth/login`**

  Logs in a user and returns an access token.

  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```

  Response:

  ```json
  {
    "access_token": "your_jwt_token"
  }
  ```

- **`POST /api/auth/logout`**

  Logs out a user by invalidating their token.

### Job Endpoints

- **`GET /api/jobs`**

  Searches for jobs by title. Requires an authorization token.

  Query Parameters:

  - `title`: The job title to search for.

  Headers:

  ```http
  Authorization: Bearer your_jwt_token
  ```

  Response:

  ```json
  [
    {
      "job_name": "Software Engineer",
      "company_name": "Tech Company"
    }
  ]
  ```

## License

This project is licensed under the MIT License.
```


### Project Structure

Here’s a reminder of the project structure for clarity:

```
job-search-backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── jobs.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
├── import_jobs.py
├── pyproject.toml
├── requirements.txt
├── .env
└── README.md
```

This README provides all the necessary information to set up and run the backend for the job search application, including installation steps, configuration, and API endpoint details.