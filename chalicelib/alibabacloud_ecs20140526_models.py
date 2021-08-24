# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
print('6.0')
from Tea.model import TeaModel
print('6.1')
from typing import Dict, List, Any
print('6.2')

class AcceptInquiredSystemEventRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        event_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.event_id is not None:
            result['EventId'] = self.event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        return self


class AcceptInquiredSystemEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AcceptInquiredSystemEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AcceptInquiredSystemEventResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AcceptInquiredSystemEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ActivateRouterInterfaceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        router_interface_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.router_interface_id = router_interface_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')
        return self


class ActivateRouterInterfaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ActivateRouterInterfaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ActivateRouterInterfaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ActivateRouterInterfaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddBandwidthPackageIpsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        bandwidth_package_id: str = None,
        ip_count: str = None,
        client_token: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.ip_count = ip_count
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.ip_count is not None:
            result['IpCount'] = self.ip_count
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddBandwidthPackageIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddBandwidthPackageIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddBandwidthPackageIpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddBandwidthPackageIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTagsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddTagsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        resource_type: str = None,
        resource_id: str = None,
        tag: List[AddTagsRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = AddTagsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class AddTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



class DescribeSpotPriceHistoryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        zone_id: str = None,
        network_type: str = None,
        instance_type: str = None,
        spot_duration: int = None,
        io_optimized: str = None,
        start_time: str = None,
        end_time: str = None,
        ostype: str = None,
        offset: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.zone_id = zone_id
        self.network_type = network_type
        self.instance_type = instance_type
        self.spot_duration = spot_duration
        self.io_optimized = io_optimized
        self.start_time = start_time
        self.end_time = end_time
        self.ostype = ostype
        self.offset = offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.offset is not None:
            result['Offset'] = self.offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        return self


class DescribeSpotPriceHistoryResponseBodySpotPricesSpotPriceType(TeaModel):
    def __init__(
        self,
        io_optimized: str = None,
        zone_id: str = None,
        spot_price: float = None,
        timestamp: str = None,
        network_type: str = None,
        instance_type: str = None,
        origin_price: float = None,
    ):
        self.io_optimized = io_optimized
        self.zone_id = zone_id
        self.spot_price = spot_price
        self.timestamp = timestamp
        self.network_type = network_type
        self.instance_type = instance_type
        self.origin_price = origin_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.spot_price is not None:
            result['SpotPrice'] = self.spot_price
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('SpotPrice') is not None:
            self.spot_price = m.get('SpotPrice')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        return self


class DescribeSpotPriceHistoryResponseBodySpotPrices(TeaModel):
    def __init__(
        self,
        spot_price_type: List[DescribeSpotPriceHistoryResponseBodySpotPricesSpotPriceType] = None,
    ):
        self.spot_price_type = spot_price_type

    def validate(self):
        if self.spot_price_type:
            for k in self.spot_price_type:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SpotPriceType'] = []
        if self.spot_price_type is not None:
            for k in self.spot_price_type:
                result['SpotPriceType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.spot_price_type = []
        if m.get('SpotPriceType') is not None:
            for k in m.get('SpotPriceType'):
                temp_model = DescribeSpotPriceHistoryResponseBodySpotPricesSpotPriceType()
                self.spot_price_type.append(temp_model.from_map(k))
        return self


class DescribeSpotPriceHistoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        currency: str = None,
        next_offset: int = None,
        spot_prices: DescribeSpotPriceHistoryResponseBodySpotPrices = None,
    ):
        self.request_id = request_id
        self.currency = currency
        self.next_offset = next_offset
        self.spot_prices = spot_prices

    def validate(self):
        if self.spot_prices:
            self.spot_prices.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.next_offset is not None:
            result['NextOffset'] = self.next_offset
        if self.spot_prices is not None:
            result['SpotPrices'] = self.spot_prices.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('NextOffset') is not None:
            self.next_offset = m.get('NextOffset')
        if m.get('SpotPrices') is not None:
            temp_model = DescribeSpotPriceHistoryResponseBodySpotPrices()
            self.spot_prices = temp_model.from_map(m['SpotPrices'])
        return self


class DescribeSpotPriceHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSpotPriceHistoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSpotPriceHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStorageCapacityUnitsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        name: str = None,
        capacity: int = None,
        allocation_type: str = None,
        storage_capacity_unit_id: List[str] = None,
        status: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.name = name
        self.capacity = capacity
        self.allocation_type = allocation_type
        self.storage_capacity_unit_id = storage_capacity_unit_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.allocation_type is not None:
            result['AllocationType'] = self.allocation_type
        if self.storage_capacity_unit_id is not None:
            result['StorageCapacityUnitId'] = self.storage_capacity_unit_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('AllocationType') is not None:
            self.allocation_type = m.get('AllocationType')
        if m.get('StorageCapacityUnitId') is not None:
            self.storage_capacity_unit_id = m.get('StorageCapacityUnitId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnit(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        status: str = None,
        start_time: str = None,
        capacity: int = None,
        description: str = None,
        allocation_status: str = None,
        expired_time: str = None,
        storage_capacity_unit_id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.creation_time = creation_time
        self.status = status
        self.start_time = start_time
        self.capacity = capacity
        self.description = description
        self.allocation_status = allocation_status
        self.expired_time = expired_time
        self.storage_capacity_unit_id = storage_capacity_unit_id
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.description is not None:
            result['Description'] = self.description
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.storage_capacity_unit_id is not None:
            result['StorageCapacityUnitId'] = self.storage_capacity_unit_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('StorageCapacityUnitId') is not None:
            self.storage_capacity_unit_id = m.get('StorageCapacityUnitId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnits(TeaModel):
    def __init__(
        self,
        storage_capacity_unit: List[DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnit] = None,
    ):
        self.storage_capacity_unit = storage_capacity_unit

    def validate(self):
        if self.storage_capacity_unit:
            for k in self.storage_capacity_unit:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['StorageCapacityUnit'] = []
        if self.storage_capacity_unit is not None:
            for k in self.storage_capacity_unit:
                result['StorageCapacityUnit'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.storage_capacity_unit = []
        if m.get('StorageCapacityUnit') is not None:
            for k in m.get('StorageCapacityUnit'):
                temp_model = DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnitsStorageCapacityUnit()
                self.storage_capacity_unit.append(temp_model.from_map(k))
        return self


class DescribeStorageCapacityUnitsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        storage_capacity_units: DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnits = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.storage_capacity_units = storage_capacity_units

    def validate(self):
        if self.storage_capacity_units:
            self.storage_capacity_units.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.storage_capacity_units is not None:
            result['StorageCapacityUnits'] = self.storage_capacity_units.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('StorageCapacityUnits') is not None:
            temp_model = DescribeStorageCapacityUnitsResponseBodyStorageCapacityUnits()
            self.storage_capacity_units = temp_model.from_map(m['StorageCapacityUnits'])
        return self


class DescribeStorageCapacityUnitsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStorageCapacityUnitsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeStorageCapacityUnitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStorageSetDetailsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        client_token: str = None,
        region_id: str = None,
        storage_set_id: str = None,
        storage_set_partition_number: int = None,
        disk_ids: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.client_token = client_token
        self.region_id = region_id
        self.storage_set_id = storage_set_id
        self.storage_set_partition_number = storage_set_partition_number
        self.disk_ids = disk_ids
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id
        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')
        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeStorageSetDetailsResponseBodyDisksDisk(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        disk_name: str = None,
        zone_id: str = None,
        storage_set_id: str = None,
        disk_id: str = None,
        category: str = None,
        storage_set_partition_number: int = None,
        region_id: str = None,
    ):
        self.creation_time = creation_time
        self.disk_name = disk_name
        self.zone_id = zone_id
        self.storage_set_id = storage_set_id
        self.disk_id = disk_id
        self.category = category
        self.storage_set_partition_number = storage_set_partition_number
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.category is not None:
            result['Category'] = self.category
        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeStorageSetDetailsResponseBodyDisks(TeaModel):
    def __init__(
        self,
        disk: List[DescribeStorageSetDetailsResponseBodyDisksDisk] = None,
    ):
        self.disk = disk

    def validate(self):
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk = []
        if m.get('Disk') is not None:
            for k in m.get('Disk'):
                temp_model = DescribeStorageSetDetailsResponseBodyDisksDisk()
                self.disk.append(temp_model.from_map(k))
        return self


class DescribeStorageSetDetailsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        disks: DescribeStorageSetDetailsResponseBodyDisks = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.disks = disks

    def validate(self):
        if self.disks:
            self.disks.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.disks is not None:
            result['Disks'] = self.disks.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Disks') is not None:
            temp_model = DescribeStorageSetDetailsResponseBodyDisks()
            self.disks = temp_model.from_map(m['Disks'])
        return self


class DescribeStorageSetDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStorageSetDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeStorageSetDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStorageSetsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        client_token: str = None,
        region_id: str = None,
        storage_set_ids: str = None,
        zone_id: str = None,
        storage_set_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.client_token = client_token
        self.region_id = region_id
        self.storage_set_ids = storage_set_ids
        self.zone_id = zone_id
        self.storage_set_name = storage_set_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_set_ids is not None:
            result['StorageSetIds'] = self.storage_set_ids
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.storage_set_name is not None:
            result['StorageSetName'] = self.storage_set_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageSetIds') is not None:
            self.storage_set_ids = m.get('StorageSetIds')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('StorageSetName') is not None:
            self.storage_set_name = m.get('StorageSetName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeStorageSetsResponseBodyStorageSetsStorageSet(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        zone_id: str = None,
        storage_set_id: str = None,
        storage_set_partition_number: int = None,
        storage_set_name: str = None,
        region_id: str = None,
    ):
        self.creation_time = creation_time
        self.description = description
        self.zone_id = zone_id
        self.storage_set_id = storage_set_id
        self.storage_set_partition_number = storage_set_partition_number
        self.storage_set_name = storage_set_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id
        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number
        if self.storage_set_name is not None:
            result['StorageSetName'] = self.storage_set_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')
        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')
        if m.get('StorageSetName') is not None:
            self.storage_set_name = m.get('StorageSetName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeStorageSetsResponseBodyStorageSets(TeaModel):
    def __init__(
        self,
        storage_set: List[DescribeStorageSetsResponseBodyStorageSetsStorageSet] = None,
    ):
        self.storage_set = storage_set

    def validate(self):
        if self.storage_set:
            for k in self.storage_set:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['StorageSet'] = []
        if self.storage_set is not None:
            for k in self.storage_set:
                result['StorageSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.storage_set = []
        if m.get('StorageSet') is not None:
            for k in m.get('StorageSet'):
                temp_model = DescribeStorageSetsResponseBodyStorageSetsStorageSet()
                self.storage_set.append(temp_model.from_map(k))
        return self


class DescribeStorageSetsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        storage_sets: DescribeStorageSetsResponseBodyStorageSets = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.storage_sets = storage_sets

    def validate(self):
        if self.storage_sets:
            self.storage_sets.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.storage_sets is not None:
            result['StorageSets'] = self.storage_sets.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('StorageSets') is not None:
            temp_model = DescribeStorageSetsResponseBodyStorageSets()
            self.storage_sets = temp_model.from_map(m['StorageSets'])
        return self


class DescribeStorageSetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStorageSetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeStorageSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeTagsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_size: int = None,
        page_number: int = None,
        resource_type: str = None,
        resource_id: str = None,
        region_id: str = None,
        category: str = None,
        tag: List[DescribeTagsRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_size = page_size
        self.page_number = page_number
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.region_id = region_id
        self.category = category
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.category is not None:
            result['Category'] = self.category
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeTagsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeTagsResponseBodyTagsTagResourceTypeCount(TeaModel):
    def __init__(
        self,
        instance: int = None,
        image: int = None,
        snapshot_policy: int = None,
        ddh: int = None,
        securitygroup: int = None,
        snapshot: int = None,
        reserved_instance: int = None,
        eni: int = None,
        launch_template: int = None,
        key_pair: int = None,
        disk: int = None,
        volume: int = None,
    ):
        self.instance = instance
        self.image = image
        self.snapshot_policy = snapshot_policy
        self.ddh = ddh
        self.securitygroup = securitygroup
        self.snapshot = snapshot
        self.reserved_instance = reserved_instance
        self.eni = eni
        self.launch_template = launch_template
        self.key_pair = key_pair
        self.disk = disk
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance is not None:
            result['Instance'] = self.instance
        if self.image is not None:
            result['Image'] = self.image
        if self.snapshot_policy is not None:
            result['SnapshotPolicy'] = self.snapshot_policy
        if self.ddh is not None:
            result['Ddh'] = self.ddh
        if self.securitygroup is not None:
            result['Securitygroup'] = self.securitygroup
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        if self.reserved_instance is not None:
            result['ReservedInstance'] = self.reserved_instance
        if self.eni is not None:
            result['Eni'] = self.eni
        if self.launch_template is not None:
            result['LaunchTemplate'] = self.launch_template
        if self.key_pair is not None:
            result['KeyPair'] = self.key_pair
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            self.instance = m.get('Instance')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('SnapshotPolicy') is not None:
            self.snapshot_policy = m.get('SnapshotPolicy')
        if m.get('Ddh') is not None:
            self.ddh = m.get('Ddh')
        if m.get('Securitygroup') is not None:
            self.securitygroup = m.get('Securitygroup')
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        if m.get('ReservedInstance') is not None:
            self.reserved_instance = m.get('ReservedInstance')
        if m.get('Eni') is not None:
            self.eni = m.get('Eni')
        if m.get('LaunchTemplate') is not None:
            self.launch_template = m.get('LaunchTemplate')
        if m.get('KeyPair') is not None:
            self.key_pair = m.get('KeyPair')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class DescribeTagsResponseBodyTagsTag(TeaModel):
    def __init__(
        self,
        resource_type_count: DescribeTagsResponseBodyTagsTagResourceTypeCount = None,
        tag_value: str = None,
        tag_key: str = None,
    ):
        self.resource_type_count = resource_type_count
        self.tag_value = tag_value
        self.tag_key = tag_key

    def validate(self):
        if self.resource_type_count:
            self.resource_type_count.validate()

    def to_map(self):
        result = dict()
        if self.resource_type_count is not None:
            result['ResourceTypeCount'] = self.resource_type_count.to_map()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypeCount') is not None:
            temp_model = DescribeTagsResponseBodyTagsTagResourceTypeCount()
            self.resource_type_count = temp_model.from_map(m['ResourceTypeCount'])
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeTagsResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeTagsResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeTagsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        tags: DescribeTagsResponseBodyTags = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Tags') is not None:
            temp_model = DescribeTagsResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        task_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSet(TeaModel):
    def __init__(
        self,
        related_item: List[DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem] = None,
    ):
        self.related_item = related_item

    def validate(self):
        if self.related_item:
            for k in self.related_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RelatedItem'] = []
        if self.related_item is not None:
            for k in self.related_item:
                result['RelatedItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.related_item = []
        if m.get('RelatedItem') is not None:
            for k in m.get('RelatedItem'):
                temp_model = DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem()
                self.related_item.append(temp_model.from_map(k))
        return self


class DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgress(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        related_item_set: DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSet = None,
        operation_status: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.related_item_set = related_item_set
        self.operation_status = operation_status

    def validate(self):
        if self.related_item_set:
            self.related_item_set.validate()

    def to_map(self):
        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.related_item_set is not None:
            result['RelatedItemSet'] = self.related_item_set.to_map()
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RelatedItemSet') is not None:
            temp_model = DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSet()
            self.related_item_set = temp_model.from_map(m['RelatedItemSet'])
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        return self


class DescribeTaskAttributeResponseBodyOperationProgressSet(TeaModel):
    def __init__(
        self,
        operation_progress: List[DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgress] = None,
    ):
        self.operation_progress = operation_progress

    def validate(self):
        if self.operation_progress:
            for k in self.operation_progress:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['OperationProgress'] = []
        if self.operation_progress is not None:
            for k in self.operation_progress:
                result['OperationProgress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation_progress = []
        if m.get('OperationProgress') is not None:
            for k in m.get('OperationProgress'):
                temp_model = DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgress()
                self.operation_progress.append(temp_model.from_map(k))
        return self


class DescribeTaskAttributeResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
        task_action: str = None,
        success_count: int = None,
        task_status: str = None,
        finished_time: str = None,
        total_count: int = None,
        task_process: str = None,
        support_cancel: str = None,
        operation_progress_set: DescribeTaskAttributeResponseBodyOperationProgressSet = None,
        creation_time: str = None,
        failed_count: int = None,
        region_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.task_action = task_action
        self.success_count = success_count
        self.task_status = task_status
        self.finished_time = finished_time
        self.total_count = total_count
        self.task_process = task_process
        self.support_cancel = support_cancel
        self.operation_progress_set = operation_progress_set
        self.creation_time = creation_time
        self.failed_count = failed_count
        self.region_id = region_id

    def validate(self):
        if self.operation_progress_set:
            self.operation_progress_set.validate()

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.task_process is not None:
            result['TaskProcess'] = self.task_process
        if self.support_cancel is not None:
            result['SupportCancel'] = self.support_cancel
        if self.operation_progress_set is not None:
            result['OperationProgressSet'] = self.operation_progress_set.to_map()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TaskProcess') is not None:
            self.task_process = m.get('TaskProcess')
        if m.get('SupportCancel') is not None:
            self.support_cancel = m.get('SupportCancel')
        if m.get('OperationProgressSet') is not None:
            temp_model = DescribeTaskAttributeResponseBodyOperationProgressSet()
            self.operation_progress_set = temp_model.from_map(m['OperationProgressSet'])
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeTaskAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTaskAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTaskAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        owner_account: str = None,
        region_id: str = None,
        task_ids: str = None,
        task_action: str = None,
        task_status: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.owner_account = owner_account
        self.region_id = region_id
        self.task_ids = task_ids
        self.task_action = task_action
        self.task_status = task_status
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeTasksResponseBodyTaskSetTask(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        task_status: str = None,
        finished_time: str = None,
        support_cancel: str = None,
        task_id: str = None,
        task_action: str = None,
    ):
        self.creation_time = creation_time
        self.task_status = task_status
        self.finished_time = finished_time
        self.support_cancel = support_cancel
        self.task_id = task_id
        self.task_action = task_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.support_cancel is not None:
            result['SupportCancel'] = self.support_cancel
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('SupportCancel') is not None:
            self.support_cancel = m.get('SupportCancel')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        return self


class DescribeTasksResponseBodyTaskSet(TeaModel):
    def __init__(
        self,
        task: List[DescribeTasksResponseBodyTaskSetTask] = None,
    ):
        self.task = task

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = DescribeTasksResponseBodyTaskSetTask()
                self.task.append(temp_model.from_map(k))
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        task_set: DescribeTasksResponseBodyTaskSet = None,
        region_id: str = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.task_set = task_set
        self.region_id = region_id

    def validate(self):
        if self.task_set:
            self.task_set.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.task_set is not None:
            result['TaskSet'] = self.task_set.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TaskSet') is not None:
            temp_model = DescribeTasksResponseBodyTaskSet()
            self.task_set = temp_model.from_map(m['TaskSet'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserBusinessBehaviorRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        status_key: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.status_key = status_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status_key is not None:
            result['statusKey'] = self.status_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('statusKey') is not None:
            self.status_key = m.get('statusKey')
        return self


class DescribeUserBusinessBehaviorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status_value: str = None,
    ):
        self.request_id = request_id
        self.status_value = status_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status_value is not None:
            result['StatusValue'] = self.status_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatusValue') is not None:
            self.status_value = m.get('StatusValue')
        return self


class DescribeUserBusinessBehaviorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserBusinessBehaviorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserBusinessBehaviorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeUserDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
        user_data: str = None,
        region_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id
        self.user_data = user_data
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeUserDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVirtualBorderRoutersRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeVirtualBorderRoutersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        filter: List[DescribeVirtualBorderRoutersRequestFilter] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.filter = filter

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeVirtualBorderRoutersRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterType(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        status: str = None,
        vlan_interface_id: str = None,
        circuit_code: str = None,
        physical_connection_owner_uid: str = None,
        local_gateway_ip: str = None,
        activation_time: str = None,
        physical_connection_business_status: str = None,
        peering_subnet_mask: str = None,
        route_table_id: str = None,
        description: str = None,
        physical_connection_status: str = None,
        recovery_time: str = None,
        termination_time: str = None,
        peer_gateway_ip: str = None,
        name: str = None,
        access_point_id: str = None,
        vbr_id: str = None,
        physical_connection_id: str = None,
        vlan_id: int = None,
    ):
        self.creation_time = creation_time
        self.status = status
        self.vlan_interface_id = vlan_interface_id
        self.circuit_code = circuit_code
        self.physical_connection_owner_uid = physical_connection_owner_uid
        self.local_gateway_ip = local_gateway_ip
        self.activation_time = activation_time
        self.physical_connection_business_status = physical_connection_business_status
        self.peering_subnet_mask = peering_subnet_mask
        self.route_table_id = route_table_id
        self.description = description
        self.physical_connection_status = physical_connection_status
        self.recovery_time = recovery_time
        self.termination_time = termination_time
        self.peer_gateway_ip = peer_gateway_ip
        self.name = name
        self.access_point_id = access_point_id
        self.vbr_id = vbr_id
        self.physical_connection_id = physical_connection_id
        self.vlan_id = vlan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.vlan_interface_id is not None:
            result['VlanInterfaceId'] = self.vlan_interface_id
        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code
        if self.physical_connection_owner_uid is not None:
            result['PhysicalConnectionOwnerUid'] = self.physical_connection_owner_uid
        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip
        if self.activation_time is not None:
            result['ActivationTime'] = self.activation_time
        if self.physical_connection_business_status is not None:
            result['PhysicalConnectionBusinessStatus'] = self.physical_connection_business_status
        if self.peering_subnet_mask is not None:
            result['PeeringSubnetMask'] = self.peering_subnet_mask
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        if self.description is not None:
            result['Description'] = self.description
        if self.physical_connection_status is not None:
            result['PhysicalConnectionStatus'] = self.physical_connection_status
        if self.recovery_time is not None:
            result['RecoveryTime'] = self.recovery_time
        if self.termination_time is not None:
            result['TerminationTime'] = self.termination_time
        if self.peer_gateway_ip is not None:
            result['PeerGatewayIp'] = self.peer_gateway_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id
        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id
        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id
        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VlanInterfaceId') is not None:
            self.vlan_interface_id = m.get('VlanInterfaceId')
        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')
        if m.get('PhysicalConnectionOwnerUid') is not None:
            self.physical_connection_owner_uid = m.get('PhysicalConnectionOwnerUid')
        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')
        if m.get('ActivationTime') is not None:
            self.activation_time = m.get('ActivationTime')
        if m.get('PhysicalConnectionBusinessStatus') is not None:
            self.physical_connection_business_status = m.get('PhysicalConnectionBusinessStatus')
        if m.get('PeeringSubnetMask') is not None:
            self.peering_subnet_mask = m.get('PeeringSubnetMask')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PhysicalConnectionStatus') is not None:
            self.physical_connection_status = m.get('PhysicalConnectionStatus')
        if m.get('RecoveryTime') is not None:
            self.recovery_time = m.get('RecoveryTime')
        if m.get('TerminationTime') is not None:
            self.termination_time = m.get('TerminationTime')
        if m.get('PeerGatewayIp') is not None:
            self.peer_gateway_ip = m.get('PeerGatewayIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')
        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')
        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')
        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')
        return self


class DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSet(TeaModel):
    def __init__(
        self,
        virtual_border_router_type: List[DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterType] = None,
    ):
        self.virtual_border_router_type = virtual_border_router_type

    def validate(self):
        if self.virtual_border_router_type:
            for k in self.virtual_border_router_type:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VirtualBorderRouterType'] = []
        if self.virtual_border_router_type is not None:
            for k in self.virtual_border_router_type:
                result['VirtualBorderRouterType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.virtual_border_router_type = []
        if m.get('VirtualBorderRouterType') is not None:
            for k in m.get('VirtualBorderRouterType'):
                temp_model = DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterType()
                self.virtual_border_router_type.append(temp_model.from_map(k))
        return self


class DescribeVirtualBorderRoutersResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        virtual_border_router_set: DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSet = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.virtual_border_router_set = virtual_border_router_set

    def validate(self):
        if self.virtual_border_router_set:
            self.virtual_border_router_set.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.virtual_border_router_set is not None:
            result['VirtualBorderRouterSet'] = self.virtual_border_router_set.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('VirtualBorderRouterSet') is not None:
            temp_model = DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSet()
            self.virtual_border_router_set = temp_model.from_map(m['VirtualBorderRouterSet'])
        return self


class DescribeVirtualBorderRoutersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVirtualBorderRoutersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVirtualBorderRoutersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVirtualBorderRoutersForPhysicalConnectionRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeVirtualBorderRoutersForPhysicalConnectionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        physical_connection_id: str = None,
        page_number: int = None,
        page_size: int = None,
        filter: List[DescribeVirtualBorderRoutersForPhysicalConnectionRequestFilter] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.physical_connection_id = physical_connection_id
        self.page_number = page_number
        self.page_size = page_size
        self.filter = filter

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeVirtualBorderRoutersForPhysicalConnectionRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSetVirtualBorderRouterForPhysicalConnectionType(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        circuit_code: str = None,
        recovery_time: str = None,
        termination_time: str = None,
        activation_time: str = None,
        vbr_owner_uid: int = None,
        vbr_id: str = None,
        vlan_id: int = None,
    ):
        self.creation_time = creation_time
        self.circuit_code = circuit_code
        self.recovery_time = recovery_time
        self.termination_time = termination_time
        self.activation_time = activation_time
        self.vbr_owner_uid = vbr_owner_uid
        self.vbr_id = vbr_id
        self.vlan_id = vlan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code
        if self.recovery_time is not None:
            result['RecoveryTime'] = self.recovery_time
        if self.termination_time is not None:
            result['TerminationTime'] = self.termination_time
        if self.activation_time is not None:
            result['ActivationTime'] = self.activation_time
        if self.vbr_owner_uid is not None:
            result['VbrOwnerUid'] = self.vbr_owner_uid
        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id
        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')
        if m.get('RecoveryTime') is not None:
            self.recovery_time = m.get('RecoveryTime')
        if m.get('TerminationTime') is not None:
            self.termination_time = m.get('TerminationTime')
        if m.get('ActivationTime') is not None:
            self.activation_time = m.get('ActivationTime')
        if m.get('VbrOwnerUid') is not None:
            self.vbr_owner_uid = m.get('VbrOwnerUid')
        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')
        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')
        return self


class DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSet(TeaModel):
    def __init__(
        self,
        virtual_border_router_for_physical_connection_type: List[DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSetVirtualBorderRouterForPhysicalConnectionType] = None,
    ):
        self.virtual_border_router_for_physical_connection_type = virtual_border_router_for_physical_connection_type

    def validate(self):
        if self.virtual_border_router_for_physical_connection_type:
            for k in self.virtual_border_router_for_physical_connection_type:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VirtualBorderRouterForPhysicalConnectionType'] = []
        if self.virtual_border_router_for_physical_connection_type is not None:
            for k in self.virtual_border_router_for_physical_connection_type:
                result['VirtualBorderRouterForPhysicalConnectionType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.virtual_border_router_for_physical_connection_type = []
        if m.get('VirtualBorderRouterForPhysicalConnectionType') is not None:
            for k in m.get('VirtualBorderRouterForPhysicalConnectionType'):
                temp_model = DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSetVirtualBorderRouterForPhysicalConnectionType()
                self.virtual_border_router_for_physical_connection_type.append(temp_model.from_map(k))
        return self


class DescribeVirtualBorderRoutersForPhysicalConnectionResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        virtual_border_router_for_physical_connection_set: DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSet = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.virtual_border_router_for_physical_connection_set = virtual_border_router_for_physical_connection_set

    def validate(self):
        if self.virtual_border_router_for_physical_connection_set:
            self.virtual_border_router_for_physical_connection_set.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.virtual_border_router_for_physical_connection_set is not None:
            result['VirtualBorderRouterForPhysicalConnectionSet'] = self.virtual_border_router_for_physical_connection_set.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('VirtualBorderRouterForPhysicalConnectionSet') is not None:
            temp_model = DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSet()
            self.virtual_border_router_for_physical_connection_set = temp_model.from_map(m['VirtualBorderRouterForPhysicalConnectionSet'])
        return self


class DescribeVirtualBorderRoutersForPhysicalConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVirtualBorderRoutersForPhysicalConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVirtualBorderRoutersForPhysicalConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vpc_id: str = None,
        region_id: str = None,
        is_default: bool = None,
        page_number: int = None,
        page_size: int = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.vpc_id = vpc_id
        self.region_id = region_id
        self.is_default = is_default
        self.page_number = page_number
        self.page_size = page_size
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DescribeVpcsResponseBodyVpcsVpcVSwitchIds(TeaModel):
    def __init__(
        self,
        v_switch_id: List[str] = None,
    ):
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeVpcsResponseBodyVpcsVpcUserCidrs(TeaModel):
    def __init__(
        self,
        user_cidr: List[str] = None,
    ):
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class DescribeVpcsResponseBodyVpcsVpc(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        vpc_name: str = None,
        status: str = None,
        vpc_id: str = None,
        vrouter_id: str = None,
        is_default: bool = None,
        cidr_block: str = None,
        description: str = None,
        v_switch_ids: DescribeVpcsResponseBodyVpcsVpcVSwitchIds = None,
        user_cidrs: DescribeVpcsResponseBodyVpcsVpcUserCidrs = None,
        region_id: str = None,
    ):
        self.creation_time = creation_time
        self.vpc_name = vpc_name
        self.status = status
        self.vpc_id = vpc_id
        self.vrouter_id = vrouter_id
        self.is_default = is_default
        self.cidr_block = cidr_block
        self.description = description
        self.v_switch_ids = v_switch_ids
        self.user_cidrs = user_cidrs
        self.region_id = region_id

    def validate(self):
        if self.v_switch_ids:
            self.v_switch_ids.validate()
        if self.user_cidrs:
            self.user_cidrs.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.description is not None:
            result['Description'] = self.description
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()
        if self.user_cidrs is not None:
            result['UserCidrs'] = self.user_cidrs.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('VSwitchIds') is not None:
            temp_model = DescribeVpcsResponseBodyVpcsVpcVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m['VSwitchIds'])
        if m.get('UserCidrs') is not None:
            temp_model = DescribeVpcsResponseBodyVpcsVpcUserCidrs()
            self.user_cidrs = temp_model.from_map(m['UserCidrs'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeVpcsResponseBodyVpcs(TeaModel):
    def __init__(
        self,
        vpc: List[DescribeVpcsResponseBodyVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = DescribeVpcsResponseBodyVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class DescribeVpcsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        vpcs: DescribeVpcsResponseBodyVpcs = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.vpcs = vpcs
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Vpcs') is not None:
            temp_model = DescribeVpcsResponseBodyVpcs()
            self.vpcs = temp_model.from_map(m['Vpcs'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeVpcsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVpcsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVRoutersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vrouter_id: str = None,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.vrouter_id = vrouter_id
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DescribeVRoutersResponseBodyVRoutersVRouterRouteTableIds(TeaModel):
    def __init__(
        self,
        route_table_id: List[str] = None,
    ):
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVRoutersResponseBodyVRoutersVRouter(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        creation_time: str = None,
        vrouter_id: str = None,
        description: str = None,
        vrouter_name: str = None,
        route_table_ids: DescribeVRoutersResponseBodyVRoutersVRouterRouteTableIds = None,
        region_id: str = None,
    ):
        self.vpc_id = vpc_id
        self.creation_time = creation_time
        self.vrouter_id = vrouter_id
        self.description = description
        self.vrouter_name = vrouter_name
        self.route_table_ids = route_table_ids
        self.region_id = region_id

    def validate(self):
        if self.route_table_ids:
            self.route_table_ids.validate()

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id
        if self.description is not None:
            result['Description'] = self.description
        if self.vrouter_name is not None:
            result['VRouterName'] = self.vrouter_name
        if self.route_table_ids is not None:
            result['RouteTableIds'] = self.route_table_ids.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('VRouterName') is not None:
            self.vrouter_name = m.get('VRouterName')
        if m.get('RouteTableIds') is not None:
            temp_model = DescribeVRoutersResponseBodyVRoutersVRouterRouteTableIds()
            self.route_table_ids = temp_model.from_map(m['RouteTableIds'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeVRoutersResponseBodyVRouters(TeaModel):
    def __init__(
        self,
        vrouter: List[DescribeVRoutersResponseBodyVRoutersVRouter] = None,
    ):
        self.vrouter = vrouter

    def validate(self):
        if self.vrouter:
            for k in self.vrouter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VRouter'] = []
        if self.vrouter is not None:
            for k in self.vrouter:
                result['VRouter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vrouter = []
        if m.get('VRouter') is not None:
            for k in m.get('VRouter'):
                temp_model = DescribeVRoutersResponseBodyVRoutersVRouter()
                self.vrouter.append(temp_model.from_map(k))
        return self


class DescribeVRoutersResponseBody(TeaModel):
    def __init__(
        self,
        vrouters: DescribeVRoutersResponseBodyVRouters = None,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.vrouters = vrouters
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.vrouters:
            self.vrouters.validate()

    def to_map(self):
        result = dict()
        if self.vrouters is not None:
            result['VRouters'] = self.vrouters.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VRouters') is not None:
            temp_model = DescribeVRoutersResponseBodyVRouters()
            self.vrouters = temp_model.from_map(m['VRouters'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeVRoutersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVRoutersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVRoutersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVSwitchesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        region_id: str = None,
        is_default: bool = None,
        page_number: int = None,
        page_size: int = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id
        self.region_id = region_id
        self.is_default = is_default
        self.page_number = page_number
        self.page_size = page_size
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DescribeVSwitchesResponseBodyVSwitchesVSwitch(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        status: str = None,
        vpc_id: str = None,
        is_default: bool = None,
        v_switch_id: str = None,
        cidr_block: str = None,
        description: str = None,
        available_ip_address_count: int = None,
        resource_group_id: str = None,
        zone_id: str = None,
        v_switch_name: str = None,
    ):
        self.creation_time = creation_time
        self.status = status
        self.vpc_id = vpc_id
        self.is_default = is_default
        self.v_switch_id = v_switch_id
        self.cidr_block = cidr_block
        self.description = description
        self.available_ip_address_count = available_ip_address_count
        self.resource_group_id = resource_group_id
        self.zone_id = zone_id
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.description is not None:
            result['Description'] = self.description
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeVSwitchesResponseBodyVSwitches(TeaModel):
    def __init__(
        self,
        v_switch: List[DescribeVSwitchesResponseBodyVSwitchesVSwitch] = None,
    ):
        self.v_switch = v_switch

    def validate(self):
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k in m.get('VSwitch'):
                temp_model = DescribeVSwitchesResponseBodyVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        return self


class DescribeVSwitchesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        v_switches: DescribeVSwitchesResponseBodyVSwitches = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.v_switches = v_switches

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('VSwitches') is not None:
            temp_model = DescribeVSwitchesResponseBodyVSwitches()
            self.v_switches = temp_model.from_map(m['VSwitches'])
        return self


class DescribeVSwitchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVSwitchesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        verbose: bool = None,
        instance_charge_type: str = None,
        spot_strategy: str = None,
        accept_language: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.verbose = verbose
        self.instance_charge_type = instance_charge_type
        self.spot_strategy = spot_strategy
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableResourceCreation(TeaModel):
    def __init__(
        self,
        resource_types: List[str] = None,
    ):
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class DescribeZonesResponseBodyZonesZoneDedicatedHostGenerations(TeaModel):
    def __init__(
        self,
        dedicated_host_generation: List[str] = None,
    ):
        self.dedicated_host_generation = dedicated_host_generation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dedicated_host_generation is not None:
            result['DedicatedHostGeneration'] = self.dedicated_host_generation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGeneration') is not None:
            self.dedicated_host_generation = m.get('DedicatedHostGeneration')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableInstanceTypes(TeaModel):
    def __init__(
        self,
        instance_types: List[str] = None,
    ):
        self.instance_types = instance_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableDiskCategories(TeaModel):
    def __init__(
        self,
        disk_categories: List[str] = None,
    ):
        self.disk_categories = disk_categories

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.disk_categories is not None:
            result['DiskCategories'] = self.disk_categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskCategories') is not None:
            self.disk_categories = m.get('DiskCategories')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableDedicatedHostTypes(TeaModel):
    def __init__(
        self,
        dedicated_host_type: List[str] = None,
    ):
        self.dedicated_host_type = dedicated_host_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dedicated_host_type is not None:
            result['DedicatedHostType'] = self.dedicated_host_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostType') is not None:
            self.dedicated_host_type = m.get('DedicatedHostType')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableVolumeCategories(TeaModel):
    def __init__(
        self,
        volume_categories: List[str] = None,
    ):
        self.volume_categories = volume_categories

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.volume_categories is not None:
            result['VolumeCategories'] = self.volume_categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VolumeCategories') is not None:
            self.volume_categories = m.get('VolumeCategories')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoSystemDiskCategories(TeaModel):
    def __init__(
        self,
        supported_system_disk_category: List[str] = None,
    ):
        self.supported_system_disk_category = supported_system_disk_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.supported_system_disk_category is not None:
            result['supportedSystemDiskCategory'] = self.supported_system_disk_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedSystemDiskCategory') is not None:
            self.supported_system_disk_category = m.get('supportedSystemDiskCategory')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceGenerations(TeaModel):
    def __init__(
        self,
        supported_instance_generation: List[str] = None,
    ):
        self.supported_instance_generation = supported_instance_generation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.supported_instance_generation is not None:
            result['supportedInstanceGeneration'] = self.supported_instance_generation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedInstanceGeneration') is not None:
            self.supported_instance_generation = m.get('supportedInstanceGeneration')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoDataDiskCategories(TeaModel):
    def __init__(
        self,
        supported_data_disk_category: List[str] = None,
    ):
        self.supported_data_disk_category = supported_data_disk_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.supported_data_disk_category is not None:
            result['supportedDataDiskCategory'] = self.supported_data_disk_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedDataDiskCategory') is not None:
            self.supported_data_disk_category = m.get('supportedDataDiskCategory')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypes(TeaModel):
    def __init__(
        self,
        supported_instance_type: List[str] = None,
    ):
        self.supported_instance_type = supported_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.supported_instance_type is not None:
            result['supportedInstanceType'] = self.supported_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedInstanceType') is not None:
            self.supported_instance_type = m.get('supportedInstanceType')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypeFamilies(TeaModel):
    def __init__(
        self,
        supported_instance_type_family: List[str] = None,
    ):
        self.supported_instance_type_family = supported_instance_type_family

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.supported_instance_type_family is not None:
            result['supportedInstanceTypeFamily'] = self.supported_instance_type_family
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedInstanceTypeFamily') is not None:
            self.supported_instance_type_family = m.get('supportedInstanceTypeFamily')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoNetworkTypes(TeaModel):
    def __init__(
        self,
        supported_network_category: List[str] = None,
    ):
        self.supported_network_category = supported_network_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.supported_network_category is not None:
            result['supportedNetworkCategory'] = self.supported_network_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportedNetworkCategory') is not None:
            self.supported_network_category = m.get('supportedNetworkCategory')
        return self


class DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfo(TeaModel):
    def __init__(
        self,
        io_optimized: bool = None,
        system_disk_categories: DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoSystemDiskCategories = None,
        instance_generations: DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceGenerations = None,
        data_disk_categories: DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoDataDiskCategories = None,
        instance_types: DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypes = None,
        instance_type_families: DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypeFamilies = None,
        network_types: DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoNetworkTypes = None,
    ):
        self.io_optimized = io_optimized
        self.system_disk_categories = system_disk_categories
        self.instance_generations = instance_generations
        self.data_disk_categories = data_disk_categories
        self.instance_types = instance_types
        self.instance_type_families = instance_type_families
        self.network_types = network_types

    def validate(self):
        if self.system_disk_categories:
            self.system_disk_categories.validate()
        if self.instance_generations:
            self.instance_generations.validate()
        if self.data_disk_categories:
            self.data_disk_categories.validate()
        if self.instance_types:
            self.instance_types.validate()
        if self.instance_type_families:
            self.instance_type_families.validate()
        if self.network_types:
            self.network_types.validate()

    def to_map(self):
        result = dict()
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.system_disk_categories is not None:
            result['SystemDiskCategories'] = self.system_disk_categories.to_map()
        if self.instance_generations is not None:
            result['InstanceGenerations'] = self.instance_generations.to_map()
        if self.data_disk_categories is not None:
            result['DataDiskCategories'] = self.data_disk_categories.to_map()
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        if self.instance_type_families is not None:
            result['InstanceTypeFamilies'] = self.instance_type_families.to_map()
        if self.network_types is not None:
            result['NetworkTypes'] = self.network_types.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('SystemDiskCategories') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoSystemDiskCategories()
            self.system_disk_categories = temp_model.from_map(m['SystemDiskCategories'])
        if m.get('InstanceGenerations') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceGenerations()
            self.instance_generations = temp_model.from_map(m['InstanceGenerations'])
        if m.get('DataDiskCategories') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoDataDiskCategories()
            self.data_disk_categories = temp_model.from_map(m['DataDiskCategories'])
        if m.get('InstanceTypes') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypes()
            self.instance_types = temp_model.from_map(m['InstanceTypes'])
        if m.get('InstanceTypeFamilies') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoInstanceTypeFamilies()
            self.instance_type_families = temp_model.from_map(m['InstanceTypeFamilies'])
        if m.get('NetworkTypes') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfoNetworkTypes()
            self.network_types = temp_model.from_map(m['NetworkTypes'])
        return self


class DescribeZonesResponseBodyZonesZoneAvailableResources(TeaModel):
    def __init__(
        self,
        resources_info: List[DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfo] = None,
    ):
        self.resources_info = resources_info

    def validate(self):
        if self.resources_info:
            for k in self.resources_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ResourcesInfo'] = []
        if self.resources_info is not None:
            for k in self.resources_info:
                result['ResourcesInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resources_info = []
        if m.get('ResourcesInfo') is not None:
            for k in m.get('ResourcesInfo'):
                temp_model = DescribeZonesResponseBodyZonesZoneAvailableResourcesResourcesInfo()
                self.resources_info.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        available_resource_creation: DescribeZonesResponseBodyZonesZoneAvailableResourceCreation = None,
        dedicated_host_generations: DescribeZonesResponseBodyZonesZoneDedicatedHostGenerations = None,
        local_name: str = None,
        available_instance_types: DescribeZonesResponseBodyZonesZoneAvailableInstanceTypes = None,
        zone_id: str = None,
        available_disk_categories: DescribeZonesResponseBodyZonesZoneAvailableDiskCategories = None,
        available_dedicated_host_types: DescribeZonesResponseBodyZonesZoneAvailableDedicatedHostTypes = None,
        available_volume_categories: DescribeZonesResponseBodyZonesZoneAvailableVolumeCategories = None,
        available_resources: DescribeZonesResponseBodyZonesZoneAvailableResources = None,
    ):
        self.available_resource_creation = available_resource_creation
        self.dedicated_host_generations = dedicated_host_generations
        self.local_name = local_name
        self.available_instance_types = available_instance_types
        self.zone_id = zone_id
        self.available_disk_categories = available_disk_categories
        self.available_dedicated_host_types = available_dedicated_host_types
        self.available_volume_categories = available_volume_categories
        self.available_resources = available_resources

    def validate(self):
        if self.available_resource_creation:
            self.available_resource_creation.validate()
        if self.dedicated_host_generations:
            self.dedicated_host_generations.validate()
        if self.available_instance_types:
            self.available_instance_types.validate()
        if self.available_disk_categories:
            self.available_disk_categories.validate()
        if self.available_dedicated_host_types:
            self.available_dedicated_host_types.validate()
        if self.available_volume_categories:
            self.available_volume_categories.validate()
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        result = dict()
        if self.available_resource_creation is not None:
            result['AvailableResourceCreation'] = self.available_resource_creation.to_map()
        if self.dedicated_host_generations is not None:
            result['DedicatedHostGenerations'] = self.dedicated_host_generations.to_map()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.available_instance_types is not None:
            result['AvailableInstanceTypes'] = self.available_instance_types.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.available_disk_categories is not None:
            result['AvailableDiskCategories'] = self.available_disk_categories.to_map()
        if self.available_dedicated_host_types is not None:
            result['AvailableDedicatedHostTypes'] = self.available_dedicated_host_types.to_map()
        if self.available_volume_categories is not None:
            result['AvailableVolumeCategories'] = self.available_volume_categories.to_map()
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableResourceCreation') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableResourceCreation()
            self.available_resource_creation = temp_model.from_map(m['AvailableResourceCreation'])
        if m.get('DedicatedHostGenerations') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneDedicatedHostGenerations()
            self.dedicated_host_generations = temp_model.from_map(m['DedicatedHostGenerations'])
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('AvailableInstanceTypes') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableInstanceTypes()
            self.available_instance_types = temp_model.from_map(m['AvailableInstanceTypes'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('AvailableDiskCategories') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableDiskCategories()
            self.available_disk_categories = temp_model.from_map(m['AvailableDiskCategories'])
        if m.get('AvailableDedicatedHostTypes') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableDedicatedHostTypes()
            self.available_dedicated_host_types = temp_model.from_map(m['AvailableDedicatedHostTypes'])
        if m.get('AvailableVolumeCategories') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableVolumeCategories()
            self.available_volume_categories = temp_model.from_map(m['AvailableVolumeCategories'])
        if m.get('AvailableResources') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneAvailableResources()
            self.available_resources = temp_model.from_map(m['AvailableResources'])
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: DescribeZonesResponseBodyZones = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeZonesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachClassicLinkVpcRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        instance_id: str = None,
        vpc_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.instance_id = instance_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DetachClassicLinkVpcResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachClassicLinkVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachClassicLinkVpcResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachClassicLinkVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachDiskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        disk_id: str = None,
        delete_with_instance: bool = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.disk_id = disk_id
        self.delete_with_instance = delete_with_instance
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DetachDiskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachDiskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachInstanceRamRoleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        ram_role_name: str = None,
        instance_ids: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.ram_role_name = ram_role_name
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSetsInstanceRamRoleSet(TeaModel):
    def __init__(
        self,
        ram_role_name: str = None,
        instance_id: str = None,
    ):
        self.ram_role_name = ram_role_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSets(TeaModel):
    def __init__(
        self,
        instance_ram_role_set: List[DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSetsInstanceRamRoleSet] = None,
    ):
        self.instance_ram_role_set = instance_ram_role_set

    def validate(self):
        if self.instance_ram_role_set:
            for k in self.instance_ram_role_set:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceRamRoleSet'] = []
        if self.instance_ram_role_set is not None:
            for k in self.instance_ram_role_set:
                result['InstanceRamRoleSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_ram_role_set = []
        if m.get('InstanceRamRoleSet') is not None:
            for k in m.get('InstanceRamRoleSet'):
                temp_model = DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSetsInstanceRamRoleSet()
                self.instance_ram_role_set.append(temp_model.from_map(k))
        return self


class DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResult(TeaModel):
    def __init__(
        self,
        instance_ram_role_sets: DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSets = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        instance_id: str = None,
    ):
        self.instance_ram_role_sets = instance_ram_role_sets
        self.success = success
        self.code = code
        self.message = message
        self.instance_id = instance_id

    def validate(self):
        if self.instance_ram_role_sets:
            self.instance_ram_role_sets.validate()

    def to_map(self):
        result = dict()
        if self.instance_ram_role_sets is not None:
            result['InstanceRamRoleSets'] = self.instance_ram_role_sets.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceRamRoleSets') is not None:
            temp_model = DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResultInstanceRamRoleSets()
            self.instance_ram_role_sets = temp_model.from_map(m['InstanceRamRoleSets'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResults(TeaModel):
    def __init__(
        self,
        detach_instance_ram_role_result: List[DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResult] = None,
    ):
        self.detach_instance_ram_role_result = detach_instance_ram_role_result

    def validate(self):
        if self.detach_instance_ram_role_result:
            for k in self.detach_instance_ram_role_result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DetachInstanceRamRoleResult'] = []
        if self.detach_instance_ram_role_result is not None:
            for k in self.detach_instance_ram_role_result:
                result['DetachInstanceRamRoleResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detach_instance_ram_role_result = []
        if m.get('DetachInstanceRamRoleResult') is not None:
            for k in m.get('DetachInstanceRamRoleResult'):
                temp_model = DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResultsDetachInstanceRamRoleResult()
                self.detach_instance_ram_role_result.append(temp_model.from_map(k))
        return self


class DetachInstanceRamRoleResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        ram_role_name: str = None,
        request_id: str = None,
        fail_count: int = None,
        detach_instance_ram_role_results: DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResults = None,
    ):
        self.total_count = total_count
        self.ram_role_name = ram_role_name
        self.request_id = request_id
        self.fail_count = fail_count
        self.detach_instance_ram_role_results = detach_instance_ram_role_results

    def validate(self):
        if self.detach_instance_ram_role_results:
            self.detach_instance_ram_role_results.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.detach_instance_ram_role_results is not None:
            result['DetachInstanceRamRoleResults'] = self.detach_instance_ram_role_results.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('DetachInstanceRamRoleResults') is not None:
            temp_model = DetachInstanceRamRoleResponseBodyDetachInstanceRamRoleResults()
            self.detach_instance_ram_role_results = temp_model.from_map(m['DetachInstanceRamRoleResults'])
        return self


class DetachInstanceRamRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachInstanceRamRoleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachInstanceRamRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachKeyPairRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        key_pair_name: str = None,
        instance_ids: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.key_pair_name = key_pair_name
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DetachKeyPairResponseBodyResultsResult(TeaModel):
    def __init__(
        self,
        success: str = None,
        code: str = None,
        message: str = None,
        instance_id: str = None,
    ):
        self.success = success
        self.code = code
        self.message = message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DetachKeyPairResponseBodyResults(TeaModel):
    def __init__(
        self,
        result: List[DetachKeyPairResponseBodyResultsResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DetachKeyPairResponseBodyResultsResult()
                self.result.append(temp_model.from_map(k))
        return self


class DetachKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
        total_count: str = None,
        request_id: str = None,
        results: DetachKeyPairResponseBodyResults = None,
        fail_count: str = None,
    ):
        self.key_pair_name = key_pair_name
        self.total_count = total_count
        self.request_id = request_id
        self.results = results
        self.fail_count = fail_count

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results.to_map()
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            temp_model = DetachKeyPairResponseBodyResults()
            self.results = temp_model.from_map(m['Results'])
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        return self


class DetachKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachKeyPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachNetworkInterfaceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        network_interface_id: str = None,
        instance_id: str = None,
        trunk_network_instance_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.network_interface_id = network_interface_id
        self.instance_id = instance_id
        self.trunk_network_instance_id = trunk_network_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.trunk_network_instance_id is not None:
            result['TrunkNetworkInstanceId'] = self.trunk_network_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TrunkNetworkInstanceId') is not None:
            self.trunk_network_instance_id = m.get('TrunkNetworkInstanceId')
        return self


class DetachNetworkInterfaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachNetworkInterfaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachNetworkInterfaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachNetworkInterfaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableActivationRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        activation_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.activation_id = activation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.activation_id is not None:
            result['ActivationId'] = self.activation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ActivationId') is not None:
            self.activation_id = m.get('ActivationId')
        return self


class DisableActivationResponseBodyActivation(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        deregistered_count: int = None,
        instance_count: int = None,
        description: str = None,
        registered_count: int = None,
        instance_name: str = None,
        disabled: bool = None,
        ip_address_range: str = None,
        time_to_live_in_hours: int = None,
        activation_id: str = None,
    ):
        self.creation_time = creation_time
        self.deregistered_count = deregistered_count
        self.instance_count = instance_count
        self.description = description
        self.registered_count = registered_count
        self.instance_name = instance_name
        self.disabled = disabled
        self.ip_address_range = ip_address_range
        self.time_to_live_in_hours = time_to_live_in_hours
        self.activation_id = activation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.deregistered_count is not None:
            result['DeregisteredCount'] = self.deregistered_count
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.description is not None:
            result['Description'] = self.description
        if self.registered_count is not None:
            result['RegisteredCount'] = self.registered_count
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.ip_address_range is not None:
            result['IpAddressRange'] = self.ip_address_range
        if self.time_to_live_in_hours is not None:
            result['TimeToLiveInHours'] = self.time_to_live_in_hours
        if self.activation_id is not None:
            result['ActivationId'] = self.activation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DeregisteredCount') is not None:
            self.deregistered_count = m.get('DeregisteredCount')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegisteredCount') is not None:
            self.registered_count = m.get('RegisteredCount')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('IpAddressRange') is not None:
            self.ip_address_range = m.get('IpAddressRange')
        if m.get('TimeToLiveInHours') is not None:
            self.time_to_live_in_hours = m.get('TimeToLiveInHours')
        if m.get('ActivationId') is not None:
            self.activation_id = m.get('ActivationId')
        return self


class DisableActivationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        activation: DisableActivationResponseBodyActivation = None,
    ):
        self.request_id = request_id
        self.activation = activation

    def validate(self):
        if self.activation:
            self.activation.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.activation is not None:
            result['Activation'] = self.activation.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Activation') is not None:
            temp_model = DisableActivationResponseBodyActivation()
            self.activation = temp_model.from_map(m['Activation'])
        return self


class DisableActivationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableActivationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableActivationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EipFillParamsRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        owner_account: str = None,
        user_cidr: str = None,
    ):
        self.data = data
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.owner_account = owner_account
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class EipFillParamsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        success: bool = None,
        request_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.success is not None:
            result['success'] = self.success
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class EipFillParamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EipFillParamsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EipFillParamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EipFillProductRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        owner_account: str = None,
        user_cidr: str = None,
    ):
        self.data = data
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.owner_account = owner_account
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class EipFillProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        success: bool = None,
        request_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.success is not None:
            result['success'] = self.success
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class EipFillProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EipFillProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EipFillProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EipNotifyPaidRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        owner_account: str = None,
        user_cidr: str = None,
    ):
        self.data = data
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.owner_account = owner_account
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class EipNotifyPaidResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        success: bool = None,
        request_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.success is not None:
            result['success'] = self.success
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class EipNotifyPaidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EipNotifyPaidResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EipNotifyPaidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnablePhysicalConnectionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        physical_connection_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        owner_account: str = None,
        user_cidr: str = None,
    ):
        self.region_id = region_id
        self.physical_connection_id = physical_connection_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.owner_account = owner_account
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class EnablePhysicalConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnablePhysicalConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnablePhysicalConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnablePhysicalConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportImageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        image_id: str = None,
        ossbucket: str = None,
        ossprefix: str = None,
        image_format: str = None,
        role_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.image_id = image_id
        self.ossbucket = ossbucket
        self.ossprefix = ossprefix
        self.image_format = image_format
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        if self.ossprefix is not None:
            result['OSSPrefix'] = self.ossprefix
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        if m.get('OSSPrefix') is not None:
            self.ossprefix = m.get('OSSPrefix')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ExportImageResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
        region_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ExportImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportSnapshotRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snapshot_id: str = None,
        region_id: str = None,
        oss_bucket: str = None,
        role_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.snapshot_id = snapshot_id
        self.region_id = region_id
        self.oss_bucket = oss_bucket
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ExportSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceConsoleOutputRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        instance_id: str = None,
        remove_symbols: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.instance_id = instance_id
        self.remove_symbols = remove_symbols

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remove_symbols is not None:
            result['RemoveSymbols'] = self.remove_symbols
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RemoveSymbols') is not None:
            self.remove_symbols = m.get('RemoveSymbols')
        return self


class GetInstanceConsoleOutputResponseBody(TeaModel):
    def __init__(
        self,
        console_output: str = None,
        request_id: str = None,
        last_update_time: str = None,
        instance_id: str = None,
    ):
        self.console_output = console_output
        self.request_id = request_id
        self.last_update_time = last_update_time
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.console_output is not None:
            result['ConsoleOutput'] = self.console_output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleOutput') is not None:
            self.console_output = m.get('ConsoleOutput')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInstanceConsoleOutputResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceConsoleOutputResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceConsoleOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceScreenshotRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        instance_id: str = None,
        wake_up: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.instance_id = instance_id
        self.wake_up = wake_up

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.wake_up is not None:
            result['WakeUp'] = self.wake_up
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('WakeUp') is not None:
            self.wake_up = m.get('WakeUp')
        return self


class GetInstanceScreenshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
        screenshot: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id
        self.screenshot = screenshot

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.screenshot is not None:
            result['Screenshot'] = self.screenshot
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Screenshot') is not None:
            self.screenshot = m.get('Screenshot')
        return self


class GetInstanceScreenshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceScreenshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceScreenshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportImageRequestDiskDeviceMapping(TeaModel):
    def __init__(
        self,
        disk_im_size: int = None,
        device: str = None,
        ossbucket: str = None,
        format: str = None,
        ossobject: str = None,
        disk_image_size: int = None,
    ):
        self.disk_im_size = disk_im_size
        self.device = device
        self.ossbucket = ossbucket
        self.format = format
        self.ossobject = ossobject
        self.disk_image_size = disk_image_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.disk_im_size is not None:
            result['DiskImSize'] = self.disk_im_size
        if self.device is not None:
            result['Device'] = self.device
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        if self.format is not None:
            result['Format'] = self.format
        if self.ossobject is not None:
            result['OSSObject'] = self.ossobject
        if self.disk_image_size is not None:
            result['DiskImageSize'] = self.disk_image_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskImSize') is not None:
            self.disk_im_size = m.get('DiskImSize')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('OSSObject') is not None:
            self.ossobject = m.get('OSSObject')
        if m.get('DiskImageSize') is not None:
            self.disk_image_size = m.get('DiskImageSize')
        return self


class ImportImageRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ImportImageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        image_name: str = None,
        description: str = None,
        architecture: str = None,
        ostype: str = None,
        platform: str = None,
        boot_mode: str = None,
        role_name: str = None,
        license_type: str = None,
        resource_group_id: str = None,
        disk_device_mapping: List[ImportImageRequestDiskDeviceMapping] = None,
        tag: List[ImportImageRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.image_name = image_name
        self.description = description
        self.architecture = architecture
        self.ostype = ostype
        self.platform = platform
        self.boot_mode = boot_mode
        self.role_name = role_name
        self.license_type = license_type
        self.resource_group_id = resource_group_id
        self.disk_device_mapping = disk_device_mapping
        self.tag = tag

    def validate(self):
        if self.disk_device_mapping:
            for k in self.disk_device_mapping:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.description is not None:
            result['Description'] = self.description
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.boot_mode is not None:
            result['BootMode'] = self.boot_mode
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.license_type is not None:
            result['LicenseType'] = self.license_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['DiskDeviceMapping'] = []
        if self.disk_device_mapping is not None:
            for k in self.disk_device_mapping:
                result['DiskDeviceMapping'].append(k.to_map() if k else None)
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('BootMode') is not None:
            self.boot_mode = m.get('BootMode')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.disk_device_mapping = []
        if m.get('DiskDeviceMapping') is not None:
            for k in m.get('DiskDeviceMapping'):
                temp_model = ImportImageRequestDiskDeviceMapping()
                self.disk_device_mapping.append(temp_model.from_map(k))
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ImportImageRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ImportImageResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
        image_id: str = None,
        region_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.image_id = image_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ImportImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportKeyPairRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ImportKeyPairRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        key_pair_name: str = None,
        public_key_body: str = None,
        resource_group_id: str = None,
        tag: List[ImportKeyPairRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.key_pair_name = key_pair_name
        self.public_key_body = public_key_body
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.public_key_body is not None:
            result['PublicKeyBody'] = self.public_key_body
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PublicKeyBody') is not None:
            self.public_key_body = m.get('PublicKeyBody')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ImportKeyPairRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ImportKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        key_pair_finger_print: str = None,
        key_pair_name: str = None,
        request_id: str = None,
    ):
        self.key_pair_finger_print = key_pair_finger_print
        self.key_pair_name = key_pair_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportKeyPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportSnapshotRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snapshot_name: str = None,
        region_id: str = None,
        oss_bucket: str = None,
        oss_object: str = None,
        role_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.snapshot_name = snapshot_name
        self.region_id = region_id
        self.oss_bucket = oss_bucket
        self.oss_object = oss_object
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_object is not None:
            result['OssObject'] = self.oss_object
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ImportSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        snapshot_id: str = None,
        task_id: str = None,
        request_id: str = None,
    ):
        self.snapshot_id = snapshot_id
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallCloudAssistantRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        instance_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class InstallCloudAssistantResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InstallCloudAssistantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InstallCloudAssistantResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InstallCloudAssistantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeCommandRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        command_id: str = None,
        timed: bool = None,
        frequency: str = None,
        parameters: Dict[str, Any] = None,
        username: str = None,
        windows_password_name: str = None,
        instance_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.command_id = command_id
        self.timed = timed
        self.frequency = frequency
        self.parameters = parameters
        self.username = username
        self.windows_password_name = windows_password_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.timed is not None:
            result['Timed'] = self.timed
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.username is not None:
            result['Username'] = self.username
        if self.windows_password_name is not None:
            result['WindowsPasswordName'] = self.windows_password_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('Timed') is not None:
            self.timed = m.get('Timed')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WindowsPasswordName') is not None:
            self.windows_password_name = m.get('WindowsPasswordName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class InvokeCommandShrinkRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        command_id: str = None,
        timed: bool = None,
        frequency: str = None,
        parameters_shrink: str = None,
        username: str = None,
        windows_password_name: str = None,
        instance_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.command_id = command_id
        self.timed = timed
        self.frequency = frequency
        self.parameters_shrink = parameters_shrink
        self.username = username
        self.windows_password_name = windows_password_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.timed is not None:
            result['Timed'] = self.timed
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.username is not None:
            result['Username'] = self.username
        if self.windows_password_name is not None:
            result['WindowsPasswordName'] = self.windows_password_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('Timed') is not None:
            self.timed = m.get('Timed')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WindowsPasswordName') is not None:
            self.windows_password_name = m.get('WindowsPasswordName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class InvokeCommandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        invoke_id: str = None,
    ):
        self.request_id = request_id
        self.invoke_id = invoke_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        return self


class InvokeCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InvokeCommandResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InvokeCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinResourceGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        resource_type: str = None,
        resource_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class JoinResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JoinResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = JoinResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        instance_id: str = None,
        network_interface_id: str = None,
        region_id: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_group_id = security_group_id
        self.instance_id = instance_id
        self.network_interface_id = network_interface_id
        self.region_id = region_id
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class JoinSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JoinSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = JoinSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LeaveSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        instance_id: str = None,
        network_interface_id: str = None,
        region_id: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_group_id = security_group_id
        self.instance_id = instance_id
        self.network_interface_id = network_interface_id
        self.region_id = region_id
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class LeaveSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LeaveSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LeaveSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LeaveSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequestTagFilter(TeaModel):
    def __init__(
        self,
        tag_values: List[str] = None,
        tag_key: str = None,
    ):
        self.tag_values = tag_values
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        next_token: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
        tag_filter: List[ListTagResourcesRequestTagFilter] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.next_token = next_token
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag
        self.tag_filter = tag_filter

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.tag_filter:
            for k in self.tag_filter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        result['TagFilter'] = []
        if self.tag_filter is not None:
            for k in self.tag_filter:
                result['TagFilter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        self.tag_filter = []
        if m.get('TagFilter') is not None:
            for k in m.get('TagFilter'):
                temp_model = ListTagResourcesRequestTagFilter()
                self.tag_filter.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoProvisioningGroupRequestLaunchTemplateConfig(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        max_price: float = None,
        priority: int = None,
        weighted_capacity: float = None,
        instance_type: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.max_price = max_price
        self.priority = priority
        self.weighted_capacity = weighted_capacity
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.max_price is not None:
            result['MaxPrice'] = self.max_price
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ModifyAutoProvisioningGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        auto_provisioning_group_id: str = None,
        excess_capacity_termination_policy: str = None,
        default_target_capacity_type: str = None,
        terminate_instances_with_expiration: bool = None,
        max_spot_price: float = None,
        total_target_capacity: str = None,
        pay_as_you_go_target_capacity: str = None,
        spot_target_capacity: str = None,
        auto_provisioning_group_name: str = None,
        launch_template_config: List[ModifyAutoProvisioningGroupRequestLaunchTemplateConfig] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.auto_provisioning_group_id = auto_provisioning_group_id
        self.excess_capacity_termination_policy = excess_capacity_termination_policy
        self.default_target_capacity_type = default_target_capacity_type
        self.terminate_instances_with_expiration = terminate_instances_with_expiration
        self.max_spot_price = max_spot_price
        self.total_target_capacity = total_target_capacity
        self.pay_as_you_go_target_capacity = pay_as_you_go_target_capacity
        self.spot_target_capacity = spot_target_capacity
        self.auto_provisioning_group_name = auto_provisioning_group_name
        self.launch_template_config = launch_template_config

    def validate(self):
        if self.launch_template_config:
            for k in self.launch_template_config:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.auto_provisioning_group_id is not None:
            result['AutoProvisioningGroupId'] = self.auto_provisioning_group_id
        if self.excess_capacity_termination_policy is not None:
            result['ExcessCapacityTerminationPolicy'] = self.excess_capacity_termination_policy
        if self.default_target_capacity_type is not None:
            result['DefaultTargetCapacityType'] = self.default_target_capacity_type
        if self.terminate_instances_with_expiration is not None:
            result['TerminateInstancesWithExpiration'] = self.terminate_instances_with_expiration
        if self.max_spot_price is not None:
            result['MaxSpotPrice'] = self.max_spot_price
        if self.total_target_capacity is not None:
            result['TotalTargetCapacity'] = self.total_target_capacity
        if self.pay_as_you_go_target_capacity is not None:
            result['PayAsYouGoTargetCapacity'] = self.pay_as_you_go_target_capacity
        if self.spot_target_capacity is not None:
            result['SpotTargetCapacity'] = self.spot_target_capacity
        if self.auto_provisioning_group_name is not None:
            result['AutoProvisioningGroupName'] = self.auto_provisioning_group_name
        result['LaunchTemplateConfig'] = []
        if self.launch_template_config is not None:
            for k in self.launch_template_config:
                result['LaunchTemplateConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AutoProvisioningGroupId') is not None:
            self.auto_provisioning_group_id = m.get('AutoProvisioningGroupId')
        if m.get('ExcessCapacityTerminationPolicy') is not None:
            self.excess_capacity_termination_policy = m.get('ExcessCapacityTerminationPolicy')
        if m.get('DefaultTargetCapacityType') is not None:
            self.default_target_capacity_type = m.get('DefaultTargetCapacityType')
        if m.get('TerminateInstancesWithExpiration') is not None:
            self.terminate_instances_with_expiration = m.get('TerminateInstancesWithExpiration')
        if m.get('MaxSpotPrice') is not None:
            self.max_spot_price = m.get('MaxSpotPrice')
        if m.get('TotalTargetCapacity') is not None:
            self.total_target_capacity = m.get('TotalTargetCapacity')
        if m.get('PayAsYouGoTargetCapacity') is not None:
            self.pay_as_you_go_target_capacity = m.get('PayAsYouGoTargetCapacity')
        if m.get('SpotTargetCapacity') is not None:
            self.spot_target_capacity = m.get('SpotTargetCapacity')
        if m.get('AutoProvisioningGroupName') is not None:
            self.auto_provisioning_group_name = m.get('AutoProvisioningGroupName')
        self.launch_template_config = []
        if m.get('LaunchTemplateConfig') is not None:
            for k in m.get('LaunchTemplateConfig'):
                temp_model = ModifyAutoProvisioningGroupRequestLaunchTemplateConfig()
                self.launch_template_config.append(temp_model.from_map(k))
        return self


class ModifyAutoProvisioningGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAutoProvisioningGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAutoProvisioningGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAutoProvisioningGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoSnapshotPolicyRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        system_disk_policy_enabled: bool = None,
        system_disk_policy_time_period: int = None,
        system_disk_policy_retention_days: int = None,
        system_disk_policy_retention_last_week: bool = None,
        data_disk_policy_enabled: bool = None,
        data_disk_policy_time_period: int = None,
        data_disk_policy_retention_days: int = None,
        data_disk_policy_retention_last_week: bool = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.system_disk_policy_enabled = system_disk_policy_enabled
        self.system_disk_policy_time_period = system_disk_policy_time_period
        self.system_disk_policy_retention_days = system_disk_policy_retention_days
        self.system_disk_policy_retention_last_week = system_disk_policy_retention_last_week
        self.data_disk_policy_enabled = data_disk_policy_enabled
        self.data_disk_policy_time_period = data_disk_policy_time_period
        self.data_disk_policy_retention_days = data_disk_policy_retention_days
        self.data_disk_policy_retention_last_week = data_disk_policy_retention_last_week
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.system_disk_policy_enabled is not None:
            result['SystemDiskPolicyEnabled'] = self.system_disk_policy_enabled
        if self.system_disk_policy_time_period is not None:
            result['SystemDiskPolicyTimePeriod'] = self.system_disk_policy_time_period
        if self.system_disk_policy_retention_days is not None:
            result['SystemDiskPolicyRetentionDays'] = self.system_disk_policy_retention_days
        if self.system_disk_policy_retention_last_week is not None:
            result['SystemDiskPolicyRetentionLastWeek'] = self.system_disk_policy_retention_last_week
        if self.data_disk_policy_enabled is not None:
            result['DataDiskPolicyEnabled'] = self.data_disk_policy_enabled
        if self.data_disk_policy_time_period is not None:
            result['DataDiskPolicyTimePeriod'] = self.data_disk_policy_time_period
        if self.data_disk_policy_retention_days is not None:
            result['DataDiskPolicyRetentionDays'] = self.data_disk_policy_retention_days
        if self.data_disk_policy_retention_last_week is not None:
            result['DataDiskPolicyRetentionLastWeek'] = self.data_disk_policy_retention_last_week
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SystemDiskPolicyEnabled') is not None:
            self.system_disk_policy_enabled = m.get('SystemDiskPolicyEnabled')
        if m.get('SystemDiskPolicyTimePeriod') is not None:
            self.system_disk_policy_time_period = m.get('SystemDiskPolicyTimePeriod')
        if m.get('SystemDiskPolicyRetentionDays') is not None:
            self.system_disk_policy_retention_days = m.get('SystemDiskPolicyRetentionDays')
        if m.get('SystemDiskPolicyRetentionLastWeek') is not None:
            self.system_disk_policy_retention_last_week = m.get('SystemDiskPolicyRetentionLastWeek')
        if m.get('DataDiskPolicyEnabled') is not None:
            self.data_disk_policy_enabled = m.get('DataDiskPolicyEnabled')
        if m.get('DataDiskPolicyTimePeriod') is not None:
            self.data_disk_policy_time_period = m.get('DataDiskPolicyTimePeriod')
        if m.get('DataDiskPolicyRetentionDays') is not None:
            self.data_disk_policy_retention_days = m.get('DataDiskPolicyRetentionDays')
        if m.get('DataDiskPolicyRetentionLastWeek') is not None:
            self.data_disk_policy_retention_last_week = m.get('DataDiskPolicyRetentionLastWeek')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAutoSnapshotPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAutoSnapshotPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoSnapshotPolicyExRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        auto_snapshot_policy_id: str = None,
        auto_snapshot_policy_name: str = None,
        time_points: str = None,
        repeat_weekdays: str = None,
        retention_days: int = None,
        enable_cross_region_copy: bool = None,
        target_copy_regions: str = None,
        copied_snapshots_retention_days: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        self.time_points = time_points
        self.repeat_weekdays = repeat_weekdays
        self.retention_days = retention_days
        self.enable_cross_region_copy = enable_cross_region_copy
        self.target_copy_regions = target_copy_regions
        self.copied_snapshots_retention_days = copied_snapshots_retention_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.auto_snapshot_policy_id is not None:
            result['autoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.auto_snapshot_policy_name is not None:
            result['autoSnapshotPolicyName'] = self.auto_snapshot_policy_name
        if self.time_points is not None:
            result['timePoints'] = self.time_points
        if self.repeat_weekdays is not None:
            result['repeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        if self.enable_cross_region_copy is not None:
            result['EnableCrossRegionCopy'] = self.enable_cross_region_copy
        if self.target_copy_regions is not None:
            result['TargetCopyRegions'] = self.target_copy_regions
        if self.copied_snapshots_retention_days is not None:
            result['CopiedSnapshotsRetentionDays'] = self.copied_snapshots_retention_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('autoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('autoSnapshotPolicyId')
        if m.get('autoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('autoSnapshotPolicyName')
        if m.get('timePoints') is not None:
            self.time_points = m.get('timePoints')
        if m.get('repeatWeekdays') is not None:
            self.repeat_weekdays = m.get('repeatWeekdays')
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        if m.get('EnableCrossRegionCopy') is not None:
            self.enable_cross_region_copy = m.get('EnableCrossRegionCopy')
        if m.get('TargetCopyRegions') is not None:
            self.target_copy_regions = m.get('TargetCopyRegions')
        if m.get('CopiedSnapshotsRetentionDays') is not None:
            self.copied_snapshots_retention_days = m.get('CopiedSnapshotsRetentionDays')
        return self


class ModifyAutoSnapshotPolicyExResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAutoSnapshotPolicyExResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAutoSnapshotPolicyExResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAutoSnapshotPolicyExResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBandwidthPackageSpecRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        bandwidth_package_id: str = None,
        bandwidth: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth = bandwidth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        return self


class ModifyBandwidthPackageSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBandwidthPackageSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBandwidthPackageSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBandwidthPackageSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCapacityReservationRequestPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyCapacityReservationRequest(TeaModel):
    def __init__(
        self,
        private_pool_options: ModifyCapacityReservationRequestPrivatePoolOptions = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        description: str = None,
        start_time: str = None,
        end_time: str = None,
        end_time_type: str = None,
        platform: str = None,
        instance_amount: int = None,
    ):
        self.private_pool_options = private_pool_options
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.end_time_type = end_time_type
        self.platform = platform
        self.instance_amount = instance_amount

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()

    def to_map(self):
        result = dict()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_type is not None:
            result['EndTimeType'] = self.end_time_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.instance_amount is not None:
            result['InstanceAmount'] = self.instance_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = ModifyCapacityReservationRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeType') is not None:
            self.end_time_type = m.get('EndTimeType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('InstanceAmount') is not None:
            self.instance_amount = m.get('InstanceAmount')
        return self


class ModifyCapacityReservationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCapacityReservationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCapacityReservationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCapacityReservationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCommandRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        command_id: str = None,
        name: str = None,
        description: str = None,
        command_content: str = None,
        working_dir: str = None,
        timeout: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.command_id = command_id
        self.name = name
        self.description = description
        self.command_content = command_content
        self.working_dir = working_dir
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class ModifyCommandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCommandResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostAttributeRequestNetworkAttributes(TeaModel):
    def __init__(
        self,
        slb_udp_timeout: int = None,
        udp_timeout: int = None,
    ):
        self.slb_udp_timeout = slb_udp_timeout
        self.udp_timeout = udp_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.slb_udp_timeout is not None:
            result['SlbUdpTimeout'] = self.slb_udp_timeout
        if self.udp_timeout is not None:
            result['UdpTimeout'] = self.udp_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlbUdpTimeout') is not None:
            self.slb_udp_timeout = m.get('SlbUdpTimeout')
        if m.get('UdpTimeout') is not None:
            self.udp_timeout = m.get('UdpTimeout')
        return self


class ModifyDedicatedHostAttributeRequest(TeaModel):
    def __init__(
        self,
        network_attributes: ModifyDedicatedHostAttributeRequestNetworkAttributes = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        dedicated_host_id: str = None,
        dedicated_host_name: str = None,
        description: str = None,
        action_on_maintenance: str = None,
        auto_placement: str = None,
        dedicated_host_cluster_id: str = None,
        cpu_over_commit_ratio: float = None,
    ):
        self.network_attributes = network_attributes
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.dedicated_host_id = dedicated_host_id
        self.dedicated_host_name = dedicated_host_name
        self.description = description
        self.action_on_maintenance = action_on_maintenance
        self.auto_placement = auto_placement
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        self.cpu_over_commit_ratio = cpu_over_commit_ratio

    def validate(self):
        if self.network_attributes:
            self.network_attributes.validate()

    def to_map(self):
        result = dict()
        if self.network_attributes is not None:
            result['NetworkAttributes'] = self.network_attributes.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.description is not None:
            result['Description'] = self.description
        if self.action_on_maintenance is not None:
            result['ActionOnMaintenance'] = self.action_on_maintenance
        if self.auto_placement is not None:
            result['AutoPlacement'] = self.auto_placement
        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id
        if self.cpu_over_commit_ratio is not None:
            result['CpuOverCommitRatio'] = self.cpu_over_commit_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkAttributes') is not None:
            temp_model = ModifyDedicatedHostAttributeRequestNetworkAttributes()
            self.network_attributes = temp_model.from_map(m['NetworkAttributes'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ActionOnMaintenance') is not None:
            self.action_on_maintenance = m.get('ActionOnMaintenance')
        if m.get('AutoPlacement') is not None:
            self.auto_placement = m.get('AutoPlacement')
        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')
        if m.get('CpuOverCommitRatio') is not None:
            self.cpu_over_commit_ratio = m.get('CpuOverCommitRatio')
        return self


class ModifyDedicatedHostAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDedicatedHostAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostAutoReleaseTimeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_id: str = None,
        auto_release_time: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_id = dedicated_host_id
        self.auto_release_time = auto_release_time
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyDedicatedHostAutoReleaseTimeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostAutoReleaseTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDedicatedHostAutoReleaseTimeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostAutoReleaseTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostAutoRenewAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        dedicated_host_ids: str = None,
        region_id: str = None,
        duration: int = None,
        period_unit: str = None,
        auto_renew: bool = None,
        renewal_status: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.dedicated_host_ids = dedicated_host_ids
        self.region_id = region_id
        self.duration = duration
        self.period_unit = period_unit
        self.auto_renew = auto_renew
        self.renewal_status = renewal_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dedicated_host_ids is not None:
            result['DedicatedHostIds'] = self.dedicated_host_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DedicatedHostIds') is not None:
            self.dedicated_host_ids = m.get('DedicatedHostIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        return self


class ModifyDedicatedHostAutoRenewAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostAutoRenewAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDedicatedHostAutoRenewAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostClusterAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        dedicated_host_cluster_id: str = None,
        dedicated_host_cluster_name: str = None,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        self.dedicated_host_cluster_name = dedicated_host_cluster_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id
        if self.dedicated_host_cluster_name is not None:
            result['DedicatedHostClusterName'] = self.dedicated_host_cluster_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')
        if m.get('DedicatedHostClusterName') is not None:
            self.dedicated_host_cluster_name = m.get('DedicatedHostClusterName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyDedicatedHostClusterAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostClusterAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDedicatedHostClusterAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostClusterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostsChargeTypeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_ids: str = None,
        region_id: str = None,
        period: int = None,
        period_unit: str = None,
        dry_run: bool = None,
        auto_pay: bool = None,
        dedicated_host_charge_type: str = None,
        client_token: str = None,
        owner_account: str = None,
        detail_fee: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_ids = dedicated_host_ids
        self.region_id = region_id
        self.period = period
        self.period_unit = period_unit
        self.dry_run = dry_run
        self.auto_pay = auto_pay
        self.dedicated_host_charge_type = dedicated_host_charge_type
        self.client_token = client_token
        self.owner_account = owner_account
        self.detail_fee = detail_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_ids is not None:
            result['DedicatedHostIds'] = self.dedicated_host_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.dedicated_host_charge_type is not None:
            result['DedicatedHostChargeType'] = self.dedicated_host_charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.detail_fee is not None:
            result['DetailFee'] = self.detail_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostIds') is not None:
            self.dedicated_host_ids = m.get('DedicatedHostIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('DedicatedHostChargeType') is not None:
            self.dedicated_host_charge_type = m.get('DedicatedHostChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DetailFee') is not None:
            self.detail_fee = m.get('DetailFee')
        return self


class ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstancesFeeOfInstance(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        currency: str = None,
        fee: str = None,
    ):
        self.instance_id = instance_id
        self.currency = currency
        self.fee = fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.fee is not None:
            result['Fee'] = self.fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Fee') is not None:
            self.fee = m.get('Fee')
        return self


class ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstances(TeaModel):
    def __init__(
        self,
        fee_of_instance: List[ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstancesFeeOfInstance] = None,
    ):
        self.fee_of_instance = fee_of_instance

    def validate(self):
        if self.fee_of_instance:
            for k in self.fee_of_instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FeeOfInstance'] = []
        if self.fee_of_instance is not None:
            for k in self.fee_of_instance:
                result['FeeOfInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fee_of_instance = []
        if m.get('FeeOfInstance') is not None:
            for k in m.get('FeeOfInstance'):
                temp_model = ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstancesFeeOfInstance()
                self.fee_of_instance.append(temp_model.from_map(k))
        return self


class ModifyDedicatedHostsChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        fee_of_instances: ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstances = None,
        request_id: str = None,
        order_id: str = None,
    ):
        self.fee_of_instances = fee_of_instances
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        if self.fee_of_instances:
            self.fee_of_instances.validate()

    def to_map(self):
        result = dict()
        if self.fee_of_instances is not None:
            result['FeeOfInstances'] = self.fee_of_instances.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeeOfInstances') is not None:
            temp_model = ModifyDedicatedHostsChargeTypeResponseBodyFeeOfInstances()
            self.fee_of_instances = temp_model.from_map(m['FeeOfInstances'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyDedicatedHostsChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDedicatedHostsChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostsChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDemandRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        client_token: str = None,
        region_id: str = None,
        zone_id: str = None,
        demand_id: str = None,
        demand_name: str = None,
        demand_description: str = None,
        instance_type: str = None,
        amount: int = None,
        instance_charge_type: str = None,
        period: int = None,
        period_unit: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.client_token = client_token
        self.region_id = region_id
        self.zone_id = zone_id
        self.demand_id = demand_id
        self.demand_name = demand_name
        self.demand_description = demand_description
        self.instance_type = instance_type
        self.amount = amount
        self.instance_charge_type = instance_charge_type
        self.period = period
        self.period_unit = period_unit
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.demand_id is not None:
            result['DemandId'] = self.demand_id
        if self.demand_name is not None:
            result['DemandName'] = self.demand_name
        if self.demand_description is not None:
            result['DemandDescription'] = self.demand_description
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DemandId') is not None:
            self.demand_id = m.get('DemandId')
        if m.get('DemandName') is not None:
            self.demand_name = m.get('DemandName')
        if m.get('DemandDescription') is not None:
            self.demand_description = m.get('DemandDescription')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ModifyDemandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDemandResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeploymentSetAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        deployment_set_id: str = None,
        description: str = None,
        deployment_set_name: str = None,
        region_id: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.deployment_set_id = deployment_set_id
        self.description = description
        self.deployment_set_name = deployment_set_name
        self.region_id = region_id
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.description is not None:
            result['Description'] = self.description
        if self.deployment_set_name is not None:
            result['DeploymentSetName'] = self.deployment_set_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeploymentSetName') is not None:
            self.deployment_set_name = m.get('DeploymentSetName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyDeploymentSetAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDeploymentSetAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDeploymentSetAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDeploymentSetAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        disk_id: str = None,
        disk_name: str = None,
        description: str = None,
        delete_with_instance: bool = None,
        delete_auto_snapshot: bool = None,
        enable_auto_snapshot: bool = None,
        owner_account: str = None,
        disk_ids: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.disk_id = disk_id
        self.disk_name = disk_name
        self.description = description
        self.delete_with_instance = delete_with_instance
        self.delete_auto_snapshot = delete_auto_snapshot
        self.enable_auto_snapshot = enable_auto_snapshot
        self.owner_account = owner_account
        self.disk_ids = disk_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.description is not None:
            result['Description'] = self.description
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.delete_auto_snapshot is not None:
            result['DeleteAutoSnapshot'] = self.delete_auto_snapshot
        if self.enable_auto_snapshot is not None:
            result['EnableAutoSnapshot'] = self.enable_auto_snapshot
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('DeleteAutoSnapshot') is not None:
            self.delete_auto_snapshot = m.get('DeleteAutoSnapshot')
        if m.get('EnableAutoSnapshot') is not None:
            self.enable_auto_snapshot = m.get('EnableAutoSnapshot')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')
        return self


class ModifyDiskAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDiskAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDiskAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDiskAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskChargeTypeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        region_id: str = None,
        disk_ids: str = None,
        auto_pay: bool = None,
        client_token: str = None,
        owner_account: str = None,
        disk_charge_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.region_id = region_id
        self.disk_ids = disk_ids
        self.auto_pay = auto_pay
        self.client_token = client_token
        self.owner_account = owner_account
        self.disk_charge_type = disk_charge_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')
        return self


class ModifyDiskChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyDiskChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDiskChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDiskChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskSpecRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        disk_id: str = None,
        performance_level: str = None,
        disk_category: str = None,
        dry_run: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.disk_id = disk_id
        self.performance_level = performance_level
        self.disk_category = disk_category
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class ModifyDiskSpecResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
        order_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyDiskSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDiskSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDiskSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEipAddressAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        allocation_id: str = None,
        bandwidth: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.allocation_id = allocation_id
        self.bandwidth = bandwidth
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyEipAddressAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyEipAddressAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyEipAddressAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyEipAddressAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElasticityAssuranceRequestPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyElasticityAssuranceRequest(TeaModel):
    def __init__(
        self,
        private_pool_options: ModifyElasticityAssuranceRequestPrivatePoolOptions = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        description: str = None,
    ):
        self.private_pool_options = private_pool_options
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.description = description

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()

    def to_map(self):
        result = dict()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = ModifyElasticityAssuranceRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyElasticityAssuranceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyElasticityAssuranceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyElasticityAssuranceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyElasticityAssuranceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyForwardEntryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        forward_table_id: str = None,
        forward_entry_id: str = None,
        external_ip: str = None,
        external_port: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.forward_table_id = forward_table_id
        self.forward_entry_id = forward_entry_id
        self.external_ip = external_ip
        self.external_port = external_port
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.forward_table_id is not None:
            result['ForwardTableId'] = self.forward_table_id
        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port
        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ForwardTableId') is not None:
            self.forward_table_id = m.get('ForwardTableId')
        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')
        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyForwardEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyForwardEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyForwardEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyForwardEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHaVipAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        client_token: str = None,
        region_id: str = None,
        ha_vip_id: str = None,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.client_token = client_token
        self.region_id = region_id
        self.ha_vip_id = ha_vip_id
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ha_vip_id is not None:
            result['HaVipId'] = self.ha_vip_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HaVipId') is not None:
            self.ha_vip_id = m.get('HaVipId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyHaVipAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHaVipAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHaVipAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHaVipAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHpcClusterAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        client_token: str = None,
        owner_account: str = None,
        hpc_cluster_id: str = None,
        description: str = None,
        name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.client_token = client_token
        self.owner_account = owner_account
        self.hpc_cluster_id = hpc_cluster_id
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyHpcClusterAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHpcClusterAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHpcClusterAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHpcClusterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        image_id: str = None,
        image_name: str = None,
        status: str = None,
        image_family: str = None,
        boot_mode: str = None,
        license_type: str = None,
        description: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.image_id = image_id
        self.image_name = image_name
        self.status = status
        self.image_family = image_family
        self.boot_mode = boot_mode
        self.license_type = license_type
        self.description = description
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.status is not None:
            result['Status'] = self.status
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.boot_mode is not None:
            result['BootMode'] = self.boot_mode
        if self.license_type is not None:
            result['LicenseType'] = self.license_type
        if self.description is not None:
            result['Description'] = self.description
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('BootMode') is not None:
            self.boot_mode = m.get('BootMode')
        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyImageAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyImageAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyImageAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyImageAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageShareGroupPermissionRequest(TeaModel):
    def __init__(
        self,
        add_group: List[str] = None,
        remove_group: List[str] = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        image_id: str = None,
        owner_account: str = None,
    ):
        self.add_group = add_group
        self.remove_group = remove_group
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.image_id = image_id
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.add_group is not None:
            result['AddGroup'] = self.add_group
        if self.remove_group is not None:
            result['RemoveGroup'] = self.remove_group
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddGroup') is not None:
            self.add_group = m.get('AddGroup')
        if m.get('RemoveGroup') is not None:
            self.remove_group = m.get('RemoveGroup')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyImageShareGroupPermissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyImageShareGroupPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyImageShareGroupPermissionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyImageShareGroupPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageSharePermissionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        image_id: str = None,
        owner_account: str = None,
        launch_permission: str = None,
        add_account: List[str] = None,
        remove_account: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.image_id = image_id
        self.owner_account = owner_account
        self.launch_permission = launch_permission
        self.add_account = add_account
        self.remove_account = remove_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.launch_permission is not None:
            result['LaunchPermission'] = self.launch_permission
        if self.add_account is not None:
            result['AddAccount'] = self.add_account
        if self.remove_account is not None:
            result['RemoveAccount'] = self.remove_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('LaunchPermission') is not None:
            self.launch_permission = m.get('LaunchPermission')
        if m.get('AddAccount') is not None:
            self.add_account = m.get('AddAccount')
        if m.get('RemoveAccount') is not None:
            self.remove_account = m.get('RemoveAccount')
        return self


class ModifyImageSharePermissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyImageSharePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyImageSharePermissionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyImageSharePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttachmentAttributesRequestPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        match_criteria: str = None,
        id: str = None,
    ):
        self.match_criteria = match_criteria
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ModifyInstanceAttachmentAttributesRequest(TeaModel):
    def __init__(
        self,
        private_pool_options: ModifyInstanceAttachmentAttributesRequestPrivatePoolOptions = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.private_pool_options = private_pool_options
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()

    def to_map(self):
        result = dict()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = ModifyInstanceAttachmentAttributesRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyInstanceAttachmentAttributesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceAttachmentAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceAttachmentAttributesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAttachmentAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        password: str = None,
        host_name: str = None,
        instance_name: str = None,
        description: str = None,
        owner_account: str = None,
        user_data: str = None,
        recyclable: bool = None,
        credit_specification: str = None,
        deletion_protection: bool = None,
        network_interface_queue_number: int = None,
        security_group_ids: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.password = password
        self.host_name = host_name
        self.instance_name = instance_name
        self.description = description
        self.owner_account = owner_account
        self.user_data = user_data
        self.recyclable = recyclable
        self.credit_specification = credit_specification
        self.deletion_protection = deletion_protection
        self.network_interface_queue_number = network_interface_queue_number
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.description is not None:
            result['Description'] = self.description
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.recyclable is not None:
            result['Recyclable'] = self.recyclable
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.network_interface_queue_number is not None:
            result['NetworkInterfaceQueueNumber'] = self.network_interface_queue_number
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Recyclable') is not None:
            self.recyclable = m.get('Recyclable')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('NetworkInterfaceQueueNumber') is not None:
            self.network_interface_queue_number = m.get('NetworkInterfaceQueueNumber')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAutoReleaseTimeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        instance_id: str = None,
        auto_release_time: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.instance_id = instance_id
        self.auto_release_time = auto_release_time
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyInstanceAutoReleaseTimeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceAutoReleaseTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceAutoReleaseTimeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAutoReleaseTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAutoRenewAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        instance_id: str = None,
        region_id: str = None,
        duration: int = None,
        auto_renew: bool = None,
        renewal_status: str = None,
        period_unit: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.instance_id = instance_id
        self.region_id = region_id
        self.duration = duration
        self.auto_renew = auto_renew
        self.renewal_status = renewal_status
        self.period_unit = period_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        return self


class ModifyInstanceAutoRenewAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceAutoRenewAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceAutoRenewAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceChargeTypeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_ids: str = None,
        region_id: str = None,
        period: int = None,
        period_unit: str = None,
        include_data_disks: bool = None,
        dry_run: bool = None,
        auto_pay: bool = None,
        instance_charge_type: str = None,
        client_token: str = None,
        owner_account: str = None,
        is_detail_fee: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_ids = instance_ids
        self.region_id = region_id
        self.period = period
        self.period_unit = period_unit
        self.include_data_disks = include_data_disks
        self.dry_run = dry_run
        self.auto_pay = auto_pay
        self.instance_charge_type = instance_charge_type
        self.client_token = client_token
        self.owner_account = owner_account
        self.is_detail_fee = is_detail_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.include_data_disks is not None:
            result['IncludeDataDisks'] = self.include_data_disks
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.is_detail_fee is not None:
            result['IsDetailFee'] = self.is_detail_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('IncludeDataDisks') is not None:
            self.include_data_disks = m.get('IncludeDataDisks')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('IsDetailFee') is not None:
            self.is_detail_fee = m.get('IsDetailFee')
        return self


class ModifyInstanceChargeTypeResponseBodyFeeOfInstancesFeeOfInstance(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        currency: str = None,
        fee: str = None,
    ):
        self.instance_id = instance_id
        self.currency = currency
        self.fee = fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.fee is not None:
            result['Fee'] = self.fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Fee') is not None:
            self.fee = m.get('Fee')
        return self


class ModifyInstanceChargeTypeResponseBodyFeeOfInstances(TeaModel):
    def __init__(
        self,
        fee_of_instance: List[ModifyInstanceChargeTypeResponseBodyFeeOfInstancesFeeOfInstance] = None,
    ):
        self.fee_of_instance = fee_of_instance

    def validate(self):
        if self.fee_of_instance:
            for k in self.fee_of_instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FeeOfInstance'] = []
        if self.fee_of_instance is not None:
            for k in self.fee_of_instance:
                result['FeeOfInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fee_of_instance = []
        if m.get('FeeOfInstance') is not None:
            for k in m.get('FeeOfInstance'):
                temp_model = ModifyInstanceChargeTypeResponseBodyFeeOfInstancesFeeOfInstance()
                self.fee_of_instance.append(temp_model.from_map(k))
        return self


class ModifyInstanceChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        fee_of_instances: ModifyInstanceChargeTypeResponseBodyFeeOfInstances = None,
        request_id: str = None,
        order_id: str = None,
    ):
        self.fee_of_instances = fee_of_instances
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        if self.fee_of_instances:
            self.fee_of_instances.validate()

    def to_map(self):
        result = dict()
        if self.fee_of_instances is not None:
            result['FeeOfInstances'] = self.fee_of_instances.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeeOfInstances') is not None:
            temp_model = ModifyInstanceChargeTypeResponseBodyFeeOfInstances()
            self.fee_of_instances = temp_model.from_map(m['FeeOfInstances'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyInstanceChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceDeploymentRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        instance_id: str = None,
        dedicated_host_id: str = None,
        deployment_set_id: str = None,
        deployment_set_group_no: int = None,
        force: bool = None,
        affinity: str = None,
        tenancy: str = None,
        migration_type: str = None,
        instance_type: str = None,
        dedicated_host_cluster_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.instance_id = instance_id
        self.dedicated_host_id = dedicated_host_id
        self.deployment_set_id = deployment_set_id
        self.deployment_set_group_no = deployment_set_group_no
        self.force = force
        self.affinity = affinity
        self.tenancy = tenancy
        self.migration_type = migration_type
        self.instance_type = instance_type
        self.dedicated_host_cluster_id = dedicated_host_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.deployment_set_group_no is not None:
            result['DeploymentSetGroupNo'] = self.deployment_set_group_no
        if self.force is not None:
            result['Force'] = self.force
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('DeploymentSetGroupNo') is not None:
            self.deployment_set_group_no = m.get('DeploymentSetGroupNo')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')
        return self


class ModifyInstanceDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceDeploymentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMaintenanceAttributesRequestMaintenanceWindow(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ModifyInstanceMaintenanceAttributesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        action_on_maintenance: str = None,
        notify_on_maintenance: bool = None,
        instance_id: List[str] = None,
        maintenance_window: List[ModifyInstanceMaintenanceAttributesRequestMaintenanceWindow] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.action_on_maintenance = action_on_maintenance
        self.notify_on_maintenance = notify_on_maintenance
        self.instance_id = instance_id
        self.maintenance_window = maintenance_window

    def validate(self):
        if self.maintenance_window:
            for k in self.maintenance_window:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.action_on_maintenance is not None:
            result['ActionOnMaintenance'] = self.action_on_maintenance
        if self.notify_on_maintenance is not None:
            result['NotifyOnMaintenance'] = self.notify_on_maintenance
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['MaintenanceWindow'] = []
        if self.maintenance_window is not None:
            for k in self.maintenance_window:
                result['MaintenanceWindow'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ActionOnMaintenance') is not None:
            self.action_on_maintenance = m.get('ActionOnMaintenance')
        if m.get('NotifyOnMaintenance') is not None:
            self.notify_on_maintenance = m.get('NotifyOnMaintenance')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.maintenance_window = []
        if m.get('MaintenanceWindow') is not None:
            for k in m.get('MaintenanceWindow'):
                temp_model = ModifyInstanceMaintenanceAttributesRequestMaintenanceWindow()
                self.maintenance_window.append(temp_model.from_map(k))
        return self


class ModifyInstanceMaintenanceAttributesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceMaintenanceAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceMaintenanceAttributesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceMaintenanceAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMetadataOptionsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        instance_id: str = None,
        http_endpoint: str = None,
        http_tokens: str = None,
        http_put_response_hop_limit: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.instance_id = instance_id
        self.http_endpoint = http_endpoint
        self.http_tokens = http_tokens
        self.http_put_response_hop_limit = http_put_response_hop_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.http_endpoint is not None:
            result['HttpEndpoint'] = self.http_endpoint
        if self.http_tokens is not None:
            result['HttpTokens'] = self.http_tokens
        if self.http_put_response_hop_limit is not None:
            result['HttpPutResponseHopLimit'] = self.http_put_response_hop_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('HttpEndpoint') is not None:
            self.http_endpoint = m.get('HttpEndpoint')
        if m.get('HttpTokens') is not None:
            self.http_tokens = m.get('HttpTokens')
        if m.get('HttpPutResponseHopLimit') is not None:
            self.http_put_response_hop_limit = m.get('HttpPutResponseHopLimit')
        return self


class ModifyInstanceMetadataOptionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceMetadataOptionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceMetadataOptionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceMetadataOptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceNetworkSpecRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        internet_max_bandwidth_out: int = None,
        internet_max_bandwidth_in: int = None,
        isp: str = None,
        network_charge_type: str = None,
        allocate_public_ip: bool = None,
        start_time: str = None,
        end_time: str = None,
        auto_pay: bool = None,
        client_token: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.isp = isp
        self.network_charge_type = network_charge_type
        self.allocate_public_ip = allocate_public_ip
        self.start_time = start_time
        self.end_time = end_time
        self.auto_pay = auto_pay
        self.client_token = client_token
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.network_charge_type is not None:
            result['NetworkChargeType'] = self.network_charge_type
        if self.allocate_public_ip is not None:
            result['AllocatePublicIp'] = self.allocate_public_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('NetworkChargeType') is not None:
            self.network_charge_type = m.get('NetworkChargeType')
        if m.get('AllocatePublicIp') is not None:
            self.allocate_public_ip = m.get('AllocatePublicIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyInstanceNetworkSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyInstanceNetworkSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceNetworkSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceNetworkSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceSpecRequestTemporary(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        internet_max_bandwidth_out: int = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.internet_max_bandwidth_out = internet_max_bandwidth_out

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        return self


class ModifyInstanceSpecRequestSystemDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
    ):
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class ModifyInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        temporary: ModifyInstanceSpecRequestTemporary = None,
        system_disk: ModifyInstanceSpecRequestSystemDisk = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_max_bandwidth_out: int = None,
        internet_max_bandwidth_in: int = None,
        owner_account: str = None,
        async_: bool = None,
        allow_migrate_across_zone: bool = None,
        client_token: str = None,
    ):
        self.temporary = temporary
        self.system_disk = system_disk
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.owner_account = owner_account
        self.async_ = async_
        self.allow_migrate_across_zone = allow_migrate_across_zone
        self.client_token = client_token

    def validate(self):
        if self.temporary:
            self.temporary.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        if self.temporary is not None:
            result['Temporary'] = self.temporary.to_map()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.allow_migrate_across_zone is not None:
            result['AllowMigrateAcrossZone'] = self.allow_migrate_across_zone
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Temporary') is not None:
            temp_model = ModifyInstanceSpecRequestTemporary()
            self.temporary = temp_model.from_map(m['Temporary'])
        if m.get('SystemDisk') is not None:
            temp_model = ModifyInstanceSpecRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('AllowMigrateAcrossZone') is not None:
            self.allow_migrate_across_zone = m.get('AllowMigrateAcrossZone')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyInstanceSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceVncPasswdRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        region_id: str = None,
        vnc_password: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.region_id = region_id
        self.vnc_password = vnc_password
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vnc_password is not None:
            result['VncPassword'] = self.vnc_password
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VncPassword') is not None:
            self.vnc_password = m.get('VncPassword')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyInstanceVncPasswdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceVncPasswdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceVncPasswdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceVncPasswdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceVpcAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        v_switch_id: str = None,
        private_ip_address: str = None,
        vpc_id: str = None,
        owner_account: str = None,
        security_group_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.v_switch_id = v_switch_id
        self.private_ip_address = private_ip_address
        self.vpc_id = vpc_id
        self.owner_account = owner_account
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class ModifyInstanceVpcAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceVpcAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceVpcAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceVpcAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLaunchTemplateDefaultVersionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        launch_template_id: str = None,
        launch_template_name: str = None,
        default_version_number: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.launch_template_id = launch_template_id
        self.launch_template_name = launch_template_name
        self.default_version_number = default_version_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_name is not None:
            result['LaunchTemplateName'] = self.launch_template_name
        if self.default_version_number is not None:
            result['DefaultVersionNumber'] = self.default_version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateName') is not None:
            self.launch_template_name = m.get('LaunchTemplateName')
        if m.get('DefaultVersionNumber') is not None:
            self.default_version_number = m.get('DefaultVersionNumber')
        return self


class ModifyLaunchTemplateDefaultVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyLaunchTemplateDefaultVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyLaunchTemplateDefaultVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyLaunchTemplateDefaultVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyManagedInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.instance_id = instance_id
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class ModifyManagedInstanceResponseBodyInstance(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        instance_id: str = None,
    ):
        self.instance_name = instance_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyManagedInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance: ModifyManagedInstanceResponseBodyInstance = None,
    ):
        self.request_id = request_id
        self.instance = instance

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Instance') is not None:
            temp_model = ModifyManagedInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        return self


class ModifyManagedInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyManagedInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyManagedInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNetworkInterfaceAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        network_interface_name: str = None,
        network_interface_id: str = None,
        queue_number: int = None,
        description: str = None,
        security_group_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.network_interface_name = network_interface_name
        self.network_interface_id = network_interface_id
        self.queue_number = queue_number
        self.description = description
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.queue_number is not None:
            result['QueueNumber'] = self.queue_number
        if self.description is not None:
            result['Description'] = self.description
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('QueueNumber') is not None:
            self.queue_number = m.get('QueueNumber')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class ModifyNetworkInterfaceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNetworkInterfaceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyNetworkInterfaceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyNetworkInterfaceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPhysicalConnectionAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        physical_connection_id: str = None,
        line_operator: str = None,
        bandwidth: int = None,
        peer_location: str = None,
        port_type: str = None,
        redundant_physical_connection_id: str = None,
        description: str = None,
        name: str = None,
        client_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        user_cidr: str = None,
        circuit_code: str = None,
    ):
        self.region_id = region_id
        self.physical_connection_id = physical_connection_id
        self.line_operator = line_operator
        self.bandwidth = bandwidth
        self.peer_location = peer_location
        self.port_type = port_type
        self.redundant_physical_connection_id = redundant_physical_connection_id
        self.description = description
        self.name = name
        self.client_token = client_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.user_cidr = user_cidr
        self.circuit_code = circuit_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id
        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.peer_location is not None:
            result['PeerLocation'] = self.peer_location
        if self.port_type is not None:
            result['PortType'] = self.port_type
        if self.redundant_physical_connection_id is not None:
            result['RedundantPhysicalConnectionId'] = self.redundant_physical_connection_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')
        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('PeerLocation') is not None:
            self.peer_location = m.get('PeerLocation')
        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')
        if m.get('RedundantPhysicalConnectionId') is not None:
            self.redundant_physical_connection_id = m.get('RedundantPhysicalConnectionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')
        return self


class ModifyPhysicalConnectionAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPhysicalConnectionAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPhysicalConnectionAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyPhysicalConnectionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPrepayInstanceSpecRequestSystemDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
    ):
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class ModifyPrepayInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        system_disk: ModifyPrepayInstanceSpecRequestSystemDisk = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        region_id: str = None,
        instance_type: str = None,
        operator_type: str = None,
        client_token: str = None,
        auto_pay: bool = None,
        migrate_across_zone: bool = None,
        owner_account: str = None,
        reboot_time: str = None,
        end_time: str = None,
        reboot_when_finished: bool = None,
    ):
        self.system_disk = system_disk
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.region_id = region_id
        self.instance_type = instance_type
        self.operator_type = operator_type
        self.client_token = client_token
        self.auto_pay = auto_pay
        self.migrate_across_zone = migrate_across_zone
        self.owner_account = owner_account
        self.reboot_time = reboot_time
        self.end_time = end_time
        self.reboot_when_finished = reboot_when_finished

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.migrate_across_zone is not None:
            result['MigrateAcrossZone'] = self.migrate_across_zone
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.reboot_time is not None:
            result['RebootTime'] = self.reboot_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.reboot_when_finished is not None:
            result['RebootWhenFinished'] = self.reboot_when_finished
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = ModifyPrepayInstanceSpecRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('MigrateAcrossZone') is not None:
            self.migrate_across_zone = m.get('MigrateAcrossZone')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RebootTime') is not None:
            self.reboot_time = m.get('RebootTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RebootWhenFinished') is not None:
            self.reboot_when_finished = m.get('RebootWhenFinished')
        return self


class ModifyPrepayInstanceSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyPrepayInstanceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPrepayInstanceSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyPrepayInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyReservedInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        reserved_instance_id: str = None,
        reserved_instance_name: str = None,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.reserved_instance_id = reserved_instance_id
        self.reserved_instance_name = reserved_instance_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserved_instance_id is not None:
            result['ReservedInstanceId'] = self.reserved_instance_id
        if self.reserved_instance_name is not None:
            result['ReservedInstanceName'] = self.reserved_instance_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReservedInstanceId') is not None:
            self.reserved_instance_id = m.get('ReservedInstanceId')
        if m.get('ReservedInstanceName') is not None:
            self.reserved_instance_name = m.get('ReservedInstanceName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyReservedInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ModifyReservedInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyReservedInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyReservedInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyReservedInstancesRequestConfiguration(TeaModel):
    def __init__(
        self,
        reserved_instance_name: str = None,
        zone_id: str = None,
        scope: str = None,
        instance_type: str = None,
        instance_amount: int = None,
    ):
        self.reserved_instance_name = reserved_instance_name
        self.zone_id = zone_id
        self.scope = scope
        self.instance_type = instance_type
        self.instance_amount = instance_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.reserved_instance_name is not None:
            result['ReservedInstanceName'] = self.reserved_instance_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_amount is not None:
            result['InstanceAmount'] = self.instance_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservedInstanceName') is not None:
            self.reserved_instance_name = m.get('ReservedInstanceName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceAmount') is not None:
            self.instance_amount = m.get('InstanceAmount')
        return self


class ModifyReservedInstancesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        reserved_instance_id: List[str] = None,
        configuration: List[ModifyReservedInstancesRequestConfiguration] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.reserved_instance_id = reserved_instance_id
        self.configuration = configuration

    def validate(self):
        if self.configuration:
            for k in self.configuration:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserved_instance_id is not None:
            result['ReservedInstanceId'] = self.reserved_instance_id
        result['Configuration'] = []
        if self.configuration is not None:
            for k in self.configuration:
                result['Configuration'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReservedInstanceId') is not None:
            self.reserved_instance_id = m.get('ReservedInstanceId')
        self.configuration = []
        if m.get('Configuration') is not None:
            for k in m.get('Configuration'):
                temp_model = ModifyReservedInstancesRequestConfiguration()
                self.configuration.append(temp_model.from_map(k))
        return self


class ModifyReservedInstancesResponseBodyReservedInstanceIdSets(TeaModel):
    def __init__(
        self,
        reserved_instance_id: List[str] = None,
    ):
        self.reserved_instance_id = reserved_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.reserved_instance_id is not None:
            result['ReservedInstanceId'] = self.reserved_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservedInstanceId') is not None:
            self.reserved_instance_id = m.get('ReservedInstanceId')
        return self


class ModifyReservedInstancesResponseBody(TeaModel):
    def __init__(
        self,
        reserved_instance_id_sets: ModifyReservedInstancesResponseBodyReservedInstanceIdSets = None,
        request_id: str = None,
    ):
        self.reserved_instance_id_sets = reserved_instance_id_sets
        self.request_id = request_id

    def validate(self):
        if self.reserved_instance_id_sets:
            self.reserved_instance_id_sets.validate()

    def to_map(self):
        result = dict()
        if self.reserved_instance_id_sets is not None:
            result['ReservedInstanceIdSets'] = self.reserved_instance_id_sets.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservedInstanceIdSets') is not None:
            temp_model = ModifyReservedInstancesResponseBodyReservedInstanceIdSets()
            self.reserved_instance_id_sets = temp_model.from_map(m['ReservedInstanceIdSets'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyReservedInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyReservedInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyReservedInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRouterInterfaceAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        router_interface_id: str = None,
        name: str = None,
        description: str = None,
        opposite_interface_id: str = None,
        opposite_router_id: str = None,
        opposite_router_type: str = None,
        opposite_interface_owner_id: int = None,
        health_check_source_ip: str = None,
        health_check_target_ip: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.router_interface_id = router_interface_id
        self.name = name
        self.description = description
        self.opposite_interface_id = opposite_interface_id
        self.opposite_router_id = opposite_router_id
        self.opposite_router_type = opposite_router_type
        self.opposite_interface_owner_id = opposite_interface_owner_id
        self.health_check_source_ip = health_check_source_ip
        self.health_check_target_ip = health_check_target_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.opposite_interface_id is not None:
            result['OppositeInterfaceId'] = self.opposite_interface_id
        if self.opposite_router_id is not None:
            result['OppositeRouterId'] = self.opposite_router_id
        if self.opposite_router_type is not None:
            result['OppositeRouterType'] = self.opposite_router_type
        if self.opposite_interface_owner_id is not None:
            result['OppositeInterfaceOwnerId'] = self.opposite_interface_owner_id
        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip
        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OppositeInterfaceId') is not None:
            self.opposite_interface_id = m.get('OppositeInterfaceId')
        if m.get('OppositeRouterId') is not None:
            self.opposite_router_id = m.get('OppositeRouterId')
        if m.get('OppositeRouterType') is not None:
            self.opposite_router_type = m.get('OppositeRouterType')
        if m.get('OppositeInterfaceOwnerId') is not None:
            self.opposite_interface_owner_id = m.get('OppositeInterfaceOwnerId')
        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')
        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')
        return self


class ModifyRouterInterfaceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyRouterInterfaceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRouterInterfaceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyRouterInterfaceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRouterInterfaceSpecRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        router_interface_id: str = None,
        spec: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        owner_account: str = None,
        user_cidr: str = None,
    ):
        self.region_id = region_id
        self.router_interface_id = router_interface_id
        self.spec = spec
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.owner_account = owner_account
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class ModifyRouterInterfaceSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        spec: str = None,
    ):
        self.request_id = request_id
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class ModifyRouterInterfaceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRouterInterfaceSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyRouterInterfaceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        description: str = None,
        security_group_name: str = None,
        region_id: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_group_id = security_group_id
        self.description = description
        self.security_group_name = security_group_name
        self.region_id = region_id
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifySecurityGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySecurityGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySecurityGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySecurityGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupEgressRuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        security_group_id: str = None,
        ip_protocol: str = None,
        port_range: str = None,
        dest_group_id: str = None,
        dest_group_owner_id: int = None,
        dest_group_owner_account: str = None,
        dest_cidr_ip: str = None,
        ipv_6dest_cidr_ip: str = None,
        source_cidr_ip: str = None,
        ipv_6source_cidr_ip: str = None,
        source_port_range: str = None,
        policy: str = None,
        priority: str = None,
        nic_type: str = None,
        client_token: str = None,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.ip_protocol = ip_protocol
        self.port_range = port_range
        self.dest_group_id = dest_group_id
        self.dest_group_owner_id = dest_group_owner_id
        self.dest_group_owner_account = dest_group_owner_account
        self.dest_cidr_ip = dest_cidr_ip
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        self.source_cidr_ip = source_cidr_ip
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        self.source_port_range = source_port_range
        self.policy = policy
        self.priority = priority
        self.nic_type = nic_type
        self.client_token = client_token
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.dest_group_id is not None:
            result['DestGroupId'] = self.dest_group_id
        if self.dest_group_owner_id is not None:
            result['DestGroupOwnerId'] = self.dest_group_owner_id
        if self.dest_group_owner_account is not None:
            result['DestGroupOwnerAccount'] = self.dest_group_owner_account
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip
        if self.ipv_6dest_cidr_ip is not None:
            result['Ipv6DestCidrIp'] = self.ipv_6dest_cidr_ip
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.nic_type is not None:
            result['NicType'] = self.nic_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('DestGroupId') is not None:
            self.dest_group_id = m.get('DestGroupId')
        if m.get('DestGroupOwnerId') is not None:
            self.dest_group_owner_id = m.get('DestGroupOwnerId')
        if m.get('DestGroupOwnerAccount') is not None:
            self.dest_group_owner_account = m.get('DestGroupOwnerAccount')
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')
        if m.get('Ipv6DestCidrIp') is not None:
            self.ipv_6dest_cidr_ip = m.get('Ipv6DestCidrIp')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('NicType') is not None:
            self.nic_type = m.get('NicType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifySecurityGroupEgressRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySecurityGroupEgressRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySecurityGroupEgressRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySecurityGroupEgressRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupPolicyRequest(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        region_id: str = None,
        inner_access_policy: str = None,
        client_token: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        owner_id: int = None,
    ):
        self.security_group_id = security_group_id
        self.region_id = region_id
        self.inner_access_policy = inner_access_policy
        self.client_token = client_token
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.inner_access_policy is not None:
            result['InnerAccessPolicy'] = self.inner_access_policy
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InnerAccessPolicy') is not None:
            self.inner_access_policy = m.get('InnerAccessPolicy')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ModifySecurityGroupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySecurityGroupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySecurityGroupPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySecurityGroupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupRuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        security_group_id: str = None,
        ip_protocol: str = None,
        port_range: str = None,
        source_group_id: str = None,
        source_group_owner_id: int = None,
        source_group_owner_account: str = None,
        source_cidr_ip: str = None,
        ipv_6source_cidr_ip: str = None,
        source_port_range: str = None,
        dest_cidr_ip: str = None,
        ipv_6dest_cidr_ip: str = None,
        policy: str = None,
        priority: str = None,
        nic_type: str = None,
        client_token: str = None,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.ip_protocol = ip_protocol
        self.port_range = port_range
        self.source_group_id = source_group_id
        self.source_group_owner_id = source_group_owner_id
        self.source_group_owner_account = source_group_owner_account
        self.source_cidr_ip = source_cidr_ip
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        self.source_port_range = source_port_range
        self.dest_cidr_ip = dest_cidr_ip
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        self.policy = policy
        self.priority = priority
        self.nic_type = nic_type
        self.client_token = client_token
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.source_group_id is not None:
            result['SourceGroupId'] = self.source_group_id
        if self.source_group_owner_id is not None:
            result['SourceGroupOwnerId'] = self.source_group_owner_id
        if self.source_group_owner_account is not None:
            result['SourceGroupOwnerAccount'] = self.source_group_owner_account
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip
        if self.ipv_6dest_cidr_ip is not None:
            result['Ipv6DestCidrIp'] = self.ipv_6dest_cidr_ip
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.nic_type is not None:
            result['NicType'] = self.nic_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('SourceGroupId') is not None:
            self.source_group_id = m.get('SourceGroupId')
        if m.get('SourceGroupOwnerId') is not None:
            self.source_group_owner_id = m.get('SourceGroupOwnerId')
        if m.get('SourceGroupOwnerAccount') is not None:
            self.source_group_owner_account = m.get('SourceGroupOwnerAccount')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')
        if m.get('Ipv6DestCidrIp') is not None:
            self.ipv_6dest_cidr_ip = m.get('Ipv6DestCidrIp')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('NicType') is not None:
            self.nic_type = m.get('NicType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifySecurityGroupRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySecurityGroupRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySecurityGroupRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySecurityGroupRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySnapshotAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        description: str = None,
        disable_instant_access: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.snapshot_id = snapshot_id
        self.snapshot_name = snapshot_name
        self.description = description
        self.disable_instant_access = disable_instant_access

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_instant_access is not None:
            result['DisableInstantAccess'] = self.disable_instant_access
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableInstantAccess') is not None:
            self.disable_instant_access = m.get('DisableInstantAccess')
        return self


class ModifySnapshotAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySnapshotAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySnapshotAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySnapshotAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySnapshotGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        snapshot_group_id: str = None,
        name: str = None,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.snapshot_group_id = snapshot_group_id
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_group_id is not None:
            result['SnapshotGroupId'] = self.snapshot_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotGroupId') is not None:
            self.snapshot_group_id = m.get('SnapshotGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifySnapshotGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySnapshotGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySnapshotGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySnapshotGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyStorageCapacityUnitAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        storage_capacity_unit_id: str = None,
        name: str = None,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.storage_capacity_unit_id = storage_capacity_unit_id
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_capacity_unit_id is not None:
            result['StorageCapacityUnitId'] = self.storage_capacity_unit_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageCapacityUnitId') is not None:
            self.storage_capacity_unit_id = m.get('StorageCapacityUnitId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyStorageCapacityUnitAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyStorageCapacityUnitAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyStorageCapacityUnitAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyStorageCapacityUnitAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyStorageSetAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        client_token: str = None,
        region_id: str = None,
        storage_set_id: str = None,
        storage_set_name: str = None,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.client_token = client_token
        self.region_id = region_id
        self.storage_set_id = storage_set_id
        self.storage_set_name = storage_set_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id
        if self.storage_set_name is not None:
            result['StorageSetName'] = self.storage_set_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')
        if m.get('StorageSetName') is not None:
            self.storage_set_name = m.get('StorageSetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyStorageSetAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyStorageSetAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyStorageSetAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyStorageSetAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserBusinessBehaviorRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        status_key: str = None,
        status_value: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.status_key = status_key
        self.status_value = status_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status_key is not None:
            result['statusKey'] = self.status_key
        if self.status_value is not None:
            result['statusValue'] = self.status_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('statusKey') is not None:
            self.status_key = m.get('statusKey')
        if m.get('statusValue') is not None:
            self.status_value = m.get('statusValue')
        return self


class ModifyUserBusinessBehaviorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUserBusinessBehaviorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyUserBusinessBehaviorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUserBusinessBehaviorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVirtualBorderRouterAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vbr_id: str = None,
        vlan_id: int = None,
        circuit_code: str = None,
        local_gateway_ip: str = None,
        peer_gateway_ip: str = None,
        peering_subnet_mask: str = None,
        description: str = None,
        name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        owner_account: str = None,
        user_cidr: str = None,
    ):
        self.region_id = region_id
        self.vbr_id = vbr_id
        self.vlan_id = vlan_id
        self.circuit_code = circuit_code
        self.local_gateway_ip = local_gateway_ip
        self.peer_gateway_ip = peer_gateway_ip
        self.peering_subnet_mask = peering_subnet_mask
        self.description = description
        self.name = name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.owner_account = owner_account
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id
        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id
        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code
        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip
        if self.peer_gateway_ip is not None:
            result['PeerGatewayIp'] = self.peer_gateway_ip
        if self.peering_subnet_mask is not None:
            result['PeeringSubnetMask'] = self.peering_subnet_mask
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')
        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')
        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')
        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')
        if m.get('PeerGatewayIp') is not None:
            self.peer_gateway_ip = m.get('PeerGatewayIp')
        if m.get('PeeringSubnetMask') is not None:
            self.peering_subnet_mask = m.get('PeeringSubnetMask')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class ModifyVirtualBorderRouterAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVirtualBorderRouterAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyVirtualBorderRouterAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyVirtualBorderRouterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vpc_id: str = None,
        description: str = None,
        vpc_name: str = None,
        cidr_block: str = None,
        region_id: str = None,
        owner_account: str = None,
        user_cidr: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.vpc_id = vpc_id
        self.description = description
        self.vpc_name = vpc_name
        self.cidr_block = cidr_block
        self.region_id = region_id
        self.owner_account = owner_account
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.description is not None:
            result['Description'] = self.description
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class ModifyVpcAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVpcAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyVpcAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyVpcAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVRouterAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        vrouter_id: str = None,
        vrouter_name: str = None,
        description: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.vrouter_id = vrouter_id
        self.vrouter_name = vrouter_name
        self.description = description
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id
        if self.vrouter_name is not None:
            result['VRouterName'] = self.vrouter_name
        if self.description is not None:
            result['Description'] = self.description
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')
        if m.get('VRouterName') is not None:
            self.vrouter_name = m.get('VRouterName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyVRouterAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVRouterAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyVRouterAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyVRouterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVSwitchAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        region_id: str = None,
        description: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.region_id = region_id
        self.description = description
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyVSwitchAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVSwitchAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyVSwitchAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyVSwitchAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PurchaseReservedInstancesOfferingRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PurchaseReservedInstancesOfferingRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        tag: List[PurchaseReservedInstancesOfferingRequestTag] = None,
        resource_group_id: str = None,
        zone_id: str = None,
        reserved_instance_name: str = None,
        instance_type: str = None,
        scope: str = None,
        instance_amount: int = None,
        offering_type: str = None,
        description: str = None,
        platform: str = None,
        period: int = None,
        period_unit: str = None,
        client_token: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.tag = tag
        self.resource_group_id = resource_group_id
        self.zone_id = zone_id
        self.reserved_instance_name = reserved_instance_name
        self.instance_type = instance_type
        self.scope = scope
        self.instance_amount = instance_amount
        self.offering_type = offering_type
        self.description = description
        self.platform = platform
        self.period = period
        self.period_unit = period_unit
        self.client_token = client_token

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.reserved_instance_name is not None:
            result['ReservedInstanceName'] = self.reserved_instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.instance_amount is not None:
            result['InstanceAmount'] = self.instance_amount
        if self.offering_type is not None:
            result['OfferingType'] = self.offering_type
        if self.description is not None:
            result['Description'] = self.description
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = PurchaseReservedInstancesOfferingRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ReservedInstanceName') is not None:
            self.reserved_instance_name = m.get('ReservedInstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('InstanceAmount') is not None:
            self.instance_amount = m.get('InstanceAmount')
        if m.get('OfferingType') is not None:
            self.offering_type = m.get('OfferingType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class PurchaseReservedInstancesOfferingResponseBodyReservedInstanceIdSets(TeaModel):
    def __init__(
        self,
        reserved_instance_id: List[str] = None,
    ):
        self.reserved_instance_id = reserved_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.reserved_instance_id is not None:
            result['ReservedInstanceId'] = self.reserved_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservedInstanceId') is not None:
            self.reserved_instance_id = m.get('ReservedInstanceId')
        return self


class PurchaseReservedInstancesOfferingResponseBody(TeaModel):
    def __init__(
        self,
        reserved_instance_id_sets: PurchaseReservedInstancesOfferingResponseBodyReservedInstanceIdSets = None,
        request_id: str = None,
    ):
        self.reserved_instance_id_sets = reserved_instance_id_sets
        self.request_id = request_id

    def validate(self):
        if self.reserved_instance_id_sets:
            self.reserved_instance_id_sets.validate()

    def to_map(self):
        result = dict()
        if self.reserved_instance_id_sets is not None:
            result['ReservedInstanceIdSets'] = self.reserved_instance_id_sets.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservedInstanceIdSets') is not None:
            temp_model = PurchaseReservedInstancesOfferingResponseBodyReservedInstanceIdSets()
            self.reserved_instance_id_sets = temp_model.from_map(m['ReservedInstanceIdSets'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PurchaseReservedInstancesOfferingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PurchaseReservedInstancesOfferingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PurchaseReservedInstancesOfferingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PurchaseStorageCapacityUnitRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        name: str = None,
        capacity: int = None,
        description: str = None,
        start_time: str = None,
        period: int = None,
        period_unit: str = None,
        from_app: str = None,
        client_token: str = None,
        amount: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.name = name
        self.capacity = capacity
        self.description = description
        self.start_time = start_time
        self.period = period
        self.period_unit = period_unit
        self.from_app = from_app
        self.client_token = client_token
        self.amount = amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.description is not None:
            result['Description'] = self.description
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.amount is not None:
            result['Amount'] = self.amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        return self


class PurchaseStorageCapacityUnitResponseBodyStorageCapacityUnitIds(TeaModel):
    def __init__(
        self,
        storage_capacity_unit_id: List[str] = None,
    ):
        self.storage_capacity_unit_id = storage_capacity_unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.storage_capacity_unit_id is not None:
            result['StorageCapacityUnitId'] = self.storage_capacity_unit_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageCapacityUnitId') is not None:
            self.storage_capacity_unit_id = m.get('StorageCapacityUnitId')
        return self


class PurchaseStorageCapacityUnitResponseBody(TeaModel):
    def __init__(
        self,
        storage_capacity_unit_ids: PurchaseStorageCapacityUnitResponseBodyStorageCapacityUnitIds = None,
        request_id: str = None,
        order_id: str = None,
    ):
        self.storage_capacity_unit_ids = storage_capacity_unit_ids
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        if self.storage_capacity_unit_ids:
            self.storage_capacity_unit_ids.validate()

    def to_map(self):
        result = dict()
        if self.storage_capacity_unit_ids is not None:
            result['StorageCapacityUnitIds'] = self.storage_capacity_unit_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageCapacityUnitIds') is not None:
            temp_model = PurchaseStorageCapacityUnitResponseBodyStorageCapacityUnitIds()
            self.storage_capacity_unit_ids = temp_model.from_map(m['StorageCapacityUnitIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class PurchaseStorageCapacityUnitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PurchaseStorageCapacityUnitResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PurchaseStorageCapacityUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReActivateInstancesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        instance_id: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.instance_id = instance_id
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ReActivateInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReActivateInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReActivateInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReActivateInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        force_stop: bool = None,
        owner_account: str = None,
        dry_run: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.force_stop = force_stop
        self.owner_account = owner_account
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class RebootInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebootInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RebootInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RebootInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootInstancesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        dry_run: bool = None,
        region_id: str = None,
        force_reboot: bool = None,
        batch_optimization: str = None,
        instance_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.dry_run = dry_run
        self.region_id = region_id
        self.force_reboot = force_reboot
        self.batch_optimization = batch_optimization
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.force_reboot is not None:
            result['ForceReboot'] = self.force_reboot
        if self.batch_optimization is not None:
            result['BatchOptimization'] = self.batch_optimization
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ForceReboot') is not None:
            self.force_reboot = m.get('ForceReboot')
        if m.get('BatchOptimization') is not None:
            self.batch_optimization = m.get('BatchOptimization')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RebootInstancesResponseBodyInstanceResponsesInstanceResponse(TeaModel):
    def __init__(
        self,
        current_status: str = None,
        previous_status: str = None,
        code: str = None,
        message: str = None,
        instance_id: str = None,
    ):
        self.current_status = current_status
        self.previous_status = previous_status
        self.code = code
        self.message = message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status
        if self.previous_status is not None:
            result['PreviousStatus'] = self.previous_status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')
        if m.get('PreviousStatus') is not None:
            self.previous_status = m.get('PreviousStatus')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RebootInstancesResponseBodyInstanceResponses(TeaModel):
    def __init__(
        self,
        instance_response: List[RebootInstancesResponseBodyInstanceResponsesInstanceResponse] = None,
    ):
        self.instance_response = instance_response

    def validate(self):
        if self.instance_response:
            for k in self.instance_response:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceResponse'] = []
        if self.instance_response is not None:
            for k in self.instance_response:
                result['InstanceResponse'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_response = []
        if m.get('InstanceResponse') is not None:
            for k in m.get('InstanceResponse'):
                temp_model = RebootInstancesResponseBodyInstanceResponsesInstanceResponse()
                self.instance_response.append(temp_model.from_map(k))
        return self


class RebootInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_responses: RebootInstancesResponseBodyInstanceResponses = None,
    ):
        self.request_id = request_id
        self.instance_responses = instance_responses

    def validate(self):
        if self.instance_responses:
            self.instance_responses.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_responses is not None:
            result['InstanceResponses'] = self.instance_responses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceResponses') is not None:
            temp_model = RebootInstancesResponseBodyInstanceResponses()
            self.instance_responses = temp_model.from_map(m['InstanceResponses'])
        return self


class RebootInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RebootInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RebootInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverVirtualBorderRouterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vbr_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        owner_account: str = None,
        user_cidr: str = None,
    ):
        self.region_id = region_id
        self.vbr_id = vbr_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.owner_account = owner_account
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class RecoverVirtualBorderRouterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecoverVirtualBorderRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecoverVirtualBorderRouterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RecoverVirtualBorderRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RedeployDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        dedicated_host_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.dedicated_host_id = dedicated_host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        return self


class RedeployDedicatedHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RedeployDedicatedHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RedeployDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RedeployDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RedeployInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        instance_id: str = None,
        force_stop: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.instance_id = instance_id
        self.force_stop = force_stop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        return self


class RedeployInstanceResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RedeployInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RedeployInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RedeployInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReInitDiskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        disk_id: str = None,
        owner_account: str = None,
        password: str = None,
        key_pair_name: str = None,
        auto_start_instance: bool = None,
        security_enhancement_strategy: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.disk_id = disk_id
        self.owner_account = owner_account
        self.password = password
        self.key_pair_name = key_pair_name
        self.auto_start_instance = auto_start_instance
        self.security_enhancement_strategy = security_enhancement_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.password is not None:
            result['Password'] = self.password
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.auto_start_instance is not None:
            result['AutoStartInstance'] = self.auto_start_instance
        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('AutoStartInstance') is not None:
            self.auto_start_instance = m.get('AutoStartInstance')
        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')
        return self


class ReInitDiskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReInitDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReInitDiskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReInitDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseCapacityReservationRequestPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ReleaseCapacityReservationRequest(TeaModel):
    def __init__(
        self,
        private_pool_options: ReleaseCapacityReservationRequestPrivatePoolOptions = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        dry_run: bool = None,
    ):
        self.private_pool_options = private_pool_options
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.dry_run = dry_run

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()

    def to_map(self):
        result = dict()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = ReleaseCapacityReservationRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class ReleaseCapacityReservationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseCapacityReservationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseCapacityReservationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseCapacityReservationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        dedicated_host_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.dedicated_host_id = dedicated_host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        return self


class ReleaseDedicatedHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseDedicatedHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseEipAddressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        allocation_id: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.allocation_id = allocation_id
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ReleaseEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePublicIpAddressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        public_ip_address: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.public_ip_address = public_ip_address
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ReleasePublicIpAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleasePublicIpAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleasePublicIpAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleasePublicIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveBandwidthPackageIpsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        bandwidth_package_id: str = None,
        client_token: str = None,
        removed_ip_addresses: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.client_token = client_token
        self.removed_ip_addresses = removed_ip_addresses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.removed_ip_addresses is not None:
            result['RemovedIpAddresses'] = self.removed_ip_addresses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RemovedIpAddresses') is not None:
            self.removed_ip_addresses = m.get('RemovedIpAddresses')
        return self


class RemoveBandwidthPackageIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveBandwidthPackageIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveBandwidthPackageIpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveBandwidthPackageIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTagsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class RemoveTagsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        resource_type: str = None,
        resource_id: str = None,
        tag: List[RemoveTagsRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = RemoveTagsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class RemoveTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewDedicatedHostsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        dedicated_host_ids: str = None,
        region_id: str = None,
        period: int = None,
        period_unit: str = None,
        client_token: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.dedicated_host_ids = dedicated_host_ids
        self.region_id = region_id
        self.period = period
        self.period_unit = period_unit
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dedicated_host_ids is not None:
            result['DedicatedHostIds'] = self.dedicated_host_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DedicatedHostIds') is not None:
            self.dedicated_host_ids = m.get('DedicatedHostIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RenewDedicatedHostsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewDedicatedHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewDedicatedHostsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewDedicatedHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        instance_id: str = None,
        period: int = None,
        period_unit: str = None,
        expected_renew_day: int = None,
    ):
        self.client_token = client_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.instance_id = instance_id
        self.period = period
        self.period_unit = period_unit
        self.expected_renew_day = expected_renew_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.expected_renew_day is not None:
            result['ExpectedRenewDay'] = self.expected_renew_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ExpectedRenewDay') is not None:
            self.expected_renew_day = m.get('ExpectedRenewDay')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceSystemDiskRequestSystemDisk(TeaModel):
    def __init__(
        self,
        size: int = None,
    ):
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ReplaceSystemDiskRequest(TeaModel):
    def __init__(
        self,
        system_disk: ReplaceSystemDiskRequestSystemDisk = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        image_id: str = None,
        client_token: str = None,
        owner_account: str = None,
        use_additional_service: bool = None,
        password: str = None,
        password_inherit: bool = None,
        key_pair_name: str = None,
        disk_id: str = None,
        platform: str = None,
        architecture: str = None,
        security_enhancement_strategy: str = None,
    ):
        self.system_disk = system_disk
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.image_id = image_id
        self.client_token = client_token
        self.owner_account = owner_account
        self.use_additional_service = use_additional_service
        self.password = password
        self.password_inherit = password_inherit
        self.key_pair_name = key_pair_name
        self.disk_id = disk_id
        self.platform = platform
        self.architecture = architecture
        self.security_enhancement_strategy = security_enhancement_strategy

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.use_additional_service is not None:
            result['UseAdditionalService'] = self.use_additional_service
        if self.password is not None:
            result['Password'] = self.password
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = ReplaceSystemDiskRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UseAdditionalService') is not None:
            self.use_additional_service = m.get('UseAdditionalService')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')
        return self


class ReplaceSystemDiskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        disk_id: str = None,
    ):
        self.request_id = request_id
        self.disk_id = disk_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        return self


class ReplaceSystemDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReplaceSystemDiskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReplaceSystemDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportInstancesStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        reason: str = None,
        description: str = None,
        start_time: str = None,
        end_time: str = None,
        issue_category: str = None,
        instance_id: List[str] = None,
        disk_id: List[str] = None,
        device: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.reason = reason
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.issue_category = issue_category
        self.instance_id = instance_id
        self.disk_id = disk_id
        self.device = device

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.description is not None:
            result['Description'] = self.description
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.issue_category is not None:
            result['IssueCategory'] = self.issue_category
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.device is not None:
            result['Device'] = self.device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IssueCategory') is not None:
            self.issue_category = m.get('IssueCategory')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        return self


class ReportInstancesStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportInstancesStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReportInstancesStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReportInstancesStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDiskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        disk_id: str = None,
        snapshot_id: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.disk_id = disk_id
        self.snapshot_id = snapshot_id
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ResetDiskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetDiskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDisksRequestDisk(TeaModel):
    def __init__(
        self,
        snapshot_id: str = None,
        disk_id: str = None,
    ):
        self.snapshot_id = snapshot_id
        self.disk_id = disk_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        return self


class ResetDisksRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        disk: List[ResetDisksRequestDisk] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.disk = disk

    def validate(self):
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.disk = []
        if m.get('Disk') is not None:
            for k in m.get('Disk'):
                temp_model = ResetDisksRequestDisk()
                self.disk.append(temp_model.from_map(k))
        return self


class ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSet(TeaModel):
    def __init__(
        self,
        related_item: List[ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem] = None,
    ):
        self.related_item = related_item

    def validate(self):
        if self.related_item:
            for k in self.related_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RelatedItem'] = []
        if self.related_item is not None:
            for k in self.related_item:
                result['RelatedItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.related_item = []
        if m.get('RelatedItem') is not None:
            for k in m.get('RelatedItem'):
                temp_model = ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem()
                self.related_item.append(temp_model.from_map(k))
        return self


class ResetDisksResponseBodyOperationProgressSetOperationProgress(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        related_item_set: ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSet = None,
        operation_status: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.related_item_set = related_item_set
        self.operation_status = operation_status

    def validate(self):
        if self.related_item_set:
            self.related_item_set.validate()

    def to_map(self):
        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.related_item_set is not None:
            result['RelatedItemSet'] = self.related_item_set.to_map()
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RelatedItemSet') is not None:
            temp_model = ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSet()
            self.related_item_set = temp_model.from_map(m['RelatedItemSet'])
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        return self


class ResetDisksResponseBodyOperationProgressSet(TeaModel):
    def __init__(
        self,
        operation_progress: List[ResetDisksResponseBodyOperationProgressSetOperationProgress] = None,
    ):
        self.operation_progress = operation_progress

    def validate(self):
        if self.operation_progress:
            for k in self.operation_progress:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['OperationProgress'] = []
        if self.operation_progress is not None:
            for k in self.operation_progress:
                result['OperationProgress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation_progress = []
        if m.get('OperationProgress') is not None:
            for k in m.get('OperationProgress'):
                temp_model = ResetDisksResponseBodyOperationProgressSetOperationProgress()
                self.operation_progress.append(temp_model.from_map(k))
        return self


class ResetDisksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operation_progress_set: ResetDisksResponseBodyOperationProgressSet = None,
    ):
        self.request_id = request_id
        self.operation_progress_set = operation_progress_set

    def validate(self):
        if self.operation_progress_set:
            self.operation_progress_set.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_progress_set is not None:
            result['OperationProgressSet'] = self.operation_progress_set.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationProgressSet') is not None:
            temp_model = ResetDisksResponseBodyOperationProgressSet()
            self.operation_progress_set = temp_model.from_map(m['OperationProgressSet'])
        return self


class ResetDisksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetDisksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetDisksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeDiskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        disk_id: str = None,
        type: str = None,
        new_size: int = None,
        client_token: str = None,
        owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.disk_id = disk_id
        self.type = type
        self.new_size = new_size
        self.client_token = client_token
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.type is not None:
            result['Type'] = self.type
        if self.new_size is not None:
            result['NewSize'] = self.new_size
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NewSize') is not None:
            self.new_size = m.get('NewSize')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ResizeDiskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ResizeDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResizeDiskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResizeDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        security_group_id: str = None,
        dest_cidr_ip: str = None,
        ipv_6dest_cidr_ip: str = None,
        port_range: str = None,
        ip_protocol: str = None,
        source_group_id: str = None,
        source_group_owner_id: int = None,
        source_group_owner_account: str = None,
        source_cidr_ip: str = None,
        ipv_6source_cidr_ip: str = None,
        source_port_range: str = None,
        policy: str = None,
        priority: str = None,
        nic_type: str = None,
        client_token: str = None,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.dest_cidr_ip = dest_cidr_ip
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        self.port_range = port_range
        self.ip_protocol = ip_protocol
        self.source_group_id = source_group_id
        self.source_group_owner_id = source_group_owner_id
        self.source_group_owner_account = source_group_owner_account
        self.source_cidr_ip = source_cidr_ip
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        self.source_port_range = source_port_range
        self.policy = policy
        self.priority = priority
        self.nic_type = nic_type
        self.client_token = client_token
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip
        if self.ipv_6dest_cidr_ip is not None:
            result['Ipv6DestCidrIp'] = self.ipv_6dest_cidr_ip
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.source_group_id is not None:
            result['SourceGroupId'] = self.source_group_id
        if self.source_group_owner_id is not None:
            result['SourceGroupOwnerId'] = self.source_group_owner_id
        if self.source_group_owner_account is not None:
            result['SourceGroupOwnerAccount'] = self.source_group_owner_account
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.nic_type is not None:
            result['NicType'] = self.nic_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')
        if m.get('Ipv6DestCidrIp') is not None:
            self.ipv_6dest_cidr_ip = m.get('Ipv6DestCidrIp')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('SourceGroupId') is not None:
            self.source_group_id = m.get('SourceGroupId')
        if m.get('SourceGroupOwnerId') is not None:
            self.source_group_owner_id = m.get('SourceGroupOwnerId')
        if m.get('SourceGroupOwnerAccount') is not None:
            self.source_group_owner_account = m.get('SourceGroupOwnerAccount')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('NicType') is not None:
            self.nic_type = m.get('NicType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class RevokeSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RevokeSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RevokeSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeSecurityGroupEgressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        security_group_id: str = None,
        ip_protocol: str = None,
        port_range: str = None,
        dest_group_id: str = None,
        dest_group_owner_id: int = None,
        dest_group_owner_account: str = None,
        dest_cidr_ip: str = None,
        ipv_6dest_cidr_ip: str = None,
        source_cidr_ip: str = None,
        ipv_6source_cidr_ip: str = None,
        source_port_range: str = None,
        policy: str = None,
        priority: str = None,
        nic_type: str = None,
        client_token: str = None,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.ip_protocol = ip_protocol
        self.port_range = port_range
        self.dest_group_id = dest_group_id
        self.dest_group_owner_id = dest_group_owner_id
        self.dest_group_owner_account = dest_group_owner_account
        self.dest_cidr_ip = dest_cidr_ip
        self.ipv_6dest_cidr_ip = ipv_6dest_cidr_ip
        self.source_cidr_ip = source_cidr_ip
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        self.source_port_range = source_port_range
        self.policy = policy
        self.priority = priority
        self.nic_type = nic_type
        self.client_token = client_token
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.dest_group_id is not None:
            result['DestGroupId'] = self.dest_group_id
        if self.dest_group_owner_id is not None:
            result['DestGroupOwnerId'] = self.dest_group_owner_id
        if self.dest_group_owner_account is not None:
            result['DestGroupOwnerAccount'] = self.dest_group_owner_account
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip
        if self.ipv_6dest_cidr_ip is not None:
            result['Ipv6DestCidrIp'] = self.ipv_6dest_cidr_ip
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.nic_type is not None:
            result['NicType'] = self.nic_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('DestGroupId') is not None:
            self.dest_group_id = m.get('DestGroupId')
        if m.get('DestGroupOwnerId') is not None:
            self.dest_group_owner_id = m.get('DestGroupOwnerId')
        if m.get('DestGroupOwnerAccount') is not None:
            self.dest_group_owner_account = m.get('DestGroupOwnerAccount')
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')
        if m.get('Ipv6DestCidrIp') is not None:
            self.ipv_6dest_cidr_ip = m.get('Ipv6DestCidrIp')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('NicType') is not None:
            self.nic_type = m.get('NicType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class RevokeSecurityGroupEgressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeSecurityGroupEgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RevokeSecurityGroupEgressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RevokeSecurityGroupEgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCommandRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        name: str = None,
        description: str = None,
        type: str = None,
        command_content: str = None,
        working_dir: str = None,
        timeout: int = None,
        enable_parameter: bool = None,
        timed: bool = None,
        frequency: str = None,
        parameters: Dict[str, Any] = None,
        keep_command: bool = None,
        content_encoding: str = None,
        username: str = None,
        windows_password_name: str = None,
        instance_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.name = name
        self.description = description
        self.type = type
        self.command_content = command_content
        self.working_dir = working_dir
        self.timeout = timeout
        self.enable_parameter = enable_parameter
        self.timed = timed
        self.frequency = frequency
        self.parameters = parameters
        self.keep_command = keep_command
        self.content_encoding = content_encoding
        self.username = username
        self.windows_password_name = windows_password_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.type is not None:
            result['Type'] = self.type
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter
        if self.timed is not None:
            result['Timed'] = self.timed
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.keep_command is not None:
            result['KeepCommand'] = self.keep_command
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.username is not None:
            result['Username'] = self.username
        if self.windows_password_name is not None:
            result['WindowsPasswordName'] = self.windows_password_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')
        if m.get('Timed') is not None:
            self.timed = m.get('Timed')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('KeepCommand') is not None:
            self.keep_command = m.get('KeepCommand')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WindowsPasswordName') is not None:
            self.windows_password_name = m.get('WindowsPasswordName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RunCommandShrinkRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        name: str = None,
        description: str = None,
        type: str = None,
        command_content: str = None,
        working_dir: str = None,
        timeout: int = None,
        enable_parameter: bool = None,
        timed: bool = None,
        frequency: str = None,
        parameters_shrink: str = None,
        keep_command: bool = None,
        content_encoding: str = None,
        username: str = None,
        windows_password_name: str = None,
        instance_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.name = name
        self.description = description
        self.type = type
        self.command_content = command_content
        self.working_dir = working_dir
        self.timeout = timeout
        self.enable_parameter = enable_parameter
        self.timed = timed
        self.frequency = frequency
        self.parameters_shrink = parameters_shrink
        self.keep_command = keep_command
        self.content_encoding = content_encoding
        self.username = username
        self.windows_password_name = windows_password_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.type is not None:
            result['Type'] = self.type
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter
        if self.timed is not None:
            result['Timed'] = self.timed
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.keep_command is not None:
            result['KeepCommand'] = self.keep_command
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.username is not None:
            result['Username'] = self.username
        if self.windows_password_name is not None:
            result['WindowsPasswordName'] = self.windows_password_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')
        if m.get('Timed') is not None:
            self.timed = m.get('Timed')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('KeepCommand') is not None:
            self.keep_command = m.get('KeepCommand')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WindowsPasswordName') is not None:
            self.windows_password_name = m.get('WindowsPasswordName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RunCommandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        command_id: str = None,
        invoke_id: str = None,
    ):
        self.request_id = request_id
        self.command_id = command_id
        self.invoke_id = invoke_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        return self


class RunCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunCommandResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunInstancesRequestSystemDisk(TeaModel):
    def __init__(
        self,
        size: str = None,
        category: str = None,
        disk_name: str = None,
        description: str = None,
        performance_level: str = None,
        auto_snapshot_policy_id: str = None,
    ):
        self.size = size
        self.category = category
        self.disk_name = disk_name
        self.description = description
        self.performance_level = performance_level
        self.auto_snapshot_policy_id = auto_snapshot_policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        if self.category is not None:
            result['Category'] = self.category
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.description is not None:
            result['Description'] = self.description
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        return self


class RunInstancesRequestCpuOptions(TeaModel):
    def __init__(
        self,
        core: int = None,
        threads_per_core: int = None,
        numa: str = None,
    ):
        self.core = core
        self.threads_per_core = threads_per_core
        self.numa = numa

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.core is not None:
            result['Core'] = self.core
        if self.threads_per_core is not None:
            result['ThreadsPerCore'] = self.threads_per_core
        if self.numa is not None:
            result['Numa'] = self.numa
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')
        if m.get('ThreadsPerCore') is not None:
            self.threads_per_core = m.get('ThreadsPerCore')
        if m.get('Numa') is not None:
            self.numa = m.get('Numa')
        return self


class RunInstancesRequestPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        match_criteria: str = None,
        id: str = None,
    ):
        self.match_criteria = match_criteria
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class RunInstancesRequestSchedulerOptions(TeaModel):
    def __init__(
        self,
        dedicated_host_cluster_id: str = None,
    ):
        self.dedicated_host_cluster_id = dedicated_host_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')
        return self


class RunInstancesRequestDataDisk(TeaModel):
    def __init__(
        self,
        performance_level: str = None,
        auto_snapshot_policy_id: str = None,
        encrypted: str = None,
        description: str = None,
        snapshot_id: str = None,
        device: str = None,
        size: int = None,
        disk_name: str = None,
        category: str = None,
        encrypt_algorithm: str = None,
        delete_with_instance: bool = None,
        kmskey_id: str = None,
    ):
        self.performance_level = performance_level
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.encrypted = encrypted
        self.description = description
        self.snapshot_id = snapshot_id
        self.device = device
        self.size = size
        self.disk_name = disk_name
        self.category = category
        self.encrypt_algorithm = encrypt_algorithm
        self.delete_with_instance = delete_with_instance
        self.kmskey_id = kmskey_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.device is not None:
            result['Device'] = self.device
        if self.size is not None:
            result['Size'] = self.size
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.category is not None:
            result['Category'] = self.category
        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        return self


class RunInstancesRequestArn(TeaModel):
    def __init__(
        self,
        role_type: str = None,
        rolearn: str = None,
        assume_role_for: int = None,
    ):
        self.role_type = role_type
        self.rolearn = rolearn
        self.assume_role_for = assume_role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.rolearn is not None:
            result['Rolearn'] = self.rolearn
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('Rolearn') is not None:
            self.rolearn = m.get('Rolearn')
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')
        return self


class RunInstancesRequestNetworkInterface(TeaModel):
    def __init__(
        self,
        network_interface_name: str = None,
        v_switch_id: str = None,
        description: str = None,
        security_group_id: str = None,
        primary_ip_address: str = None,
        queue_number: int = None,
        security_group_ids: List[str] = None,
    ):
        self.network_interface_name = network_interface_name
        self.v_switch_id = v_switch_id
        self.description = description
        self.security_group_id = security_group_id
        self.primary_ip_address = primary_ip_address
        self.queue_number = queue_number
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.description is not None:
            result['Description'] = self.description
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address
        if self.queue_number is not None:
            result['QueueNumber'] = self.queue_number
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')
        if m.get('QueueNumber') is not None:
            self.queue_number = m.get('QueueNumber')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class RunInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class RunInstancesRequest(TeaModel):
    def __init__(
        self,
        system_disk: RunInstancesRequestSystemDisk = None,
        cpu_options: RunInstancesRequestCpuOptions = None,
        private_pool_options: RunInstancesRequestPrivatePoolOptions = None,
        scheduler_options: RunInstancesRequestSchedulerOptions = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        image_id: str = None,
        image_family: str = None,
        instance_type: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        instance_name: str = None,
        description: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        host_name: str = None,
        unique_suffix: bool = None,
        password: str = None,
        password_inherit: bool = None,
        zone_id: str = None,
        internet_charge_type: str = None,
        io_optimized: str = None,
        user_data: str = None,
        key_pair_name: str = None,
        ram_role_name: str = None,
        amount: int = None,
        min_amount: int = None,
        auto_release_time: str = None,
        spot_strategy: str = None,
        spot_duration: int = None,
        spot_price_limit: float = None,
        spot_interruption_behavior: str = None,
        security_enhancement_strategy: str = None,
        client_token: str = None,
        hpc_cluster_id: str = None,
        dry_run: bool = None,
        dedicated_host_id: str = None,
        launch_template_id: str = None,
        launch_template_name: str = None,
        launch_template_version: int = None,
        resource_group_id: str = None,
        period: int = None,
        period_unit: str = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        instance_charge_type: str = None,
        deployment_set_id: str = None,
        deployment_set_group_no: int = None,
        private_ip_address: str = None,
        credit_specification: str = None,
        ipv_6address_count: int = None,
        network_interface_queue_number: int = None,
        deletion_protection: bool = None,
        affinity: str = None,
        tenancy: str = None,
        storage_set_id: str = None,
        storage_set_partition_number: int = None,
        http_endpoint: str = None,
        http_tokens: str = None,
        http_put_response_hop_limit: int = None,
        isp: str = None,
        security_group_ids: List[str] = None,
        data_disk: List[RunInstancesRequestDataDisk] = None,
        arn: List[RunInstancesRequestArn] = None,
        network_interface: List[RunInstancesRequestNetworkInterface] = None,
        tag: List[RunInstancesRequestTag] = None,
        ipv_6address: List[str] = None,
    ):
        self.system_disk = system_disk
        self.cpu_options = cpu_options
        self.private_pool_options = private_pool_options
        self.scheduler_options = scheduler_options
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.image_id = image_id
        self.image_family = image_family
        self.instance_type = instance_type
        self.security_group_id = security_group_id
        self.v_switch_id = v_switch_id
        self.instance_name = instance_name
        self.description = description
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.host_name = host_name
        self.unique_suffix = unique_suffix
        self.password = password
        self.password_inherit = password_inherit
        self.zone_id = zone_id
        self.internet_charge_type = internet_charge_type
        self.io_optimized = io_optimized
        self.user_data = user_data
        self.key_pair_name = key_pair_name
        self.ram_role_name = ram_role_name
        self.amount = amount
        self.min_amount = min_amount
        self.auto_release_time = auto_release_time
        self.spot_strategy = spot_strategy
        self.spot_duration = spot_duration
        self.spot_price_limit = spot_price_limit
        self.spot_interruption_behavior = spot_interruption_behavior
        self.security_enhancement_strategy = security_enhancement_strategy
        self.client_token = client_token
        self.hpc_cluster_id = hpc_cluster_id
        self.dry_run = dry_run
        self.dedicated_host_id = dedicated_host_id
        self.launch_template_id = launch_template_id
        self.launch_template_name = launch_template_name
        self.launch_template_version = launch_template_version
        self.resource_group_id = resource_group_id
        self.period = period
        self.period_unit = period_unit
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.instance_charge_type = instance_charge_type
        self.deployment_set_id = deployment_set_id
        self.deployment_set_group_no = deployment_set_group_no
        self.private_ip_address = private_ip_address
        self.credit_specification = credit_specification
        self.ipv_6address_count = ipv_6address_count
        self.network_interface_queue_number = network_interface_queue_number
        self.deletion_protection = deletion_protection
        self.affinity = affinity
        self.tenancy = tenancy
        self.storage_set_id = storage_set_id
        self.storage_set_partition_number = storage_set_partition_number
        self.http_endpoint = http_endpoint
        self.http_tokens = http_tokens
        self.http_put_response_hop_limit = http_put_response_hop_limit
        self.isp = isp
        self.security_group_ids = security_group_ids
        self.data_disk = data_disk
        self.arn = arn
        self.network_interface = network_interface
        self.tag = tag
        self.ipv_6address = ipv_6address

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()
        if self.cpu_options:
            self.cpu_options.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.scheduler_options:
            self.scheduler_options.validate()
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.arn:
            for k in self.arn:
                if k:
                    k.validate()
        if self.network_interface:
            for k in self.network_interface:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.cpu_options is not None:
            result['CpuOptions'] = self.cpu_options.to_map()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.description is not None:
            result['Description'] = self.description
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.unique_suffix is not None:
            result['UniqueSuffix'] = self.unique_suffix
        if self.password is not None:
            result['Password'] = self.password
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.min_amount is not None:
            result['MinAmount'] = self.min_amount
        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior
        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_name is not None:
            result['LaunchTemplateName'] = self.launch_template_name
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.deployment_set_group_no is not None:
            result['DeploymentSetGroupNo'] = self.deployment_set_group_no
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.network_interface_queue_number is not None:
            result['NetworkInterfaceQueueNumber'] = self.network_interface_queue_number
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id
        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number
        if self.http_endpoint is not None:
            result['HttpEndpoint'] = self.http_endpoint
        if self.http_tokens is not None:
            result['HttpTokens'] = self.http_tokens
        if self.http_put_response_hop_limit is not None:
            result['HttpPutResponseHopLimit'] = self.http_put_response_hop_limit
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        result['Arn'] = []
        if self.arn is not None:
            for k in self.arn:
                result['Arn'].append(k.to_map() if k else None)
        result['NetworkInterface'] = []
        if self.network_interface is not None:
            for k in self.network_interface:
                result['NetworkInterface'].append(k.to_map() if k else None)
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = RunInstancesRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('CpuOptions') is not None:
            temp_model = RunInstancesRequestCpuOptions()
            self.cpu_options = temp_model.from_map(m['CpuOptions'])
        if m.get('PrivatePoolOptions') is not None:
            temp_model = RunInstancesRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('SchedulerOptions') is not None:
            temp_model = RunInstancesRequestSchedulerOptions()
            self.scheduler_options = temp_model.from_map(m['SchedulerOptions'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('UniqueSuffix') is not None:
            self.unique_suffix = m.get('UniqueSuffix')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('MinAmount') is not None:
            self.min_amount = m.get('MinAmount')
        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')
        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateName') is not None:
            self.launch_template_name = m.get('LaunchTemplateName')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('DeploymentSetGroupNo') is not None:
            self.deployment_set_group_no = m.get('DeploymentSetGroupNo')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('NetworkInterfaceQueueNumber') is not None:
            self.network_interface_queue_number = m.get('NetworkInterfaceQueueNumber')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')
        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')
        if m.get('HttpEndpoint') is not None:
            self.http_endpoint = m.get('HttpEndpoint')
        if m.get('HttpTokens') is not None:
            self.http_tokens = m.get('HttpTokens')
        if m.get('HttpPutResponseHopLimit') is not None:
            self.http_put_response_hop_limit = m.get('HttpPutResponseHopLimit')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = RunInstancesRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        self.arn = []
        if m.get('Arn') is not None:
            for k in m.get('Arn'):
                temp_model = RunInstancesRequestArn()
                self.arn.append(temp_model.from_map(k))
        self.network_interface = []
        if m.get('NetworkInterface') is not None:
            for k in m.get('NetworkInterface'):
                temp_model = RunInstancesRequestNetworkInterface()
                self.network_interface.append(temp_model.from_map(k))
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = RunInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')
        return self


class RunInstancesResponseBodyInstanceIdSets(TeaModel):
    def __init__(
        self,
        instance_id_set: List[str] = None,
    ):
        self.instance_id_set = instance_id_set

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id_set is not None:
            result['InstanceIdSet'] = self.instance_id_set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdSet') is not None:
            self.instance_id_set = m.get('InstanceIdSet')
        return self


class RunInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id_sets: RunInstancesResponseBodyInstanceIdSets = None,
        order_id: str = None,
        trade_price: float = None,
    ):
        self.request_id = request_id
        self.instance_id_sets = instance_id_sets
        self.order_id = order_id
        self.trade_price = trade_price

    def validate(self):
        if self.instance_id_sets:
            self.instance_id_sets.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id_sets is not None:
            result['InstanceIdSets'] = self.instance_id_sets.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceIdSets') is not None:
            temp_model = RunInstancesResponseBodyInstanceIdSets()
            self.instance_id_sets = temp_model.from_map(m['InstanceIdSets'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class RunInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendFileRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        name: str = None,
        description: str = None,
        timeout: int = None,
        target_dir: str = None,
        content_type: str = None,
        content: str = None,
        file_owner: str = None,
        file_group: str = None,
        file_mode: str = None,
        overwrite: bool = None,
        instance_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.name = name
        self.description = description
        self.timeout = timeout
        self.target_dir = target_dir
        self.content_type = content_type
        self.content = content
        self.file_owner = file_owner
        self.file_group = file_group
        self.file_mode = file_mode
        self.overwrite = overwrite
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.target_dir is not None:
            result['TargetDir'] = self.target_dir
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content is not None:
            result['Content'] = self.content
        if self.file_owner is not None:
            result['FileOwner'] = self.file_owner
        if self.file_group is not None:
            result['FileGroup'] = self.file_group
        if self.file_mode is not None:
            result['FileMode'] = self.file_mode
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TargetDir') is not None:
            self.target_dir = m.get('TargetDir')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileOwner') is not None:
            self.file_owner = m.get('FileOwner')
        if m.get('FileGroup') is not None:
            self.file_group = m.get('FileGroup')
        if m.get('FileMode') is not None:
            self.file_mode = m.get('FileMode')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class SendFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        invoke_id: str = None,
    ):
        self.request_id = request_id
        self.invoke_id = invoke_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        return self


class SendFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SendFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartElasticityAssuranceRequestPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StartElasticityAssuranceRequest(TeaModel):
    def __init__(
        self,
        private_pool_options: StartElasticityAssuranceRequestPrivatePoolOptions = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
    ):
        self.private_pool_options = private_pool_options
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()

    def to_map(self):
        result = dict()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = StartElasticityAssuranceRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartElasticityAssuranceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartElasticityAssuranceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartElasticityAssuranceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartElasticityAssuranceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartImagePipelineExecutionRequestTemplateTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class StartImagePipelineExecutionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        template_tag: List[StartImagePipelineExecutionRequestTemplateTag] = None,
        image_pipeline_id: str = None,
        client_token: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.template_tag = template_tag
        self.image_pipeline_id = image_pipeline_id
        self.client_token = client_token

    def validate(self):
        if self.template_tag:
            for k in self.template_tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['TemplateTag'] = []
        if self.template_tag is not None:
            for k in self.template_tag:
                result['TemplateTag'].append(k.to_map() if k else None)
        if self.image_pipeline_id is not None:
            result['ImagePipelineId'] = self.image_pipeline_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.template_tag = []
        if m.get('TemplateTag') is not None:
            for k in m.get('TemplateTag'):
                temp_model = StartImagePipelineExecutionRequestTemplateTag()
                self.template_tag.append(temp_model.from_map(k))
        if m.get('ImagePipelineId') is not None:
            self.image_pipeline_id = m.get('ImagePipelineId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class StartImagePipelineExecutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        execution_id: str = None,
    ):
        self.request_id = request_id
        self.execution_id = execution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        return self


class StartImagePipelineExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartImagePipelineExecutionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartImagePipelineExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        source_region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        init_local_disk: bool = None,
        owner_account: str = None,
        dry_run: bool = None,
    ):
        self.source_region_id = source_region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.init_local_disk = init_local_disk
        self.owner_account = owner_account
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.init_local_disk is not None:
            result['InitLocalDisk'] = self.init_local_disk
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InitLocalDisk') is not None:
            self.init_local_disk = m.get('InitLocalDisk')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstancesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        dry_run: bool = None,
        region_id: str = None,
        batch_optimization: str = None,
        instance_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.dry_run = dry_run
        self.region_id = region_id
        self.batch_optimization = batch_optimization
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.batch_optimization is not None:
            result['BatchOptimization'] = self.batch_optimization
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BatchOptimization') is not None:
            self.batch_optimization = m.get('BatchOptimization')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StartInstancesResponseBodyInstanceResponsesInstanceResponse(TeaModel):
    def __init__(
        self,
        current_status: str = None,
        previous_status: str = None,
        code: str = None,
        message: str = None,
        instance_id: str = None,
    ):
        self.current_status = current_status
        self.previous_status = previous_status
        self.code = code
        self.message = message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status
        if self.previous_status is not None:
            result['PreviousStatus'] = self.previous_status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')
        if m.get('PreviousStatus') is not None:
            self.previous_status = m.get('PreviousStatus')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StartInstancesResponseBodyInstanceResponses(TeaModel):
    def __init__(
        self,
        instance_response: List[StartInstancesResponseBodyInstanceResponsesInstanceResponse] = None,
    ):
        self.instance_response = instance_response

    def validate(self):
        if self.instance_response:
            for k in self.instance_response:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceResponse'] = []
        if self.instance_response is not None:
            for k in self.instance_response:
                result['InstanceResponse'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_response = []
        if m.get('InstanceResponse') is not None:
            for k in m.get('InstanceResponse'):
                temp_model = StartInstancesResponseBodyInstanceResponsesInstanceResponse()
                self.instance_response.append(temp_model.from_map(k))
        return self


class StartInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_responses: StartInstancesResponseBodyInstanceResponses = None,
    ):
        self.request_id = request_id
        self.instance_responses = instance_responses

    def validate(self):
        if self.instance_responses:
            self.instance_responses.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_responses is not None:
            result['InstanceResponses'] = self.instance_responses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceResponses') is not None:
            temp_model = StartInstancesResponseBodyInstanceResponses()
            self.instance_responses = temp_model.from_map(m['InstanceResponses'])
        return self


class StartInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        instance_id: str = None,
        confirm_stop: bool = None,
        force_stop: bool = None,
        owner_account: str = None,
        stopped_mode: str = None,
        dry_run: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.instance_id = instance_id
        self.confirm_stop = confirm_stop
        self.force_stop = force_stop
        self.owner_account = owner_account
        self.stopped_mode = stopped_mode
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.confirm_stop is not None:
            result['ConfirmStop'] = self.confirm_stop
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConfirmStop') is not None:
            self.confirm_stop = m.get('ConfirmStop')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstancesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        dry_run: bool = None,
        region_id: str = None,
        force_stop: bool = None,
        stopped_mode: str = None,
        batch_optimization: str = None,
        instance_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.dry_run = dry_run
        self.region_id = region_id
        self.force_stop = force_stop
        self.stopped_mode = stopped_mode
        self.batch_optimization = batch_optimization
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode
        if self.batch_optimization is not None:
            result['BatchOptimization'] = self.batch_optimization
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')
        if m.get('BatchOptimization') is not None:
            self.batch_optimization = m.get('BatchOptimization')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StopInstancesResponseBodyInstanceResponsesInstanceResponse(TeaModel):
    def __init__(
        self,
        current_status: str = None,
        previous_status: str = None,
        code: str = None,
        message: str = None,
        instance_id: str = None,
    ):
        self.current_status = current_status
        self.previous_status = previous_status
        self.code = code
        self.message = message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status
        if self.previous_status is not None:
            result['PreviousStatus'] = self.previous_status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')
        if m.get('PreviousStatus') is not None:
            self.previous_status = m.get('PreviousStatus')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StopInstancesResponseBodyInstanceResponses(TeaModel):
    def __init__(
        self,
        instance_response: List[StopInstancesResponseBodyInstanceResponsesInstanceResponse] = None,
    ):
        self.instance_response = instance_response

    def validate(self):
        if self.instance_response:
            for k in self.instance_response:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceResponse'] = []
        if self.instance_response is not None:
            for k in self.instance_response:
                result['InstanceResponse'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_response = []
        if m.get('InstanceResponse') is not None:
            for k in m.get('InstanceResponse'):
                temp_model = StopInstancesResponseBodyInstanceResponsesInstanceResponse()
                self.instance_response.append(temp_model.from_map(k))
        return self


class StopInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_responses: StopInstancesResponseBodyInstanceResponses = None,
    ):
        self.request_id = request_id
        self.instance_responses = instance_responses

    def validate(self):
        if self.instance_responses:
            self.instance_responses.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_responses is not None:
            result['InstanceResponses'] = self.instance_responses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceResponses') is not None:
            temp_model = StopInstancesResponseBodyInstanceResponses()
            self.instance_responses = temp_model.from_map(m['InstanceResponses'])
        return self


class StopInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInvocationRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        invoke_id: str = None,
        instance_id: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.invoke_id = invoke_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StopInvocationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInvocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopInvocationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopInvocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        owner_account: str = None,
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.owner_account = owner_account
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminatePhysicalConnectionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        physical_connection_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        owner_account: str = None,
        user_cidr: str = None,
    ):
        self.region_id = region_id
        self.physical_connection_id = physical_connection_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.owner_account = owner_account
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class TerminatePhysicalConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TerminatePhysicalConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TerminatePhysicalConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TerminatePhysicalConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateVirtualBorderRouterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vbr_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        owner_account: str = None,
        user_cidr: str = None,
    ):
        self.region_id = region_id
        self.vbr_id = vbr_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.owner_account = owner_account
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class TerminateVirtualBorderRouterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TerminateVirtualBorderRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TerminateVirtualBorderRouterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TerminateVirtualBorderRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassignIpv6AddressesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        network_interface_id: str = None,
        ipv_6address: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.network_interface_id = network_interface_id
        self.ipv_6address = ipv_6address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')
        return self


class UnassignIpv6AddressesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnassignIpv6AddressesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnassignIpv6AddressesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnassignIpv6AddressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassignPrivateIpAddressesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        network_interface_id: str = None,
        private_ip_address: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.network_interface_id = network_interface_id
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class UnassignPrivateIpAddressesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnassignPrivateIpAddressesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnassignPrivateIpAddressesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnassignPrivateIpAddressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassociateEipAddressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        allocation_id: str = None,
        instance_id: str = None,
        owner_account: str = None,
        instance_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.allocation_id = allocation_id
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class UnassociateEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnassociateEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnassociateEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnassociateEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassociateHaVipRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        client_token: str = None,
        region_id: str = None,
        ha_vip_id: str = None,
        instance_id: str = None,
        force: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.client_token = client_token
        self.region_id = region_id
        self.ha_vip_id = ha_vip_id
        self.instance_id = instance_id
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ha_vip_id is not None:
            result['HaVipId'] = self.ha_vip_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HaVipId') is not None:
            self.ha_vip_id = m.get('HaVipId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class UnassociateHaVipResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnassociateHaVipResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnassociateHaVipResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnassociateHaVipResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


