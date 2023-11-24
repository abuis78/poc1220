"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'filter_eml_file' block
    filter_eml_file(container=container)

    return

@phantom.playbook_block()
def filter_eml_file(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_eml_file() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.name", "==", "eml_file"]
        ],
        name="filter_eml_file:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        parse_indicator_from_eml(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def parse_indicator_from_eml(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("parse_indicator_from_eml() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    id_value = container.get("id", None)
    filtered_artifact_0_data_filter_eml_file = phantom.collect2(container=container, datapath=["filtered-data:filter_eml_file:condition_1:artifact:*.cef.vaultId","filtered-data:filter_eml_file:condition_1:artifact:*.id"])

    parameters = []

    # build parameters list for 'parse_indicator_from_eml' call
    for filtered_artifact_0_item_filter_eml_file in filtered_artifact_0_data_filter_eml_file:
        parameters.append({
            "severity": "medium",
            "parse_domains": True,
            "run_automation": True,
            "remap_cef_fields": "Do not apply CEF -> CIM remapping, only apply custom remap",
            "custom_remap_json": "{}",
            "vault_id": filtered_artifact_0_item_filter_eml_file[0],
            "file_type": "email",
            "container_id": id_value,
            "context": {'artifact_id': filtered_artifact_0_item_filter_eml_file[1]},
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("extract ioc", parameters=parameters, name="parse_indicator_from_eml", assets=["parser"], callback=decision_1)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["artifact:*.name", "==", "File Artifact"]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        playbook_prepoc_malware_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    playbook_prepoc_phishing_1(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def playbook_prepoc_malware_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_prepoc_malware_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "poc1220/prePOC Malware", returns the playbook_run_id
    playbook_run_id = phantom.playbook("poc1220/prePOC Malware", container=container, name="playbook_prepoc_malware_1", callback=playbook_prepoc_malware_1_callback)

    return


@phantom.playbook_block()
def playbook_prepoc_malware_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_prepoc_malware_1_callback() called")

    
    # Downstream End block cannot be called directly, since execution will call on_finish automatically.
    # Using placeholder callback function so child playbook is run synchronously.


    return


@phantom.playbook_block()
def playbook_prepoc_phishing_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_prepoc_phishing_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "poc1220/prePOC Phishing", returns the playbook_run_id
    playbook_run_id = phantom.playbook("poc1220/prePOC Phishing", container=container, name="playbook_prepoc_phishing_1", callback=playbook_prepoc_phishing_1_callback)

    return


@phantom.playbook_block()
def playbook_prepoc_phishing_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_prepoc_phishing_1_callback() called")

    
    # Downstream End block cannot be called directly, since execution will call on_finish automatically.
    # Using placeholder callback function so child playbook is run synchronously.


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