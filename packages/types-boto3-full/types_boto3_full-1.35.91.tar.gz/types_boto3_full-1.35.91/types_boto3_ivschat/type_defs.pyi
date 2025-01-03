"""
Type annotations for ivschat service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ivschat/type_defs/)

Usage::

    ```python
    from types_boto3_ivschat.type_defs import CloudWatchLogsDestinationConfigurationTypeDef

    data: CloudWatchLogsDestinationConfigurationTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Mapping, Sequence

from .literals import ChatTokenCapabilityType, FallbackResultType, LoggingConfigurationStateType

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "CloudWatchLogsDestinationConfigurationTypeDef",
    "CreateChatTokenRequestRequestTypeDef",
    "CreateChatTokenResponseTypeDef",
    "CreateLoggingConfigurationRequestRequestTypeDef",
    "CreateLoggingConfigurationResponseTypeDef",
    "CreateRoomRequestRequestTypeDef",
    "CreateRoomResponseTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeleteMessageRequestRequestTypeDef",
    "DeleteMessageResponseTypeDef",
    "DeleteRoomRequestRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "DisconnectUserRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FirehoseDestinationConfigurationTypeDef",
    "GetLoggingConfigurationRequestRequestTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetRoomRequestRequestTypeDef",
    "GetRoomResponseTypeDef",
    "ListLoggingConfigurationsRequestRequestTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListRoomsRequestRequestTypeDef",
    "ListRoomsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingConfigurationSummaryTypeDef",
    "MessageReviewHandlerTypeDef",
    "ResponseMetadataTypeDef",
    "RoomSummaryTypeDef",
    "S3DestinationConfigurationTypeDef",
    "SendEventRequestRequestTypeDef",
    "SendEventResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "UpdateRoomRequestRequestTypeDef",
    "UpdateRoomResponseTypeDef",
)

class CloudWatchLogsDestinationConfigurationTypeDef(TypedDict):
    logGroupName: str

class CreateChatTokenRequestRequestTypeDef(TypedDict):
    roomIdentifier: str
    userId: str
    capabilities: NotRequired[Sequence[ChatTokenCapabilityType]]
    sessionDurationInMinutes: NotRequired[int]
    attributes: NotRequired[Mapping[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class MessageReviewHandlerTypeDef(TypedDict):
    uri: NotRequired[str]
    fallbackResult: NotRequired[FallbackResultType]

class DeleteLoggingConfigurationRequestRequestTypeDef(TypedDict):
    identifier: str

DeleteMessageRequestRequestTypeDef = TypedDict(
    "DeleteMessageRequestRequestTypeDef",
    {
        "roomIdentifier": str,
        "id": str,
        "reason": NotRequired[str],
    },
)

class DeleteRoomRequestRequestTypeDef(TypedDict):
    identifier: str

class FirehoseDestinationConfigurationTypeDef(TypedDict):
    deliveryStreamName: str

class S3DestinationConfigurationTypeDef(TypedDict):
    bucketName: str

class DisconnectUserRequestRequestTypeDef(TypedDict):
    roomIdentifier: str
    userId: str
    reason: NotRequired[str]

class GetLoggingConfigurationRequestRequestTypeDef(TypedDict):
    identifier: str

class GetRoomRequestRequestTypeDef(TypedDict):
    identifier: str

class ListLoggingConfigurationsRequestRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListRoomsRequestRequestTypeDef(TypedDict):
    name: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    messageReviewHandlerUri: NotRequired[str]
    loggingConfigurationIdentifier: NotRequired[str]

class ListTagsForResourceRequestRequestTypeDef(TypedDict):
    resourceArn: str

class SendEventRequestRequestTypeDef(TypedDict):
    roomIdentifier: str
    eventName: str
    attributes: NotRequired[Mapping[str, str]]

class TagResourceRequestRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateChatTokenResponseTypeDef(TypedDict):
    token: str
    tokenExpirationTime: datetime
    sessionExpirationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

DeleteMessageResponseTypeDef = TypedDict(
    "DeleteMessageResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

SendEventResponseTypeDef = TypedDict(
    "SendEventResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateRoomRequestRequestTypeDef(TypedDict):
    name: NotRequired[str]
    maximumMessageRatePerSecond: NotRequired[int]
    maximumMessageLength: NotRequired[int]
    messageReviewHandler: NotRequired[MessageReviewHandlerTypeDef]
    tags: NotRequired[Mapping[str, str]]
    loggingConfigurationIdentifiers: NotRequired[Sequence[str]]

CreateRoomResponseTypeDef = TypedDict(
    "CreateRoomResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "maximumMessageRatePerSecond": int,
        "maximumMessageLength": int,
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "tags": dict[str, str],
        "loggingConfigurationIdentifiers": list[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRoomResponseTypeDef = TypedDict(
    "GetRoomResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "maximumMessageRatePerSecond": int,
        "maximumMessageLength": int,
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "tags": dict[str, str],
        "loggingConfigurationIdentifiers": list[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RoomSummaryTypeDef = TypedDict(
    "RoomSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "messageReviewHandler": NotRequired[MessageReviewHandlerTypeDef],
        "createTime": NotRequired[datetime],
        "updateTime": NotRequired[datetime],
        "tags": NotRequired[dict[str, str]],
        "loggingConfigurationIdentifiers": NotRequired[list[str]],
    },
)

class UpdateRoomRequestRequestTypeDef(TypedDict):
    identifier: str
    name: NotRequired[str]
    maximumMessageRatePerSecond: NotRequired[int]
    maximumMessageLength: NotRequired[int]
    messageReviewHandler: NotRequired[MessageReviewHandlerTypeDef]
    loggingConfigurationIdentifiers: NotRequired[Sequence[str]]

UpdateRoomResponseTypeDef = TypedDict(
    "UpdateRoomResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "maximumMessageRatePerSecond": int,
        "maximumMessageLength": int,
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "tags": dict[str, str],
        "loggingConfigurationIdentifiers": list[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DestinationConfigurationTypeDef(TypedDict):
    s3: NotRequired[S3DestinationConfigurationTypeDef]
    cloudWatchLogs: NotRequired[CloudWatchLogsDestinationConfigurationTypeDef]
    firehose: NotRequired[FirehoseDestinationConfigurationTypeDef]

class ListRoomsResponseTypeDef(TypedDict):
    rooms: list[RoomSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateLoggingConfigurationRequestRequestTypeDef(TypedDict):
    destinationConfiguration: DestinationConfigurationTypeDef
    name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

CreateLoggingConfigurationResponseTypeDef = TypedDict(
    "CreateLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "createTime": datetime,
        "updateTime": datetime,
        "name": str,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "state": Literal["ACTIVE"],
        "tags": dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLoggingConfigurationResponseTypeDef = TypedDict(
    "GetLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "createTime": datetime,
        "updateTime": datetime,
        "name": str,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "state": LoggingConfigurationStateType,
        "tags": dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoggingConfigurationSummaryTypeDef = TypedDict(
    "LoggingConfigurationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "createTime": NotRequired[datetime],
        "updateTime": NotRequired[datetime],
        "name": NotRequired[str],
        "destinationConfiguration": NotRequired[DestinationConfigurationTypeDef],
        "state": NotRequired[LoggingConfigurationStateType],
        "tags": NotRequired[dict[str, str]],
    },
)

class UpdateLoggingConfigurationRequestRequestTypeDef(TypedDict):
    identifier: str
    name: NotRequired[str]
    destinationConfiguration: NotRequired[DestinationConfigurationTypeDef]

UpdateLoggingConfigurationResponseTypeDef = TypedDict(
    "UpdateLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "createTime": datetime,
        "updateTime": datetime,
        "name": str,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "state": Literal["ACTIVE"],
        "tags": dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListLoggingConfigurationsResponseTypeDef(TypedDict):
    loggingConfigurations: list[LoggingConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
