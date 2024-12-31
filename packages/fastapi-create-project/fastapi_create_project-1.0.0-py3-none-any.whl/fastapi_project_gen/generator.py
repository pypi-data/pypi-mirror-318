import os

def generate_project(name: str):
    """
    Generate a FastAPI project structure with models, views, routes, and schemas.
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
                "user_routes.py": "from fastapi import APIRouter\n\nrouter = APIRouter()\n\n@router.get('/')\ndef read_users():\n    return {'message': 'List of users'}\n",
            },
            "schemas": {
                "__init__.py": "",
                "user_schema.py": "from pydantic import BaseModel\n\nclass UserSchema(BaseModel):\n    name: str\n    email: str\n",
            },
            "views": {
                "__init__.py": "",
                "user_view.py": "from fastapi import FastAPI\nfrom app.routes.user_routes import router\n\napp = FastAPI()\n\napp.include_router(router, prefix='/users', tags=['Users'])\n",
            },
        },
        "tests": {
            "__init__.py": "",
            "test_app.py": "def test_sample():\n    assert True\n",
        },
        ".env": "SECRET_KEY=your_secret_key\nDATABASE_URL=mongodb://localhost:27017\n",
        "README.md": "# FastAPI Project\n\nGenerated with FastAPI Project Generator.",
        "main.py": "from app.views.user_view import app\n\nif __name__ == '__main__':\n    import uvicorn\n    uvicorn.run(app, host='0.0.0.0', port=8000)\n",
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
