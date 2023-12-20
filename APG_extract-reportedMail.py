"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'select_reported_info' block
    select_reported_info(container=container)

    return

@phantom.playbook_block()
def select_reported_info(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("select_reported_info() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["artifact:*.name", "==", "Reported Mail"],
            ["artifact:*.label", "==", "Vault Artifact"]
        ],
        name="select_reported_info:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        extract_ioc_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    # collect filtered artifact ids and results for 'if' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["artifact:*.name", "==", "KB4 User Comment"],
            ["artifact:*.label", "==", "Vault Artifact"]
        ],
        name="select_reported_info:condition_2",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_2 or matched_results_2:
        apg_extractjsonfromfile_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_2, filtered_results=matched_results_2)

    return


@phantom.playbook_block()
def extract_ioc_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("extract_ioc_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    id_value = container.get("id", None)
    filtered_artifact_0_data_select_reported_info = phantom.collect2(container=container, datapath=["filtered-data:select_reported_info:condition_1:artifact:*.cef.vaultId","filtered-data:select_reported_info:condition_1:artifact:*.id","filtered-data:select_reported_info:condition_1:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'extract_ioc_1' call
    for filtered_artifact_0_item_select_reported_info in filtered_artifact_0_data_select_reported_info:
        parameters.append({
            "text": "",
            "label": "",
            "severity": "medium",
            "vault_id": filtered_artifact_0_item_select_reported_info[0],
            "file_type": "email",
            "container_id": id_value,
            "artifact_tags": "reported_mail",
            "parse_domains": False,
            "run_automation": False,
            "remap_cef_fields": "Do not apply CEF -> CIM remapping, only apply custom remap",
            "custom_remap_json": "{}",
            "context": {'artifact_id': filtered_artifact_0_item_select_reported_info[1], 'artifact_external_id': filtered_artifact_0_item_select_reported_info[2]},
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("extract ioc", parameters=parameters, name="extract_ioc_1", assets=["parser"], callback=debug_3)

    return


@phantom.playbook_block()
def playbook_prepoc_url_sanitize_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_prepoc_url_sanitize_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "poc1220/prePoc URL sanitize", returns the playbook_run_id
    playbook_run_id = phantom.playbook("poc1220/prePoc URL sanitize", container=container, name="playbook_prepoc_url_sanitize_1", callback=playbook_prepoc_url_sanitize_1_callback, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_prepoc_url_sanitize_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_prepoc_url_sanitize_1_callback() called")

    
    # Downstream End block cannot be called directly, since execution will call on_finish automatically.
    # Using placeholder callback function so child playbook is run synchronously.


    return


@phantom.playbook_block()
def apg_extractjsonfromfile_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("apg_extractjsonfromfile_1() called")

    id_value = container.get("id", None)
    filtered_artifact_0_data_select_reported_info = phantom.collect2(container=container, datapath=["filtered-data:select_reported_info:condition_2:artifact:*.cef.vaultId","filtered-data:select_reported_info:condition_2:artifact:*.id","filtered-data:select_reported_info:condition_2:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'apg_extractjsonfromfile_1' call
    for filtered_artifact_0_item_select_reported_info in filtered_artifact_0_data_select_reported_info:
        parameters.append({
            "vaultId": filtered_artifact_0_item_select_reported_info[0],
            "containerId": id_value,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="poc1220/APG_extractJsonFromFile", parameters=parameters, name="apg_extractjsonfromfile_1")

    return


@phantom.playbook_block()
def filter_transport_mail_artifacts_0(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_transport_mail_artifacts_0() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["transport_mail", "in", "artifact:*.tags"]
        ],
        name="filter_transport_mail_artifacts_0:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        pass

    return


@phantom.playbook_block()
def select_reported_mail_artifacts_0(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("select_reported_mail_artifacts_0() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["reported_mail", "in", "artifact:*.tags"]
        ],
        name="select_reported_mail_artifacts_0:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        artifact_update_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def artifact_update_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_update_2() called")

    filtered_artifact_0_data_filter_transport_mail_artifacts_0 = phantom.collect2(container=container, datapath=["filtered-data:filter_transport_mail_artifacts_0:condition_1:artifact:*.id","filtered-data:filter_transport_mail_artifacts_0:condition_1:artifact:*.id","filtered-data:filter_transport_mail_artifacts_0:condition_1:artifact:*.external_id"])
    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.name","artifact:*.id","artifact:*.external_id"])

    parameters = []

    # build parameters list for 'artifact_update_2' call
    for filtered_artifact_0_item_filter_transport_mail_artifacts_0 in filtered_artifact_0_data_filter_transport_mail_artifacts_0:
        for container_artifact_item in container_artifact_data:
            parameters.append({
                "artifact_id": filtered_artifact_0_item_filter_transport_mail_artifacts_0[0],
                "name": None,
                "label": container_artifact_item[0],
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

    phantom.custom_function(custom_function="community/artifact_update", parameters=parameters, name="artifact_update_2", callback=playbook_prepoc_url_sanitize_1)

    return


@phantom.playbook_block()
def debug_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("debug_3() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.tags","artifact:*.id","artifact:*.external_id"])

    container_artifact_header_item_0 = [item[0] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "input_1": container_artifact_header_item_0,
        "input_2": None,
        "input_3": None,
        "input_4": None,
        "input_5": None,
        "input_6": None,
        "input_7": None,
        "input_8": None,
        "input_9": None,
        "input_10": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_3", callback=select_reported_mail_artifacts_0)

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