"""
Type annotations for ec2-instance-connect service Client.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ec2_instance_connect/client/)

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_ec2_instance_connect.client import EC2InstanceConnectClient

    session = Session()
    client: EC2InstanceConnectClient = session.client("ec2-instance-connect")
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
    SendSerialConsoleSSHPublicKeyRequestRequestTypeDef,
    SendSerialConsoleSSHPublicKeyResponseTypeDef,
    SendSSHPublicKeyRequestRequestTypeDef,
    SendSSHPublicKeyResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("EC2InstanceConnectClient",)

class Exceptions(BaseClientExceptions):
    AuthException: type[BotocoreClientError]
    ClientError: type[BotocoreClientError]
    EC2InstanceNotFoundException: type[BotocoreClientError]
    EC2InstanceStateInvalidException: type[BotocoreClientError]
    EC2InstanceTypeInvalidException: type[BotocoreClientError]
    EC2InstanceUnavailableException: type[BotocoreClientError]
    InvalidArgsException: type[BotocoreClientError]
    SerialConsoleAccessDisabledException: type[BotocoreClientError]
    SerialConsoleSessionLimitExceededException: type[BotocoreClientError]
    SerialConsoleSessionUnavailableException: type[BotocoreClientError]
    SerialConsoleSessionUnsupportedException: type[BotocoreClientError]
    ServiceException: type[BotocoreClientError]
    ThrottlingException: type[BotocoreClientError]

class EC2InstanceConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ec2_instance_connect/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EC2InstanceConnectClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ec2_instance_connect/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect/client/can_paginate.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ec2_instance_connect/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect/client/generate_presigned_url.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ec2_instance_connect/client/#generate_presigned_url)
        """

    def send_ssh_public_key(
        self, **kwargs: Unpack[SendSSHPublicKeyRequestRequestTypeDef]
    ) -> SendSSHPublicKeyResponseTypeDef:
        """
        Pushes an SSH public key to the specified EC2 instance for use by the specified
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect/client/send_ssh_public_key.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ec2_instance_connect/client/#send_ssh_public_key)
        """

    def send_serial_console_ssh_public_key(
        self, **kwargs: Unpack[SendSerialConsoleSSHPublicKeyRequestRequestTypeDef]
    ) -> SendSerialConsoleSSHPublicKeyResponseTypeDef:
        """
        Pushes an SSH public key to the specified EC2 instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect/client/send_serial_console_ssh_public_key.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ec2_instance_connect/client/#send_serial_console_ssh_public_key)
        """
