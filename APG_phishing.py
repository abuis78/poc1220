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