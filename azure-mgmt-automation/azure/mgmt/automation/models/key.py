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


class Key(Model):
    """Automation key which is used to register a DSC Node.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar key_name: Automation key name. Possible values include: 'Primary',
     'Secondary'
    :vartype key_name: str or ~azure.mgmt.automation.models.AutomationKeyName
    :ivar permissions: Automation key permissions. Possible values include:
     'Read', 'Full'
    :vartype permissions: str or
     ~azure.mgmt.automation.models.AutomationKeyPermissions
    :ivar value: Value of the Automation Key used for registration.
    :vartype value: str
    """

    _validation = {
        'key_name': {'readonly': True},
        'permissions': {'readonly': True},
        'value': {'readonly': True},
    }

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self):
        super(Key, self).__init__()
        self.key_name = None
        self.permissions = None
        self.value = None
