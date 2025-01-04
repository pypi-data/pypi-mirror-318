"""
Type annotations for dynamodbstreams service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dynamodbstreams/type_defs/)

Usage::

    ```python
    from types_boto3_dynamodbstreams.type_defs import AttributeValueTypeDef

    data: AttributeValueTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any

from .literals import (
    KeyTypeType,
    OperationTypeType,
    ShardIteratorTypeType,
    StreamStatusType,
    StreamViewTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AttributeValueTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "DescribeStreamOutputTypeDef",
    "GetRecordsInputRequestTypeDef",
    "GetRecordsOutputTypeDef",
    "GetShardIteratorInputRequestTypeDef",
    "GetShardIteratorOutputTypeDef",
    "IdentityTypeDef",
    "KeySchemaElementTypeDef",
    "ListStreamsInputRequestTypeDef",
    "ListStreamsOutputTypeDef",
    "RecordTypeDef",
    "ResponseMetadataTypeDef",
    "SequenceNumberRangeTypeDef",
    "ShardTypeDef",
    "StreamDescriptionTypeDef",
    "StreamRecordTypeDef",
    "StreamTypeDef",
)


class AttributeValueTypeDef(TypedDict):
    S: NotRequired[str]
    N: NotRequired[str]
    B: NotRequired[bytes]
    SS: NotRequired[list[str]]
    NS: NotRequired[list[str]]
    BS: NotRequired[list[bytes]]
    M: NotRequired[dict[str, dict[str, Any]]]
    L: NotRequired[list[dict[str, Any]]]
    NULL: NotRequired[bool]
    BOOL: NotRequired[bool]


class DescribeStreamInputRequestTypeDef(TypedDict):
    StreamArn: str
    Limit: NotRequired[int]
    ExclusiveStartShardId: NotRequired[str]


class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]


class GetRecordsInputRequestTypeDef(TypedDict):
    ShardIterator: str
    Limit: NotRequired[int]


class GetShardIteratorInputRequestTypeDef(TypedDict):
    StreamArn: str
    ShardId: str
    ShardIteratorType: ShardIteratorTypeType
    SequenceNumber: NotRequired[str]


IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "PrincipalId": NotRequired[str],
        "Type": NotRequired[str],
    },
)


class KeySchemaElementTypeDef(TypedDict):
    AttributeName: str
    KeyType: KeyTypeType


class ListStreamsInputRequestTypeDef(TypedDict):
    TableName: NotRequired[str]
    Limit: NotRequired[int]
    ExclusiveStartStreamArn: NotRequired[str]


class StreamTypeDef(TypedDict):
    StreamArn: NotRequired[str]
    TableName: NotRequired[str]
    StreamLabel: NotRequired[str]


class SequenceNumberRangeTypeDef(TypedDict):
    StartingSequenceNumber: NotRequired[str]
    EndingSequenceNumber: NotRequired[str]


class StreamRecordTypeDef(TypedDict):
    ApproximateCreationDateTime: NotRequired[datetime]
    Keys: NotRequired[dict[str, AttributeValueTypeDef]]
    NewImage: NotRequired[dict[str, AttributeValueTypeDef]]
    OldImage: NotRequired[dict[str, AttributeValueTypeDef]]
    SequenceNumber: NotRequired[str]
    SizeBytes: NotRequired[int]
    StreamViewType: NotRequired[StreamViewTypeType]


class GetShardIteratorOutputTypeDef(TypedDict):
    ShardIterator: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListStreamsOutputTypeDef(TypedDict):
    Streams: list[StreamTypeDef]
    LastEvaluatedStreamArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ShardTypeDef(TypedDict):
    ShardId: NotRequired[str]
    SequenceNumberRange: NotRequired[SequenceNumberRangeTypeDef]
    ParentShardId: NotRequired[str]


class RecordTypeDef(TypedDict):
    eventID: NotRequired[str]
    eventName: NotRequired[OperationTypeType]
    eventVersion: NotRequired[str]
    eventSource: NotRequired[str]
    awsRegion: NotRequired[str]
    dynamodb: NotRequired[StreamRecordTypeDef]
    userIdentity: NotRequired[IdentityTypeDef]


class StreamDescriptionTypeDef(TypedDict):
    StreamArn: NotRequired[str]
    StreamLabel: NotRequired[str]
    StreamStatus: NotRequired[StreamStatusType]
    StreamViewType: NotRequired[StreamViewTypeType]
    CreationRequestDateTime: NotRequired[datetime]
    TableName: NotRequired[str]
    KeySchema: NotRequired[list[KeySchemaElementTypeDef]]
    Shards: NotRequired[list[ShardTypeDef]]
    LastEvaluatedShardId: NotRequired[str]


class GetRecordsOutputTypeDef(TypedDict):
    Records: list[RecordTypeDef]
    NextShardIterator: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeStreamOutputTypeDef(TypedDict):
    StreamDescription: StreamDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
