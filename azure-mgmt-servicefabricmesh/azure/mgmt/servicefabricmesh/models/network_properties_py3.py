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


class NetworkProperties(Model):
    """Describes a network.

    All required parameters must be populated in order to send to Azure.

    :param description: User readable description of the network.
    :type description: str
    :param address_prefix: Required. the address prefix for this network.
    :type address_prefix: str
    :param ingress_config: Configuration for public connectivity for this
     network.
    :type ingress_config: ~azure.mgmt.servicefabricmesh.models.IngressConfig
    """

    _validation = {
        'address_prefix': {'required': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'address_prefix': {'key': 'addressPrefix', 'type': 'str'},
        'ingress_config': {'key': 'ingressConfig', 'type': 'IngressConfig'},
    }

    def __init__(self, *, address_prefix: str, description: str=None, ingress_config=None, **kwargs) -> None:
        super(NetworkProperties, self).__init__(**kwargs)
        self.description = description
        self.address_prefix = address_prefix
        self.ingress_config = ingress_config
