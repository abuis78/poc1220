def url_safelink_extract(protected_url=None, **kwargs):
    """
    Args:
        protected_url: asasd
    
    Returns a JSON-serializable object that implements the configured data paths:
        actual_url
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import urllib.parse
    
    outputs = {}
    
    # Write your custom code here...

    # Parsen der URL, um die Parameter zu extrahieren
    parsed_url = urllib.parse.urlparse(protected_url)
    query_params = urllib.parse.parse_qs(parsed_url.query)

    # Extrahieren des 'url'-Parameters
    encoded_actual_url = query_params.get('url')
    if encoded_actual_url:
        # URL-decodierung des ersten Wertes im 'url'-Parameter
        actual_url = urllib.parse.unquote(encoded_actual_url[0])
    else:
        return "Keine 'url' Parameter gefunden."
    outputs["actual_url"] = actual_url
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
