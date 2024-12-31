import os

def generate_project(name: str):
    """
    Generate a FastAPI project structure with models, views, routes, schemas, requirements.txt, and README.md.
    """
    PROJECT_STRUCTURE = {
        "app": {
            "__init__.py": "",
            "models": {
                "__init__.py": "",
                "user.py": "from pydantic import BaseModel\n\nclass User(BaseModel):\n    id: str\n    name: str\n    email: str\n",
            },
            "routes": {
                "__init__.py": "",
                "user_routes.py": """from fastapi import APIRouter
from app.schemas.user_schema import UserSchema

router = APIRouter()

@router.get("/")
def get_users():
    return {"message": "List of users"}

@router.post("/create")
def create_user(user: UserSchema):
    return {"message": f"User {user.name} created!"}
""",
            },
            "schemas": {
                "__init__.py": "",
                "user_schema.py": """from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    email: str
""",
            },
            "views": {
                "__init__.py": "",
                "user_view.py": """from fastapi import FastAPI
from app.routes.user_routes import router

app = FastAPI()

app.include_router(router, prefix='/users', tags=['Users'])
""",
            },
        },
        "tests": {
            "__init__.py": "",
            "test_app.py": """from fastapi.testclient import TestClient
from app.views.user_view import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/create", json={"name": "John", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "User John created!"}
""",
        },
        ".env": "SECRET_KEY=your_secret_key\nDATABASE_URL=mongodb://localhost:27017\n",
        "README.md": """# FastAPI Project

This is a basic FastAPI project generated with FastAPI Project Generator.

## Setup

1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On MacOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    uvicorn app.views.user_view:app --reload
    ```

The application will be running at http://127.0.0.1:8000.

## Available Routes

- `GET /users`: List of users (not implemented yet)
- `POST /users/create`: Create a user
""",
        "requirements.txt": "fastapi==0.95.0\nuvicorn==0.22.0\npydantic==1.10.2\n",
        "main.py": """from app.views.user_view import app

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
""",
    }

    def create_structure(base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            else:
                with open(path, "w") as file:
                    file.write(content)

    base_path = os.path.join(os.getcwd(), name)
    create_structure(base_path, PROJECT_STRUCTURE)
    print(f"FastAPI project structure created at {base_path}")

def main():
    """
    Main entry point for the library when used as a CLI tool.
    Prompts the user for input if no arguments are provided.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Generate a FastAPI project structure.")
    parser.add_argument(
        "name", nargs="?", type=str, help="Name of the FastAPI project (optional)"
    )
    args = parser.parse_args()

    # Prompt for the project name if not provided as an argument
    if not args.name:
        project_name = input("Enter the name of your FastAPI project: ").strip()
        if not project_name:
            print("Error: Project name cannot be empty!")
            return
    else:
        project_name = args.name

    # Generate the project structure
    generate_project(project_name)
