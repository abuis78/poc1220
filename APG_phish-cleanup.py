"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'are_tags_already_set' block
    are_tags_already_set(container=container)

    return

@phantom.playbook_block()
def categorize_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("categorize_artifact() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["artifact:*.name", "==", "Email Artifact"],
            ["soardemo@apg.at", "in", "artifact:*.cef.toEmail"]
        ],
        name="categorize_artifact:condition_1",
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
        name="categorize_artifact:condition_2",
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
        name="categorize_artifact:condition_3",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_3 or matched_results_3:
        artifact_update_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_3, filtered_results=matched_results_3)

    return


@phantom.playbook_block()
def artifact_update_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_update_1() called")

    filtered_artifact_0_data_categorize_artifact = phantom.collect2(container=container, datapath=["filtered-data:categorize_artifact:condition_2:artifact:*.id","filtered-data:categorize_artifact:condition_2:artifact:*.id","filtered-data:categorize_artifact:condition_2:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'artifact_update_1' call
    for filtered_artifact_0_item_categorize_artifact in filtered_artifact_0_data_categorize_artifact:
        parameters.append({
            "name": "Reported Mail",
            "tags": None,
            "label": None,
            "severity": None,
            "cef_field": None,
            "cef_value": None,
            "input_json": None,
            "artifact_id": filtered_artifact_0_item_categorize_artifact[0],
            "cef_data_type": None,
            "overwrite_tags": None,
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

    filtered_artifact_0_data_categorize_artifact = phantom.collect2(container=container, datapath=["filtered-data:categorize_artifact:condition_3:artifact:*.id","filtered-data:categorize_artifact:condition_3:artifact:*.id","filtered-data:categorize_artifact:condition_3:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'artifact_update_2' call
    for filtered_artifact_0_item_categorize_artifact in filtered_artifact_0_data_categorize_artifact:
        parameters.append({
            "name": "KB4 User Comment",
            "tags": None,
            "label": None,
            "severity": None,
            "cef_field": None,
            "cef_value": None,
            "input_json": None,
            "artifact_id": filtered_artifact_0_item_categorize_artifact[0],
            "cef_data_type": None,
            "overwrite_tags": None,
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

    filtered_artifact_0_data_categorize_artifact = phantom.collect2(container=container, datapath=["filtered-data:categorize_artifact:condition_1:artifact:*.id","filtered-data:categorize_artifact:condition_1:artifact:*.id","filtered-data:categorize_artifact:condition_1:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'artifact_update_5' call
    for filtered_artifact_0_item_categorize_artifact in filtered_artifact_0_data_categorize_artifact:
        parameters.append({
            "name": "Transport Mail",
            "tags": None,
            "label": None,
            "severity": None,
            "cef_field": None,
            "cef_value": None,
            "input_json": None,
            "artifact_id": filtered_artifact_0_item_categorize_artifact[0],
            "cef_data_type": None,
            "overwrite_tags": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_update", parameters=parameters, name="artifact_update_5")

    return


@phantom.playbook_block()
def are_tags_already_set(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("are_tags_already_set() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["transport_mail", "in", "artifact:*.tags"]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        select_all_extracted_artifacts_0(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    artifact_update_3(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def artifact_update_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_update_3() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.id","artifact:*.name","artifact:*.id","artifact:*.external_id"])

    parameters = []

    # build parameters list for 'artifact_update_3' call
    for container_artifact_item in container_artifact_data:
        parameters.append({
            "artifact_id": container_artifact_item[0],
            "name": None,
            "label": container_artifact_item[1],
            "severity": "Informational",
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

    phantom.custom_function(custom_function="community/artifact_update", parameters=parameters, name="artifact_update_3", callback=categorize_artifact)

    return


@phantom.playbook_block()
def select_all_extracted_artifacts_0(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("select_all_extracted_artifacts_0() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["transport_mail", "not in", "artifact:*.tags"]
        ],
        name="select_all_extracted_artifacts_0:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        artifact_delete(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def artifact_update_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_update_4() called")

    filtered_artifact_0_data_select_all_extracted_artifacts_0 = phantom.collect2(container=container, datapath=["filtered-data:select_all_extracted_artifacts_0:condition_1:artifact:*.id","filtered-data:select_all_extracted_artifacts_0:condition_1:artifact:*.id","filtered-data:select_all_extracted_artifacts_0:condition_1:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'artifact_update_4' call
    for filtered_artifact_0_item_select_all_extracted_artifacts_0 in filtered_artifact_0_data_select_all_extracted_artifacts_0:
        parameters.append({
            "artifact_id": filtered_artifact_0_item_select_all_extracted_artifacts_0[0],
            "name": None,
            "label": None,
            "severity": None,
            "cef_field": None,
            "cef_value": None,
            "cef_data_type": None,
            "tags": "to_delete",
            "overwrite_tags": False,
            "input_json": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_update", parameters=parameters, name="artifact_update_4")

    return


@phantom.playbook_block()
def artifact_delete(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_delete() called")

    filtered_artifact_0_data_select_all_extracted_artifacts_0 = phantom.collect2(container=container, datapath=["filtered-data:select_all_extracted_artifacts_0:condition_1:artifact:*.id"])

    filtered_artifact_0__id = [item[0] for item in filtered_artifact_0_data_select_all_extracted_artifacts_0]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    
    for id in filtered_artifact_0__id:
        phantom.delete_artifact(id)

    ################################################################################
    ## Custom Code End
    ################################################################################

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