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
def playbook_apg_create_mc_incident_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_apg_create_mc_incident_1() called")

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
    playbook_run_id = phantom.playbook("poc1220/APG_create-mc-incident", container=container, name="playbook_apg_create_mc_incident_1", callback=playbook_apg_create_mc_incident_1_callback, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_apg_create_mc_incident_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_apg_create_mc_incident_1_callback() called")

    
    # Downstream End block cannot be called directly, since execution will call on_finish automatically.
    # Using placeholder callback function so child playbook is run synchronously.


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
        playbook_apg_create_mc_incident_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

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