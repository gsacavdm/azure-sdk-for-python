# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HealthEvaluationWrapper(Model):
    """Wrapper object for health evaluation.

    :param health_evaluation:
    :type health_evaluation: :class:`HealthEvaluation
     <azure.servicefabric.models.HealthEvaluation>`
    """ 

    _attribute_map = {
        'health_evaluation': {'key': 'HealthEvaluation', 'type': 'HealthEvaluation'},
    }

    def __init__(self, health_evaluation=None):
        self.health_evaluation = health_evaluation