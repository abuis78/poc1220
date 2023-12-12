"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'create_incidents_1' block
    create_incidents_1(container=container)

    return

@phantom.playbook_block()
def create_incidents_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("create_incidents_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    playbook_input_subject = phantom.collect2(container=container, datapath=["playbook_input:subject"])
    playbook_input_incident_type = phantom.collect2(container=container, datapath=["playbook_input:incident_type"])

    parameters = []

    # build parameters list for 'create_incidents_1' call
    for playbook_input_subject_item in playbook_input_subject:
        for playbook_input_incident_type_item in playbook_input_incident_type:
            if playbook_input_subject_item[0] is not None and playbook_input_incident_type_item[0] is not None:
                parameters.append({
                    "name": playbook_input_subject_item[0],
                    "incident_type": playbook_input_incident_type_item[0],
                })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("create incidents", parameters=parameters, name="create_incidents_1", assets=["builtin_mc_connector"], callback=artifact_create_1)

    return


@phantom.playbook_block()
def artifact_create_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_create_1() called")

    id_value = container.get("id", None)
    create_incidents_1_result_data = phantom.collect2(container=container, datapath=["create_incidents_1:action_result.data.*.id","create_incidents_1:action_result.parameter.context.artifact_id","create_incidents_1:action_result.parameter.context.artifact_external_id"], action_results=results)

    parameters = []

    # build parameters list for 'artifact_create_1' call
    for create_incidents_1_result_item in create_incidents_1_result_data:
        parameters.append({
            "name": "mc_id",
            "tags": None,
            "label": None,
            "severity": "Low",
            "cef_field": "id",
            "cef_value": create_incidents_1_result_item[0],
            "container": id_value,
            "input_json": None,
            "cef_data_type": None,
            "run_automation": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="artifact_create_1")

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