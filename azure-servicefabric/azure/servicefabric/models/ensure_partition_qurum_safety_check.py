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

from .partition_safety_check import PartitionSafetyCheck


class EnsurePartitionQurumSafetyCheck(PartitionSafetyCheck):
    """Safety check that ensures that a quorum of replicas are not lost for a
    partition.

    :param kind: Constant filled by server.
    :type kind: str
    :param partition_id:
    :type partition_id: str
    """

    _validation = {
        'kind': {'required': True},
    }

    def __init__(self, partition_id=None):
        super(EnsurePartitionQurumSafetyCheck, self).__init__(partition_id=partition_id)
        self.kind = 'EnsurePartitionQuorum'
