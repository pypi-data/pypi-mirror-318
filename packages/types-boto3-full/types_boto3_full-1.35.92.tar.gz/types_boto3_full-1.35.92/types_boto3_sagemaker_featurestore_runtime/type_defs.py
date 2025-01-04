"""
Type annotations for sagemaker-featurestore-runtime service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_featurestore_runtime/type_defs/)

Usage::

    ```python
    from types_boto3_sagemaker_featurestore_runtime.type_defs import BatchGetRecordErrorTypeDef

    data: BatchGetRecordErrorTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Sequence, Union

from .literals import (
    DeletionModeType,
    ExpirationTimeResponseType,
    TargetStoreType,
    TtlDurationUnitType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "BatchGetRecordErrorTypeDef",
    "BatchGetRecordIdentifierOutputTypeDef",
    "BatchGetRecordIdentifierTypeDef",
    "BatchGetRecordIdentifierUnionTypeDef",
    "BatchGetRecordRequestRequestTypeDef",
    "BatchGetRecordResponseTypeDef",
    "BatchGetRecordResultDetailTypeDef",
    "DeleteRecordRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FeatureValueOutputTypeDef",
    "FeatureValueTypeDef",
    "FeatureValueUnionTypeDef",
    "GetRecordRequestRequestTypeDef",
    "GetRecordResponseTypeDef",
    "PutRecordRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TtlDurationTypeDef",
)


class BatchGetRecordErrorTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    ErrorCode: str
    ErrorMessage: str


class BatchGetRecordIdentifierOutputTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifiersValueAsString: list[str]
    FeatureNames: NotRequired[list[str]]


class BatchGetRecordIdentifierTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifiersValueAsString: Sequence[str]
    FeatureNames: NotRequired[Sequence[str]]


class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]


class FeatureValueOutputTypeDef(TypedDict):
    FeatureName: str
    ValueAsString: NotRequired[str]
    ValueAsStringList: NotRequired[list[str]]


class DeleteRecordRequestRequestTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    EventTime: str
    TargetStores: NotRequired[Sequence[TargetStoreType]]
    DeletionMode: NotRequired[DeletionModeType]


class FeatureValueTypeDef(TypedDict):
    FeatureName: str
    ValueAsString: NotRequired[str]
    ValueAsStringList: NotRequired[Sequence[str]]


class GetRecordRequestRequestTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    FeatureNames: NotRequired[Sequence[str]]
    ExpirationTimeResponse: NotRequired[ExpirationTimeResponseType]


class TtlDurationTypeDef(TypedDict):
    Unit: TtlDurationUnitType
    Value: int


BatchGetRecordIdentifierUnionTypeDef = Union[
    BatchGetRecordIdentifierTypeDef, BatchGetRecordIdentifierOutputTypeDef
]


class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetRecordResultDetailTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    Record: list[FeatureValueOutputTypeDef]
    ExpiresAt: NotRequired[str]


class GetRecordResponseTypeDef(TypedDict):
    Record: list[FeatureValueOutputTypeDef]
    ExpiresAt: str
    ResponseMetadata: ResponseMetadataTypeDef


FeatureValueUnionTypeDef = Union[FeatureValueTypeDef, FeatureValueOutputTypeDef]


class BatchGetRecordRequestRequestTypeDef(TypedDict):
    Identifiers: Sequence[BatchGetRecordIdentifierUnionTypeDef]
    ExpirationTimeResponse: NotRequired[ExpirationTimeResponseType]


class BatchGetRecordResponseTypeDef(TypedDict):
    Records: list[BatchGetRecordResultDetailTypeDef]
    Errors: list[BatchGetRecordErrorTypeDef]
    UnprocessedIdentifiers: list[BatchGetRecordIdentifierOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutRecordRequestRequestTypeDef(TypedDict):
    FeatureGroupName: str
    Record: Sequence[FeatureValueUnionTypeDef]
    TargetStores: NotRequired[Sequence[TargetStoreType]]
    TtlDuration: NotRequired[TtlDurationTypeDef]
