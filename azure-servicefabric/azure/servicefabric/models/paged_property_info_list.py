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


class PagedPropertyInfoList(Model):
    """The paged list of Service Fabric properties under a given name. The list is
    paged when all of the results cannot fit in a single message. The next set
    of results can be obtained by executing the same query with the
    continuation token provided in this list.

    :param continuation_token:
    :type continuation_token: str
    :param is_consistent: Indicates whether any property under the given name
     has been modified during the enumeration. If there was a modification,
     this property value is false.
    :type is_consistent: bool
    :param properties:
    :type properties: list of :class:`PropertyInfo
     <azure.servicefabric.models.PropertyInfo>`
    """

    _attribute_map = {
        'continuation_token': {'key': 'ContinuationToken', 'type': 'str'},
        'is_consistent': {'key': 'IsConsistent', 'type': 'bool'},
        'properties': {'key': 'Properties', 'type': '[PropertyInfo]'},
    }

    def __init__(self, continuation_token=None, is_consistent=None, properties=None):
        self.continuation_token = continuation_token
        self.is_consistent = is_consistent
        self.properties = properties