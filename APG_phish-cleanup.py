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
def filter_email_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_email_artifact() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["artifact:*.name", "==", "Email Artifact"],
            ["soardemo@apg.at", "in", "artifact:*.cef.toEmail"]
        ],
        name="filter_email_artifact:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        artifact_update_5(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    # collect filtered artifact ids and results for 'if' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["artifact:*.name", "==", "Vault Artifact"],
            [".eml", "in", "artifact:*.cef.fileName"]
        ],
        name="filter_email_artifact:condition_2",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_2 or matched_results_2:
        artifact_update_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_2, filtered_results=matched_results_2)

    # collect filtered artifact ids and results for 'if' condition 3
    matched_artifacts_3, matched_results_3 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["artifact:*.name", "==", "Vault Artifact"],
            [".json", "in", "artifact:*.cef.fileName"]
        ],
        name="filter_email_artifact:condition_3",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_3 or matched_results_3:
        artifact_update_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_3, filtered_results=matched_results_3)

    return


@phantom.playbook_block()
def artifact_update_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_update_1() called")

    filtered_artifact_0_data_filter_email_artifact = phantom.collect2(container=container, datapath=["filtered-data:filter_email_artifact:condition_2:artifact:*.id","filtered-data:filter_email_artifact:condition_2:artifact:*.id","filtered-data:filter_email_artifact:condition_2:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'artifact_update_1' call
    for filtered_artifact_0_item_filter_email_artifact in filtered_artifact_0_data_filter_email_artifact:
        parameters.append({
            "artifact_id": filtered_artifact_0_item_filter_email_artifact[0],
            "name": None,
            "label": "Reported Mail",
            "severity": None,
            "cef_field": None,
            "cef_value": None,
            "cef_data_type": None,
            "tags": None,
            "overwrite_tags": None,
            "input_json": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_update", parameters=parameters, name="artifact_update_1")

    return


@phantom.playbook_block()
def artifact_update_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_update_2() called")

    filtered_artifact_0_data_filter_email_artifact = phantom.collect2(container=container, datapath=["filtered-data:filter_email_artifact:condition_3:artifact:*.id","filtered-data:filter_email_artifact:condition_3:artifact:*.id","filtered-data:filter_email_artifact:condition_3:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'artifact_update_2' call
    for filtered_artifact_0_item_filter_email_artifact in filtered_artifact_0_data_filter_email_artifact:
        parameters.append({
            "artifact_id": filtered_artifact_0_item_filter_email_artifact[0],
            "name": None,
            "label": "User Comment",
            "severity": None,
            "cef_field": None,
            "cef_value": None,
            "cef_data_type": None,
            "tags": None,
            "overwrite_tags": None,
            "input_json": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_update", parameters=parameters, name="artifact_update_2")

    return


@phantom.playbook_block()
def artifact_update_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_update_5() called")

    filtered_artifact_0_data_filter_email_artifact = phantom.collect2(container=container, datapath=["filtered-data:filter_email_artifact:condition_1:artifact:*.id","filtered-data:filter_email_artifact:condition_1:artifact:*.id","filtered-data:filter_email_artifact:condition_1:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'artifact_update_5' call
    for filtered_artifact_0_item_filter_email_artifact in filtered_artifact_0_data_filter_email_artifact:
        parameters.append({
            "artifact_id": filtered_artifact_0_item_filter_email_artifact[0],
            "name": None,
            "label": "Transport Mail",
            "severity": None,
            "cef_field": None,
            "cef_value": None,
            "cef_data_type": None,
            "tags": None,
            "overwrite_tags": None,
            "input_json": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_update", parameters=parameters, name="artifact_update_5", callback=artifact_update_6)

    return


@phantom.playbook_block()
def artifact_update_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_update_6() called")

    filtered_artifact_0_data_filter_email_artifact = phantom.collect2(container=container, datapath=["filtered-data:filter_email_artifact:condition_1:artifact:*.id","filtered-data:filter_email_artifact:condition_1:artifact:*.id","filtered-data:filter_email_artifact:condition_1:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'artifact_update_6' call
    for filtered_artifact_0_item_filter_email_artifact in filtered_artifact_0_data_filter_email_artifact:
        parameters.append({
            "artifact_id": filtered_artifact_0_item_filter_email_artifact[0],
            "name": None,
            "label": None,
            "severity": None,
            "cef_field": None,
            "cef_value": None,
            "cef_data_type": None,
            "tags": "transport_mail",
            "overwrite_tags": None,
            "input_json": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_update", parameters=parameters, name="artifact_update_6")

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