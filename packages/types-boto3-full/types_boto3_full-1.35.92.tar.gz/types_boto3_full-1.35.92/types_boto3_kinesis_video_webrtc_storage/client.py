"""
Type annotations for kinesis-video-webrtc-storage service Client.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_webrtc_storage/client/)

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_kinesis_video_webrtc_storage.client import KinesisVideoWebRTCStorageClient

    session = Session()
    client: KinesisVideoWebRTCStorageClient = session.client("kinesis-video-webrtc-storage")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Any, Mapping

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    EmptyResponseMetadataTypeDef,
    JoinStorageSessionAsViewerInputRequestTypeDef,
    JoinStorageSessionInputRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("KinesisVideoWebRTCStorageClient",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: type[BotocoreClientError]
    ClientError: type[BotocoreClientError]
    ClientLimitExceededException: type[BotocoreClientError]
    InvalidArgumentException: type[BotocoreClientError]
    ResourceNotFoundException: type[BotocoreClientError]


class KinesisVideoWebRTCStorageClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-webrtc-storage.html#KinesisVideoWebRTCStorage.Client)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_webrtc_storage/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisVideoWebRTCStorageClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-webrtc-storage.html#KinesisVideoWebRTCStorage.Client)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_webrtc_storage/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-webrtc-storage/client/can_paginate.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_webrtc_storage/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-webrtc-storage/client/generate_presigned_url.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_webrtc_storage/client/#generate_presigned_url)
        """

    def join_storage_session(
        self, **kwargs: Unpack[JoinStorageSessionInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Before using this API, you must call the
        <code>GetSignalingChannelEndpoint</code> API to request the WEBRTC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-webrtc-storage/client/join_storage_session.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_webrtc_storage/client/#join_storage_session)
        """

    def join_storage_session_as_viewer(
        self, **kwargs: Unpack[JoinStorageSessionAsViewerInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Join the ongoing one way-video and/or multi-way audio WebRTC session as a
        viewer for an input channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-webrtc-storage/client/join_storage_session_as_viewer.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_webrtc_storage/client/#join_storage_session_as_viewer)
        """
