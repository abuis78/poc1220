def APG_extractJsonFromFile(vaultId=None, containerId=None, **kwargs):
    """
    Args:
        vaultId
        containerId
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    success, message, info = phantom.vault_info(vault_id=vaultId, file_name=None, container_id=containerId, trace=False)
    path = info[0]["path"]
    phantom.debug(path)
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
