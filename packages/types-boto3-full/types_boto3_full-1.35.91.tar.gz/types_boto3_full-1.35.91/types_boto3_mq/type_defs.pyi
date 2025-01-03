"""
Type annotations for mq service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mq/type_defs/)

Usage::

    ```python
    from types_boto3_mq.type_defs import ActionRequiredTypeDef

    data: ActionRequiredTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Mapping, Sequence

from .literals import (
    AuthenticationStrategyType,
    BrokerStateType,
    BrokerStorageTypeType,
    ChangeTypeType,
    DataReplicationModeType,
    DayOfWeekType,
    DeploymentModeType,
    EngineTypeType,
    PromoteModeType,
    SanitizationWarningReasonType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ActionRequiredTypeDef",
    "AvailabilityZoneTypeDef",
    "BrokerEngineTypeTypeDef",
    "BrokerInstanceOptionTypeDef",
    "BrokerInstanceTypeDef",
    "BrokerSummaryTypeDef",
    "ConfigurationIdTypeDef",
    "ConfigurationRevisionTypeDef",
    "ConfigurationTypeDef",
    "ConfigurationsTypeDef",
    "CreateBrokerRequestRequestTypeDef",
    "CreateBrokerResponseTypeDef",
    "CreateConfigurationRequestRequestTypeDef",
    "CreateConfigurationResponseTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "DataReplicationCounterpartTypeDef",
    "DataReplicationMetadataOutputTypeDef",
    "DeleteBrokerRequestRequestTypeDef",
    "DeleteBrokerResponseTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeBrokerEngineTypesRequestRequestTypeDef",
    "DescribeBrokerEngineTypesResponseTypeDef",
    "DescribeBrokerInstanceOptionsRequestRequestTypeDef",
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    "DescribeBrokerRequestRequestTypeDef",
    "DescribeBrokerResponseTypeDef",
    "DescribeConfigurationRequestRequestTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionOptionsTypeDef",
    "EngineVersionTypeDef",
    "LdapServerMetadataInputTypeDef",
    "LdapServerMetadataOutputTypeDef",
    "ListBrokersRequestPaginateTypeDef",
    "ListBrokersRequestRequestTypeDef",
    "ListBrokersResponseTypeDef",
    "ListConfigurationRevisionsRequestRequestTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "LogsSummaryTypeDef",
    "LogsTypeDef",
    "PaginatorConfigTypeDef",
    "PendingLogsTypeDef",
    "PromoteRequestRequestTypeDef",
    "PromoteResponseTypeDef",
    "RebootBrokerRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SanitizationWarningTypeDef",
    "UpdateBrokerRequestRequestTypeDef",
    "UpdateBrokerResponseTypeDef",
    "UpdateConfigurationRequestRequestTypeDef",
    "UpdateConfigurationResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UserPendingChangesTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "WeeklyStartTimeTypeDef",
)

class ActionRequiredTypeDef(TypedDict):
    ActionRequiredCode: NotRequired[str]
    ActionRequiredInfo: NotRequired[str]

class AvailabilityZoneTypeDef(TypedDict):
    Name: NotRequired[str]

class EngineVersionTypeDef(TypedDict):
    Name: NotRequired[str]

class BrokerInstanceTypeDef(TypedDict):
    ConsoleURL: NotRequired[str]
    Endpoints: NotRequired[list[str]]
    IpAddress: NotRequired[str]

class BrokerSummaryTypeDef(TypedDict):
    DeploymentMode: DeploymentModeType
    EngineType: EngineTypeType
    BrokerArn: NotRequired[str]
    BrokerId: NotRequired[str]
    BrokerName: NotRequired[str]
    BrokerState: NotRequired[BrokerStateType]
    Created: NotRequired[datetime]
    HostInstanceType: NotRequired[str]

class ConfigurationIdTypeDef(TypedDict):
    Id: str
    Revision: NotRequired[int]

class ConfigurationRevisionTypeDef(TypedDict):
    Created: datetime
    Revision: int
    Description: NotRequired[str]

class EncryptionOptionsTypeDef(TypedDict):
    UseAwsOwnedKey: bool
    KmsKeyId: NotRequired[str]

class LdapServerMetadataInputTypeDef(TypedDict):
    Hosts: Sequence[str]
    RoleBase: str
    RoleSearchMatching: str
    ServiceAccountPassword: str
    ServiceAccountUsername: str
    UserBase: str
    UserSearchMatching: str
    RoleName: NotRequired[str]
    RoleSearchSubtree: NotRequired[bool]
    UserRoleName: NotRequired[str]
    UserSearchSubtree: NotRequired[bool]

class LogsTypeDef(TypedDict):
    Audit: NotRequired[bool]
    General: NotRequired[bool]

class UserTypeDef(TypedDict):
    Password: str
    Username: str
    ConsoleAccess: NotRequired[bool]
    Groups: NotRequired[Sequence[str]]
    ReplicationUser: NotRequired[bool]

class WeeklyStartTimeTypeDef(TypedDict):
    DayOfWeek: DayOfWeekType
    TimeOfDay: str
    TimeZone: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateConfigurationRequestRequestTypeDef(TypedDict):
    EngineType: EngineTypeType
    Name: str
    AuthenticationStrategy: NotRequired[AuthenticationStrategyType]
    EngineVersion: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateTagsRequestRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: NotRequired[Mapping[str, str]]

class CreateUserRequestRequestTypeDef(TypedDict):
    BrokerId: str
    Password: str
    Username: str
    ConsoleAccess: NotRequired[bool]
    Groups: NotRequired[Sequence[str]]
    ReplicationUser: NotRequired[bool]

class DataReplicationCounterpartTypeDef(TypedDict):
    BrokerId: str
    Region: str

class DeleteBrokerRequestRequestTypeDef(TypedDict):
    BrokerId: str

class DeleteTagsRequestRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class DeleteUserRequestRequestTypeDef(TypedDict):
    BrokerId: str
    Username: str

class DescribeBrokerEngineTypesRequestRequestTypeDef(TypedDict):
    EngineType: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeBrokerInstanceOptionsRequestRequestTypeDef(TypedDict):
    EngineType: NotRequired[str]
    HostInstanceType: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    StorageType: NotRequired[str]

class DescribeBrokerRequestRequestTypeDef(TypedDict):
    BrokerId: str

class LdapServerMetadataOutputTypeDef(TypedDict):
    Hosts: list[str]
    RoleBase: str
    RoleSearchMatching: str
    ServiceAccountUsername: str
    UserBase: str
    UserSearchMatching: str
    RoleName: NotRequired[str]
    RoleSearchSubtree: NotRequired[bool]
    UserRoleName: NotRequired[str]
    UserSearchSubtree: NotRequired[bool]

class UserSummaryTypeDef(TypedDict):
    Username: str
    PendingChange: NotRequired[ChangeTypeType]

class DescribeConfigurationRequestRequestTypeDef(TypedDict):
    ConfigurationId: str

class DescribeConfigurationRevisionRequestRequestTypeDef(TypedDict):
    ConfigurationId: str
    ConfigurationRevision: str

class DescribeUserRequestRequestTypeDef(TypedDict):
    BrokerId: str
    Username: str

class UserPendingChangesTypeDef(TypedDict):
    PendingChange: ChangeTypeType
    ConsoleAccess: NotRequired[bool]
    Groups: NotRequired[list[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListBrokersRequestRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListConfigurationRevisionsRequestRequestTypeDef(TypedDict):
    ConfigurationId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListConfigurationsRequestRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsRequestRequestTypeDef(TypedDict):
    ResourceArn: str

class ListUsersRequestRequestTypeDef(TypedDict):
    BrokerId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class PendingLogsTypeDef(TypedDict):
    Audit: NotRequired[bool]
    General: NotRequired[bool]

class PromoteRequestRequestTypeDef(TypedDict):
    BrokerId: str
    Mode: PromoteModeType

class RebootBrokerRequestRequestTypeDef(TypedDict):
    BrokerId: str

class SanitizationWarningTypeDef(TypedDict):
    Reason: SanitizationWarningReasonType
    AttributeName: NotRequired[str]
    ElementName: NotRequired[str]

class UpdateConfigurationRequestRequestTypeDef(TypedDict):
    ConfigurationId: str
    Data: str
    Description: NotRequired[str]

class UpdateUserRequestRequestTypeDef(TypedDict):
    BrokerId: str
    Username: str
    ConsoleAccess: NotRequired[bool]
    Groups: NotRequired[Sequence[str]]
    Password: NotRequired[str]
    ReplicationUser: NotRequired[bool]

class BrokerInstanceOptionTypeDef(TypedDict):
    AvailabilityZones: NotRequired[list[AvailabilityZoneTypeDef]]
    EngineType: NotRequired[EngineTypeType]
    HostInstanceType: NotRequired[str]
    StorageType: NotRequired[BrokerStorageTypeType]
    SupportedDeploymentModes: NotRequired[list[DeploymentModeType]]
    SupportedEngineVersions: NotRequired[list[str]]

class BrokerEngineTypeTypeDef(TypedDict):
    EngineType: NotRequired[EngineTypeType]
    EngineVersions: NotRequired[list[EngineVersionTypeDef]]

class ConfigurationsTypeDef(TypedDict):
    Current: NotRequired[ConfigurationIdTypeDef]
    History: NotRequired[list[ConfigurationIdTypeDef]]
    Pending: NotRequired[ConfigurationIdTypeDef]

class ConfigurationTypeDef(TypedDict):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategyType
    Created: datetime
    Description: str
    EngineType: EngineTypeType
    EngineVersion: str
    Id: str
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    Tags: NotRequired[dict[str, str]]

class CreateBrokerRequestRequestTypeDef(TypedDict):
    BrokerName: str
    DeploymentMode: DeploymentModeType
    EngineType: EngineTypeType
    HostInstanceType: str
    PubliclyAccessible: bool
    Users: Sequence[UserTypeDef]
    AuthenticationStrategy: NotRequired[AuthenticationStrategyType]
    AutoMinorVersionUpgrade: NotRequired[bool]
    Configuration: NotRequired[ConfigurationIdTypeDef]
    CreatorRequestId: NotRequired[str]
    EncryptionOptions: NotRequired[EncryptionOptionsTypeDef]
    EngineVersion: NotRequired[str]
    LdapServerMetadata: NotRequired[LdapServerMetadataInputTypeDef]
    Logs: NotRequired[LogsTypeDef]
    MaintenanceWindowStartTime: NotRequired[WeeklyStartTimeTypeDef]
    SecurityGroups: NotRequired[Sequence[str]]
    StorageType: NotRequired[BrokerStorageTypeType]
    SubnetIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Mapping[str, str]]
    DataReplicationMode: NotRequired[DataReplicationModeType]
    DataReplicationPrimaryBrokerArn: NotRequired[str]

class UpdateBrokerRequestRequestTypeDef(TypedDict):
    BrokerId: str
    AuthenticationStrategy: NotRequired[AuthenticationStrategyType]
    AutoMinorVersionUpgrade: NotRequired[bool]
    Configuration: NotRequired[ConfigurationIdTypeDef]
    EngineVersion: NotRequired[str]
    HostInstanceType: NotRequired[str]
    LdapServerMetadata: NotRequired[LdapServerMetadataInputTypeDef]
    Logs: NotRequired[LogsTypeDef]
    MaintenanceWindowStartTime: NotRequired[WeeklyStartTimeTypeDef]
    SecurityGroups: NotRequired[Sequence[str]]
    DataReplicationMode: NotRequired[DataReplicationModeType]

class CreateBrokerResponseTypeDef(TypedDict):
    BrokerArn: str
    BrokerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationResponseTypeDef(TypedDict):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategyType
    Created: datetime
    Id: str
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBrokerResponseTypeDef(TypedDict):
    BrokerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationResponseTypeDef(TypedDict):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategyType
    Created: datetime
    Description: str
    EngineType: EngineTypeType
    EngineVersion: str
    Id: str
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    Tags: dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationRevisionResponseTypeDef(TypedDict):
    ConfigurationId: str
    Created: datetime
    Data: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListBrokersResponseTypeDef(TypedDict):
    BrokerSummaries: list[BrokerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListConfigurationRevisionsResponseTypeDef(TypedDict):
    ConfigurationId: str
    MaxResults: int
    Revisions: list[ConfigurationRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsResponseTypeDef(TypedDict):
    Tags: dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PromoteResponseTypeDef(TypedDict):
    BrokerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataReplicationMetadataOutputTypeDef(TypedDict):
    DataReplicationRole: str
    DataReplicationCounterpart: NotRequired[DataReplicationCounterpartTypeDef]

class ListUsersResponseTypeDef(TypedDict):
    BrokerId: str
    MaxResults: int
    Users: list[UserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeUserResponseTypeDef(TypedDict):
    BrokerId: str
    ConsoleAccess: bool
    Groups: list[str]
    Pending: UserPendingChangesTypeDef
    Username: str
    ReplicationUser: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListBrokersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class LogsSummaryTypeDef(TypedDict):
    General: bool
    GeneralLogGroup: str
    Audit: NotRequired[bool]
    AuditLogGroup: NotRequired[str]
    Pending: NotRequired[PendingLogsTypeDef]

class UpdateConfigurationResponseTypeDef(TypedDict):
    Arn: str
    Created: datetime
    Id: str
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    Warnings: list[SanitizationWarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBrokerInstanceOptionsResponseTypeDef(TypedDict):
    BrokerInstanceOptions: list[BrokerInstanceOptionTypeDef]
    MaxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeBrokerEngineTypesResponseTypeDef(TypedDict):
    BrokerEngineTypes: list[BrokerEngineTypeTypeDef]
    MaxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListConfigurationsResponseTypeDef(TypedDict):
    Configurations: list[ConfigurationTypeDef]
    MaxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateBrokerResponseTypeDef(TypedDict):
    AuthenticationStrategy: AuthenticationStrategyType
    AutoMinorVersionUpgrade: bool
    BrokerId: str
    Configuration: ConfigurationIdTypeDef
    EngineVersion: str
    HostInstanceType: str
    LdapServerMetadata: LdapServerMetadataOutputTypeDef
    Logs: LogsTypeDef
    MaintenanceWindowStartTime: WeeklyStartTimeTypeDef
    SecurityGroups: list[str]
    DataReplicationMetadata: DataReplicationMetadataOutputTypeDef
    DataReplicationMode: DataReplicationModeType
    PendingDataReplicationMetadata: DataReplicationMetadataOutputTypeDef
    PendingDataReplicationMode: DataReplicationModeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBrokerResponseTypeDef(TypedDict):
    ActionsRequired: list[ActionRequiredTypeDef]
    AuthenticationStrategy: AuthenticationStrategyType
    AutoMinorVersionUpgrade: bool
    BrokerArn: str
    BrokerId: str
    BrokerInstances: list[BrokerInstanceTypeDef]
    BrokerName: str
    BrokerState: BrokerStateType
    Configurations: ConfigurationsTypeDef
    Created: datetime
    DeploymentMode: DeploymentModeType
    EncryptionOptions: EncryptionOptionsTypeDef
    EngineType: EngineTypeType
    EngineVersion: str
    HostInstanceType: str
    LdapServerMetadata: LdapServerMetadataOutputTypeDef
    Logs: LogsSummaryTypeDef
    MaintenanceWindowStartTime: WeeklyStartTimeTypeDef
    PendingAuthenticationStrategy: AuthenticationStrategyType
    PendingEngineVersion: str
    PendingHostInstanceType: str
    PendingLdapServerMetadata: LdapServerMetadataOutputTypeDef
    PendingSecurityGroups: list[str]
    PubliclyAccessible: bool
    SecurityGroups: list[str]
    StorageType: BrokerStorageTypeType
    SubnetIds: list[str]
    Tags: dict[str, str]
    Users: list[UserSummaryTypeDef]
    DataReplicationMetadata: DataReplicationMetadataOutputTypeDef
    DataReplicationMode: DataReplicationModeType
    PendingDataReplicationMetadata: DataReplicationMetadataOutputTypeDef
    PendingDataReplicationMode: DataReplicationModeType
    ResponseMetadata: ResponseMetadataTypeDef
