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

from .resource_py3 import Resource


class VpnGateway(Resource):
    """VpnGateway Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param virtual_hub: The VirtualHub to which the gateway belongs
    :type virtual_hub: ~azure.mgmt.network.v2018_06_01.models.SubResource
    :param connections: list of all vpn connections to the gateway.
    :type connections:
     list[~azure.mgmt.network.v2018_06_01.models.VpnConnection]
    :param bgp_settings: Local network gateway's BGP speaker settings.
    :type bgp_settings: ~azure.mgmt.network.v2018_06_01.models.BgpSettings
    :param provisioning_state: The provisioning state of the resource.
     Possible values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :type provisioning_state: str or
     ~azure.mgmt.network.v2018_06_01.models.ProvisioningState
    :param policies: The policies applied to this vpn gateway.
    :type policies: ~azure.mgmt.network.v2018_06_01.models.Policies
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'virtual_hub': {'key': 'properties.virtualHub', 'type': 'SubResource'},
        'connections': {'key': 'properties.connections', 'type': '[VpnConnection]'},
        'bgp_settings': {'key': 'properties.bgpSettings', 'type': 'BgpSettings'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'policies': {'key': 'properties.policies', 'type': 'Policies'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, virtual_hub=None, connections=None, bgp_settings=None, provisioning_state=None, policies=None, **kwargs) -> None:
        super(VpnGateway, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.virtual_hub = virtual_hub
        self.connections = connections
        self.bgp_settings = bgp_settings
        self.provisioning_state = provisioning_state
        self.policies = policies
        self.etag = None
