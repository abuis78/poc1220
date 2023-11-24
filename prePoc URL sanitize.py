"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'filter_safelinks_url_artifacts' block
    filter_safelinks_url_artifacts(container=container)

    return

@phantom.playbook_block()
def filter_safelinks_url_artifacts(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_safelinks_url_artifacts() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="and",
        conditions=[
            ["artifact:*.name", "==", "URL Artifact"],
            ["safelinks.protection.outlook.com", "in", "artifact:*.cef.requestURL"]
        ],
        name="filter_safelinks_url_artifacts:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        url_safelink_extract_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def debug_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_1() called")

    filtered_artifact_0_data_filter_1 = phantom.collect2(container=container, datapath=["filtered-data:filter_1:condition_1:artifact:*.id","filtered-data:filter_1:condition_1:artifact:*.id"])
    url_safelink_extract_2__result = phantom.collect2(container=container, datapath=["url_safelink_extract_2:custom_function_result.data.actual_url"])
    format_json_artifact_update__as_list = phantom.get_format_data(name="format_json_artifact_update__as_list")

    filtered_artifact_0__id = [item[0] for item in filtered_artifact_0_data_filter_1]
    url_safelink_extract_2_data_actual_url = [item[0] for item in url_safelink_extract_2__result]

    parameters = []

    parameters.append({
        "input_1": filtered_artifact_0__id,
        "input_2": url_safelink_extract_2_data_actual_url,
        "input_3": format_json_artifact_update__as_list,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_1")

    return


@phantom.playbook_block()
def url_safelink_extract_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("url_safelink_extract_2() called")

    filtered_artifact_0_data_filter_safelinks_url_artifacts = phantom.collect2(container=container, datapath=["filtered-data:filter_safelinks_url_artifacts:condition_1:artifact:*.cef.requestURL","filtered-data:filter_safelinks_url_artifacts:condition_1:artifact:*.id"])

    parameters = []

    # build parameters list for 'url_safelink_extract_2' call
    for filtered_artifact_0_item_filter_safelinks_url_artifacts in filtered_artifact_0_data_filter_safelinks_url_artifacts:
        parameters.append({
            "protected_url": filtered_artifact_0_item_filter_safelinks_url_artifacts[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="poc1220/url_safelink_extract", parameters=parameters, name="url_safelink_extract_2", callback=format_json_artifact_update)

    return


@phantom.playbook_block()
def format_json_artifact_update(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_json_artifact_update() called")

    template = """%%\n{{\"cef\": {{ \"requestURL\": {0}, \"requestURL_old\": {1} }}\n}}\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "url_safelink_extract_2:custom_function_result.data.actual_url",
        "filtered-data:filter_safelinks_url_artifacts:condition_1:artifact:*.cef.requestURL"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_json_artifact_update")

    debug_1(container=container)

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