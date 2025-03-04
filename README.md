# User Management

This is a Flask-based web application that provides endpoints for user management, including creating, reading, updating, and deleting users. It also incorporates JWT-based authentication and password hashing for security.

## Features

- **User Authentication**: Users can log in with their credentials to receive a JWT token.
- **JWT Authentication**: Secure access to user-related endpoints via token-based authentication.
- **Password Hashing**: Passwords are hashed using `bcrypt` to ensure security.
- **MongoDB**: The application uses MongoDB as a database to store user data.

## Technologies Used

- Flask
- Flask-PyMongo
- Flask-Bcrypt
- Flask-JWT-Extended
- Flasgger (Swagger UI integration)
- MongoDB
- Docker (for containerization)

## Endpoints

### 1. **Login**
- **Route**: `/login`
- **Method**: `POST`
- **Parameters**:
    - `email` (string) - User's email address
    - `password` (string) - User's password
- **Description**: Login with email and password to receive a JWT token.
- **Response**:
    - `200 OK`: `{ "token": "JWT_TOKEN" }`
    - `401 Unauthorized`: Invalid credentials or missing parameters.

### 2. **Get All Users**
- **Route**: `/users`
- **Method**: `GET`
- **Authentication**: Required (JWT token)
- **Description**: Get a list of all users.
- **Response**:
    - `200 OK`: A list of users in JSON format.

### 3. **Get User by ID**
- **Route**: `/users/<id>`
- **Method**: `GET`
- **Authentication**: Required (JWT token)
- **Description**: Retrieve a user by their unique ID.
- **Response**:
    - `200 OK`: User details in JSON format.
    - `404 Not Found`: If the user does not exist.

### 4. **Create User**
- **Route**: `/users`
- **Method**: `POST`
- **Parameters**:
    - `name` (string) - User's name
    - `email` (string) - User's email address
    - `password` (string) - User's password
- **Description**: Create a new user with the provided details.
- **Response**:
    - `201 Created`: `{ "message": "User created", "id": "<user_id>" }`
    - `400 Bad Request`: Missing required fields.

### 5. **Update User**
- **Route**: `/users/<id>`
- **Method**: `PUT`
- **Authentication**: Required (JWT token)
- **Parameters**:
    - `name` (string) - User's name
    - `email` (string) - User's email address
    - `password` (string) - User's password
- **Description**: Update a user's details.
- **Response**:
    - `200 OK`: `{ "message": "User updated" }`
    - `404 Not Found`: If the user does not exist.

### 6. **Delete User**
- **Route**: `/users/<id>`
- **Method**: `DELETE`
- **Authentication**: Required (JWT token)
- **Description**: Delete a user by their ID.
- **Response**:
    - `200 OK`: `{ "message": "User deleted" }`
    - `404 Not Found`: If the user does not exist.

## Running the Application

### Docker Setup

To run the application with Docker, follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    ```

2. Create a .env file:
    ```bash
    MONGO_URI=mongodb://localhost:27017/userdb
    WT_SECRET_KEY=jwt-secret-string
    ```

3. Build the Docker containers:
    ```bash
    docker-compose build
    ```

4. Start the application and MongoDB container:
    ```bash
    docker-compose up
    ```

5. The application will be available at `http://localhost:5000`.

## Swagger UI

To view the API documentation and test the endpoints, visit: `http://localhost:5000/swagger`

