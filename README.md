# Expense Tracker API

This is a FastAPI application that allows users to track their expenses. Users can register, login, and manage their expenses through various API endpoints.

## Setup and Installation

1. Clone the repository
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic python-jose python-multipart
   ```
4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Access the API documentation at: `http://127.0.0.1:8000/docs`

## API Endpoints

### Authentication

#### Register a New User

- **Endpoint**: `POST /auth/register`
- **Description**: Create a new user account
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword"
  }
  ```
- **Response**: User details with ID

#### Login

- **Endpoint**: `POST /auth/login`
- **Description**: Login with email and password to get an access token
- **Request Body**:
  ```json
  {
    "username": "john@example.com",
    "password": "securepassword"
  }
  ```
- **Response**: JWT access token
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1...",
    "token_type": "bearer"
  }
  ```

> **Important**: After logging in, you must include the JWT token in the header of all subsequent requests as follows:
>
> ```
> token: eyJhbGciOiJIUzI1...
> ```

### Expenses

#### Create an Expense

- **Endpoint**: `POST /expenses/`
- **Auth Required**: Yes (JWT token)
- **Request Body**:
  ```json
  {
    "amount": 25.5,
    "description": "Lunch at restaurant",
    "category": "FOOD",
    "created_at": "2023-05-15"
  }
  ```
- **Response**: Created expense details

#### Get All Expenses

- **Endpoint**: `GET /expenses/`
- **Auth Required**: Yes (JWT token)
- **Response**: List of all expenses for the authenticated user

#### Get Expense by ID

- **Endpoint**: `GET /expenses/{expense_id}`
- **Auth Required**: Yes (JWT token)
- **Response**: Details of the specified expense

#### Get Expenses by Category

- **Endpoint**: `GET /expenses/category/{expense_category}`
- **Auth Required**: Yes (JWT token)
- **Path Parameters**:
  - `expense_category`: One of `FOOD`, `TRANSPORTATION`, `ENTERTAINMENT`, `INVESTMENT`, `OTHER`
- **Response**: List of expenses in the specified category

#### Update an Expense

- **Endpoint**: `PUT /expenses/id-update/{expense_id}`
- **Auth Required**: Yes (JWT token)
- **Request Body**: Same as for creating an expense
- **Response**: Updated expense details with success message

#### Delete an Expense

- **Endpoint**: `DELETE /expenses/id-delete/{expense_id}`
- **Auth Required**: Yes (JWT token)
- **Response**: 204 No Content (successful deletion)

## Authentication Flow

1. **Register**: Create a new user account using the `/auth/register` endpoint.
2. **Login**: Use the `/auth/login` endpoint with your email and password to get a JWT token.
3. **Use the Token**: Include the token in the `token` header of all subsequent requests.

Example workflow in Postman:

1. Send a POST request to `/auth/login` with your credentials
2. Copy the access token from the response
3. For all other requests, add a header with key `token` and the value as your access token

## Expense Categories

The application supports the following expense categories:

- `FOOD`
- `TRANSPORTATION`
- `ENTERTAINMENT`
- `INVESTMENT`
- `OTHER`

**Note**: Category values are case-sensitive and must be in uppercase when used in requests.

## Response Status Codes

- `200 OK`: Request succeeded
- `201 Created`: Resource created successfully
- `204 No Content`: Request succeeded but no content to return (e.g., after deletion)
- `400 Bad Request`: Invalid request format or parameters
- `401 Unauthorized`: Authentication required or failed
- `404 Not Found`: Resource not found
- `422 Unprocessable Entity`: Request validation failed

## Database

The application uses SQLite for data storage, with the database file located at `expense_database.db` in the project root.

## Development

To modify or extend the application:

1. Navigate to the `app` directory
2. Modify the relevant files:
   - `models/`: Database models
   - `schemas/`: Pydantic schemas for request/response validation
   - `routes/`: API route handlers
   - `dependencies/`: Dependency functions (like authentication)

---

For any questions or issues, please contact the repository owner.
