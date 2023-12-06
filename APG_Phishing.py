"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'select_email_vault' block
    select_email_vault(container=container)

    return

@phantom.playbook_block()
def select_email_vault(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("select_email_vault() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["reported_mail", "in", "artifact:*.tags"]
        ],
        name="select_email_vault:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        extract_ioc_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def extract_ioc_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("extract_ioc_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    id_value = container.get("id", None)
    filtered_artifact_0_data_select_email_vault = phantom.collect2(container=container, datapath=["filtered-data:select_email_vault:condition_1:artifact:*.cef.bodyHtml","filtered-data:select_email_vault:condition_1:artifact:*.id","filtered-data:select_email_vault:condition_1:artifact:*.external_id"])

    parameters = []

    # build parameters list for 'extract_ioc_1' call
    for filtered_artifact_0_item_select_email_vault in filtered_artifact_0_data_select_email_vault:
        parameters.append({
            "severity": "medium",
            "parse_domains": False,
            "run_automation": False,
            "remap_cef_fields": "Do not apply CEF -> CIM remapping, only apply custom remap",
            "custom_remap_json": "{}",
            "vault_id": "",
            "file_type": "html",
            "label": "",
            "artifact_tags": "reporting_mail",
            "container_id": id_value,
            "text": filtered_artifact_0_item_select_email_vault[0],
            "context": {'artifact_id': filtered_artifact_0_item_select_email_vault[1], 'artifact_external_id': filtered_artifact_0_item_select_email_vault[2]},
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("extract ioc", parameters=parameters, name="extract_ioc_1", assets=["parser"])

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