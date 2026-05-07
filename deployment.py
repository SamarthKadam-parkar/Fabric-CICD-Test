from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items

fabricWorkspace = FabricWorkspace (

    client_id = ${{secrets.CLIENT_ID}} ,
    tenant_id = ,
    client_secret = ,
)
