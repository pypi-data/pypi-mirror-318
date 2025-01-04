"""
Type annotations for service-quotas service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_service_quotas.client import ServiceQuotasClient

    session = Session()
    client: ServiceQuotasClient = session.client("service-quotas")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Any, Mapping, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAWSDefaultServiceQuotasPaginator,
    ListRequestedServiceQuotaChangeHistoryByQuotaPaginator,
    ListRequestedServiceQuotaChangeHistoryPaginator,
    ListServiceQuotaIncreaseRequestsInTemplatePaginator,
    ListServiceQuotasPaginator,
    ListServicesPaginator,
)
from .type_defs import (
    DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef,
    GetAssociationForServiceQuotaTemplateResponseTypeDef,
    GetAWSDefaultServiceQuotaRequestRequestTypeDef,
    GetAWSDefaultServiceQuotaResponseTypeDef,
    GetRequestedServiceQuotaChangeRequestRequestTypeDef,
    GetRequestedServiceQuotaChangeResponseTypeDef,
    GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef,
    GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef,
    GetServiceQuotaRequestRequestTypeDef,
    GetServiceQuotaResponseTypeDef,
    ListAWSDefaultServiceQuotasRequestRequestTypeDef,
    ListAWSDefaultServiceQuotasResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef,
    ListRequestedServiceQuotaChangeHistoryResponseTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef,
    ListServiceQuotasRequestRequestTypeDef,
    ListServiceQuotasResponseTypeDef,
    ListServicesRequestRequestTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef,
    PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef,
    RequestServiceQuotaIncreaseRequestRequestTypeDef,
    RequestServiceQuotaIncreaseResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ServiceQuotasClient",)

class Exceptions(BaseClientExceptions):
    AWSServiceAccessNotEnabledException: type[BotocoreClientError]
    AccessDeniedException: type[BotocoreClientError]
    ClientError: type[BotocoreClientError]
    DependencyAccessDeniedException: type[BotocoreClientError]
    IllegalArgumentException: type[BotocoreClientError]
    InvalidPaginationTokenException: type[BotocoreClientError]
    InvalidResourceStateException: type[BotocoreClientError]
    NoAvailableOrganizationException: type[BotocoreClientError]
    NoSuchResourceException: type[BotocoreClientError]
    OrganizationNotInAllFeaturesModeException: type[BotocoreClientError]
    QuotaExceededException: type[BotocoreClientError]
    ResourceAlreadyExistsException: type[BotocoreClientError]
    ServiceException: type[BotocoreClientError]
    ServiceQuotaTemplateNotInUseException: type[BotocoreClientError]
    TagPolicyViolationException: type[BotocoreClientError]
    TemplatesNotAvailableInRegionException: type[BotocoreClientError]
    TooManyRequestsException: type[BotocoreClientError]
    TooManyTagsException: type[BotocoreClientError]

class ServiceQuotasClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ServiceQuotasClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/can_paginate.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/generate_presigned_url.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#generate_presigned_url)
        """

    def associate_service_quota_template(self) -> dict[str, Any]:
        """
        Associates your quota request template with your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/associate_service_quota_template.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#associate_service_quota_template)
        """

    def delete_service_quota_increase_request_from_template(
        self, **kwargs: Unpack[DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef]
    ) -> dict[str, Any]:
        """
        Deletes the quota increase request for the specified quota from your quota
        request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/delete_service_quota_increase_request_from_template.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#delete_service_quota_increase_request_from_template)
        """

    def disassociate_service_quota_template(self) -> dict[str, Any]:
        """
        Disables your quota request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/disassociate_service_quota_template.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#disassociate_service_quota_template)
        """

    def get_aws_default_service_quota(
        self, **kwargs: Unpack[GetAWSDefaultServiceQuotaRequestRequestTypeDef]
    ) -> GetAWSDefaultServiceQuotaResponseTypeDef:
        """
        Retrieves the default value for the specified quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_aws_default_service_quota.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_aws_default_service_quota)
        """

    def get_association_for_service_quota_template(
        self,
    ) -> GetAssociationForServiceQuotaTemplateResponseTypeDef:
        """
        Retrieves the status of the association for the quota request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_association_for_service_quota_template.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_association_for_service_quota_template)
        """

    def get_requested_service_quota_change(
        self, **kwargs: Unpack[GetRequestedServiceQuotaChangeRequestRequestTypeDef]
    ) -> GetRequestedServiceQuotaChangeResponseTypeDef:
        """
        Retrieves information about the specified quota increase request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_requested_service_quota_change.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_requested_service_quota_change)
        """

    def get_service_quota(
        self, **kwargs: Unpack[GetServiceQuotaRequestRequestTypeDef]
    ) -> GetServiceQuotaResponseTypeDef:
        """
        Retrieves the applied quota value for the specified quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_service_quota.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_service_quota)
        """

    def get_service_quota_increase_request_from_template(
        self, **kwargs: Unpack[GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef]
    ) -> GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef:
        """
        Retrieves information about the specified quota increase request in your quota
        request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_service_quota_increase_request_from_template.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_service_quota_increase_request_from_template)
        """

    def list_aws_default_service_quotas(
        self, **kwargs: Unpack[ListAWSDefaultServiceQuotasRequestRequestTypeDef]
    ) -> ListAWSDefaultServiceQuotasResponseTypeDef:
        """
        Lists the default values for the quotas for the specified Amazon Web Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_aws_default_service_quotas.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_aws_default_service_quotas)
        """

    def list_requested_service_quota_change_history(
        self, **kwargs: Unpack[ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef]
    ) -> ListRequestedServiceQuotaChangeHistoryResponseTypeDef:
        """
        Retrieves the quota increase requests for the specified Amazon Web Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_requested_service_quota_change_history.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_requested_service_quota_change_history)
        """

    def list_requested_service_quota_change_history_by_quota(
        self, **kwargs: Unpack[ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef]
    ) -> ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef:
        """
        Retrieves the quota increase requests for the specified quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_requested_service_quota_change_history_by_quota.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_requested_service_quota_change_history_by_quota)
        """

    def list_service_quota_increase_requests_in_template(
        self, **kwargs: Unpack[ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef]
    ) -> ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef:
        """
        Lists the quota increase requests in the specified quota request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_service_quota_increase_requests_in_template.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_service_quota_increase_requests_in_template)
        """

    def list_service_quotas(
        self, **kwargs: Unpack[ListServiceQuotasRequestRequestTypeDef]
    ) -> ListServiceQuotasResponseTypeDef:
        """
        Lists the applied quota values for the specified Amazon Web Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_service_quotas.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_service_quotas)
        """

    def list_services(
        self, **kwargs: Unpack[ListServicesRequestRequestTypeDef]
    ) -> ListServicesResponseTypeDef:
        """
        Lists the names and codes for the Amazon Web Services integrated with Service
        Quotas.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_services.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_services)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags assigned to the specified applied quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/list_tags_for_resource.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#list_tags_for_resource)
        """

    def put_service_quota_increase_request_into_template(
        self, **kwargs: Unpack[PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef]
    ) -> PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef:
        """
        Adds a quota increase request to your quota request template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/put_service_quota_increase_request_into_template.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#put_service_quota_increase_request_into_template)
        """

    def request_service_quota_increase(
        self, **kwargs: Unpack[RequestServiceQuotaIncreaseRequestRequestTypeDef]
    ) -> RequestServiceQuotaIncreaseResponseTypeDef:
        """
        Submits a quota increase request for the specified quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/request_service_quota_increase.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#request_service_quota_increase)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> dict[str, Any]:
        """
        Adds tags to the specified applied quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/tag_resource.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> dict[str, Any]:
        """
        Removes tags from the specified applied quota.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/untag_resource.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_aws_default_service_quotas"]
    ) -> ListAWSDefaultServiceQuotasPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_requested_service_quota_change_history_by_quota"]
    ) -> ListRequestedServiceQuotaChangeHistoryByQuotaPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_requested_service_quota_change_history"]
    ) -> ListRequestedServiceQuotaChangeHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_quota_increase_requests_in_template"]
    ) -> ListServiceQuotaIncreaseRequestsInTemplatePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_quotas"]
    ) -> ListServiceQuotasPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_services"]
    ) -> ListServicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/client/get_paginator.html)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/client/#get_paginator)
        """
