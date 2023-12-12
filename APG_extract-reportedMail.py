"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'filter_transport_mail_artifacts_0' block
    filter_transport_mail_artifacts_0(container=container)

    return

@phantom.playbook_block()
def select_reported_info(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("select_reported_info() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["artifact:*.name", "==", "Vault Artifact"],
            ["artifact:*.label", "==", "Reported Mail"]
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
            ["artifact:*.name", "==", "Vault Artifact"],
            ["artifact:*.label", "==", "KB4 User Comment"]
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

    phantom.act("extract ioc", parameters=parameters, name="extract_ioc_1", assets=["parser"], callback=playbook_prepoc_url_sanitize_1)

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
    playbook_run_id = phantom.playbook("poc1220/prePoc URL sanitize", container=container, inputs=inputs)

    return


@phantom.playbook_block()
def apg_extractjsonfromfile_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("apg_extractjsonfromfile_1() called")

    id_value = container.get("id", None)
    filtered_artifact_0_data_select_reported_info = phantom.collect2(container=container, datapath=["filtered-data:select_reported_info:condition_2:artifact:*.id","filtered-data:select_reported_info:condition_2:artifact:*.id","filtered-data:select_reported_info:condition_2:artifact:*.external_id"])

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
        select_reported_info(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

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