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

from .replica_health_py3 import ReplicaHealth


class StatelessServiceInstanceHealth(ReplicaHealth):
    """Represents the health of the stateless service instance.
    Contains the instance aggregated health state, the health events and the
    unhealthy evaluations.
    .

    All required parameters must be populated in order to send to Azure.

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
    :param partition_id: Id of the partition to which this replica belongs.
    :type partition_id: str
    :param service_kind: Required. Constant filled by server.
    :type service_kind: str
    :param instance_id: Id of a stateless service instance. InstanceId is used
     by Service Fabric to uniquely identify an instance of a partition of a
     stateless service. It is unique within a partition and does not change for
     the lifetime of the instance. If the instance has failed over on the same
     or different node, it will get a different value for the InstanceId.
    :type instance_id: str
    """

    _validation = {
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'health_events': {'key': 'HealthEvents', 'type': '[HealthEvent]'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
        'health_statistics': {'key': 'HealthStatistics', 'type': 'HealthStatistics'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
        'instance_id': {'key': 'InstanceId', 'type': 'str'},
    }

    def __init__(self, *, aggregated_health_state=None, health_events=None, unhealthy_evaluations=None, health_statistics=None, partition_id: str=None, instance_id: str=None, **kwargs) -> None:
        super(StatelessServiceInstanceHealth, self).__init__(aggregated_health_state=aggregated_health_state, health_events=health_events, unhealthy_evaluations=unhealthy_evaluations, health_statistics=health_statistics, partition_id=partition_id, **kwargs)
        self.instance_id = instance_id
        self.service_kind = 'Stateless'
