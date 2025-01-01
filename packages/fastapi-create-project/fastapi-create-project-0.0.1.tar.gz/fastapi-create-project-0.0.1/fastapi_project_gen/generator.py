import os
import click  # You can use click to easily handle command-line arguments

# Function to create the FastAPI project structure
def create_file_structure(project_name, apps):
    # Define base directory for the project
    base_dir = os.path.join(os.getcwd(), project_name)
    os.makedirs(base_dir, exist_ok=True)
    
    # Create the app directory
    app_dir = os.path.join(base_dir, "app")
    os.makedirs(app_dir, exist_ok=True)
    
    # Create the main.py file
    create_main_file(base_dir)
    
    # Create app-specific directories and files
    app_imports = []
    for app_name in apps.split(","):
        app_name = app_name.strip()
        app_path = os.path.join(app_dir, app_name)
        os.makedirs(app_path, exist_ok=True)
        
        # Create files within the app directory
        create_app_files(app_path, app_name)
        
        # Collect imports for main.py
        app_imports.append(f"from app.{app_name}.routes import router as {app_name}_router")
    
    # Append routes to main.py
    append_routes_to_main(base_dir, app_imports, apps)

    # Create requirements.txt
    create_requirements_txt(base_dir)

    print(f"Project '{project_name}' created successfully at {base_dir}")

def create_main_file(base_dir):
    main_content = '''from fastapi import FastAPI

app = FastAPI()

# Routes will be dynamically added here
'''
    with open(os.path.join(base_dir, "main.py"), 'w') as f:
        f.write(main_content)

def create_app_files(app_path, app_name):
    # Define content for app files
    routes_content = f'''from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {{'message': 'Hello from the {app_name} app!'}}
'''
    schema_content = f'''from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None
'''
    models_content = f'''# Database models for the {app_name} app
# Example: SQLAlchemy model for Item
'''
    crud_content = f'''from .models import Item

def get_items():
    # This is a sample function; in a real app, you would query your database here.
    return [
        {{'name': 'Item 1', 'description': 'A sample item', 'price': 10.0, 'tax': 1.5}}
    ]
'''

    # Create the files
    with open(os.path.join(app_path, "routes.py"), 'w') as f:
        f.write(routes_content)
    
    with open(os.path.join(app_path, "schema.py"), 'w') as f:
        f.write(schema_content)
    
    with open(os.path.join(app_path, "models.py"), 'w') as f:
        f.write(models_content)
    
    with open(os.path.join(app_path, "crud.py"), 'w') as f:
        f.write(crud_content)

def append_routes_to_main(base_dir, app_imports, apps):
    main_file_path = os.path.join(base_dir, "main.py")
    with open(main_file_path, "a") as f:
        for import_statement in app_imports:
            f.write(f"\n{import_statement}")
        
        f.write("\n\n")
        for app_name in apps.split(","):
            app_name = app_name.strip()
            f.write(f"app.include_router({app_name}_router, prefix='/{app_name}')\n")

def create_requirements_txt(base_dir):
    requirements_content = '''fastapi
uvicorn
'''
    with open(os.path.join(base_dir, "requirements.txt"), 'w') as f:
        f.write(requirements_content)

# Command-line interface for creating the project
@click.command()
@click.argument("project_name")
@click.option("--apps", default="auth,product", help="Comma-separated list of apps to create.")
def main(project_name, apps):
    """Scaffold a new FastAPI project with multiple apps."""
    create_file_structure(project_name, apps)

if __name__ == "__main__":
    main()
