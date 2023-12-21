"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'vault_file_to_base64_3' block
    vault_file_to_base64_3(container=container)

    return

@phantom.playbook_block()
def add_incident_file_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_incident_file_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    vault_file_to_base64_3__result = phantom.collect2(container=container, datapath=["vault_file_to_base64_3:custom_function_result.data.base64_data"])
    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.fileName","artifact:*.id","artifact:*.external_id"])

    parameters = []

    # build parameters list for 'add_incident_file_1' call
    for vault_file_to_base64_3__result_item in vault_file_to_base64_3__result:
        for container_artifact_item in container_artifact_data:
            if vault_file_to_base64_3__result_item[0] is not None and container_artifact_item[0] is not None:
                parameters.append({
                    "id": "acbc6d1c-4210-4474-9d9b-a7957969ae1f",
                    "data": vault_file_to_base64_3__result_item[0],
                    "file_name": container_artifact_item[0],
                    "source_type": "Incident",
                    "context": {'artifact_id': container_artifact_item[1], 'artifact_external_id': container_artifact_item[2]},
                })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add incident file", parameters=parameters, name="add_incident_file_1", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def vault_file_to_base64_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("vault_file_to_base64_3() called")

    id_value = container.get("id", None)
    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.vaultId","artifact:*.id","artifact:*.external_id"])

    parameters = []

    # build parameters list for 'vault_file_to_base64_3' call
    for container_artifact_item in container_artifact_data:
        parameters.append({
            "vault_id": container_artifact_item[0],
            "container_id": id_value,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="poc1220/vault_file_to_base64", parameters=parameters, name="vault_file_to_base64_3", callback=add_incident_file_1)

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return