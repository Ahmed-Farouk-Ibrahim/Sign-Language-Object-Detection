import os
from pathlib import Path
import logging

# Configure logging to display the time and message format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of files and directories to be created for the project structure
project_name = "Sign_Language_Object_Detection"


list_of_files = [
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/_01_data_ingestion.py",
    f"{project_name}/components/_02_data_validation.py",
    f"{project_name}/components/_03_model_trainer.py",
    f"{project_name}/components/_04_model_pusher.py",

    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",
    
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    "notebook/trials.ipynb",
    "notebook/project_notebook.ipynb",

    "template/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"


]

# Iterate over the list of files and create necessary directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create the directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create an empty file if it does not exist or is of size zero
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
