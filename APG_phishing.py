"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_apg_phish_cleanup_1' block
    playbook_apg_phish_cleanup_1(container=container)

    return

@phantom.playbook_block()
def playbook_apg_phish_cleanup_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_apg_phish_cleanup_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "poc1220/APG_phish-cleanup", returns the playbook_run_id
    playbook_run_id = phantom.playbook("poc1220/APG_phish-cleanup", container=container, inputs=inputs)

    playbook_apg_extract_reportedmail_1(container=container)

    return


@phantom.playbook_block()
def playbook_apg_extract_reportedmail_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_apg_extract_reportedmail_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "poc1220/APG_extract-reportedMail", returns the playbook_run_id
    playbook_run_id = phantom.playbook("poc1220/APG_extract-reportedMail", container=container)

    select_reported_mail(container=container)

    return


@phantom.playbook_block()
def select_reported_mail(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("select_reported_mail() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["reported_mail", "in", "artifact:*.tags"],
            ["artifact:*.name", "==", "Email Artifact"]
        ],
        name="select_reported_mail:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        playbook_apg_create_mc_incident_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def create_events_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("create_events_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    filtered_artifact_0_data_select_reported_mail = phantom.collect2(container=container, datapath=["filtered-data:select_reported_mail:condition_1:artifact:*.cef.emailHeaders","filtered-data:select_reported_mail:condition_1:artifact:*.id","filtered-data:select_reported_mail:condition_1:artifact:*.external_id"])
    playbook_apg_create_mc_incident_2_output_mc_id = phantom.collect2(container=container, datapath=["playbook_apg_create_mc_incident_2:playbook_output:mc_id"])

    parameters = []

    # build parameters list for 'create_events_1' call
    for filtered_artifact_0_item_select_reported_mail in filtered_artifact_0_data_select_reported_mail:
        for playbook_apg_create_mc_incident_2_output_mc_id_item in playbook_apg_create_mc_incident_2_output_mc_id:
            if playbook_apg_create_mc_incident_2_output_mc_id_item[0] is not None:
                parameters.append({
                    "pairs": [
                        { "name": "headers", "value": filtered_artifact_0_item_select_reported_mail[0] },
                    ],
                    "incident_id": playbook_apg_create_mc_incident_2_output_mc_id_item[0],
                    "context": {'artifact_id': filtered_artifact_0_item_select_reported_mail[1], 'artifact_external_id': filtered_artifact_0_item_select_reported_mail[2]},
                })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("create events", parameters=parameters, name="create_events_1", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def playbook_apg_create_mc_incident_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_apg_create_mc_incident_2() called")

    filtered_artifact_0_data_select_reported_mail = phantom.collect2(container=container, datapath=["filtered-data:select_reported_mail:condition_1:artifact:*.cef.emailHeaders.Subject"])

    filtered_artifact_0__cef_emailheaders_subject = [item[0] for item in filtered_artifact_0_data_select_reported_mail]

    inputs = {
        "subject": filtered_artifact_0__cef_emailheaders_subject,
        "incident_type": ["phishing"],
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "poc1220/APG_create-mc-incident", returns the playbook_run_id
    playbook_run_id = phantom.playbook("poc1220/APG_create-mc-incident", container=container, name="playbook_apg_create_mc_incident_2", callback=create_events_1, inputs=inputs)

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