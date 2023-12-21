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
    playbook_run_id = phantom.playbook("poc1220/APG_extract-reportedMail", container=container, name="playbook_apg_extract_reportedmail_1", callback=filter_1)

    return


@phantom.playbook_block()
def filter_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_1() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["reported_mail", "in", "artifact:*.tags"],
            ["artifact:*.name", "==", "Email Artifact"]
        ],
        name="filter_1:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        generate_mc_title(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def playbook_apg_create_mc_incident_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_apg_create_mc_incident_2() called")

    generate_mc_title = phantom.get_format_data(name="generate_mc_title")

    inputs = {
        "subject": generate_mc_title,
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
    playbook_run_id = phantom.playbook("poc1220/APG_create-mc-incident", container=container, name="playbook_apg_create_mc_incident_2", callback=playbook_apg_mc_emailincident_1, inputs=inputs)

    return


@phantom.playbook_block()
def generate_mc_title(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("generate_mc_title() called")

    template = """Phishing - {0}\n"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:filter_1:condition_1:artifact:*.cef.emailHeaders.Subject"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="generate_mc_title")

    playbook_apg_create_mc_incident_2(container=container)

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
    playbook_run_id = phantom.playbook("poc1220/APG_phish-cleanup", container=container, name="playbook_apg_phish_cleanup_1", callback=playbook_apg_extract_reportedmail_1, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_apg_mc_emailincident_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_apg_mc_emailincident_1() called")

    playbook_apg_create_mc_incident_2_output_mc_id = phantom.collect2(container=container, datapath=["playbook_apg_create_mc_incident_2:playbook_output:mc_id"])

    playbook_apg_create_mc_incident_2_output_mc_id_values = [item[0] for item in playbook_apg_create_mc_incident_2_output_mc_id]

    inputs = {
        "mc_id": playbook_apg_create_mc_incident_2_output_mc_id_values,
        "mail_tag": ["reported_mail"],
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "poc1220/APG_mc-emailIncident", returns the playbook_run_id
    playbook_run_id = phantom.playbook("poc1220/APG_mc-emailIncident", container=container, inputs=inputs)

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