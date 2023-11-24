"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_prepoc_url_sanitize_1' block
    playbook_prepoc_url_sanitize_1(container=container)

    return

@phantom.playbook_block()
def playbook_prepoc_url_check_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_prepoc_url_check_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "poc1220/prePOC URL check", returns the playbook_run_id
    playbook_run_id = phantom.playbook("poc1220/prePOC URL check", container=container, name="playbook_prepoc_url_check_1", callback=add_note_2, inputs=inputs)

    return


@phantom.playbook_block()
def add_note_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_note_2() called")

    playbook_prepoc_url_check_1_output_report = phantom.collect2(container=container, datapath=["playbook_prepoc_url_check_1:playbook_output:report"])

    playbook_prepoc_url_check_1_output_report_values = [item[0] for item in playbook_prepoc_url_check_1_output_report]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_note(container=container, content=playbook_prepoc_url_check_1_output_report_values, note_format="markdown", note_type="general", title="Virus Total")

    return


@phantom.playbook_block()
def playbook_prepoc_url_sanitize_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
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
    playbook_run_id = phantom.playbook("poc1220/prePoc URL sanitize", container=container, name="playbook_prepoc_url_sanitize_1", callback=playbook_prepoc_url_check_1, inputs=inputs)

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