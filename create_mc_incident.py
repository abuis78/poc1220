"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'filter_email_artifact' block
    filter_email_artifact(container=container)

    return

@phantom.playbook_block()
def create_incidents_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("create_incidents_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_icident_name = phantom.get_format_data(name="format_icident_name")

    parameters = []

    if format_icident_name is not None:
        parameters.append({
            "name": format_icident_name,
            "incident_type": "phishing",
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
def format_icident_name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_icident_name() called")

    template = """Phishing Incident: {0}\n"""

    # parameter list for template variable replacement
    parameters = [
        "container:name"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_icident_name")

    create_incidents_1(container=container)

    return


@phantom.playbook_block()
def filter_email_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_email_artifact() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.name", "==", "Email Artifact"]
        ],
        name="filter_email_artifact:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        format_icident_name(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

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