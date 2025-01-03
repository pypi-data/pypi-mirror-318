"""
Type annotations for accessanalyzer service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_accessanalyzer/type_defs/)

Usage::

    ```python
    from types_boto3_accessanalyzer.type_defs import AccessPreviewStatusReasonTypeDef

    data: AccessPreviewStatusReasonTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Mapping, Sequence, Union

from .literals import (
    AccessCheckPolicyTypeType,
    AccessCheckResourceTypeType,
    AccessPreviewStatusReasonCodeType,
    AccessPreviewStatusType,
    AclPermissionType,
    AnalyzerStatusType,
    CheckAccessNotGrantedResultType,
    CheckNoNewAccessResultType,
    CheckNoPublicAccessResultType,
    FindingChangeTypeType,
    FindingSourceTypeType,
    FindingStatusType,
    FindingStatusUpdateType,
    FindingTypeType,
    JobErrorCodeType,
    JobStatusType,
    KmsGrantOperationType,
    LocaleType,
    OrderByType,
    PolicyTypeType,
    ReasonCodeType,
    RecommendedRemediationActionType,
    ResourceControlPolicyRestrictionType,
    ResourceTypeType,
    StatusType,
    TypeType,
    ValidatePolicyFindingTypeType,
    ValidatePolicyResourceTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccessPreviewFindingTypeDef",
    "AccessPreviewStatusReasonTypeDef",
    "AccessPreviewSummaryTypeDef",
    "AccessPreviewTypeDef",
    "AccessTypeDef",
    "AclGranteeTypeDef",
    "AnalysisRuleCriteriaOutputTypeDef",
    "AnalysisRuleCriteriaTypeDef",
    "AnalysisRuleCriteriaUnionTypeDef",
    "AnalysisRuleOutputTypeDef",
    "AnalysisRuleTypeDef",
    "AnalysisRuleUnionTypeDef",
    "AnalyzedResourceSummaryTypeDef",
    "AnalyzedResourceTypeDef",
    "AnalyzerConfigurationOutputTypeDef",
    "AnalyzerConfigurationTypeDef",
    "AnalyzerSummaryTypeDef",
    "ApplyArchiveRuleRequestRequestTypeDef",
    "ArchiveRuleSummaryTypeDef",
    "CancelPolicyGenerationRequestRequestTypeDef",
    "CheckAccessNotGrantedRequestRequestTypeDef",
    "CheckAccessNotGrantedResponseTypeDef",
    "CheckNoNewAccessRequestRequestTypeDef",
    "CheckNoNewAccessResponseTypeDef",
    "CheckNoPublicAccessRequestRequestTypeDef",
    "CheckNoPublicAccessResponseTypeDef",
    "CloudTrailDetailsTypeDef",
    "CloudTrailPropertiesTypeDef",
    "ConfigurationOutputTypeDef",
    "ConfigurationTypeDef",
    "ConfigurationUnionTypeDef",
    "CreateAccessPreviewRequestRequestTypeDef",
    "CreateAccessPreviewResponseTypeDef",
    "CreateAnalyzerRequestRequestTypeDef",
    "CreateAnalyzerResponseTypeDef",
    "CreateArchiveRuleRequestRequestTypeDef",
    "CriterionOutputTypeDef",
    "CriterionTypeDef",
    "CriterionUnionTypeDef",
    "DeleteAnalyzerRequestRequestTypeDef",
    "DeleteArchiveRuleRequestRequestTypeDef",
    "DynamodbStreamConfigurationTypeDef",
    "DynamodbTableConfigurationTypeDef",
    "EbsSnapshotConfigurationOutputTypeDef",
    "EbsSnapshotConfigurationTypeDef",
    "EbsSnapshotConfigurationUnionTypeDef",
    "EcrRepositoryConfigurationTypeDef",
    "EfsFileSystemConfigurationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExternalAccessDetailsTypeDef",
    "FindingDetailsTypeDef",
    "FindingSourceDetailTypeDef",
    "FindingSourceTypeDef",
    "FindingSummaryTypeDef",
    "FindingSummaryV2TypeDef",
    "FindingTypeDef",
    "GenerateFindingRecommendationRequestRequestTypeDef",
    "GeneratedPolicyPropertiesTypeDef",
    "GeneratedPolicyResultTypeDef",
    "GeneratedPolicyTypeDef",
    "GetAccessPreviewRequestRequestTypeDef",
    "GetAccessPreviewResponseTypeDef",
    "GetAnalyzedResourceRequestRequestTypeDef",
    "GetAnalyzedResourceResponseTypeDef",
    "GetAnalyzerRequestRequestTypeDef",
    "GetAnalyzerResponseTypeDef",
    "GetArchiveRuleRequestRequestTypeDef",
    "GetArchiveRuleResponseTypeDef",
    "GetFindingRecommendationRequestPaginateTypeDef",
    "GetFindingRecommendationRequestRequestTypeDef",
    "GetFindingRecommendationResponseTypeDef",
    "GetFindingRequestRequestTypeDef",
    "GetFindingResponseTypeDef",
    "GetFindingV2RequestPaginateTypeDef",
    "GetFindingV2RequestRequestTypeDef",
    "GetFindingV2ResponseTypeDef",
    "GetGeneratedPolicyRequestRequestTypeDef",
    "GetGeneratedPolicyResponseTypeDef",
    "IamRoleConfigurationTypeDef",
    "InlineArchiveRuleTypeDef",
    "JobDetailsTypeDef",
    "JobErrorTypeDef",
    "KmsGrantConfigurationOutputTypeDef",
    "KmsGrantConfigurationTypeDef",
    "KmsGrantConfigurationUnionTypeDef",
    "KmsGrantConstraintsOutputTypeDef",
    "KmsGrantConstraintsTypeDef",
    "KmsGrantConstraintsUnionTypeDef",
    "KmsKeyConfigurationOutputTypeDef",
    "KmsKeyConfigurationTypeDef",
    "KmsKeyConfigurationUnionTypeDef",
    "ListAccessPreviewFindingsRequestPaginateTypeDef",
    "ListAccessPreviewFindingsRequestRequestTypeDef",
    "ListAccessPreviewFindingsResponseTypeDef",
    "ListAccessPreviewsRequestPaginateTypeDef",
    "ListAccessPreviewsRequestRequestTypeDef",
    "ListAccessPreviewsResponseTypeDef",
    "ListAnalyzedResourcesRequestPaginateTypeDef",
    "ListAnalyzedResourcesRequestRequestTypeDef",
    "ListAnalyzedResourcesResponseTypeDef",
    "ListAnalyzersRequestPaginateTypeDef",
    "ListAnalyzersRequestRequestTypeDef",
    "ListAnalyzersResponseTypeDef",
    "ListArchiveRulesRequestPaginateTypeDef",
    "ListArchiveRulesRequestRequestTypeDef",
    "ListArchiveRulesResponseTypeDef",
    "ListFindingsRequestPaginateTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListFindingsV2RequestPaginateTypeDef",
    "ListFindingsV2RequestRequestTypeDef",
    "ListFindingsV2ResponseTypeDef",
    "ListPolicyGenerationsRequestPaginateTypeDef",
    "ListPolicyGenerationsRequestRequestTypeDef",
    "ListPolicyGenerationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "NetworkOriginConfigurationOutputTypeDef",
    "NetworkOriginConfigurationTypeDef",
    "NetworkOriginConfigurationUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PathElementTypeDef",
    "PolicyGenerationDetailsTypeDef",
    "PolicyGenerationTypeDef",
    "PositionTypeDef",
    "RdsDbClusterSnapshotAttributeValueOutputTypeDef",
    "RdsDbClusterSnapshotAttributeValueTypeDef",
    "RdsDbClusterSnapshotAttributeValueUnionTypeDef",
    "RdsDbClusterSnapshotConfigurationOutputTypeDef",
    "RdsDbClusterSnapshotConfigurationTypeDef",
    "RdsDbClusterSnapshotConfigurationUnionTypeDef",
    "RdsDbSnapshotAttributeValueOutputTypeDef",
    "RdsDbSnapshotAttributeValueTypeDef",
    "RdsDbSnapshotAttributeValueUnionTypeDef",
    "RdsDbSnapshotConfigurationOutputTypeDef",
    "RdsDbSnapshotConfigurationTypeDef",
    "RdsDbSnapshotConfigurationUnionTypeDef",
    "ReasonSummaryTypeDef",
    "RecommendationErrorTypeDef",
    "RecommendedStepTypeDef",
    "ResponseMetadataTypeDef",
    "S3AccessPointConfigurationOutputTypeDef",
    "S3AccessPointConfigurationTypeDef",
    "S3AccessPointConfigurationUnionTypeDef",
    "S3BucketAclGrantConfigurationTypeDef",
    "S3BucketConfigurationOutputTypeDef",
    "S3BucketConfigurationTypeDef",
    "S3BucketConfigurationUnionTypeDef",
    "S3ExpressDirectoryBucketConfigurationTypeDef",
    "S3PublicAccessBlockConfigurationTypeDef",
    "SecretsManagerSecretConfigurationTypeDef",
    "SnsTopicConfigurationTypeDef",
    "SortCriteriaTypeDef",
    "SpanTypeDef",
    "SqsQueueConfigurationTypeDef",
    "StartPolicyGenerationRequestRequestTypeDef",
    "StartPolicyGenerationResponseTypeDef",
    "StartResourceScanRequestRequestTypeDef",
    "StatusReasonTypeDef",
    "SubstringTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimestampTypeDef",
    "TrailPropertiesTypeDef",
    "TrailTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UnusedAccessConfigurationOutputTypeDef",
    "UnusedAccessConfigurationTypeDef",
    "UnusedAccessConfigurationUnionTypeDef",
    "UnusedActionTypeDef",
    "UnusedIamRoleDetailsTypeDef",
    "UnusedIamUserAccessKeyDetailsTypeDef",
    "UnusedIamUserPasswordDetailsTypeDef",
    "UnusedPermissionDetailsTypeDef",
    "UnusedPermissionsRecommendedStepTypeDef",
    "UpdateAnalyzerRequestRequestTypeDef",
    "UpdateAnalyzerResponseTypeDef",
    "UpdateArchiveRuleRequestRequestTypeDef",
    "UpdateFindingsRequestRequestTypeDef",
    "ValidatePolicyFindingTypeDef",
    "ValidatePolicyRequestPaginateTypeDef",
    "ValidatePolicyRequestRequestTypeDef",
    "ValidatePolicyResponseTypeDef",
    "VpcConfigurationTypeDef",
)

class AccessPreviewStatusReasonTypeDef(TypedDict):
    code: AccessPreviewStatusReasonCodeType

class AccessTypeDef(TypedDict):
    actions: NotRequired[Sequence[str]]
    resources: NotRequired[Sequence[str]]

AclGranteeTypeDef = TypedDict(
    "AclGranteeTypeDef",
    {
        "id": NotRequired[str],
        "uri": NotRequired[str],
    },
)

class AnalysisRuleCriteriaOutputTypeDef(TypedDict):
    accountIds: NotRequired[list[str]]
    resourceTags: NotRequired[list[dict[str, str]]]

class AnalysisRuleCriteriaTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]
    resourceTags: NotRequired[Sequence[Mapping[str, str]]]

class AnalyzedResourceSummaryTypeDef(TypedDict):
    resourceArn: str
    resourceOwnerAccount: str
    resourceType: ResourceTypeType

class AnalyzedResourceTypeDef(TypedDict):
    resourceArn: str
    resourceType: ResourceTypeType
    createdAt: datetime
    analyzedAt: datetime
    updatedAt: datetime
    isPublic: bool
    resourceOwnerAccount: str
    actions: NotRequired[list[str]]
    sharedVia: NotRequired[list[str]]
    status: NotRequired[FindingStatusType]
    error: NotRequired[str]

class StatusReasonTypeDef(TypedDict):
    code: ReasonCodeType

class ApplyArchiveRuleRequestRequestTypeDef(TypedDict):
    analyzerArn: str
    ruleName: str
    clientToken: NotRequired[str]

class CriterionOutputTypeDef(TypedDict):
    eq: NotRequired[list[str]]
    neq: NotRequired[list[str]]
    contains: NotRequired[list[str]]
    exists: NotRequired[bool]

class CancelPolicyGenerationRequestRequestTypeDef(TypedDict):
    jobId: str

class ReasonSummaryTypeDef(TypedDict):
    description: NotRequired[str]
    statementIndex: NotRequired[int]
    statementId: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CheckNoNewAccessRequestRequestTypeDef(TypedDict):
    newPolicyDocument: str
    existingPolicyDocument: str
    policyType: AccessCheckPolicyTypeType

class CheckNoPublicAccessRequestRequestTypeDef(TypedDict):
    policyDocument: str
    resourceType: AccessCheckResourceTypeType

TimestampTypeDef = Union[datetime, str]

class TrailTypeDef(TypedDict):
    cloudTrailArn: str
    regions: NotRequired[Sequence[str]]
    allRegions: NotRequired[bool]

class TrailPropertiesTypeDef(TypedDict):
    cloudTrailArn: str
    regions: NotRequired[list[str]]
    allRegions: NotRequired[bool]

class DynamodbStreamConfigurationTypeDef(TypedDict):
    streamPolicy: NotRequired[str]

class DynamodbTableConfigurationTypeDef(TypedDict):
    tablePolicy: NotRequired[str]

class EbsSnapshotConfigurationOutputTypeDef(TypedDict):
    userIds: NotRequired[list[str]]
    groups: NotRequired[list[str]]
    kmsKeyId: NotRequired[str]

class EcrRepositoryConfigurationTypeDef(TypedDict):
    repositoryPolicy: NotRequired[str]

class EfsFileSystemConfigurationTypeDef(TypedDict):
    fileSystemPolicy: NotRequired[str]

class IamRoleConfigurationTypeDef(TypedDict):
    trustPolicy: NotRequired[str]

class S3ExpressDirectoryBucketConfigurationTypeDef(TypedDict):
    bucketPolicy: NotRequired[str]

class SecretsManagerSecretConfigurationTypeDef(TypedDict):
    kmsKeyId: NotRequired[str]
    secretPolicy: NotRequired[str]

class SnsTopicConfigurationTypeDef(TypedDict):
    topicPolicy: NotRequired[str]

class SqsQueueConfigurationTypeDef(TypedDict):
    queuePolicy: NotRequired[str]

class CriterionTypeDef(TypedDict):
    eq: NotRequired[Sequence[str]]
    neq: NotRequired[Sequence[str]]
    contains: NotRequired[Sequence[str]]
    exists: NotRequired[bool]

class DeleteAnalyzerRequestRequestTypeDef(TypedDict):
    analyzerName: str
    clientToken: NotRequired[str]

class DeleteArchiveRuleRequestRequestTypeDef(TypedDict):
    analyzerName: str
    ruleName: str
    clientToken: NotRequired[str]

class EbsSnapshotConfigurationTypeDef(TypedDict):
    userIds: NotRequired[Sequence[str]]
    groups: NotRequired[Sequence[str]]
    kmsKeyId: NotRequired[str]

class UnusedIamRoleDetailsTypeDef(TypedDict):
    lastAccessed: NotRequired[datetime]

class UnusedIamUserAccessKeyDetailsTypeDef(TypedDict):
    accessKeyId: str
    lastAccessed: NotRequired[datetime]

class UnusedIamUserPasswordDetailsTypeDef(TypedDict):
    lastAccessed: NotRequired[datetime]

class FindingSourceDetailTypeDef(TypedDict):
    accessPointArn: NotRequired[str]
    accessPointAccount: NotRequired[str]

FindingSummaryV2TypeDef = TypedDict(
    "FindingSummaryV2TypeDef",
    {
        "analyzedAt": datetime,
        "createdAt": datetime,
        "id": str,
        "resourceType": ResourceTypeType,
        "resourceOwnerAccount": str,
        "status": FindingStatusType,
        "updatedAt": datetime,
        "error": NotRequired[str],
        "resource": NotRequired[str],
        "findingType": NotRequired[FindingTypeType],
    },
)
GenerateFindingRecommendationRequestRequestTypeDef = TypedDict(
    "GenerateFindingRecommendationRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
    },
)

class GeneratedPolicyTypeDef(TypedDict):
    policy: str

class GetAccessPreviewRequestRequestTypeDef(TypedDict):
    accessPreviewId: str
    analyzerArn: str

class GetAnalyzedResourceRequestRequestTypeDef(TypedDict):
    analyzerArn: str
    resourceArn: str

class GetAnalyzerRequestRequestTypeDef(TypedDict):
    analyzerName: str

class GetArchiveRuleRequestRequestTypeDef(TypedDict):
    analyzerName: str
    ruleName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

GetFindingRecommendationRequestRequestTypeDef = TypedDict(
    "GetFindingRecommendationRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class RecommendationErrorTypeDef(TypedDict):
    code: str
    message: str

GetFindingRequestRequestTypeDef = TypedDict(
    "GetFindingRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
    },
)
GetFindingV2RequestRequestTypeDef = TypedDict(
    "GetFindingV2RequestRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class GetGeneratedPolicyRequestRequestTypeDef(TypedDict):
    jobId: str
    includeResourcePlaceholders: NotRequired[bool]
    includeServiceLevelTemplate: NotRequired[bool]

class JobErrorTypeDef(TypedDict):
    code: JobErrorCodeType
    message: str

class KmsGrantConstraintsOutputTypeDef(TypedDict):
    encryptionContextEquals: NotRequired[dict[str, str]]
    encryptionContextSubset: NotRequired[dict[str, str]]

class KmsGrantConstraintsTypeDef(TypedDict):
    encryptionContextEquals: NotRequired[Mapping[str, str]]
    encryptionContextSubset: NotRequired[Mapping[str, str]]

class ListAccessPreviewsRequestRequestTypeDef(TypedDict):
    analyzerArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListAnalyzedResourcesRequestRequestTypeDef(TypedDict):
    analyzerArn: str
    resourceType: NotRequired[ResourceTypeType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

ListAnalyzersRequestRequestTypeDef = TypedDict(
    "ListAnalyzersRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "type": NotRequired[TypeType],
    },
)

class ListArchiveRulesRequestRequestTypeDef(TypedDict):
    analyzerName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SortCriteriaTypeDef(TypedDict):
    attributeName: NotRequired[str]
    orderBy: NotRequired[OrderByType]

class ListPolicyGenerationsRequestRequestTypeDef(TypedDict):
    principalArn: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class PolicyGenerationTypeDef(TypedDict):
    jobId: str
    principalArn: str
    status: JobStatusType
    startedOn: datetime
    completedOn: NotRequired[datetime]

class ListTagsForResourceRequestRequestTypeDef(TypedDict):
    resourceArn: str

class VpcConfigurationTypeDef(TypedDict):
    vpcId: str

class SubstringTypeDef(TypedDict):
    start: int
    length: int

class PolicyGenerationDetailsTypeDef(TypedDict):
    principalArn: str

class PositionTypeDef(TypedDict):
    line: int
    column: int
    offset: int

class RdsDbClusterSnapshotAttributeValueOutputTypeDef(TypedDict):
    accountIds: NotRequired[list[str]]

class RdsDbClusterSnapshotAttributeValueTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]

class RdsDbSnapshotAttributeValueOutputTypeDef(TypedDict):
    accountIds: NotRequired[list[str]]

class RdsDbSnapshotAttributeValueTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]

class UnusedPermissionsRecommendedStepTypeDef(TypedDict):
    recommendedAction: RecommendedRemediationActionType
    policyUpdatedAt: NotRequired[datetime]
    recommendedPolicy: NotRequired[str]
    existingPolicyId: NotRequired[str]

class S3PublicAccessBlockConfigurationTypeDef(TypedDict):
    ignorePublicAcls: bool
    restrictPublicBuckets: bool

class StartResourceScanRequestRequestTypeDef(TypedDict):
    analyzerArn: str
    resourceArn: str
    resourceOwnerAccount: NotRequired[str]

class TagResourceRequestRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UnusedActionTypeDef(TypedDict):
    action: str
    lastAccessed: NotRequired[datetime]

class UpdateFindingsRequestRequestTypeDef(TypedDict):
    analyzerArn: str
    status: FindingStatusUpdateType
    ids: NotRequired[Sequence[str]]
    resourceArn: NotRequired[str]
    clientToken: NotRequired[str]

class ValidatePolicyRequestRequestTypeDef(TypedDict):
    policyDocument: str
    policyType: PolicyTypeType
    locale: NotRequired[LocaleType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    validatePolicyResourceType: NotRequired[ValidatePolicyResourceTypeType]

AccessPreviewSummaryTypeDef = TypedDict(
    "AccessPreviewSummaryTypeDef",
    {
        "id": str,
        "analyzerArn": str,
        "createdAt": datetime,
        "status": AccessPreviewStatusType,
        "statusReason": NotRequired[AccessPreviewStatusReasonTypeDef],
    },
)

class CheckAccessNotGrantedRequestRequestTypeDef(TypedDict):
    policyDocument: str
    access: Sequence[AccessTypeDef]
    policyType: AccessCheckPolicyTypeType

class S3BucketAclGrantConfigurationTypeDef(TypedDict):
    permission: AclPermissionType
    grantee: AclGranteeTypeDef

class AnalysisRuleOutputTypeDef(TypedDict):
    exclusions: NotRequired[list[AnalysisRuleCriteriaOutputTypeDef]]

AnalysisRuleCriteriaUnionTypeDef = Union[
    AnalysisRuleCriteriaTypeDef, AnalysisRuleCriteriaOutputTypeDef
]
ArchiveRuleSummaryTypeDef = TypedDict(
    "ArchiveRuleSummaryTypeDef",
    {
        "ruleName": str,
        "filter": dict[str, CriterionOutputTypeDef],
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)

class CheckAccessNotGrantedResponseTypeDef(TypedDict):
    result: CheckAccessNotGrantedResultType
    message: str
    reasons: list[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CheckNoNewAccessResponseTypeDef(TypedDict):
    result: CheckNoNewAccessResultType
    message: str
    reasons: list[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CheckNoPublicAccessResponseTypeDef(TypedDict):
    result: CheckNoPublicAccessResultType
    message: str
    reasons: list[ReasonSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

CreateAccessPreviewResponseTypeDef = TypedDict(
    "CreateAccessPreviewResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateAnalyzerResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnalyzedResourceResponseTypeDef(TypedDict):
    resource: AnalyzedResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnalyzedResourcesResponseTypeDef(TypedDict):
    analyzedResources: list[AnalyzedResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartPolicyGenerationResponseTypeDef(TypedDict):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CloudTrailDetailsTypeDef(TypedDict):
    trails: Sequence[TrailTypeDef]
    accessRole: str
    startTime: TimestampTypeDef
    endTime: NotRequired[TimestampTypeDef]

class CloudTrailPropertiesTypeDef(TypedDict):
    trailProperties: list[TrailPropertiesTypeDef]
    startTime: datetime
    endTime: datetime

CriterionUnionTypeDef = Union[CriterionTypeDef, CriterionOutputTypeDef]
ListAccessPreviewFindingsRequestRequestTypeDef = TypedDict(
    "ListAccessPreviewFindingsRequestRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
UpdateArchiveRuleRequestRequestTypeDef = TypedDict(
    "UpdateArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
        "filter": Mapping[str, CriterionTypeDef],
        "clientToken": NotRequired[str],
    },
)
EbsSnapshotConfigurationUnionTypeDef = Union[
    EbsSnapshotConfigurationTypeDef, EbsSnapshotConfigurationOutputTypeDef
]
FindingSourceTypeDef = TypedDict(
    "FindingSourceTypeDef",
    {
        "type": FindingSourceTypeType,
        "detail": NotRequired[FindingSourceDetailTypeDef],
    },
)

class ListFindingsV2ResponseTypeDef(TypedDict):
    findings: list[FindingSummaryV2TypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

GetFindingRecommendationRequestPaginateTypeDef = TypedDict(
    "GetFindingRecommendationRequestPaginateTypeDef",
    {
        "analyzerArn": str,
        "id": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetFindingV2RequestPaginateTypeDef = TypedDict(
    "GetFindingV2RequestPaginateTypeDef",
    {
        "analyzerArn": str,
        "id": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccessPreviewFindingsRequestPaginateTypeDef = TypedDict(
    "ListAccessPreviewFindingsRequestPaginateTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListAccessPreviewsRequestPaginateTypeDef(TypedDict):
    analyzerArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAnalyzedResourcesRequestPaginateTypeDef(TypedDict):
    analyzerArn: str
    resourceType: NotRequired[ResourceTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListAnalyzersRequestPaginateTypeDef = TypedDict(
    "ListAnalyzersRequestPaginateTypeDef",
    {
        "type": NotRequired[TypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListArchiveRulesRequestPaginateTypeDef(TypedDict):
    analyzerName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyGenerationsRequestPaginateTypeDef(TypedDict):
    principalArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ValidatePolicyRequestPaginateTypeDef(TypedDict):
    policyDocument: str
    policyType: PolicyTypeType
    locale: NotRequired[LocaleType]
    validatePolicyResourceType: NotRequired[ValidatePolicyResourceTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class JobDetailsTypeDef(TypedDict):
    jobId: str
    status: JobStatusType
    startedOn: datetime
    completedOn: NotRequired[datetime]
    jobError: NotRequired[JobErrorTypeDef]

class KmsGrantConfigurationOutputTypeDef(TypedDict):
    operations: list[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: NotRequired[str]
    constraints: NotRequired[KmsGrantConstraintsOutputTypeDef]

KmsGrantConstraintsUnionTypeDef = Union[
    KmsGrantConstraintsTypeDef, KmsGrantConstraintsOutputTypeDef
]
ListFindingsRequestPaginateTypeDef = TypedDict(
    "ListFindingsRequestPaginateTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "sort": NotRequired[SortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "sort": NotRequired[SortCriteriaTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFindingsV2RequestPaginateTypeDef = TypedDict(
    "ListFindingsV2RequestPaginateTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "sort": NotRequired[SortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsV2RequestRequestTypeDef = TypedDict(
    "ListFindingsV2RequestRequestTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sort": NotRequired[SortCriteriaTypeDef],
    },
)

class ListPolicyGenerationsResponseTypeDef(TypedDict):
    policyGenerations: list[PolicyGenerationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class NetworkOriginConfigurationOutputTypeDef(TypedDict):
    vpcConfiguration: NotRequired[VpcConfigurationTypeDef]
    internetConfiguration: NotRequired[dict[str, Any]]

class NetworkOriginConfigurationTypeDef(TypedDict):
    vpcConfiguration: NotRequired[VpcConfigurationTypeDef]
    internetConfiguration: NotRequired[Mapping[str, Any]]

class PathElementTypeDef(TypedDict):
    index: NotRequired[int]
    key: NotRequired[str]
    substring: NotRequired[SubstringTypeDef]
    value: NotRequired[str]

class SpanTypeDef(TypedDict):
    start: PositionTypeDef
    end: PositionTypeDef

class RdsDbClusterSnapshotConfigurationOutputTypeDef(TypedDict):
    attributes: NotRequired[dict[str, RdsDbClusterSnapshotAttributeValueOutputTypeDef]]
    kmsKeyId: NotRequired[str]

RdsDbClusterSnapshotAttributeValueUnionTypeDef = Union[
    RdsDbClusterSnapshotAttributeValueTypeDef, RdsDbClusterSnapshotAttributeValueOutputTypeDef
]

class RdsDbSnapshotConfigurationOutputTypeDef(TypedDict):
    attributes: NotRequired[dict[str, RdsDbSnapshotAttributeValueOutputTypeDef]]
    kmsKeyId: NotRequired[str]

RdsDbSnapshotAttributeValueUnionTypeDef = Union[
    RdsDbSnapshotAttributeValueTypeDef, RdsDbSnapshotAttributeValueOutputTypeDef
]

class RecommendedStepTypeDef(TypedDict):
    unusedPermissionsRecommendedStep: NotRequired[UnusedPermissionsRecommendedStepTypeDef]

class UnusedPermissionDetailsTypeDef(TypedDict):
    serviceNamespace: str
    actions: NotRequired[list[UnusedActionTypeDef]]
    lastAccessed: NotRequired[datetime]

class ListAccessPreviewsResponseTypeDef(TypedDict):
    accessPreviews: list[AccessPreviewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UnusedAccessConfigurationOutputTypeDef(TypedDict):
    unusedAccessAge: NotRequired[int]
    analysisRule: NotRequired[AnalysisRuleOutputTypeDef]

class AnalysisRuleTypeDef(TypedDict):
    exclusions: NotRequired[Sequence[AnalysisRuleCriteriaUnionTypeDef]]

class GetArchiveRuleResponseTypeDef(TypedDict):
    archiveRule: ArchiveRuleSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListArchiveRulesResponseTypeDef(TypedDict):
    archiveRules: list[ArchiveRuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartPolicyGenerationRequestRequestTypeDef(TypedDict):
    policyGenerationDetails: PolicyGenerationDetailsTypeDef
    cloudTrailDetails: NotRequired[CloudTrailDetailsTypeDef]
    clientToken: NotRequired[str]

class GeneratedPolicyPropertiesTypeDef(TypedDict):
    principalArn: str
    isComplete: NotRequired[bool]
    cloudTrailProperties: NotRequired[CloudTrailPropertiesTypeDef]

CreateArchiveRuleRequestRequestTypeDef = TypedDict(
    "CreateArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
        "filter": Mapping[str, CriterionUnionTypeDef],
        "clientToken": NotRequired[str],
    },
)
InlineArchiveRuleTypeDef = TypedDict(
    "InlineArchiveRuleTypeDef",
    {
        "ruleName": str,
        "filter": Mapping[str, CriterionUnionTypeDef],
    },
)
AccessPreviewFindingTypeDef = TypedDict(
    "AccessPreviewFindingTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "createdAt": datetime,
        "changeType": FindingChangeTypeType,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
        "existingFindingId": NotRequired[str],
        "existingFindingStatus": NotRequired[FindingStatusType],
        "principal": NotRequired[dict[str, str]],
        "action": NotRequired[list[str]],
        "condition": NotRequired[dict[str, str]],
        "resource": NotRequired[str],
        "isPublic": NotRequired[bool],
        "error": NotRequired[str],
        "sources": NotRequired[list[FindingSourceTypeDef]],
        "resourceControlPolicyRestriction": NotRequired[ResourceControlPolicyRestrictionType],
    },
)

class ExternalAccessDetailsTypeDef(TypedDict):
    condition: dict[str, str]
    action: NotRequired[list[str]]
    isPublic: NotRequired[bool]
    principal: NotRequired[dict[str, str]]
    sources: NotRequired[list[FindingSourceTypeDef]]
    resourceControlPolicyRestriction: NotRequired[ResourceControlPolicyRestrictionType]

FindingSummaryTypeDef = TypedDict(
    "FindingSummaryTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "condition": dict[str, str],
        "createdAt": datetime,
        "analyzedAt": datetime,
        "updatedAt": datetime,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
        "principal": NotRequired[dict[str, str]],
        "action": NotRequired[list[str]],
        "resource": NotRequired[str],
        "isPublic": NotRequired[bool],
        "error": NotRequired[str],
        "sources": NotRequired[list[FindingSourceTypeDef]],
        "resourceControlPolicyRestriction": NotRequired[ResourceControlPolicyRestrictionType],
    },
)
FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "condition": dict[str, str],
        "createdAt": datetime,
        "analyzedAt": datetime,
        "updatedAt": datetime,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
        "principal": NotRequired[dict[str, str]],
        "action": NotRequired[list[str]],
        "resource": NotRequired[str],
        "isPublic": NotRequired[bool],
        "error": NotRequired[str],
        "sources": NotRequired[list[FindingSourceTypeDef]],
        "resourceControlPolicyRestriction": NotRequired[ResourceControlPolicyRestrictionType],
    },
)

class KmsKeyConfigurationOutputTypeDef(TypedDict):
    keyPolicies: NotRequired[dict[str, str]]
    grants: NotRequired[list[KmsGrantConfigurationOutputTypeDef]]

class KmsGrantConfigurationTypeDef(TypedDict):
    operations: Sequence[KmsGrantOperationType]
    granteePrincipal: str
    issuingAccount: str
    retiringPrincipal: NotRequired[str]
    constraints: NotRequired[KmsGrantConstraintsUnionTypeDef]

class S3AccessPointConfigurationOutputTypeDef(TypedDict):
    accessPointPolicy: NotRequired[str]
    publicAccessBlock: NotRequired[S3PublicAccessBlockConfigurationTypeDef]
    networkOrigin: NotRequired[NetworkOriginConfigurationOutputTypeDef]

NetworkOriginConfigurationUnionTypeDef = Union[
    NetworkOriginConfigurationTypeDef, NetworkOriginConfigurationOutputTypeDef
]

class LocationTypeDef(TypedDict):
    path: list[PathElementTypeDef]
    span: SpanTypeDef

class RdsDbClusterSnapshotConfigurationTypeDef(TypedDict):
    attributes: NotRequired[Mapping[str, RdsDbClusterSnapshotAttributeValueUnionTypeDef]]
    kmsKeyId: NotRequired[str]

class RdsDbSnapshotConfigurationTypeDef(TypedDict):
    attributes: NotRequired[Mapping[str, RdsDbSnapshotAttributeValueUnionTypeDef]]
    kmsKeyId: NotRequired[str]

class GetFindingRecommendationResponseTypeDef(TypedDict):
    startedAt: datetime
    completedAt: datetime
    error: RecommendationErrorTypeDef
    resourceArn: str
    recommendedSteps: list[RecommendedStepTypeDef]
    recommendationType: Literal["UnusedPermissionRecommendation"]
    status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AnalyzerConfigurationOutputTypeDef(TypedDict):
    unusedAccess: NotRequired[UnusedAccessConfigurationOutputTypeDef]

AnalysisRuleUnionTypeDef = Union[AnalysisRuleTypeDef, AnalysisRuleOutputTypeDef]

class GeneratedPolicyResultTypeDef(TypedDict):
    properties: GeneratedPolicyPropertiesTypeDef
    generatedPolicies: NotRequired[list[GeneratedPolicyTypeDef]]

class ListAccessPreviewFindingsResponseTypeDef(TypedDict):
    findings: list[AccessPreviewFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class FindingDetailsTypeDef(TypedDict):
    externalAccessDetails: NotRequired[ExternalAccessDetailsTypeDef]
    unusedPermissionDetails: NotRequired[UnusedPermissionDetailsTypeDef]
    unusedIamUserAccessKeyDetails: NotRequired[UnusedIamUserAccessKeyDetailsTypeDef]
    unusedIamRoleDetails: NotRequired[UnusedIamRoleDetailsTypeDef]
    unusedIamUserPasswordDetails: NotRequired[UnusedIamUserPasswordDetailsTypeDef]

class ListFindingsResponseTypeDef(TypedDict):
    findings: list[FindingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetFindingResponseTypeDef(TypedDict):
    finding: FindingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

KmsGrantConfigurationUnionTypeDef = Union[
    KmsGrantConfigurationTypeDef, KmsGrantConfigurationOutputTypeDef
]

class S3BucketConfigurationOutputTypeDef(TypedDict):
    bucketPolicy: NotRequired[str]
    bucketAclGrants: NotRequired[list[S3BucketAclGrantConfigurationTypeDef]]
    bucketPublicAccessBlock: NotRequired[S3PublicAccessBlockConfigurationTypeDef]
    accessPoints: NotRequired[dict[str, S3AccessPointConfigurationOutputTypeDef]]

class S3AccessPointConfigurationTypeDef(TypedDict):
    accessPointPolicy: NotRequired[str]
    publicAccessBlock: NotRequired[S3PublicAccessBlockConfigurationTypeDef]
    networkOrigin: NotRequired[NetworkOriginConfigurationUnionTypeDef]

class ValidatePolicyFindingTypeDef(TypedDict):
    findingDetails: str
    findingType: ValidatePolicyFindingTypeType
    issueCode: str
    learnMoreLink: str
    locations: list[LocationTypeDef]

RdsDbClusterSnapshotConfigurationUnionTypeDef = Union[
    RdsDbClusterSnapshotConfigurationTypeDef, RdsDbClusterSnapshotConfigurationOutputTypeDef
]
RdsDbSnapshotConfigurationUnionTypeDef = Union[
    RdsDbSnapshotConfigurationTypeDef, RdsDbSnapshotConfigurationOutputTypeDef
]
AnalyzerSummaryTypeDef = TypedDict(
    "AnalyzerSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TypeType,
        "createdAt": datetime,
        "status": AnalyzerStatusType,
        "lastResourceAnalyzed": NotRequired[str],
        "lastResourceAnalyzedAt": NotRequired[datetime],
        "tags": NotRequired[dict[str, str]],
        "statusReason": NotRequired[StatusReasonTypeDef],
        "configuration": NotRequired[AnalyzerConfigurationOutputTypeDef],
    },
)

class UpdateAnalyzerResponseTypeDef(TypedDict):
    configuration: AnalyzerConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UnusedAccessConfigurationTypeDef(TypedDict):
    unusedAccessAge: NotRequired[int]
    analysisRule: NotRequired[AnalysisRuleUnionTypeDef]

class GetGeneratedPolicyResponseTypeDef(TypedDict):
    jobDetails: JobDetailsTypeDef
    generatedPolicyResult: GeneratedPolicyResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

GetFindingV2ResponseTypeDef = TypedDict(
    "GetFindingV2ResponseTypeDef",
    {
        "analyzedAt": datetime,
        "createdAt": datetime,
        "error": str,
        "id": str,
        "resource": str,
        "resourceType": ResourceTypeType,
        "resourceOwnerAccount": str,
        "status": FindingStatusType,
        "updatedAt": datetime,
        "findingDetails": list[FindingDetailsTypeDef],
        "findingType": FindingTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "nextToken": NotRequired[str],
    },
)

class KmsKeyConfigurationTypeDef(TypedDict):
    keyPolicies: NotRequired[Mapping[str, str]]
    grants: NotRequired[Sequence[KmsGrantConfigurationUnionTypeDef]]

class ConfigurationOutputTypeDef(TypedDict):
    ebsSnapshot: NotRequired[EbsSnapshotConfigurationOutputTypeDef]
    ecrRepository: NotRequired[EcrRepositoryConfigurationTypeDef]
    iamRole: NotRequired[IamRoleConfigurationTypeDef]
    efsFileSystem: NotRequired[EfsFileSystemConfigurationTypeDef]
    kmsKey: NotRequired[KmsKeyConfigurationOutputTypeDef]
    rdsDbClusterSnapshot: NotRequired[RdsDbClusterSnapshotConfigurationOutputTypeDef]
    rdsDbSnapshot: NotRequired[RdsDbSnapshotConfigurationOutputTypeDef]
    secretsManagerSecret: NotRequired[SecretsManagerSecretConfigurationTypeDef]
    s3Bucket: NotRequired[S3BucketConfigurationOutputTypeDef]
    snsTopic: NotRequired[SnsTopicConfigurationTypeDef]
    sqsQueue: NotRequired[SqsQueueConfigurationTypeDef]
    s3ExpressDirectoryBucket: NotRequired[S3ExpressDirectoryBucketConfigurationTypeDef]
    dynamodbStream: NotRequired[DynamodbStreamConfigurationTypeDef]
    dynamodbTable: NotRequired[DynamodbTableConfigurationTypeDef]

S3AccessPointConfigurationUnionTypeDef = Union[
    S3AccessPointConfigurationTypeDef, S3AccessPointConfigurationOutputTypeDef
]

class ValidatePolicyResponseTypeDef(TypedDict):
    findings: list[ValidatePolicyFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetAnalyzerResponseTypeDef(TypedDict):
    analyzer: AnalyzerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnalyzersResponseTypeDef(TypedDict):
    analyzers: list[AnalyzerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

UnusedAccessConfigurationUnionTypeDef = Union[
    UnusedAccessConfigurationTypeDef, UnusedAccessConfigurationOutputTypeDef
]
KmsKeyConfigurationUnionTypeDef = Union[
    KmsKeyConfigurationTypeDef, KmsKeyConfigurationOutputTypeDef
]
AccessPreviewTypeDef = TypedDict(
    "AccessPreviewTypeDef",
    {
        "id": str,
        "analyzerArn": str,
        "configurations": dict[str, ConfigurationOutputTypeDef],
        "createdAt": datetime,
        "status": AccessPreviewStatusType,
        "statusReason": NotRequired[AccessPreviewStatusReasonTypeDef],
    },
)

class S3BucketConfigurationTypeDef(TypedDict):
    bucketPolicy: NotRequired[str]
    bucketAclGrants: NotRequired[Sequence[S3BucketAclGrantConfigurationTypeDef]]
    bucketPublicAccessBlock: NotRequired[S3PublicAccessBlockConfigurationTypeDef]
    accessPoints: NotRequired[Mapping[str, S3AccessPointConfigurationUnionTypeDef]]

class AnalyzerConfigurationTypeDef(TypedDict):
    unusedAccess: NotRequired[UnusedAccessConfigurationUnionTypeDef]

class GetAccessPreviewResponseTypeDef(TypedDict):
    accessPreview: AccessPreviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

S3BucketConfigurationUnionTypeDef = Union[
    S3BucketConfigurationTypeDef, S3BucketConfigurationOutputTypeDef
]
CreateAnalyzerRequestRequestTypeDef = TypedDict(
    "CreateAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
        "type": TypeType,
        "archiveRules": NotRequired[Sequence[InlineArchiveRuleTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
        "configuration": NotRequired[AnalyzerConfigurationTypeDef],
    },
)

class UpdateAnalyzerRequestRequestTypeDef(TypedDict):
    analyzerName: str
    configuration: NotRequired[AnalyzerConfigurationTypeDef]

class ConfigurationTypeDef(TypedDict):
    ebsSnapshot: NotRequired[EbsSnapshotConfigurationUnionTypeDef]
    ecrRepository: NotRequired[EcrRepositoryConfigurationTypeDef]
    iamRole: NotRequired[IamRoleConfigurationTypeDef]
    efsFileSystem: NotRequired[EfsFileSystemConfigurationTypeDef]
    kmsKey: NotRequired[KmsKeyConfigurationUnionTypeDef]
    rdsDbClusterSnapshot: NotRequired[RdsDbClusterSnapshotConfigurationUnionTypeDef]
    rdsDbSnapshot: NotRequired[RdsDbSnapshotConfigurationUnionTypeDef]
    secretsManagerSecret: NotRequired[SecretsManagerSecretConfigurationTypeDef]
    s3Bucket: NotRequired[S3BucketConfigurationUnionTypeDef]
    snsTopic: NotRequired[SnsTopicConfigurationTypeDef]
    sqsQueue: NotRequired[SqsQueueConfigurationTypeDef]
    s3ExpressDirectoryBucket: NotRequired[S3ExpressDirectoryBucketConfigurationTypeDef]
    dynamodbStream: NotRequired[DynamodbStreamConfigurationTypeDef]
    dynamodbTable: NotRequired[DynamodbTableConfigurationTypeDef]

ConfigurationUnionTypeDef = Union[ConfigurationTypeDef, ConfigurationOutputTypeDef]

class CreateAccessPreviewRequestRequestTypeDef(TypedDict):
    analyzerArn: str
    configurations: Mapping[str, ConfigurationUnionTypeDef]
    clientToken: NotRequired[str]
