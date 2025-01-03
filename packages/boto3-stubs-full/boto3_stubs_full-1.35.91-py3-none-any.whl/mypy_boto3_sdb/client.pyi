"""
Type annotations for sdb service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sdb.client import SimpleDBClient

    session = Session()
    client: SimpleDBClient = session.client("sdb")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Any, Mapping, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListDomainsPaginator, SelectPaginator
from .type_defs import (
    BatchDeleteAttributesRequestRequestTypeDef,
    BatchPutAttributesRequestRequestTypeDef,
    CreateDomainRequestRequestTypeDef,
    DeleteAttributesRequestRequestTypeDef,
    DeleteDomainRequestRequestTypeDef,
    DomainMetadataRequestRequestTypeDef,
    DomainMetadataResultTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAttributesRequestRequestTypeDef,
    GetAttributesResultTypeDef,
    ListDomainsRequestRequestTypeDef,
    ListDomainsResultTypeDef,
    PutAttributesRequestRequestTypeDef,
    SelectRequestRequestTypeDef,
    SelectResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SimpleDBClient",)

class Exceptions(BaseClientExceptions):
    AttributeDoesNotExist: type[BotocoreClientError]
    ClientError: type[BotocoreClientError]
    DuplicateItemName: type[BotocoreClientError]
    InvalidNextToken: type[BotocoreClientError]
    InvalidNumberPredicates: type[BotocoreClientError]
    InvalidNumberValueTests: type[BotocoreClientError]
    InvalidParameterValue: type[BotocoreClientError]
    InvalidQueryExpression: type[BotocoreClientError]
    MissingParameter: type[BotocoreClientError]
    NoSuchDomain: type[BotocoreClientError]
    NumberDomainAttributesExceeded: type[BotocoreClientError]
    NumberDomainBytesExceeded: type[BotocoreClientError]
    NumberDomainsExceeded: type[BotocoreClientError]
    NumberItemAttributesExceeded: type[BotocoreClientError]
    NumberSubmittedAttributesExceeded: type[BotocoreClientError]
    NumberSubmittedItemsExceeded: type[BotocoreClientError]
    RequestTimeout: type[BotocoreClientError]
    TooManyRequestedAttributes: type[BotocoreClientError]

class SimpleDBClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb.html#SimpleDB.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SimpleDBClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb.html#SimpleDB.Client)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/can_paginate.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/generate_presigned_url.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#generate_presigned_url)
        """

    def batch_delete_attributes(
        self, **kwargs: Unpack[BatchDeleteAttributesRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Performs multiple DeleteAttributes operations in a single call, which reduces
        round trips and latencies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/batch_delete_attributes.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#batch_delete_attributes)
        """

    def batch_put_attributes(
        self, **kwargs: Unpack[BatchPutAttributesRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        The <code>BatchPutAttributes</code> operation creates or replaces attributes
        within one or more items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/batch_put_attributes.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#batch_put_attributes)
        """

    def create_domain(
        self, **kwargs: Unpack[CreateDomainRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        The <code>CreateDomain</code> operation creates a new domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/create_domain.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#create_domain)
        """

    def delete_attributes(
        self, **kwargs: Unpack[DeleteAttributesRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes one or more attributes associated with an item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/delete_attributes.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#delete_attributes)
        """

    def delete_domain(
        self, **kwargs: Unpack[DeleteDomainRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        The <code>DeleteDomain</code> operation deletes a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/delete_domain.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#delete_domain)
        """

    def domain_metadata(
        self, **kwargs: Unpack[DomainMetadataRequestRequestTypeDef]
    ) -> DomainMetadataResultTypeDef:
        """
        Returns information about the domain, including when the domain was created,
        the number of items and attributes in the domain, and the size of the attribute
        names and values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/domain_metadata.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#domain_metadata)
        """

    def get_attributes(
        self, **kwargs: Unpack[GetAttributesRequestRequestTypeDef]
    ) -> GetAttributesResultTypeDef:
        """
        Returns all of the attributes associated with the specified item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/get_attributes.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#get_attributes)
        """

    def list_domains(
        self, **kwargs: Unpack[ListDomainsRequestRequestTypeDef]
    ) -> ListDomainsResultTypeDef:
        """
        The <code>ListDomains</code> operation lists all domains associated with the
        Access Key ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/list_domains.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#list_domains)
        """

    def put_attributes(
        self, **kwargs: Unpack[PutAttributesRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        The PutAttributes operation creates or replaces attributes in an item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/put_attributes.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#put_attributes)
        """

    def select(self, **kwargs: Unpack[SelectRequestRequestTypeDef]) -> SelectResultTypeDef:
        """
        The <code>Select</code> operation returns a set of attributes for
        <code>ItemNames</code> that match the select expression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/select.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#select)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domains"]
    ) -> ListDomainsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/get_paginator.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["select"]
    ) -> SelectPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/get_paginator.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#get_paginator)
        """
