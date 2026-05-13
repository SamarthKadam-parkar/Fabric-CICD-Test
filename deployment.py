import os
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
from fabric_cicd import FabricWorkspace, publish_all_items
# Load environment variables
load_dotenv()
# Workspace config
TEST_WORKSPACE_ID = os.getenv("DEV_WORKSPACE_ID")
token_credential = ClientSecretCredential(
    client_id=os.getenv("CLIENT_ID"), 
    client_secret=os.getenv("CLIENT_SECRET"), 
    tenant_id=os.getenv("TENANT_ID")
    )
# Create workspace object
ws = FabricWorkspace(
   workspace_id=TEST_WORKSPACE_ID,
   token_credential=token_credential,
   environment="test",
   repository_directory=".",
   item_type_in_scope=[
       "Lakehouse",
       "Notebook",
       "DataPipeline",
       "Environment",
       "SemanticModel",
       "Report"
   ],
   parameter_file="pr-validation.yml"
)
print("Starting deployment to DEV workspace...")
publish_all_items(ws)
print("Deployment completed successfully")