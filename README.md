# FastAPI Blog Application

A modern, RESTful blog application built with FastAPI, featuring user authentication, JWT-based authorization, and full CRUD operations for blog posts. This project demonstrates industry-standard practices in API development, database management, and security implementation.

## 🚀 Features

### Authentication & Authorization
- **User Registration**: Secure signup with email validation and password hashing
- **JWT-Based Authentication**: Secure login system with OAuth2 bearer tokens
- **Protected Routes**: Role-based access control for post operations
- **Password Security**: Industry-standard password hashing using Werkzeug

### Blog Post Management
- **Create Posts**: Authenticated users can create new blog posts
- **Read Posts**: 
  - Fetch all posts across the platform
  - Retrieve individual posts by ID
- **Update Posts**: Edit own posts with authorization checks
- **Delete Posts**: Remove own posts with proper validation
- **Author Attribution**: Automatic association of posts with their creators

### Technical Highlights
- **RESTful API Design**: Clean, intuitive endpoint structure
- **Database ORM**: SQLAlchemy with modern Python 3.11+ type hints
- **Data Validation**: Pydantic schemas for request/response validation
- **CORS Support**: Cross-Origin Resource Sharing configured for web clients
- **Auto-Documentation**: Interactive API docs via FastAPI's built-in Swagger UI

## 🛠️ Tech Stack

### Core Technologies
- **FastAPI** (v0.115.12): Modern, high-performance web framework for building APIs
- **SQLAlchemy** (v2.0.41): Powerful ORM for database operations
- **Pydantic** (v2.11.7): Data validation using Python type annotations
- **Uvicorn** (v0.34.3): ASGI server for running FastAPI applications

### Security & Authentication
- **python-jose** (v3.5.0): JWT token creation and validation
- **Werkzeug** (via bcrypt): Password hashing utilities
- **OAuth2**: Standard authentication protocol implementation

### Database
- **SQLite**: Lightweight, serverless database for development
- **Alembic** (v1.16.1): Database migration tool (included in requirements)

### Development Tools
- **python-dotenv** (v1.1.0): Environment variable management
- **PyMySQL** (v1.1.1): MySQL connector (for future PostgreSQL/MySQL migration)

## 📋 Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git (for version control)

## 🚦 Getting Started

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd fastapi_blog_project
```

2. **Create virtual environment**
```bash
python -m venv .venv
```

3. **Activate virtual environment**

**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory (optional for development):
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///blog.db
```

### Running the Application

1. **Start the server**
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

2. **Access interactive API documentation**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📚 API Documentation

### Authentication Endpoints

#### Sign Up
```http
POST /signup
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

#### Login
```http
POST /login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepassword123"
}

Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "john_doe"
  }
}
```

### Post Endpoints

All post endpoints require authentication via Bearer token:
```http
Authorization: Bearer <your-jwt-token>
```

#### Get All Posts
```http
GET /posts
```

#### Create Post
```http
POST /posts
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "My First Blog Post",
  "content": "This is the content of my blog post..."
}
```

#### Get Single Post
```http
GET /posts/{post_id}
Authorization: Bearer <token>
```

#### Update Post
```http
PUT /posts/{post_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Updated Title",
  "content": "Updated content..."
}
```

#### Delete Post
```http
DELETE /posts/{post_id}
Authorization: Bearer <token>
```

### User Endpoints

#### Get All Users
```http
GET /users
```

## 🏗️ Project Structure

```
fastapi_blog_project/
├── main.py              # Application entry point and configuration
├── database.py          # Database connection and session management
├── models.py            # SQLAlchemy ORM models (User, Post)
├── schemas.py           # Pydantic schemas for validation
├── auth.py              # Authentication routes and logic
├── utils.py             # JWT token creation and user verification
├── routers/
│   ├── posts.py         # Post-related endpoints
│   └── users.py         # User-related endpoints
├── blog.db              # SQLite database (auto-created)
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔐 Security Features

1. **Password Hashing**: Uses Werkzeug's security functions for secure password storage
2. **JWT Tokens**: Short-lived tokens with user ID payload
3. **Authorization Checks**: Verifies ownership before allowing post modifications
4. **CORS Configuration**: Controls cross-origin access to API resources
5. **SQL Injection Prevention**: SQLAlchemy ORM parameterized queries
6. **Input Validation**: Pydantic schemas validate all incoming data

## 🧪 Testing the API

### Using cURL

**Sign up:**
```bash
curl -X POST "http://localhost:8000/signup" \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"testpass123"}'
```

**Login:**
```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpass123"}'
```

**Create Post:**
```bash
curl -X POST "http://localhost:8000/posts" \
  -H "Authorization: Bearer <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Post","content":"This is a test post"}'
```

### Using Python requests

```python
import requests

# Signup
response = requests.post('http://localhost:8000/signup', json={
    'username': 'testuser',
    'email': 'test@example.com',
    'password': 'testpass123'
})

# Login
response = requests.post('http://localhost:8000/login', json={
    'email': 'test@example.com',
    'password': 'testpass123'
})
token = response.json()['access_token']

# Create Post
headers = {'Authorization': f'Bearer {token}'}
response = requests.post('http://localhost:8000/posts', 
    headers=headers,
    json={'title': 'Test Post', 'content': 'This is a test post'}
)
```

## 🚀 Future Enhancements

- [ ] PostgreSQL/MySQL database integration
- [ ] Refresh token implementation
- [ ] Email verification for signup
- [ ] Password reset functionality
- [ ] Post pagination and filtering
- [ ] Comment system
- [ ] Like/feature system
- [ ] Docker containerization
- [ ] Comprehensive test suite with pytest
- [ ] API rate limiting
- [ ] Logging and monitoring setup
- [ ] CI/CD pipeline configuration

## 📝 Database Schema

### Users Table
- `id` (Primary Key)
- `username` (Unique, Indexed)
- `email` (Unique, Indexed)
- `password` (Hashed)

### Posts Table
- `id` (Primary Key)
- `title`
- `content`
- `user_id` (Foreign Key → users.id)
- Relationship: Posts belong to Users (One-to-Many)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Malik Ahsan**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourusername)

## 🙏 Acknowledgments

- FastAPI documentation and community
- SQLAlchemy team for the excellent ORM
- All contributors to the libraries used in this project

---

**Note**: This is a development project. For production deployment, ensure you:
- Use environment variables for sensitive data
- Implement proper CORS policy
- Add rate limiting
- Set up proper logging
- Use a production-grade database (PostgreSQL/MySQL)
- Implement HTTPS/TLS
- Add comprehensive error handling
- Set up monitoring and alerting