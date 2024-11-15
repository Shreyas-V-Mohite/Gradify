import os

# Define the folder structure
folder_structure = {
    "data-warehouse-pipeline": {
        "etl": {
            "extract": {},
            "transform": {},
            "load": {}
        },
        "schemas": {
            "sql": {},
            "json": {}
        },
        "pipelines": {
            "airflow": {},
            "prefect": {},
            "dagster": {}
        },
        "tests": {
            "etl": {},
            "pipeline": {},
            "warehouse": {}
        },
        "config": {
            "env": {},
            "connections.json": None
        },
        "analytics": {
            "sql": {},
            "notebooks": {}
        },
        "docs": {
            "architecture.md": None,
            "setup.md": None
        },
        ".gitignore": None,
        "README.md": None,
        "requirements.txt": None
    }
}

# def create_structure(base_path, structure):
#     for name, content in structure.items():
#         path = os.path.join(base_path, name)
#         if content is None:
#             # Create a file
#             with open(path, 'w') as f:
#                 pass
#         elif isinstance(content, dict):
#             # Create a directory and its substructure
#             os.makedirs(path, exist_ok=True)
#             create_structure(path, content)
def create_structure_with_final_message(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if content is None:
            # Create a file and log its creation
            with open(path, 'w') as f:
                pass
            print(f"Created file: {path}")
        elif isinstance(content, dict):
            # Create a directory and log its creation
            os.makedirs(path, exist_ok=True)
            print(f"Created folder: {path}")
            create_structure_with_final_message(path, content)

# print("Folder structure created successfully!")

base_path = "./"
# Create the folder structure with logging and final message
create_structure_with_final_message(base_path, folder_structure)
# Create the folder structure

# create_structure(base_path, folder_structure)

print("Folder structure created successfully!")
