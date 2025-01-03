"""
Type annotations for notifications service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/type_defs/)

Usage::

    ```python
    from mypy_boto3_notifications.type_defs import AssociateChannelRequestRequestTypeDef

    data: AssociateChannelRequestRequestTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Mapping, Sequence, Union

from .literals import (
    AggregationDurationType,
    AggregationEventTypeType,
    EventRuleStatusType,
    EventStatusType,
    LocaleCodeType,
    NotificationConfigurationStatusType,
    NotificationHubStatusType,
    NotificationTypeType,
    TextPartTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AssociateChannelRequestRequestTypeDef",
    "CreateEventRuleRequestRequestTypeDef",
    "CreateEventRuleResponseTypeDef",
    "CreateNotificationConfigurationRequestRequestTypeDef",
    "CreateNotificationConfigurationResponseTypeDef",
    "DeleteEventRuleRequestRequestTypeDef",
    "DeleteNotificationConfigurationRequestRequestTypeDef",
    "DeregisterNotificationHubRequestRequestTypeDef",
    "DeregisterNotificationHubResponseTypeDef",
    "DimensionTypeDef",
    "DisassociateChannelRequestRequestTypeDef",
    "EventRuleStatusSummaryTypeDef",
    "EventRuleStructureTypeDef",
    "GetEventRuleRequestRequestTypeDef",
    "GetEventRuleResponseTypeDef",
    "GetNotificationConfigurationRequestRequestTypeDef",
    "GetNotificationConfigurationResponseTypeDef",
    "GetNotificationEventRequestRequestTypeDef",
    "GetNotificationEventResponseTypeDef",
    "ListChannelsRequestPaginateTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListEventRulesRequestPaginateTypeDef",
    "ListEventRulesRequestRequestTypeDef",
    "ListEventRulesResponseTypeDef",
    "ListNotificationConfigurationsRequestPaginateTypeDef",
    "ListNotificationConfigurationsRequestRequestTypeDef",
    "ListNotificationConfigurationsResponseTypeDef",
    "ListNotificationEventsRequestPaginateTypeDef",
    "ListNotificationEventsRequestRequestTypeDef",
    "ListNotificationEventsResponseTypeDef",
    "ListNotificationHubsRequestPaginateTypeDef",
    "ListNotificationHubsRequestRequestTypeDef",
    "ListNotificationHubsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MediaElementTypeDef",
    "MessageComponentsSummaryTypeDef",
    "MessageComponentsTypeDef",
    "NotificationConfigurationStructureTypeDef",
    "NotificationEventOverviewTypeDef",
    "NotificationEventSummaryTypeDef",
    "NotificationEventTypeDef",
    "NotificationHubOverviewTypeDef",
    "NotificationHubStatusSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterNotificationHubRequestRequestTypeDef",
    "RegisterNotificationHubResponseTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "SourceEventMetadataSummaryTypeDef",
    "SourceEventMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TextPartValueTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEventRuleRequestRequestTypeDef",
    "UpdateEventRuleResponseTypeDef",
    "UpdateNotificationConfigurationRequestRequestTypeDef",
    "UpdateNotificationConfigurationResponseTypeDef",
)


class AssociateChannelRequestRequestTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str


class CreateEventRuleRequestRequestTypeDef(TypedDict):
    notificationConfigurationArn: str
    source: str
    eventType: str
    regions: Sequence[str]
    eventPattern: NotRequired[str]


class EventRuleStatusSummaryTypeDef(TypedDict):
    status: EventRuleStatusType
    reason: str


class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]


class CreateNotificationConfigurationRequestRequestTypeDef(TypedDict):
    name: str
    description: str
    aggregationDuration: NotRequired[AggregationDurationType]
    tags: NotRequired[Mapping[str, str]]


class DeleteEventRuleRequestRequestTypeDef(TypedDict):
    arn: str


class DeleteNotificationConfigurationRequestRequestTypeDef(TypedDict):
    arn: str


class DeregisterNotificationHubRequestRequestTypeDef(TypedDict):
    notificationHubRegion: str


class NotificationHubStatusSummaryTypeDef(TypedDict):
    status: NotificationHubStatusType
    reason: str


class DimensionTypeDef(TypedDict):
    name: str
    value: str


class DisassociateChannelRequestRequestTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str


class GetEventRuleRequestRequestTypeDef(TypedDict):
    arn: str


class GetNotificationConfigurationRequestRequestTypeDef(TypedDict):
    arn: str


class GetNotificationEventRequestRequestTypeDef(TypedDict):
    arn: str
    locale: NotRequired[LocaleCodeType]


class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]


class ListChannelsRequestRequestTypeDef(TypedDict):
    notificationConfigurationArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]


class ListEventRulesRequestRequestTypeDef(TypedDict):
    notificationConfigurationArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]


class ListNotificationConfigurationsRequestRequestTypeDef(TypedDict):
    eventRuleSource: NotRequired[str]
    channelArn: NotRequired[str]
    status: NotRequired[NotificationConfigurationStatusType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]


class NotificationConfigurationStructureTypeDef(TypedDict):
    arn: str
    name: str
    description: str
    status: NotificationConfigurationStatusType
    creationTime: datetime
    aggregationDuration: NotRequired[AggregationDurationType]


TimestampTypeDef = Union[datetime, str]


class ListNotificationHubsRequestRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]


class ListTagsForResourceRequestRequestTypeDef(TypedDict):
    arn: str


MediaElementTypeDef = TypedDict(
    "MediaElementTypeDef",
    {
        "mediaId": str,
        "type": Literal["IMAGE"],
        "url": str,
        "caption": str,
    },
)


class MessageComponentsSummaryTypeDef(TypedDict):
    headline: str


class SourceEventMetadataSummaryTypeDef(TypedDict):
    source: str
    eventType: str
    eventOriginRegion: NotRequired[str]


TextPartValueTypeDef = TypedDict(
    "TextPartValueTypeDef",
    {
        "type": TextPartTypeType,
        "displayText": NotRequired[str],
        "textByLocale": NotRequired[dict[LocaleCodeType, str]],
        "url": NotRequired[str],
    },
)


class RegisterNotificationHubRequestRequestTypeDef(TypedDict):
    notificationHubRegion: str


ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "detailUrl": NotRequired[str],
        "tags": NotRequired[list[str]],
    },
)


class TagResourceRequestRequestTypeDef(TypedDict):
    arn: str
    tags: Mapping[str, str]


class UntagResourceRequestRequestTypeDef(TypedDict):
    arn: str
    tagKeys: Sequence[str]


class UpdateEventRuleRequestRequestTypeDef(TypedDict):
    arn: str
    eventPattern: NotRequired[str]
    regions: NotRequired[Sequence[str]]


class UpdateNotificationConfigurationRequestRequestTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    description: NotRequired[str]
    aggregationDuration: NotRequired[AggregationDurationType]


class EventRuleStructureTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    source: str
    eventType: str
    eventPattern: str
    regions: list[str]
    managedRules: list[str]
    statusSummaryByRegion: dict[str, EventRuleStatusSummaryTypeDef]


class CreateEventRuleResponseTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    statusSummaryByRegion: dict[str, EventRuleStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateNotificationConfigurationResponseTypeDef(TypedDict):
    arn: str
    status: NotificationConfigurationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetEventRuleResponseTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    source: str
    eventType: str
    eventPattern: str
    regions: list[str]
    managedRules: list[str]
    statusSummaryByRegion: dict[str, EventRuleStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetNotificationConfigurationResponseTypeDef(TypedDict):
    arn: str
    name: str
    description: str
    status: NotificationConfigurationStatusType
    creationTime: datetime
    aggregationDuration: AggregationDurationType
    ResponseMetadata: ResponseMetadataTypeDef


class ListChannelsResponseTypeDef(TypedDict):
    channels: list[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]


class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEventRuleResponseTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    statusSummaryByRegion: dict[str, EventRuleStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateNotificationConfigurationResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeregisterNotificationHubResponseTypeDef(TypedDict):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class NotificationHubOverviewTypeDef(TypedDict):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummaryTypeDef
    creationTime: datetime
    lastActivationTime: NotRequired[datetime]


class RegisterNotificationHubResponseTypeDef(TypedDict):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummaryTypeDef
    creationTime: datetime
    lastActivationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class MessageComponentsTypeDef(TypedDict):
    headline: NotRequired[str]
    paragraphSummary: NotRequired[str]
    completeDescription: NotRequired[str]
    dimensions: NotRequired[list[DimensionTypeDef]]


class ListChannelsRequestPaginateTypeDef(TypedDict):
    notificationConfigurationArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListEventRulesRequestPaginateTypeDef(TypedDict):
    notificationConfigurationArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListNotificationConfigurationsRequestPaginateTypeDef(TypedDict):
    eventRuleSource: NotRequired[str]
    channelArn: NotRequired[str]
    status: NotRequired[NotificationConfigurationStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListNotificationHubsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListNotificationConfigurationsResponseTypeDef(TypedDict):
    notificationConfigurations: list[NotificationConfigurationStructureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]


class ListNotificationEventsRequestPaginateTypeDef(TypedDict):
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]
    locale: NotRequired[LocaleCodeType]
    source: NotRequired[str]
    includeChildEvents: NotRequired[bool]
    aggregateNotificationEventArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListNotificationEventsRequestRequestTypeDef(TypedDict):
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]
    locale: NotRequired[LocaleCodeType]
    source: NotRequired[str]
    includeChildEvents: NotRequired[bool]
    aggregateNotificationEventArn: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]


class NotificationEventSummaryTypeDef(TypedDict):
    schemaVersion: Literal["v1.0"]
    sourceEventMetadata: SourceEventMetadataSummaryTypeDef
    messageComponents: MessageComponentsSummaryTypeDef
    eventStatus: EventStatusType
    notificationType: NotificationTypeType


class SourceEventMetadataTypeDef(TypedDict):
    eventTypeVersion: str
    sourceEventId: str
    relatedAccount: str
    source: str
    eventOccurrenceTime: datetime
    eventType: str
    relatedResources: list[ResourceTypeDef]
    eventOriginRegion: NotRequired[str]


class ListEventRulesResponseTypeDef(TypedDict):
    eventRules: list[EventRuleStructureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]


class ListNotificationHubsResponseTypeDef(TypedDict):
    notificationHubs: list[NotificationHubOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]


class NotificationEventOverviewTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    relatedAccount: str
    creationTime: datetime
    notificationEvent: NotificationEventSummaryTypeDef
    aggregationEventType: NotRequired[AggregationEventTypeType]
    aggregateNotificationEventArn: NotRequired[str]


NotificationEventTypeDef = TypedDict(
    "NotificationEventTypeDef",
    {
        "schemaVersion": Literal["v1.0"],
        "id": str,
        "sourceEventMetadata": SourceEventMetadataTypeDef,
        "messageComponents": MessageComponentsTypeDef,
        "notificationType": NotificationTypeType,
        "textParts": dict[str, TextPartValueTypeDef],
        "media": list[MediaElementTypeDef],
        "sourceEventDetailUrl": NotRequired[str],
        "sourceEventDetailUrlDisplayText": NotRequired[str],
        "eventStatus": NotRequired[EventStatusType],
        "aggregationEventType": NotRequired[AggregationEventTypeType],
        "aggregateNotificationEventArn": NotRequired[str],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)


class ListNotificationEventsResponseTypeDef(TypedDict):
    notificationEvents: list[NotificationEventOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]


class GetNotificationEventResponseTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    content: NotificationEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
