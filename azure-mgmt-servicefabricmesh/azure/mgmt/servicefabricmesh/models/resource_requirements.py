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


class ResourceRequirements(Model):
    """This type describes the resource requirements for a container or a service.

    All required parameters must be populated in order to send to Azure.

    :param requests: Required. Describes the requested resources for a given
     container.
    :type requests: ~azure.mgmt.servicefabricmesh.models.ResourceRequests
    :param limits: Describes the maximum limits on the resources for a given
     container.
    :type limits: ~azure.mgmt.servicefabricmesh.models.ResourceLimits
    """

    _validation = {
        'requests': {'required': True},
    }

    _attribute_map = {
        'requests': {'key': 'requests', 'type': 'ResourceRequests'},
        'limits': {'key': 'limits', 'type': 'ResourceLimits'},
    }

    def __init__(self, **kwargs):
        super(ResourceRequirements, self).__init__(**kwargs)
        self.requests = kwargs.get('requests', None)
        self.limits = kwargs.get('limits', None)
