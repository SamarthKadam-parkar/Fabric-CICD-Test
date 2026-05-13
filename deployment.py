import os
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
from fabric_cicd import FabricWorkspace, publish_all_items

# --- configuration ---

# enter the dev workspace id if you are in dev brach or main workspace id if its in main branch
WORKSPACE_ID = ""

# specify environment
ENVIRONMENT = "dev"  # or "main"

# change the fabric artifacts path as per need, currently set to root folder
REPO_DIR = "."

# add or remove artifacts as per your need, if removed the CICD will not be implemnted for that specific artifact
ITEM_TYPES = [
    "Lakehouse", "Notebook", "Environment",
    "Warehouse", "DataPipeline", "SemanticModel", "Report"
]
# ----------------------

def main():
    ws = FabricWorkspace(
        workspace_id=WORKSPACE_ID,
        environment=ENVIRONMENT,
        repository_directory=REPO_DIR,
        item_type_in_scope=ITEM_TYPES
    )

    publish_all_items(ws)

if __name__ == "__main__":
    main()