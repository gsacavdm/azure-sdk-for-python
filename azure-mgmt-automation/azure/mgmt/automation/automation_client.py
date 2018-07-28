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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.automation_account_operations import AutomationAccountOperations
from .operations.operations import Operations
from .operations.statistics_operations import StatisticsOperations
from .operations.usages_operations import UsagesOperations
from .operations.keys_operations import KeysOperations
from .operations.certificate_operations import CertificateOperations
from .operations.connection_operations import ConnectionOperations
from .operations.connection_type_operations import ConnectionTypeOperations
from .operations.credential_operations import CredentialOperations
from .operations.dsc_configuration_operations import DscConfigurationOperations
from .operations.hybrid_runbook_worker_group_operations import HybridRunbookWorkerGroupOperations
from .operations.job_schedule_operations import JobScheduleOperations
from .operations.linked_workspace_operations import LinkedWorkspaceOperations
from .operations.activity_operations import ActivityOperations
from .operations.module_operations import ModuleOperations
from .operations.object_data_types_operations import ObjectDataTypesOperations
from .operations.fields_operations import FieldsOperations
from .operations.runbook_draft_operations import RunbookDraftOperations
from .operations.runbook_operations import RunbookOperations
from .operations.test_job_streams_operations import TestJobStreamsOperations
from .operations.test_job_operations import TestJobOperations
from .operations.schedule_operations import ScheduleOperations
from .operations.variable_operations import VariableOperations
from .operations.webhook_operations import WebhookOperations
from .operations.watcher_operations import WatcherOperations
from .operations.software_update_configurations_operations import SoftwareUpdateConfigurationsOperations
from .operations.software_update_configuration_runs_operations import SoftwareUpdateConfigurationRunsOperations
from .operations.software_update_configuration_machine_runs_operations import SoftwareUpdateConfigurationMachineRunsOperations
from .operations.source_control_operations import SourceControlOperations
from .operations.source_control_sync_job_operations import SourceControlSyncJobOperations
from .operations.source_control_sync_job_streams_operations import SourceControlSyncJobStreamsOperations
from .operations.job_operations import JobOperations
from .operations.job_stream_operations import JobStreamOperations
from .operations.agent_registration_information_operations import AgentRegistrationInformationOperations
from .operations.dsc_node_operations import DscNodeOperations
from .operations.node_reports_operations import NodeReportsOperations
from .operations.dsc_compilation_job_operations import DscCompilationJobOperations
from .operations.dsc_compilation_job_stream_operations import DscCompilationJobStreamOperations
from .operations.dsc_node_configuration_operations import DscNodeConfigurationOperations
from .operations.node_count_information_operations import NodeCountInformationOperations
from . import models


class AutomationClientConfiguration(AzureConfiguration):
    """Configuration for AutomationClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param count_type1: The type of counts to retrieve. Possible values
     include: 'status', 'nodeconfiguration'
    :type count_type1: str or ~azure.mgmt.automation.models.CountType
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, count_type1, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if count_type1 is None:
            raise ValueError("Parameter 'count_type1' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(AutomationClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-automation/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id
        self.count_type1 = count_type1


class AutomationClient(SDKClient):
    """Automation Client

    :ivar config: Configuration for client.
    :vartype config: AutomationClientConfiguration

    :ivar automation_account: AutomationAccount operations
    :vartype automation_account: azure.mgmt.automation.operations.AutomationAccountOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.automation.operations.Operations
    :ivar statistics: Statistics operations
    :vartype statistics: azure.mgmt.automation.operations.StatisticsOperations
    :ivar usages: Usages operations
    :vartype usages: azure.mgmt.automation.operations.UsagesOperations
    :ivar keys: Keys operations
    :vartype keys: azure.mgmt.automation.operations.KeysOperations
    :ivar certificate: Certificate operations
    :vartype certificate: azure.mgmt.automation.operations.CertificateOperations
    :ivar connection: Connection operations
    :vartype connection: azure.mgmt.automation.operations.ConnectionOperations
    :ivar connection_type: ConnectionType operations
    :vartype connection_type: azure.mgmt.automation.operations.ConnectionTypeOperations
    :ivar credential: Credential operations
    :vartype credential: azure.mgmt.automation.operations.CredentialOperations
    :ivar dsc_configuration: DscConfiguration operations
    :vartype dsc_configuration: azure.mgmt.automation.operations.DscConfigurationOperations
    :ivar hybrid_runbook_worker_group: HybridRunbookWorkerGroup operations
    :vartype hybrid_runbook_worker_group: azure.mgmt.automation.operations.HybridRunbookWorkerGroupOperations
    :ivar job_schedule: JobSchedule operations
    :vartype job_schedule: azure.mgmt.automation.operations.JobScheduleOperations
    :ivar linked_workspace: LinkedWorkspace operations
    :vartype linked_workspace: azure.mgmt.automation.operations.LinkedWorkspaceOperations
    :ivar activity: Activity operations
    :vartype activity: azure.mgmt.automation.operations.ActivityOperations
    :ivar module: Module operations
    :vartype module: azure.mgmt.automation.operations.ModuleOperations
    :ivar object_data_types: ObjectDataTypes operations
    :vartype object_data_types: azure.mgmt.automation.operations.ObjectDataTypesOperations
    :ivar fields: Fields operations
    :vartype fields: azure.mgmt.automation.operations.FieldsOperations
    :ivar runbook_draft: RunbookDraft operations
    :vartype runbook_draft: azure.mgmt.automation.operations.RunbookDraftOperations
    :ivar runbook: Runbook operations
    :vartype runbook: azure.mgmt.automation.operations.RunbookOperations
    :ivar test_job_streams: TestJobStreams operations
    :vartype test_job_streams: azure.mgmt.automation.operations.TestJobStreamsOperations
    :ivar test_job: TestJob operations
    :vartype test_job: azure.mgmt.automation.operations.TestJobOperations
    :ivar schedule: Schedule operations
    :vartype schedule: azure.mgmt.automation.operations.ScheduleOperations
    :ivar variable: Variable operations
    :vartype variable: azure.mgmt.automation.operations.VariableOperations
    :ivar webhook: Webhook operations
    :vartype webhook: azure.mgmt.automation.operations.WebhookOperations
    :ivar watcher: Watcher operations
    :vartype watcher: azure.mgmt.automation.operations.WatcherOperations
    :ivar software_update_configurations: SoftwareUpdateConfigurations operations
    :vartype software_update_configurations: azure.mgmt.automation.operations.SoftwareUpdateConfigurationsOperations
    :ivar software_update_configuration_runs: SoftwareUpdateConfigurationRuns operations
    :vartype software_update_configuration_runs: azure.mgmt.automation.operations.SoftwareUpdateConfigurationRunsOperations
    :ivar software_update_configuration_machine_runs: SoftwareUpdateConfigurationMachineRuns operations
    :vartype software_update_configuration_machine_runs: azure.mgmt.automation.operations.SoftwareUpdateConfigurationMachineRunsOperations
    :ivar source_control: SourceControl operations
    :vartype source_control: azure.mgmt.automation.operations.SourceControlOperations
    :ivar source_control_sync_job: SourceControlSyncJob operations
    :vartype source_control_sync_job: azure.mgmt.automation.operations.SourceControlSyncJobOperations
    :ivar source_control_sync_job_streams: SourceControlSyncJobStreams operations
    :vartype source_control_sync_job_streams: azure.mgmt.automation.operations.SourceControlSyncJobStreamsOperations
    :ivar job: Job operations
    :vartype job: azure.mgmt.automation.operations.JobOperations
    :ivar job_stream: JobStream operations
    :vartype job_stream: azure.mgmt.automation.operations.JobStreamOperations
    :ivar agent_registration_information: AgentRegistrationInformation operations
    :vartype agent_registration_information: azure.mgmt.automation.operations.AgentRegistrationInformationOperations
    :ivar dsc_node: DscNode operations
    :vartype dsc_node: azure.mgmt.automation.operations.DscNodeOperations
    :ivar node_reports: NodeReports operations
    :vartype node_reports: azure.mgmt.automation.operations.NodeReportsOperations
    :ivar dsc_compilation_job: DscCompilationJob operations
    :vartype dsc_compilation_job: azure.mgmt.automation.operations.DscCompilationJobOperations
    :ivar dsc_compilation_job_stream: DscCompilationJobStream operations
    :vartype dsc_compilation_job_stream: azure.mgmt.automation.operations.DscCompilationJobStreamOperations
    :ivar dsc_node_configuration: DscNodeConfiguration operations
    :vartype dsc_node_configuration: azure.mgmt.automation.operations.DscNodeConfigurationOperations
    :ivar node_count_information: NodeCountInformation operations
    :vartype node_count_information: azure.mgmt.automation.operations.NodeCountInformationOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param count_type1: The type of counts to retrieve. Possible values
     include: 'status', 'nodeconfiguration'
    :type count_type1: str or ~azure.mgmt.automation.models.CountType
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, count_type1, base_url=None):

        self.config = AutomationClientConfiguration(credentials, subscription_id, count_type1, base_url)
        super(AutomationClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.automation_account = AutomationAccountOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.statistics = StatisticsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.keys = KeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.certificate = CertificateOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.connection = ConnectionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.connection_type = ConnectionTypeOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.credential = CredentialOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dsc_configuration = DscConfigurationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.hybrid_runbook_worker_group = HybridRunbookWorkerGroupOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.job_schedule = JobScheduleOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.linked_workspace = LinkedWorkspaceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.activity = ActivityOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.module = ModuleOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.object_data_types = ObjectDataTypesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.fields = FieldsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.runbook_draft = RunbookDraftOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.runbook = RunbookOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.test_job_streams = TestJobStreamsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.test_job = TestJobOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.schedule = ScheduleOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.variable = VariableOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.webhook = WebhookOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.watcher = WatcherOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.software_update_configurations = SoftwareUpdateConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.software_update_configuration_runs = SoftwareUpdateConfigurationRunsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.software_update_configuration_machine_runs = SoftwareUpdateConfigurationMachineRunsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.source_control = SourceControlOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.source_control_sync_job = SourceControlSyncJobOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.source_control_sync_job_streams = SourceControlSyncJobStreamsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.job = JobOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.job_stream = JobStreamOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.agent_registration_information = AgentRegistrationInformationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dsc_node = DscNodeOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.node_reports = NodeReportsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dsc_compilation_job = DscCompilationJobOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dsc_compilation_job_stream = DscCompilationJobStreamOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dsc_node_configuration = DscNodeConfigurationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.node_count_information = NodeCountInformationOperations(
            self._client, self.config, self._serialize, self._deserialize)
