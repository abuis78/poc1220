"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'create_incidents_1' block
    create_incidents_1(container=container)

    return

@phantom.playbook_block()
def create_incidents_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("create_incidents_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    playbook_input_subject = phantom.collect2(container=container, datapath=["playbook_input:subject"])

    parameters = []

    # build parameters list for 'create_incidents_1' call
    for playbook_input_subject_item in playbook_input_subject:
        if playbook_input_subject_item[0] is not None:
            parameters.append({
                "name": playbook_input_subject_item[0],
                "incident_type": "",
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("create incidents", parameters=parameters, name="create_incidents_1", assets=["builtin_mc_connector"])

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