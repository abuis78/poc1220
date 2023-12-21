"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'select_email_artifacts_0' block
    select_email_artifacts_0(container=container)

    return

@phantom.playbook_block()
def select_email_artifacts_0(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("select_email_artifacts_0() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["playbook_input:mail_tag", "in", "artifact:*.tags"]
        ],
        name="select_email_artifacts_0:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        artifact_type(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def artifact_type(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("artifact_type() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["filtered-data:select_email_artifacts_0:condition_1:artifact:*.label", "==", "Email Artifact"]
        ],
        name="artifact_type:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        set_summary_fields_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def set_summary_fields_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("set_summary_fields_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    playbook_input_mc_id = phantom.collect2(container=container, datapath=["playbook_input:mc_id"])
    filtered_artifact_0_data_artifact_type = phantom.collect2(container=container, datapath=["filtered-data:artifact_type:condition_1:artifact:*.cef.emailHeaders.To","filtered-data:artifact_type:condition_1:artifact:*.id","filtered-data:artifact_type:condition_1:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'set_summary_fields_1' call
    for playbook_input_mc_id_item in playbook_input_mc_id:
        for filtered_artifact_0_item_artifact_type in filtered_artifact_0_data_artifact_type:
            if playbook_input_mc_id_item[0] is not None:
                parameters.append({
                    "incident_id": playbook_input_mc_id_item[0],
                    "pairs": [
                        { "name": "To", "value": filtered_artifact_0_item_artifact_type[0] },
                        { "name": "From", "value": filtered_artifact_0_item_artifact_type[0] },
                    ],
                    "context": {'artifact_id': filtered_artifact_0_item_artifact_type[1], 'artifact_external_id': filtered_artifact_0_item_artifact_type[2]},
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