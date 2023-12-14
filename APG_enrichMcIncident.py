"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'select_reported_email' block
    select_reported_email(container=container)

    return

@phantom.playbook_block()
def select_reported_email(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("select_reported_email() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["artifact:*.name", "==", "Email Artifact"],
            ["reported_mail", "in", "artifact:*.tags"]
        ],
        name="select_reported_email:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        select_mc_incident(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def select_mc_incident(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("select_mc_incident() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.name", "==", "mc_id"]
        ],
        name="select_mc_incident:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        add_incident_file_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def add_incident_file_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_incident_file_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    filtered_artifact_0_data_select_mc_incident = phantom.collect2(container=container, datapath=["filtered-data:select_mc_incident:condition_1:artifact:*.cef.id","filtered-data:select_mc_incident:condition_1:artifact:*.id","filtered-data:select_mc_incident:condition_1:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'add_incident_file_1' call
    for filtered_artifact_0_item_select_mc_incident in filtered_artifact_0_data_select_mc_incident:
        if filtered_artifact_0_item_select_mc_incident[0] is not None:
            parameters.append({
                "id": filtered_artifact_0_item_select_mc_incident[0],
                "data": "",
                "file_name": "",
                "source_type": "",
                "context": {'artifact_id': filtered_artifact_0_item_select_mc_incident[1], 'artifact_external_id': filtered_artifact_0_item_select_mc_incident[2]},
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