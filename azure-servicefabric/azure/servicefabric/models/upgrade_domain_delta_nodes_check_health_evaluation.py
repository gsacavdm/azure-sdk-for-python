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

from .health_evaluation import HealthEvaluation


class UpgradeDomainDeltaNodesCheckHealthEvaluation(HealthEvaluation):
    """Represents health evaluation for delta unhealthy cluster nodes in an
    upgrade domain, containing health evaluations for each unhealthy node that
    impacted current aggregated health state.
    Can be returned during cluster upgrade when cluster aggregated health state
    is Warning or Error.
    .

    All required parameters must be populated in order to send to Azure.

    :param aggregated_health_state: The health state of a Service Fabric
     entity such as Cluster, Node, Application, Service, Partition, Replica
     etc. Possible values include: 'Invalid', 'Ok', 'Warning', 'Error',
     'Unknown'
    :type aggregated_health_state: str or
     ~azure.servicefabric.models.HealthState
    :param description: Description of the health evaluation, which represents
     a summary of the evaluation process.
    :type description: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param upgrade_domain_name: Name of the upgrade domain where nodes health
     is currently evaluated.
    :type upgrade_domain_name: str
    :param baseline_error_count: Number of upgrade domain nodes with
     aggregated heath state Error in the health store at the beginning of the
     cluster upgrade.
    :type baseline_error_count: long
    :param baseline_total_count: Total number of upgrade domain nodes in the
     health store at the beginning of the cluster upgrade.
    :type baseline_total_count: long
    :param max_percent_delta_unhealthy_nodes: Maximum allowed percentage of
     upgrade domain delta unhealthy nodes from the ClusterUpgradeHealthPolicy.
    :type max_percent_delta_unhealthy_nodes: int
    :param total_count: Total number of upgrade domain nodes in the health
     store.
    :type total_count: long
    :param unhealthy_evaluations: List of unhealthy evaluations that led to
     the aggregated health state. Includes all the unhealthy
     NodeHealthEvaluation that impacted the aggregated health.
    :type unhealthy_evaluations:
     list[~azure.servicefabric.models.HealthEvaluationWrapper]
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'upgrade_domain_name': {'key': 'UpgradeDomainName', 'type': 'str'},
        'baseline_error_count': {'key': 'BaselineErrorCount', 'type': 'long'},
        'baseline_total_count': {'key': 'BaselineTotalCount', 'type': 'long'},
        'max_percent_delta_unhealthy_nodes': {'key': 'MaxPercentDeltaUnhealthyNodes', 'type': 'int'},
        'total_count': {'key': 'TotalCount', 'type': 'long'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
    }

    def __init__(self, **kwargs):
        super(UpgradeDomainDeltaNodesCheckHealthEvaluation, self).__init__(**kwargs)
        self.upgrade_domain_name = kwargs.get('upgrade_domain_name', None)
        self.baseline_error_count = kwargs.get('baseline_error_count', None)
        self.baseline_total_count = kwargs.get('baseline_total_count', None)
        self.max_percent_delta_unhealthy_nodes = kwargs.get('max_percent_delta_unhealthy_nodes', None)
        self.total_count = kwargs.get('total_count', None)
        self.unhealthy_evaluations = kwargs.get('unhealthy_evaluations', None)
        self.kind = 'UpgradeDomainDeltaNodesCheck'
