"""
Type annotations for marketplace-reporting service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_reporting/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_marketplace_reporting.client import MarketplaceReportingServiceClient

    session = Session()
    client: MarketplaceReportingServiceClient = session.client("marketplace-reporting")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Any, Mapping

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import GetBuyerDashboardInputRequestTypeDef, GetBuyerDashboardOutputTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("MarketplaceReportingServiceClient",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: type[BotocoreClientError]
    BadRequestException: type[BotocoreClientError]
    ClientError: type[BotocoreClientError]
    InternalServerException: type[BotocoreClientError]
    UnauthorizedException: type[BotocoreClientError]


class MarketplaceReportingServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-reporting.html#MarketplaceReportingService.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_reporting/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MarketplaceReportingServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-reporting.html#MarketplaceReportingService.Client)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_reporting/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-reporting/client/can_paginate.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_reporting/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-reporting/client/generate_presigned_url.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_reporting/client/#generate_presigned_url)
        """

    def get_buyer_dashboard(
        self, **kwargs: Unpack[GetBuyerDashboardInputRequestTypeDef]
    ) -> GetBuyerDashboardOutputTypeDef:
        """
        Generates an embedding URL for an Amazon QuickSight dashboard for an anonymous
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-reporting/client/get_buyer_dashboard.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_reporting/client/#get_buyer_dashboard)
        """
