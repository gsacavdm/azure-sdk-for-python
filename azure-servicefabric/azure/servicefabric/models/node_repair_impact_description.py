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

from .repair_impact_description_base import RepairImpactDescriptionBase


class NodeRepairImpactDescription(RepairImpactDescriptionBase):
    """Describes the expected impact of a repair on a set of nodes.
    This type supports the Service Fabric platform; it is not meant to be used
    directly from your code.
    .

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    :param node_impact_list: The list of nodes impacted by a repair action and
     their respective expected impact.
    :type node_impact_list: list[~azure.servicefabric.models.NodeImpact]
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'Kind', 'type': 'str'},
        'node_impact_list': {'key': 'NodeImpactList', 'type': '[NodeImpact]'},
    }

    def __init__(self, **kwargs):
        super(NodeRepairImpactDescription, self).__init__(**kwargs)
        self.node_impact_list = kwargs.get('node_impact_list', None)
        self.kind = 'Node'
