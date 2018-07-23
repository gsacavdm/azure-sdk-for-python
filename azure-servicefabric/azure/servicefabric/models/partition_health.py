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

from .entity_health import EntityHealth


class PartitionHealth(EntityHealth):
    """Information about the health of a Service Fabric partition.

    :param aggregated_health_state: The HealthState representing the
     aggregated health state of the entity computed by Health Manager.
     The health evaluation of the entity reflects all events reported on the
     entity and its children (if any).
     The aggregation is done by applying the desired health policy.
     . Possible values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str or
     ~azure.servicefabric.models.HealthState
    :param health_events: The list of health events reported on the entity.
    :type health_events: list[~azure.servicefabric.models.HealthEvent]
    :param unhealthy_evaluations: The unhealthy evaluations that show why the
     current aggregated health state was returned by Health Manager.
    :type unhealthy_evaluations:
     list[~azure.servicefabric.models.HealthEvaluationWrapper]
    :param health_statistics: Shows the health statistics for all children
     types of the queried entity.
    :type health_statistics: ~azure.servicefabric.models.HealthStatistics
    :param partition_id: ID of the partition whose health information is
     described by this object.
    :type partition_id: str
    :param replica_health_states: The list of replica health states associated
     with the partition.
    :type replica_health_states:
     list[~azure.servicefabric.models.ReplicaHealthState]
    """

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'health_events': {'key': 'HealthEvents', 'type': '[HealthEvent]'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
        'health_statistics': {'key': 'HealthStatistics', 'type': 'HealthStatistics'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'replica_health_states': {'key': 'ReplicaHealthStates', 'type': '[ReplicaHealthState]'},
    }

    def __init__(self, **kwargs):
        super(PartitionHealth, self).__init__(**kwargs)
        self.partition_id = kwargs.get('partition_id', None)
        self.replica_health_states = kwargs.get('replica_health_states', None)
