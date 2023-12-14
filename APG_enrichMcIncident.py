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
        code_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def set_summary_fields_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("set_summary_fields_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    filtered_artifact_0_data_select_reported_email = phantom.collect2(container=container, datapath=["filtered-data:select_reported_email:condition_1:artifact:*.cef.bodyHtml","filtered-data:select_reported_email:condition_1:artifact:*.id","filtered-data:select_reported_email:condition_1:artifact:*.external_id"])
    filtered_artifact_1_data_select_mc_incident = phantom.collect2(container=container, datapath=["filtered-data:select_mc_incident:condition_1:artifact:*.cef.id","filtered-data:select_mc_incident:condition_1:artifact:*.id","filtered-data:select_mc_incident:condition_1:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'set_summary_fields_1' call
    for filtered_artifact_0_item_select_reported_email in filtered_artifact_0_data_select_reported_email:
        for filtered_artifact_1_item_select_mc_incident in filtered_artifact_1_data_select_mc_incident:
            if filtered_artifact_1_item_select_mc_incident[0] is not None:
                parameters.append({
                    "pairs": [
                        { "name": "body_html", "value": filtered_artifact_0_item_select_reported_email[0] },
                    ],
                    "incident_id": filtered_artifact_1_item_select_mc_incident[0],
                    "context": {'artifact_id': filtered_artifact_1_item_select_mc_incident[1], 'artifact_external_id': filtered_artifact_1_item_select_mc_incident[2]},
                })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("set summary fields", parameters=parameters, name="set_summary_fields_1", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    filtered_artifact_0_data_select_reported_email = phantom.collect2(container=container, datapath=["filtered-data:select_reported_email:condition_1:artifact:*.cef.bodyHtml"])

    filtered_artifact_0__cef_bodyhtml = [item[0] for item in filtered_artifact_0_data_select_reported_email]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(filtered_artifact_0__cef_bodyhtml)
    output_file_path = "/tmp/output.pdf"
    # html_string_to_pdf returns False on error, and True on success    
    if not phantom.html_string_to_pdf(filtered_artifact_0__cef_bodyhtml[0], output_file_path):
        phantom.error("Failed to convert HTML string to pdf.")

    # Add the file as a container attachment using the vault API
    vault_id = phantom.vault_add(container=container, file_location=output_file_path, file_name="output.pdf")
    phantom.debug(vault_id)


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