def vault_file_to_base64(vault_id=None, container_id=None, **kwargs):
    """
    Creates a base64 encoded data from a SOAR Vault file.  Which can then be uploaded to Mission Controll.
    
    Args:
        vault_id
        container_id
    
    Returns a JSON-serializable object that implements the configured data paths:
        base64_data
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import base64
    
    outputs = {}
    
    # Write your custom code here...
    def encode_file_to_base64(file_path):
        try:
            # Datei im Bin\u00e4rmodus \u00f6ffnen
            with open(file_path, 'rb') as file:
                # Dateiinhalt lesen und als Base64 codieren
                encoded_content = base64.b64encode(file.read())
                return encoded_content.decode()
        except Exception as e:
            return f"Fehler beim Lesen der Datei: {e}"

    success, message, info = phantom.vault_info(vault_id=vault_id,container_id=container_id)
    file_path = info[0]["path"]
    encoded_data = encode_file_to_base64(file_path)
    outputs["base64_data"] = encoded_data
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
