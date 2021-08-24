# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
print("0")
from typing import Dict
print("1")
from alibabacloud_tea_openapi.client import Client as OpenApiClient
print("2")
from alibabacloud_tea_openapi import models as open_api_models
print("3")
from alibabacloud_tea_util.client import Client as UtilClient
print("4")
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
print("5")
from alibabacloud_tea_util import models as util_models
print("7")
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
print("8")
#from alibabacloud_ecs20140526 import models as ecs_20140526_models
from chalicelib import alibabacloud_ecs20140526_models as ecs_20140526_models
print("6")



class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'ecs-cn-hangzhou.aliyuncs.com',
            'ap-southeast-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'us-west-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'us-east-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-finance-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-north-2-gov-1': 'ecs.aliyuncs.com',
            'ap-northeast-2-pop': 'ecs.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'ecs.aliyuncs.com',
            'cn-beijing-finance-pop': 'ecs.aliyuncs.com',
            'cn-beijing-gov-1': 'ecs.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-edge-1': 'ecs.cn-qingdao-nebula.aliyuncs.com',
            'cn-fujian': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-finance': 'ecs.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-test-306': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ecs.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-inner': 'ecs.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-inner': 'ecs.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-wuhan': 'ecs.aliyuncs.com',
            'cn-yushanfang': 'ecs.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ecs.cn-zhangjiakou.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ecs.cn-qingdao-nebula.aliyuncs.com',
            'eu-west-1-oxs': 'ecs.cn-shenzhen-cloudstone.aliyuncs.com',
            'rus-west-1-pop': 'ecs.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ecs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_inquired_system_event_with_options(
        self,
        request: ecs_20140526_models.AcceptInquiredSystemEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AcceptInquiredSystemEventResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AcceptInquiredSystemEventResponse().from_map(
            self.do_rpcrequest('AcceptInquiredSystemEvent', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def accept_inquired_system_event_with_options_async(
        self,
        request: ecs_20140526_models.AcceptInquiredSystemEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AcceptInquiredSystemEventResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AcceptInquiredSystemEventResponse().from_map(
            await self.do_rpcrequest_async('AcceptInquiredSystemEvent', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def accept_inquired_system_event(
        self,
        request: ecs_20140526_models.AcceptInquiredSystemEventRequest,
    ) -> ecs_20140526_models.AcceptInquiredSystemEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_inquired_system_event_with_options(request, runtime)

    async def accept_inquired_system_event_async(
        self,
        request: ecs_20140526_models.AcceptInquiredSystemEventRequest,
    ) -> ecs_20140526_models.AcceptInquiredSystemEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_inquired_system_event_with_options_async(request, runtime)

    def activate_router_interface_with_options(
        self,
        request: ecs_20140526_models.ActivateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ActivateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ActivateRouterInterfaceResponse().from_map(
            self.do_rpcrequest('ActivateRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def activate_router_interface_with_options_async(
        self,
        request: ecs_20140526_models.ActivateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ActivateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ActivateRouterInterfaceResponse().from_map(
            await self.do_rpcrequest_async('ActivateRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def activate_router_interface(
        self,
        request: ecs_20140526_models.ActivateRouterInterfaceRequest,
    ) -> ecs_20140526_models.ActivateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_router_interface_with_options(request, runtime)

    async def activate_router_interface_async(
        self,
        request: ecs_20140526_models.ActivateRouterInterfaceRequest,
    ) -> ecs_20140526_models.ActivateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_router_interface_with_options_async(request, runtime)

    def add_bandwidth_package_ips_with_options(
        self,
        request: ecs_20140526_models.AddBandwidthPackageIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AddBandwidthPackageIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AddBandwidthPackageIpsResponse().from_map(
            self.do_rpcrequest('AddBandwidthPackageIps', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_bandwidth_package_ips_with_options_async(
        self,
        request: ecs_20140526_models.AddBandwidthPackageIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AddBandwidthPackageIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AddBandwidthPackageIpsResponse().from_map(
            await self.do_rpcrequest_async('AddBandwidthPackageIps', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_bandwidth_package_ips(
        self,
        request: ecs_20140526_models.AddBandwidthPackageIpsRequest,
    ) -> ecs_20140526_models.AddBandwidthPackageIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_bandwidth_package_ips_with_options(request, runtime)

    async def add_bandwidth_package_ips_async(
        self,
        request: ecs_20140526_models.AddBandwidthPackageIpsRequest,
    ) -> ecs_20140526_models.AddBandwidthPackageIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_bandwidth_package_ips_with_options_async(request, runtime)

    def describe_spot_price_history_with_options(
        self,
        request: ecs_20140526_models.DescribeSpotPriceHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSpotPriceHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSpotPriceHistoryResponse().from_map(
            self.do_rpcrequest('DescribeSpotPriceHistory', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_spot_price_history_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSpotPriceHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSpotPriceHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSpotPriceHistoryResponse().from_map(
            await self.do_rpcrequest_async('DescribeSpotPriceHistory', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_spot_price_history(
        self,
        request: ecs_20140526_models.DescribeSpotPriceHistoryRequest,
    ) -> ecs_20140526_models.DescribeSpotPriceHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_spot_price_history_with_options(request, runtime)

    async def describe_spot_price_history_async(
        self,
        request: ecs_20140526_models.DescribeSpotPriceHistoryRequest,
    ) -> ecs_20140526_models.DescribeSpotPriceHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_spot_price_history_with_options_async(request, runtime)

    def describe_storage_capacity_units_with_options(
        self,
        request: ecs_20140526_models.DescribeStorageCapacityUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageCapacityUnitsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageCapacityUnitsResponse().from_map(
            self.do_rpcrequest('DescribeStorageCapacityUnits', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_storage_capacity_units_with_options_async(
        self,
        request: ecs_20140526_models.DescribeStorageCapacityUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageCapacityUnitsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageCapacityUnitsResponse().from_map(
            await self.do_rpcrequest_async('DescribeStorageCapacityUnits', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_storage_capacity_units(
        self,
        request: ecs_20140526_models.DescribeStorageCapacityUnitsRequest,
    ) -> ecs_20140526_models.DescribeStorageCapacityUnitsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_capacity_units_with_options(request, runtime)

    async def describe_storage_capacity_units_async(
        self,
        request: ecs_20140526_models.DescribeStorageCapacityUnitsRequest,
    ) -> ecs_20140526_models.DescribeStorageCapacityUnitsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_capacity_units_with_options_async(request, runtime)

    def describe_storage_set_details_with_options(
        self,
        request: ecs_20140526_models.DescribeStorageSetDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageSetDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageSetDetailsResponse().from_map(
            self.do_rpcrequest('DescribeStorageSetDetails', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_storage_set_details_with_options_async(
        self,
        request: ecs_20140526_models.DescribeStorageSetDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageSetDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageSetDetailsResponse().from_map(
            await self.do_rpcrequest_async('DescribeStorageSetDetails', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_storage_set_details(
        self,
        request: ecs_20140526_models.DescribeStorageSetDetailsRequest,
    ) -> ecs_20140526_models.DescribeStorageSetDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_set_details_with_options(request, runtime)

    async def describe_storage_set_details_async(
        self,
        request: ecs_20140526_models.DescribeStorageSetDetailsRequest,
    ) -> ecs_20140526_models.DescribeStorageSetDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_set_details_with_options_async(request, runtime)

    def describe_storage_sets_with_options(
        self,
        request: ecs_20140526_models.DescribeStorageSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageSetsResponse().from_map(
            self.do_rpcrequest('DescribeStorageSets', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_storage_sets_with_options_async(
        self,
        request: ecs_20140526_models.DescribeStorageSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageSetsResponse().from_map(
            await self.do_rpcrequest_async('DescribeStorageSets', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_storage_sets(
        self,
        request: ecs_20140526_models.DescribeStorageSetsRequest,
    ) -> ecs_20140526_models.DescribeStorageSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_sets_with_options(request, runtime)

    async def describe_storage_sets_async(
        self,
        request: ecs_20140526_models.DescribeStorageSetsRequest,
    ) -> ecs_20140526_models.DescribeStorageSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_sets_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: ecs_20140526_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTagsResponse().from_map(
            self.do_rpcrequest('DescribeTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: ecs_20140526_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tags(
        self,
        request: ecs_20140526_models.DescribeTagsRequest,
    ) -> ecs_20140526_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: ecs_20140526_models.DescribeTagsRequest,
    ) -> ecs_20140526_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_task_attribute_with_options(
        self,
        request: ecs_20140526_models.DescribeTaskAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTaskAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTaskAttributeResponse().from_map(
            self.do_rpcrequest('DescribeTaskAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_task_attribute_with_options_async(
        self,
        request: ecs_20140526_models.DescribeTaskAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTaskAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTaskAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeTaskAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_task_attribute(
        self,
        request: ecs_20140526_models.DescribeTaskAttributeRequest,
    ) -> ecs_20140526_models.DescribeTaskAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_task_attribute_with_options(request, runtime)

    async def describe_task_attribute_async(
        self,
        request: ecs_20140526_models.DescribeTaskAttributeRequest,
    ) -> ecs_20140526_models.DescribeTaskAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_task_attribute_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: ecs_20140526_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTasksResponse().from_map(
            self.do_rpcrequest('DescribeTasks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: ecs_20140526_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeTasks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tasks(
        self,
        request: ecs_20140526_models.DescribeTasksRequest,
    ) -> ecs_20140526_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: ecs_20140526_models.DescribeTasksRequest,
    ) -> ecs_20140526_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def describe_user_business_behavior_with_options(
        self,
        request: ecs_20140526_models.DescribeUserBusinessBehaviorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeUserBusinessBehaviorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeUserBusinessBehaviorResponse().from_map(
            self.do_rpcrequest('DescribeUserBusinessBehavior', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_business_behavior_with_options_async(
        self,
        request: ecs_20140526_models.DescribeUserBusinessBehaviorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeUserBusinessBehaviorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeUserBusinessBehaviorResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserBusinessBehavior', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_business_behavior(
        self,
        request: ecs_20140526_models.DescribeUserBusinessBehaviorRequest,
    ) -> ecs_20140526_models.DescribeUserBusinessBehaviorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_business_behavior_with_options(request, runtime)

    async def describe_user_business_behavior_async(
        self,
        request: ecs_20140526_models.DescribeUserBusinessBehaviorRequest,
    ) -> ecs_20140526_models.DescribeUserBusinessBehaviorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_business_behavior_with_options_async(request, runtime)

    def describe_user_data_with_options(
        self,
        request: ecs_20140526_models.DescribeUserDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeUserDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeUserDataResponse().from_map(
            self.do_rpcrequest('DescribeUserData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_data_with_options_async(
        self,
        request: ecs_20140526_models.DescribeUserDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeUserDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeUserDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_data(
        self,
        request: ecs_20140526_models.DescribeUserDataRequest,
    ) -> ecs_20140526_models.DescribeUserDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_data_with_options(request, runtime)

    async def describe_user_data_async(
        self,
        request: ecs_20140526_models.DescribeUserDataRequest,
    ) -> ecs_20140526_models.DescribeUserDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_data_with_options_async(request, runtime)

    def describe_virtual_border_routers_with_options(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVirtualBorderRoutersResponse().from_map(
            self.do_rpcrequest('DescribeVirtualBorderRouters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_virtual_border_routers_with_options_async(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVirtualBorderRoutersResponse().from_map(
            await self.do_rpcrequest_async('DescribeVirtualBorderRouters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_virtual_border_routers(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersRequest,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_border_routers_with_options(request, runtime)

    async def describe_virtual_border_routers_async(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersRequest,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_border_routers_with_options_async(request, runtime)

    def describe_virtual_border_routers_for_physical_connection_with_options(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse().from_map(
            self.do_rpcrequest('DescribeVirtualBorderRoutersForPhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_virtual_border_routers_for_physical_connection_with_options_async(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('DescribeVirtualBorderRoutersForPhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_virtual_border_routers_for_physical_connection(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_border_routers_for_physical_connection_with_options(request, runtime)

    async def describe_virtual_border_routers_for_physical_connection_async(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_border_routers_for_physical_connection_with_options_async(request, runtime)

    def describe_vpcs_with_options(
        self,
        request: ecs_20140526_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVpcsResponse().from_map(
            self.do_rpcrequest('DescribeVpcs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpcs_with_options_async(
        self,
        request: ecs_20140526_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVpcsResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpcs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpcs(
        self,
        request: ecs_20140526_models.DescribeVpcsRequest,
    ) -> ecs_20140526_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    async def describe_vpcs_async(
        self,
        request: ecs_20140526_models.DescribeVpcsRequest,
    ) -> ecs_20140526_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpcs_with_options_async(request, runtime)

    def describe_vrouters_with_options(
        self,
        request: ecs_20140526_models.DescribeVRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVRoutersResponse().from_map(
            self.do_rpcrequest('DescribeVRouters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vrouters_with_options_async(
        self,
        request: ecs_20140526_models.DescribeVRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVRoutersResponse().from_map(
            await self.do_rpcrequest_async('DescribeVRouters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vrouters(
        self,
        request: ecs_20140526_models.DescribeVRoutersRequest,
    ) -> ecs_20140526_models.DescribeVRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vrouters_with_options(request, runtime)

    async def describe_vrouters_async(
        self,
        request: ecs_20140526_models.DescribeVRoutersRequest,
    ) -> ecs_20140526_models.DescribeVRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vrouters_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: ecs_20140526_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVSwitchesResponse().from_map(
            self.do_rpcrequest('DescribeVSwitches', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: ecs_20140526_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVSwitchesResponse().from_map(
            await self.do_rpcrequest_async('DescribeVSwitches', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vswitches(
        self,
        request: ecs_20140526_models.DescribeVSwitchesRequest,
    ) -> ecs_20140526_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: ecs_20140526_models.DescribeVSwitchesRequest,
    ) -> ecs_20140526_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: ecs_20140526_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeZonesResponse().from_map(
            self.do_rpcrequest('DescribeZones', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: ecs_20140526_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeZonesResponse().from_map(
            await self.do_rpcrequest_async('DescribeZones', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(
        self,
        request: ecs_20140526_models.DescribeZonesRequest,
    ) -> ecs_20140526_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: ecs_20140526_models.DescribeZonesRequest,
    ) -> ecs_20140526_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_classic_link_vpc_with_options(
        self,
        request: ecs_20140526_models.DetachClassicLinkVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachClassicLinkVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachClassicLinkVpcResponse().from_map(
            self.do_rpcrequest('DetachClassicLinkVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_classic_link_vpc_with_options_async(
        self,
        request: ecs_20140526_models.DetachClassicLinkVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachClassicLinkVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachClassicLinkVpcResponse().from_map(
            await self.do_rpcrequest_async('DetachClassicLinkVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_classic_link_vpc(
        self,
        request: ecs_20140526_models.DetachClassicLinkVpcRequest,
    ) -> ecs_20140526_models.DetachClassicLinkVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_classic_link_vpc_with_options(request, runtime)

    async def detach_classic_link_vpc_async(
        self,
        request: ecs_20140526_models.DetachClassicLinkVpcRequest,
    ) -> ecs_20140526_models.DetachClassicLinkVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_classic_link_vpc_with_options_async(request, runtime)

    def detach_disk_with_options(
        self,
        request: ecs_20140526_models.DetachDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachDiskResponse().from_map(
            self.do_rpcrequest('DetachDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_disk_with_options_async(
        self,
        request: ecs_20140526_models.DetachDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachDiskResponse().from_map(
            await self.do_rpcrequest_async('DetachDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_disk(
        self,
        request: ecs_20140526_models.DetachDiskRequest,
    ) -> ecs_20140526_models.DetachDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_disk_with_options(request, runtime)

    async def detach_disk_async(
        self,
        request: ecs_20140526_models.DetachDiskRequest,
    ) -> ecs_20140526_models.DetachDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_disk_with_options_async(request, runtime)

    def detach_instance_ram_role_with_options(
        self,
        request: ecs_20140526_models.DetachInstanceRamRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachInstanceRamRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachInstanceRamRoleResponse().from_map(
            self.do_rpcrequest('DetachInstanceRamRole', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_instance_ram_role_with_options_async(
        self,
        request: ecs_20140526_models.DetachInstanceRamRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachInstanceRamRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachInstanceRamRoleResponse().from_map(
            await self.do_rpcrequest_async('DetachInstanceRamRole', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_instance_ram_role(
        self,
        request: ecs_20140526_models.DetachInstanceRamRoleRequest,
    ) -> ecs_20140526_models.DetachInstanceRamRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_instance_ram_role_with_options(request, runtime)

    async def detach_instance_ram_role_async(
        self,
        request: ecs_20140526_models.DetachInstanceRamRoleRequest,
    ) -> ecs_20140526_models.DetachInstanceRamRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_instance_ram_role_with_options_async(request, runtime)

    def detach_key_pair_with_options(
        self,
        request: ecs_20140526_models.DetachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachKeyPairResponse().from_map(
            self.do_rpcrequest('DetachKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_key_pair_with_options_async(
        self,
        request: ecs_20140526_models.DetachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachKeyPairResponse().from_map(
            await self.do_rpcrequest_async('DetachKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_key_pair(
        self,
        request: ecs_20140526_models.DetachKeyPairRequest,
    ) -> ecs_20140526_models.DetachKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_key_pair_with_options(request, runtime)

    async def detach_key_pair_async(
        self,
        request: ecs_20140526_models.DetachKeyPairRequest,
    ) -> ecs_20140526_models.DetachKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_key_pair_with_options_async(request, runtime)

    def detach_network_interface_with_options(
        self,
        request: ecs_20140526_models.DetachNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachNetworkInterfaceResponse().from_map(
            self.do_rpcrequest('DetachNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_network_interface_with_options_async(
        self,
        request: ecs_20140526_models.DetachNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachNetworkInterfaceResponse().from_map(
            await self.do_rpcrequest_async('DetachNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_network_interface(
        self,
        request: ecs_20140526_models.DetachNetworkInterfaceRequest,
    ) -> ecs_20140526_models.DetachNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_network_interface_with_options(request, runtime)

    async def detach_network_interface_async(
        self,
        request: ecs_20140526_models.DetachNetworkInterfaceRequest,
    ) -> ecs_20140526_models.DetachNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_network_interface_with_options_async(request, runtime)

    def disable_activation_with_options(
        self,
        request: ecs_20140526_models.DisableActivationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DisableActivationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DisableActivationResponse().from_map(
            self.do_rpcrequest('DisableActivation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_activation_with_options_async(
        self,
        request: ecs_20140526_models.DisableActivationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DisableActivationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DisableActivationResponse().from_map(
            await self.do_rpcrequest_async('DisableActivation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_activation(
        self,
        request: ecs_20140526_models.DisableActivationRequest,
    ) -> ecs_20140526_models.DisableActivationResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_activation_with_options(request, runtime)

    async def disable_activation_async(
        self,
        request: ecs_20140526_models.DisableActivationRequest,
    ) -> ecs_20140526_models.DisableActivationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_activation_with_options_async(request, runtime)

    def eip_fill_params_with_options(
        self,
        request: ecs_20140526_models.EipFillParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipFillParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipFillParamsResponse().from_map(
            self.do_rpcrequest('EipFillParams', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def eip_fill_params_with_options_async(
        self,
        request: ecs_20140526_models.EipFillParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipFillParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipFillParamsResponse().from_map(
            await self.do_rpcrequest_async('EipFillParams', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def eip_fill_params(
        self,
        request: ecs_20140526_models.EipFillParamsRequest,
    ) -> ecs_20140526_models.EipFillParamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.eip_fill_params_with_options(request, runtime)

    async def eip_fill_params_async(
        self,
        request: ecs_20140526_models.EipFillParamsRequest,
    ) -> ecs_20140526_models.EipFillParamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.eip_fill_params_with_options_async(request, runtime)

    def eip_fill_product_with_options(
        self,
        request: ecs_20140526_models.EipFillProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipFillProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipFillProductResponse().from_map(
            self.do_rpcrequest('EipFillProduct', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def eip_fill_product_with_options_async(
        self,
        request: ecs_20140526_models.EipFillProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipFillProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipFillProductResponse().from_map(
            await self.do_rpcrequest_async('EipFillProduct', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def eip_fill_product(
        self,
        request: ecs_20140526_models.EipFillProductRequest,
    ) -> ecs_20140526_models.EipFillProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.eip_fill_product_with_options(request, runtime)

    async def eip_fill_product_async(
        self,
        request: ecs_20140526_models.EipFillProductRequest,
    ) -> ecs_20140526_models.EipFillProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.eip_fill_product_with_options_async(request, runtime)

    def eip_notify_paid_with_options(
        self,
        request: ecs_20140526_models.EipNotifyPaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipNotifyPaidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipNotifyPaidResponse().from_map(
            self.do_rpcrequest('EipNotifyPaid', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def eip_notify_paid_with_options_async(
        self,
        request: ecs_20140526_models.EipNotifyPaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipNotifyPaidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipNotifyPaidResponse().from_map(
            await self.do_rpcrequest_async('EipNotifyPaid', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def eip_notify_paid(
        self,
        request: ecs_20140526_models.EipNotifyPaidRequest,
    ) -> ecs_20140526_models.EipNotifyPaidResponse:
        runtime = util_models.RuntimeOptions()
        return self.eip_notify_paid_with_options(request, runtime)

    async def eip_notify_paid_async(
        self,
        request: ecs_20140526_models.EipNotifyPaidRequest,
    ) -> ecs_20140526_models.EipNotifyPaidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.eip_notify_paid_with_options_async(request, runtime)

    def enable_physical_connection_with_options(
        self,
        request: ecs_20140526_models.EnablePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EnablePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EnablePhysicalConnectionResponse().from_map(
            self.do_rpcrequest('EnablePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_physical_connection_with_options_async(
        self,
        request: ecs_20140526_models.EnablePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EnablePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EnablePhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('EnablePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_physical_connection(
        self,
        request: ecs_20140526_models.EnablePhysicalConnectionRequest,
    ) -> ecs_20140526_models.EnablePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_physical_connection_with_options(request, runtime)

    async def enable_physical_connection_async(
        self,
        request: ecs_20140526_models.EnablePhysicalConnectionRequest,
    ) -> ecs_20140526_models.EnablePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_physical_connection_with_options_async(request, runtime)

    def export_image_with_options(
        self,
        request: ecs_20140526_models.ExportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ExportImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ExportImageResponse().from_map(
            self.do_rpcrequest('ExportImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_image_with_options_async(
        self,
        request: ecs_20140526_models.ExportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ExportImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ExportImageResponse().from_map(
            await self.do_rpcrequest_async('ExportImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_image(
        self,
        request: ecs_20140526_models.ExportImageRequest,
    ) -> ecs_20140526_models.ExportImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_image_with_options(request, runtime)

    async def export_image_async(
        self,
        request: ecs_20140526_models.ExportImageRequest,
    ) -> ecs_20140526_models.ExportImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_image_with_options_async(request, runtime)

    def export_snapshot_with_options(
        self,
        request: ecs_20140526_models.ExportSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ExportSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ExportSnapshotResponse().from_map(
            self.do_rpcrequest('ExportSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_snapshot_with_options_async(
        self,
        request: ecs_20140526_models.ExportSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ExportSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ExportSnapshotResponse().from_map(
            await self.do_rpcrequest_async('ExportSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_snapshot(
        self,
        request: ecs_20140526_models.ExportSnapshotRequest,
    ) -> ecs_20140526_models.ExportSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_snapshot_with_options(request, runtime)

    async def export_snapshot_async(
        self,
        request: ecs_20140526_models.ExportSnapshotRequest,
    ) -> ecs_20140526_models.ExportSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_snapshot_with_options_async(request, runtime)

    def get_instance_console_output_with_options(
        self,
        request: ecs_20140526_models.GetInstanceConsoleOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.GetInstanceConsoleOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.GetInstanceConsoleOutputResponse().from_map(
            self.do_rpcrequest('GetInstanceConsoleOutput', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_console_output_with_options_async(
        self,
        request: ecs_20140526_models.GetInstanceConsoleOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.GetInstanceConsoleOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.GetInstanceConsoleOutputResponse().from_map(
            await self.do_rpcrequest_async('GetInstanceConsoleOutput', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_console_output(
        self,
        request: ecs_20140526_models.GetInstanceConsoleOutputRequest,
    ) -> ecs_20140526_models.GetInstanceConsoleOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_console_output_with_options(request, runtime)

    async def get_instance_console_output_async(
        self,
        request: ecs_20140526_models.GetInstanceConsoleOutputRequest,
    ) -> ecs_20140526_models.GetInstanceConsoleOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_console_output_with_options_async(request, runtime)

    def get_instance_screenshot_with_options(
        self,
        request: ecs_20140526_models.GetInstanceScreenshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.GetInstanceScreenshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.GetInstanceScreenshotResponse().from_map(
            self.do_rpcrequest('GetInstanceScreenshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_screenshot_with_options_async(
        self,
        request: ecs_20140526_models.GetInstanceScreenshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.GetInstanceScreenshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.GetInstanceScreenshotResponse().from_map(
            await self.do_rpcrequest_async('GetInstanceScreenshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_screenshot(
        self,
        request: ecs_20140526_models.GetInstanceScreenshotRequest,
    ) -> ecs_20140526_models.GetInstanceScreenshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_screenshot_with_options(request, runtime)

    async def get_instance_screenshot_async(
        self,
        request: ecs_20140526_models.GetInstanceScreenshotRequest,
    ) -> ecs_20140526_models.GetInstanceScreenshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_screenshot_with_options_async(request, runtime)

    def import_image_with_options(
        self,
        request: ecs_20140526_models.ImportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportImageResponse().from_map(
            self.do_rpcrequest('ImportImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_image_with_options_async(
        self,
        request: ecs_20140526_models.ImportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportImageResponse().from_map(
            await self.do_rpcrequest_async('ImportImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_image(
        self,
        request: ecs_20140526_models.ImportImageRequest,
    ) -> ecs_20140526_models.ImportImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_image_with_options(request, runtime)

    async def import_image_async(
        self,
        request: ecs_20140526_models.ImportImageRequest,
    ) -> ecs_20140526_models.ImportImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_image_with_options_async(request, runtime)

    def import_key_pair_with_options(
        self,
        request: ecs_20140526_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportKeyPairResponse().from_map(
            self.do_rpcrequest('ImportKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_key_pair_with_options_async(
        self,
        request: ecs_20140526_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportKeyPairResponse().from_map(
            await self.do_rpcrequest_async('ImportKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_key_pair(
        self,
        request: ecs_20140526_models.ImportKeyPairRequest,
    ) -> ecs_20140526_models.ImportKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    async def import_key_pair_async(
        self,
        request: ecs_20140526_models.ImportKeyPairRequest,
    ) -> ecs_20140526_models.ImportKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_key_pair_with_options_async(request, runtime)

    def import_snapshot_with_options(
        self,
        request: ecs_20140526_models.ImportSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportSnapshotResponse().from_map(
            self.do_rpcrequest('ImportSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_snapshot_with_options_async(
        self,
        request: ecs_20140526_models.ImportSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportSnapshotResponse().from_map(
            await self.do_rpcrequest_async('ImportSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_snapshot(
        self,
        request: ecs_20140526_models.ImportSnapshotRequest,
    ) -> ecs_20140526_models.ImportSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_snapshot_with_options(request, runtime)

    async def import_snapshot_async(
        self,
        request: ecs_20140526_models.ImportSnapshotRequest,
    ) -> ecs_20140526_models.ImportSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_snapshot_with_options_async(request, runtime)

    def install_cloud_assistant_with_options(
        self,
        request: ecs_20140526_models.InstallCloudAssistantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.InstallCloudAssistantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.InstallCloudAssistantResponse().from_map(
            self.do_rpcrequest('InstallCloudAssistant', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def install_cloud_assistant_with_options_async(
        self,
        request: ecs_20140526_models.InstallCloudAssistantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.InstallCloudAssistantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.InstallCloudAssistantResponse().from_map(
            await self.do_rpcrequest_async('InstallCloudAssistant', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def install_cloud_assistant(
        self,
        request: ecs_20140526_models.InstallCloudAssistantRequest,
    ) -> ecs_20140526_models.InstallCloudAssistantResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_cloud_assistant_with_options(request, runtime)

    async def install_cloud_assistant_async(
        self,
        request: ecs_20140526_models.InstallCloudAssistantRequest,
    ) -> ecs_20140526_models.InstallCloudAssistantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_cloud_assistant_with_options_async(request, runtime)

    def invoke_command_with_options(
        self,
        tmp_req: ecs_20140526_models.InvokeCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.InvokeCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = ecs_20140526_models.InvokeCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.InvokeCommandResponse().from_map(
            self.do_rpcrequest('InvokeCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invoke_command_with_options_async(
        self,
        tmp_req: ecs_20140526_models.InvokeCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.InvokeCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = ecs_20140526_models.InvokeCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.InvokeCommandResponse().from_map(
            await self.do_rpcrequest_async('InvokeCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invoke_command(
        self,
        request: ecs_20140526_models.InvokeCommandRequest,
    ) -> ecs_20140526_models.InvokeCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.invoke_command_with_options(request, runtime)

    async def invoke_command_async(
        self,
        request: ecs_20140526_models.InvokeCommandRequest,
    ) -> ecs_20140526_models.InvokeCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invoke_command_with_options_async(request, runtime)

    def join_resource_group_with_options(
        self,
        request: ecs_20140526_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.JoinResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.JoinResourceGroupResponse().from_map(
            self.do_rpcrequest('JoinResourceGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_resource_group_with_options_async(
        self,
        request: ecs_20140526_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.JoinResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.JoinResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('JoinResourceGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_resource_group(
        self,
        request: ecs_20140526_models.JoinResourceGroupRequest,
    ) -> ecs_20140526_models.JoinResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_resource_group_with_options(request, runtime)

    async def join_resource_group_async(
        self,
        request: ecs_20140526_models.JoinResourceGroupRequest,
    ) -> ecs_20140526_models.JoinResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_resource_group_with_options_async(request, runtime)

    def join_security_group_with_options(
        self,
        request: ecs_20140526_models.JoinSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.JoinSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.JoinSecurityGroupResponse().from_map(
            self.do_rpcrequest('JoinSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_security_group_with_options_async(
        self,
        request: ecs_20140526_models.JoinSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.JoinSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.JoinSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('JoinSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_security_group(
        self,
        request: ecs_20140526_models.JoinSecurityGroupRequest,
    ) -> ecs_20140526_models.JoinSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_security_group_with_options(request, runtime)

    async def join_security_group_async(
        self,
        request: ecs_20140526_models.JoinSecurityGroupRequest,
    ) -> ecs_20140526_models.JoinSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_security_group_with_options_async(request, runtime)

    def leave_security_group_with_options(
        self,
        request: ecs_20140526_models.LeaveSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.LeaveSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.LeaveSecurityGroupResponse().from_map(
            self.do_rpcrequest('LeaveSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def leave_security_group_with_options_async(
        self,
        request: ecs_20140526_models.LeaveSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.LeaveSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.LeaveSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('LeaveSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def leave_security_group(
        self,
        request: ecs_20140526_models.LeaveSecurityGroupRequest,
    ) -> ecs_20140526_models.LeaveSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.leave_security_group_with_options(request, runtime)

    async def leave_security_group_async(
        self,
        request: ecs_20140526_models.LeaveSecurityGroupRequest,
    ) -> ecs_20140526_models.LeaveSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.leave_security_group_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ecs_20140526_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ecs_20140526_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: ecs_20140526_models.ListTagResourcesRequest,
    ) -> ecs_20140526_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ecs_20140526_models.ListTagResourcesRequest,
    ) -> ecs_20140526_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_auto_provisioning_group_with_options(
        self,
        request: ecs_20140526_models.ModifyAutoProvisioningGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoProvisioningGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoProvisioningGroupResponse().from_map(
            self.do_rpcrequest('ModifyAutoProvisioningGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_auto_provisioning_group_with_options_async(
        self,
        request: ecs_20140526_models.ModifyAutoProvisioningGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoProvisioningGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoProvisioningGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyAutoProvisioningGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_provisioning_group(
        self,
        request: ecs_20140526_models.ModifyAutoProvisioningGroupRequest,
    ) -> ecs_20140526_models.ModifyAutoProvisioningGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_provisioning_group_with_options(request, runtime)

    async def modify_auto_provisioning_group_async(
        self,
        request: ecs_20140526_models.ModifyAutoProvisioningGroupRequest,
    ) -> ecs_20140526_models.ModifyAutoProvisioningGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_provisioning_group_with_options_async(request, runtime)

    def modify_auto_snapshot_policy_with_options(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoSnapshotPolicyResponse().from_map(
            self.do_rpcrequest('ModifyAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_auto_snapshot_policy_with_options_async(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoSnapshotPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_snapshot_policy(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_with_options(request, runtime)

    async def modify_auto_snapshot_policy_async(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_snapshot_policy_with_options_async(request, runtime)

    def modify_auto_snapshot_policy_ex_with_options(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse().from_map(
            self.do_rpcrequest('ModifyAutoSnapshotPolicyEx', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_auto_snapshot_policy_ex_with_options_async(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse().from_map(
            await self.do_rpcrequest_async('ModifyAutoSnapshotPolicyEx', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_snapshot_policy_ex(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyExRequest,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_ex_with_options(request, runtime)

    async def modify_auto_snapshot_policy_ex_async(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyExRequest,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_snapshot_policy_ex_with_options_async(request, runtime)

    def modify_bandwidth_package_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyBandwidthPackageSpecResponse().from_map(
            self.do_rpcrequest('ModifyBandwidthPackageSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_bandwidth_package_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyBandwidthPackageSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyBandwidthPackageSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_bandwidth_package_spec(
        self,
        request: ecs_20140526_models.ModifyBandwidthPackageSpecRequest,
    ) -> ecs_20140526_models.ModifyBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_bandwidth_package_spec_with_options(request, runtime)

    async def modify_bandwidth_package_spec_async(
        self,
        request: ecs_20140526_models.ModifyBandwidthPackageSpecRequest,
    ) -> ecs_20140526_models.ModifyBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_bandwidth_package_spec_with_options_async(request, runtime)

    def modify_capacity_reservation_with_options(
        self,
        request: ecs_20140526_models.ModifyCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyCapacityReservationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyCapacityReservationResponse().from_map(
            self.do_rpcrequest('ModifyCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_capacity_reservation_with_options_async(
        self,
        request: ecs_20140526_models.ModifyCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyCapacityReservationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyCapacityReservationResponse().from_map(
            await self.do_rpcrequest_async('ModifyCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_capacity_reservation(
        self,
        request: ecs_20140526_models.ModifyCapacityReservationRequest,
    ) -> ecs_20140526_models.ModifyCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_capacity_reservation_with_options(request, runtime)

    async def modify_capacity_reservation_async(
        self,
        request: ecs_20140526_models.ModifyCapacityReservationRequest,
    ) -> ecs_20140526_models.ModifyCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_capacity_reservation_with_options_async(request, runtime)

    def modify_command_with_options(
        self,
        request: ecs_20140526_models.ModifyCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyCommandResponse().from_map(
            self.do_rpcrequest('ModifyCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_command_with_options_async(
        self,
        request: ecs_20140526_models.ModifyCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyCommandResponse().from_map(
            await self.do_rpcrequest_async('ModifyCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_command(
        self,
        request: ecs_20140526_models.ModifyCommandRequest,
    ) -> ecs_20140526_models.ModifyCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_command_with_options(request, runtime)

    async def modify_command_async(
        self,
        request: ecs_20140526_models.ModifyCommandRequest,
    ) -> ecs_20140526_models.ModifyCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_command_with_options_async(request, runtime)

    def modify_dedicated_host_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_attribute(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    async def modify_dedicated_host_attribute_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_auto_release_time_with_options(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostAutoReleaseTime', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_auto_release_time_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostAutoReleaseTime', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_auto_release_time(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_auto_release_time_with_options(request, runtime)

    async def modify_dedicated_host_auto_release_time_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_auto_release_time_with_options_async(request, runtime)

    def modify_dedicated_host_auto_renew_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_auto_renew_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_auto_renew_attribute(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_auto_renew_attribute_with_options(request, runtime)

    async def modify_dedicated_host_auto_renew_attribute_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_auto_renew_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_cluster_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostClusterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_cluster_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostClusterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_cluster_attribute(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostClusterAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_cluster_attribute_with_options(request, runtime)

    async def modify_dedicated_host_cluster_attribute_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostClusterAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_cluster_attribute_with_options_async(request, runtime)

    def modify_dedicated_hosts_charge_type_with_options(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostsChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostsChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_hosts_charge_type_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostsChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostsChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_hosts_charge_type(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostsChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_hosts_charge_type_with_options(request, runtime)

    async def modify_dedicated_hosts_charge_type_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostsChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_hosts_charge_type_with_options_async(request, runtime)

    def modify_demand_with_options(
        self,
        request: ecs_20140526_models.ModifyDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDemandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDemandResponse().from_map(
            self.do_rpcrequest('ModifyDemand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_demand_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDemandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDemandResponse().from_map(
            await self.do_rpcrequest_async('ModifyDemand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_demand(
        self,
        request: ecs_20140526_models.ModifyDemandRequest,
    ) -> ecs_20140526_models.ModifyDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_demand_with_options(request, runtime)

    async def modify_demand_async(
        self,
        request: ecs_20140526_models.ModifyDemandRequest,
    ) -> ecs_20140526_models.ModifyDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_demand_with_options_async(request, runtime)

    def modify_deployment_set_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyDeploymentSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDeploymentSetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDeploymentSetAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDeploymentSetAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_deployment_set_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDeploymentSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDeploymentSetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDeploymentSetAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDeploymentSetAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_deployment_set_attribute(
        self,
        request: ecs_20140526_models.ModifyDeploymentSetAttributeRequest,
    ) -> ecs_20140526_models.ModifyDeploymentSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_deployment_set_attribute_with_options(request, runtime)

    async def modify_deployment_set_attribute_async(
        self,
        request: ecs_20140526_models.ModifyDeploymentSetAttributeRequest,
    ) -> ecs_20140526_models.ModifyDeploymentSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_deployment_set_attribute_with_options_async(request, runtime)

    def modify_disk_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyDiskAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDiskAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_disk_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDiskAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDiskAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_disk_attribute(
        self,
        request: ecs_20140526_models.ModifyDiskAttributeRequest,
    ) -> ecs_20140526_models.ModifyDiskAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_attribute_with_options(request, runtime)

    async def modify_disk_attribute_async(
        self,
        request: ecs_20140526_models.ModifyDiskAttributeRequest,
    ) -> ecs_20140526_models.ModifyDiskAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_attribute_with_options_async(request, runtime)

    def modify_disk_charge_type_with_options(
        self,
        request: ecs_20140526_models.ModifyDiskChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskChargeTypeResponse().from_map(
            self.do_rpcrequest('ModifyDiskChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_disk_charge_type_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDiskChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskChargeTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDiskChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_disk_charge_type(
        self,
        request: ecs_20140526_models.ModifyDiskChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyDiskChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_charge_type_with_options(request, runtime)

    async def modify_disk_charge_type_async(
        self,
        request: ecs_20140526_models.ModifyDiskChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyDiskChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_charge_type_with_options_async(request, runtime)

    def modify_disk_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyDiskSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskSpecResponse().from_map(
            self.do_rpcrequest('ModifyDiskSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_disk_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDiskSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyDiskSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_disk_spec(
        self,
        request: ecs_20140526_models.ModifyDiskSpecRequest,
    ) -> ecs_20140526_models.ModifyDiskSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_spec_with_options(request, runtime)

    async def modify_disk_spec_async(
        self,
        request: ecs_20140526_models.ModifyDiskSpecRequest,
    ) -> ecs_20140526_models.ModifyDiskSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_spec_with_options_async(request, runtime)

    def modify_eip_address_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyEipAddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyEipAddressAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyEipAddressAttributeResponse().from_map(
            self.do_rpcrequest('ModifyEipAddressAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_eip_address_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyEipAddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyEipAddressAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyEipAddressAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyEipAddressAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_eip_address_attribute(
        self,
        request: ecs_20140526_models.ModifyEipAddressAttributeRequest,
    ) -> ecs_20140526_models.ModifyEipAddressAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_eip_address_attribute_with_options(request, runtime)

    async def modify_eip_address_attribute_async(
        self,
        request: ecs_20140526_models.ModifyEipAddressAttributeRequest,
    ) -> ecs_20140526_models.ModifyEipAddressAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_eip_address_attribute_with_options_async(request, runtime)

    def modify_elasticity_assurance_with_options(
        self,
        request: ecs_20140526_models.ModifyElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyElasticityAssuranceResponse().from_map(
            self.do_rpcrequest('ModifyElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_elasticity_assurance_with_options_async(
        self,
        request: ecs_20140526_models.ModifyElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyElasticityAssuranceResponse().from_map(
            await self.do_rpcrequest_async('ModifyElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_elasticity_assurance(
        self,
        request: ecs_20140526_models.ModifyElasticityAssuranceRequest,
    ) -> ecs_20140526_models.ModifyElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_elasticity_assurance_with_options(request, runtime)

    async def modify_elasticity_assurance_async(
        self,
        request: ecs_20140526_models.ModifyElasticityAssuranceRequest,
    ) -> ecs_20140526_models.ModifyElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_elasticity_assurance_with_options_async(request, runtime)

    def modify_forward_entry_with_options(
        self,
        request: ecs_20140526_models.ModifyForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyForwardEntryResponse().from_map(
            self.do_rpcrequest('ModifyForwardEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_forward_entry_with_options_async(
        self,
        request: ecs_20140526_models.ModifyForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyForwardEntryResponse().from_map(
            await self.do_rpcrequest_async('ModifyForwardEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_forward_entry(
        self,
        request: ecs_20140526_models.ModifyForwardEntryRequest,
    ) -> ecs_20140526_models.ModifyForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_forward_entry_with_options(request, runtime)

    async def modify_forward_entry_async(
        self,
        request: ecs_20140526_models.ModifyForwardEntryRequest,
    ) -> ecs_20140526_models.ModifyForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_forward_entry_with_options_async(request, runtime)

    def modify_ha_vip_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyHaVipAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyHaVipAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyHaVipAttributeResponse().from_map(
            self.do_rpcrequest('ModifyHaVipAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ha_vip_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyHaVipAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyHaVipAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyHaVipAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyHaVipAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ha_vip_attribute(
        self,
        request: ecs_20140526_models.ModifyHaVipAttributeRequest,
    ) -> ecs_20140526_models.ModifyHaVipAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ha_vip_attribute_with_options(request, runtime)

    async def modify_ha_vip_attribute_async(
        self,
        request: ecs_20140526_models.ModifyHaVipAttributeRequest,
    ) -> ecs_20140526_models.ModifyHaVipAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ha_vip_attribute_with_options_async(request, runtime)

    def modify_hpc_cluster_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyHpcClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyHpcClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyHpcClusterAttributeResponse().from_map(
            self.do_rpcrequest('ModifyHpcClusterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_hpc_cluster_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyHpcClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyHpcClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyHpcClusterAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyHpcClusterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_hpc_cluster_attribute(
        self,
        request: ecs_20140526_models.ModifyHpcClusterAttributeRequest,
    ) -> ecs_20140526_models.ModifyHpcClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_hpc_cluster_attribute_with_options(request, runtime)

    async def modify_hpc_cluster_attribute_async(
        self,
        request: ecs_20140526_models.ModifyHpcClusterAttributeRequest,
    ) -> ecs_20140526_models.ModifyHpcClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_hpc_cluster_attribute_with_options_async(request, runtime)

    def modify_image_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageAttributeResponse().from_map(
            self.do_rpcrequest('ModifyImageAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_image_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyImageAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_attribute(
        self,
        request: ecs_20140526_models.ModifyImageAttributeRequest,
    ) -> ecs_20140526_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    async def modify_image_attribute_async(
        self,
        request: ecs_20140526_models.ModifyImageAttributeRequest,
    ) -> ecs_20140526_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_attribute_with_options_async(request, runtime)

    def modify_image_share_group_permission_with_options(
        self,
        request: ecs_20140526_models.ModifyImageShareGroupPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageShareGroupPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageShareGroupPermissionResponse().from_map(
            self.do_rpcrequest('ModifyImageShareGroupPermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_image_share_group_permission_with_options_async(
        self,
        request: ecs_20140526_models.ModifyImageShareGroupPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageShareGroupPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageShareGroupPermissionResponse().from_map(
            await self.do_rpcrequest_async('ModifyImageShareGroupPermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_share_group_permission(
        self,
        request: ecs_20140526_models.ModifyImageShareGroupPermissionRequest,
    ) -> ecs_20140526_models.ModifyImageShareGroupPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_group_permission_with_options(request, runtime)

    async def modify_image_share_group_permission_async(
        self,
        request: ecs_20140526_models.ModifyImageShareGroupPermissionRequest,
    ) -> ecs_20140526_models.ModifyImageShareGroupPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_share_group_permission_with_options_async(request, runtime)

    def modify_image_share_permission_with_options(
        self,
        request: ecs_20140526_models.ModifyImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageSharePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageSharePermissionResponse().from_map(
            self.do_rpcrequest('ModifyImageSharePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_image_share_permission_with_options_async(
        self,
        request: ecs_20140526_models.ModifyImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageSharePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageSharePermissionResponse().from_map(
            await self.do_rpcrequest_async('ModifyImageSharePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_share_permission(
        self,
        request: ecs_20140526_models.ModifyImageSharePermissionRequest,
    ) -> ecs_20140526_models.ModifyImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_permission_with_options(request, runtime)

    async def modify_image_share_permission_async(
        self,
        request: ecs_20140526_models.ModifyImageSharePermissionRequest,
    ) -> ecs_20140526_models.ModifyImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_share_permission_with_options_async(request, runtime)

    def modify_instance_attachment_attributes_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceAttachmentAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAttachmentAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_attachment_attributes_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAttachmentAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAttachmentAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attachment_attributes(
        self,
        request: ecs_20140526_models.ModifyInstanceAttachmentAttributesRequest,
    ) -> ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attachment_attributes_with_options(request, runtime)

    async def modify_instance_attachment_attributes_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAttachmentAttributesRequest,
    ) -> ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attachment_attributes_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: ecs_20140526_models.ModifyInstanceAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_instance_auto_release_time_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAutoReleaseTime', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_auto_release_time_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAutoReleaseTime', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_release_time(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoReleaseTimeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_release_time_with_options(request, runtime)

    async def modify_instance_auto_release_time_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoReleaseTimeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_release_time_with_options_async(request, runtime)

    def modify_instance_auto_renew_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_auto_renew_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_renew_attribute(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoRenewAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renew_attribute_with_options(request, runtime)

    async def modify_instance_auto_renew_attribute_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoRenewAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_renew_attribute_with_options_async(request, runtime)

    def modify_instance_charge_type_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceChargeTypeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_charge_type_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceChargeTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_charge_type(
        self,
        request: ecs_20140526_models.ModifyInstanceChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_charge_type_with_options(request, runtime)

    async def modify_instance_charge_type_async(
        self,
        request: ecs_20140526_models.ModifyInstanceChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_charge_type_with_options_async(request, runtime)

    def modify_instance_deployment_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceDeploymentResponse().from_map(
            self.do_rpcrequest('ModifyInstanceDeployment', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_deployment_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceDeploymentResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceDeployment', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_deployment(
        self,
        request: ecs_20140526_models.ModifyInstanceDeploymentRequest,
    ) -> ecs_20140526_models.ModifyInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_deployment_with_options(request, runtime)

    async def modify_instance_deployment_async(
        self,
        request: ecs_20140526_models.ModifyInstanceDeploymentRequest,
    ) -> ecs_20140526_models.ModifyInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_deployment_with_options_async(request, runtime)

    def modify_instance_maintenance_attributes_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceMaintenanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse().from_map(
            self.do_rpcrequest('ModifyInstanceMaintenanceAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_maintenance_attributes_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceMaintenanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceMaintenanceAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_maintenance_attributes(
        self,
        request: ecs_20140526_models.ModifyInstanceMaintenanceAttributesRequest,
    ) -> ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintenance_attributes_with_options(request, runtime)

    async def modify_instance_maintenance_attributes_async(
        self,
        request: ecs_20140526_models.ModifyInstanceMaintenanceAttributesRequest,
    ) -> ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_maintenance_attributes_with_options_async(request, runtime)

    def modify_instance_metadata_options_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceMetadataOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceMetadataOptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceMetadataOptionsResponse().from_map(
            self.do_rpcrequest('ModifyInstanceMetadataOptions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_metadata_options_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceMetadataOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceMetadataOptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceMetadataOptionsResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceMetadataOptions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_metadata_options(
        self,
        request: ecs_20140526_models.ModifyInstanceMetadataOptionsRequest,
    ) -> ecs_20140526_models.ModifyInstanceMetadataOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_metadata_options_with_options(request, runtime)

    async def modify_instance_metadata_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceMetadataOptionsRequest,
    ) -> ecs_20140526_models.ModifyInstanceMetadataOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_metadata_options_with_options_async(request, runtime)

    def modify_instance_network_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceNetworkSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceNetworkSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceNetworkSpecResponse().from_map(
            self.do_rpcrequest('ModifyInstanceNetworkSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_network_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceNetworkSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceNetworkSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceNetworkSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceNetworkSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_network_spec(
        self,
        request: ecs_20140526_models.ModifyInstanceNetworkSpecRequest,
    ) -> ecs_20140526_models.ModifyInstanceNetworkSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_network_spec_with_options(request, runtime)

    async def modify_instance_network_spec_async(
        self,
        request: ecs_20140526_models.ModifyInstanceNetworkSpecRequest,
    ) -> ecs_20140526_models.ModifyInstanceNetworkSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_network_spec_with_options_async(request, runtime)

    def modify_instance_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceSpecResponse().from_map(
            self.do_rpcrequest('ModifyInstanceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_spec(
        self,
        request: ecs_20140526_models.ModifyInstanceSpecRequest,
    ) -> ecs_20140526_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    async def modify_instance_spec_async(
        self,
        request: ecs_20140526_models.ModifyInstanceSpecRequest,
    ) -> ecs_20140526_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_spec_with_options_async(request, runtime)

    def modify_instance_vnc_passwd_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceVncPasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceVncPasswdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceVncPasswdResponse().from_map(
            self.do_rpcrequest('ModifyInstanceVncPasswd', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_vnc_passwd_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceVncPasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceVncPasswdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceVncPasswdResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceVncPasswd', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_vnc_passwd(
        self,
        request: ecs_20140526_models.ModifyInstanceVncPasswdRequest,
    ) -> ecs_20140526_models.ModifyInstanceVncPasswdResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vnc_passwd_with_options(request, runtime)

    async def modify_instance_vnc_passwd_async(
        self,
        request: ecs_20140526_models.ModifyInstanceVncPasswdRequest,
    ) -> ecs_20140526_models.ModifyInstanceVncPasswdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vnc_passwd_with_options_async(request, runtime)

    def modify_instance_vpc_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceVpcAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceVpcAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_vpc_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceVpcAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceVpcAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_vpc_attribute(
        self,
        request: ecs_20140526_models.ModifyInstanceVpcAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_attribute_with_options(request, runtime)

    async def modify_instance_vpc_attribute_async(
        self,
        request: ecs_20140526_models.ModifyInstanceVpcAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vpc_attribute_with_options_async(request, runtime)

    def modify_launch_template_default_version_with_options(
        self,
        request: ecs_20140526_models.ModifyLaunchTemplateDefaultVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse().from_map(
            self.do_rpcrequest('ModifyLaunchTemplateDefaultVersion', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_launch_template_default_version_with_options_async(
        self,
        request: ecs_20140526_models.ModifyLaunchTemplateDefaultVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse().from_map(
            await self.do_rpcrequest_async('ModifyLaunchTemplateDefaultVersion', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_launch_template_default_version(
        self,
        request: ecs_20140526_models.ModifyLaunchTemplateDefaultVersionRequest,
    ) -> ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_launch_template_default_version_with_options(request, runtime)

    async def modify_launch_template_default_version_async(
        self,
        request: ecs_20140526_models.ModifyLaunchTemplateDefaultVersionRequest,
    ) -> ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_launch_template_default_version_with_options_async(request, runtime)

    def modify_managed_instance_with_options(
        self,
        request: ecs_20140526_models.ModifyManagedInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyManagedInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyManagedInstanceResponse().from_map(
            self.do_rpcrequest('ModifyManagedInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_managed_instance_with_options_async(
        self,
        request: ecs_20140526_models.ModifyManagedInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyManagedInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyManagedInstanceResponse().from_map(
            await self.do_rpcrequest_async('ModifyManagedInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_managed_instance(
        self,
        request: ecs_20140526_models.ModifyManagedInstanceRequest,
    ) -> ecs_20140526_models.ModifyManagedInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_managed_instance_with_options(request, runtime)

    async def modify_managed_instance_async(
        self,
        request: ecs_20140526_models.ModifyManagedInstanceRequest,
    ) -> ecs_20140526_models.ModifyManagedInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_managed_instance_with_options_async(request, runtime)

    def modify_network_interface_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyNetworkInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyNetworkInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_network_interface_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyNetworkInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyNetworkInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_network_interface_attribute(
        self,
        request: ecs_20140526_models.ModifyNetworkInterfaceAttributeRequest,
    ) -> ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_network_interface_attribute_with_options(request, runtime)

    async def modify_network_interface_attribute_async(
        self,
        request: ecs_20140526_models.ModifyNetworkInterfaceAttributeRequest,
    ) -> ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_interface_attribute_with_options_async(request, runtime)

    def modify_physical_connection_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyPhysicalConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse().from_map(
            self.do_rpcrequest('ModifyPhysicalConnectionAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_physical_connection_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyPhysicalConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyPhysicalConnectionAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_physical_connection_attribute(
        self,
        request: ecs_20140526_models.ModifyPhysicalConnectionAttributeRequest,
    ) -> ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_physical_connection_attribute_with_options(request, runtime)

    async def modify_physical_connection_attribute_async(
        self,
        request: ecs_20140526_models.ModifyPhysicalConnectionAttributeRequest,
    ) -> ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_physical_connection_attribute_with_options_async(request, runtime)

    def modify_prepay_instance_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyPrepayInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyPrepayInstanceSpecResponse().from_map(
            self.do_rpcrequest('ModifyPrepayInstanceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_prepay_instance_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyPrepayInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyPrepayInstanceSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyPrepayInstanceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_prepay_instance_spec(
        self,
        request: ecs_20140526_models.ModifyPrepayInstanceSpecRequest,
    ) -> ecs_20140526_models.ModifyPrepayInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    async def modify_prepay_instance_spec_async(
        self,
        request: ecs_20140526_models.ModifyPrepayInstanceSpecRequest,
    ) -> ecs_20140526_models.ModifyPrepayInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_prepay_instance_spec_with_options_async(request, runtime)

    def modify_reserved_instance_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyReservedInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyReservedInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyReservedInstanceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyReservedInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_reserved_instance_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyReservedInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyReservedInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyReservedInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyReservedInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_reserved_instance_attribute(
        self,
        request: ecs_20140526_models.ModifyReservedInstanceAttributeRequest,
    ) -> ecs_20140526_models.ModifyReservedInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_reserved_instance_attribute_with_options(request, runtime)

    async def modify_reserved_instance_attribute_async(
        self,
        request: ecs_20140526_models.ModifyReservedInstanceAttributeRequest,
    ) -> ecs_20140526_models.ModifyReservedInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_reserved_instance_attribute_with_options_async(request, runtime)

    def modify_reserved_instances_with_options(
        self,
        request: ecs_20140526_models.ModifyReservedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyReservedInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyReservedInstancesResponse().from_map(
            self.do_rpcrequest('ModifyReservedInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_reserved_instances_with_options_async(
        self,
        request: ecs_20140526_models.ModifyReservedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyReservedInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyReservedInstancesResponse().from_map(
            await self.do_rpcrequest_async('ModifyReservedInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_reserved_instances(
        self,
        request: ecs_20140526_models.ModifyReservedInstancesRequest,
    ) -> ecs_20140526_models.ModifyReservedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_reserved_instances_with_options(request, runtime)

    async def modify_reserved_instances_async(
        self,
        request: ecs_20140526_models.ModifyReservedInstancesRequest,
    ) -> ecs_20140526_models.ModifyReservedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_reserved_instances_with_options_async(request, runtime)

    def modify_router_interface_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyRouterInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyRouterInterfaceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyRouterInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_router_interface_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyRouterInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyRouterInterfaceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyRouterInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_router_interface_attribute(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceAttributeRequest,
    ) -> ecs_20140526_models.ModifyRouterInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_router_interface_attribute_with_options(request, runtime)

    async def modify_router_interface_attribute_async(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceAttributeRequest,
    ) -> ecs_20140526_models.ModifyRouterInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_router_interface_attribute_with_options_async(request, runtime)

    def modify_router_interface_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyRouterInterfaceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyRouterInterfaceSpecResponse().from_map(
            self.do_rpcrequest('ModifyRouterInterfaceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_router_interface_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyRouterInterfaceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyRouterInterfaceSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyRouterInterfaceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_router_interface_spec(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceSpecRequest,
    ) -> ecs_20140526_models.ModifyRouterInterfaceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_router_interface_spec_with_options(request, runtime)

    async def modify_router_interface_spec_async(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceSpecRequest,
    ) -> ecs_20140526_models.ModifyRouterInterfaceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_router_interface_spec_with_options_async(request, runtime)

    def modify_security_group_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifySecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupAttributeResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroupAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroupAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_attribute(
        self,
        request: ecs_20140526_models.ModifySecurityGroupAttributeRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_attribute_with_options(request, runtime)

    async def modify_security_group_attribute_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupAttributeRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_attribute_with_options_async(request, runtime)

    def modify_security_group_egress_rule_with_options(
        self,
        request: ecs_20140526_models.ModifySecurityGroupEgressRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupEgressRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupEgressRuleResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroupEgressRule', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_egress_rule_with_options_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupEgressRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupEgressRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupEgressRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroupEgressRule', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_egress_rule(
        self,
        request: ecs_20140526_models.ModifySecurityGroupEgressRuleRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupEgressRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_egress_rule_with_options(request, runtime)

    async def modify_security_group_egress_rule_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupEgressRuleRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupEgressRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_egress_rule_with_options_async(request, runtime)

    def modify_security_group_policy_with_options(
        self,
        request: ecs_20140526_models.ModifySecurityGroupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupPolicyResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroupPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_policy_with_options_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroupPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_policy(
        self,
        request: ecs_20140526_models.ModifySecurityGroupPolicyRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_policy_with_options(request, runtime)

    async def modify_security_group_policy_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupPolicyRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_policy_with_options_async(request, runtime)

    def modify_security_group_rule_with_options(
        self,
        request: ecs_20140526_models.ModifySecurityGroupRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupRuleResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroupRule', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_rule_with_options_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroupRule', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_rule(
        self,
        request: ecs_20140526_models.ModifySecurityGroupRuleRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_rule_with_options(request, runtime)

    async def modify_security_group_rule_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupRuleRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_rule_with_options_async(request, runtime)

    def modify_snapshot_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifySnapshotAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySnapshotAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySnapshotAttributeResponse().from_map(
            self.do_rpcrequest('ModifySnapshotAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_snapshot_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifySnapshotAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySnapshotAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySnapshotAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifySnapshotAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_snapshot_attribute(
        self,
        request: ecs_20140526_models.ModifySnapshotAttributeRequest,
    ) -> ecs_20140526_models.ModifySnapshotAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_snapshot_attribute_with_options(request, runtime)

    async def modify_snapshot_attribute_async(
        self,
        request: ecs_20140526_models.ModifySnapshotAttributeRequest,
    ) -> ecs_20140526_models.ModifySnapshotAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_snapshot_attribute_with_options_async(request, runtime)

    def modify_snapshot_group_with_options(
        self,
        request: ecs_20140526_models.ModifySnapshotGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySnapshotGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySnapshotGroupResponse().from_map(
            self.do_rpcrequest('ModifySnapshotGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_snapshot_group_with_options_async(
        self,
        request: ecs_20140526_models.ModifySnapshotGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySnapshotGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySnapshotGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifySnapshotGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_snapshot_group(
        self,
        request: ecs_20140526_models.ModifySnapshotGroupRequest,
    ) -> ecs_20140526_models.ModifySnapshotGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_snapshot_group_with_options(request, runtime)

    async def modify_snapshot_group_async(
        self,
        request: ecs_20140526_models.ModifySnapshotGroupRequest,
    ) -> ecs_20140526_models.ModifySnapshotGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_snapshot_group_with_options_async(request, runtime)

    def modify_storage_capacity_unit_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyStorageCapacityUnitAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse().from_map(
            self.do_rpcrequest('ModifyStorageCapacityUnitAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_storage_capacity_unit_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyStorageCapacityUnitAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyStorageCapacityUnitAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_storage_capacity_unit_attribute(
        self,
        request: ecs_20140526_models.ModifyStorageCapacityUnitAttributeRequest,
    ) -> ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_capacity_unit_attribute_with_options(request, runtime)

    async def modify_storage_capacity_unit_attribute_async(
        self,
        request: ecs_20140526_models.ModifyStorageCapacityUnitAttributeRequest,
    ) -> ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_storage_capacity_unit_attribute_with_options_async(request, runtime)

    def modify_storage_set_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyStorageSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyStorageSetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyStorageSetAttributeResponse().from_map(
            self.do_rpcrequest('ModifyStorageSetAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_storage_set_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyStorageSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyStorageSetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyStorageSetAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyStorageSetAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_storage_set_attribute(
        self,
        request: ecs_20140526_models.ModifyStorageSetAttributeRequest,
    ) -> ecs_20140526_models.ModifyStorageSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_set_attribute_with_options(request, runtime)

    async def modify_storage_set_attribute_async(
        self,
        request: ecs_20140526_models.ModifyStorageSetAttributeRequest,
    ) -> ecs_20140526_models.ModifyStorageSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_storage_set_attribute_with_options_async(request, runtime)

    def modify_user_business_behavior_with_options(
        self,
        request: ecs_20140526_models.ModifyUserBusinessBehaviorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyUserBusinessBehaviorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyUserBusinessBehaviorResponse().from_map(
            self.do_rpcrequest('ModifyUserBusinessBehavior', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_user_business_behavior_with_options_async(
        self,
        request: ecs_20140526_models.ModifyUserBusinessBehaviorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyUserBusinessBehaviorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyUserBusinessBehaviorResponse().from_map(
            await self.do_rpcrequest_async('ModifyUserBusinessBehavior', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user_business_behavior(
        self,
        request: ecs_20140526_models.ModifyUserBusinessBehaviorRequest,
    ) -> ecs_20140526_models.ModifyUserBusinessBehaviorResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_business_behavior_with_options(request, runtime)

    async def modify_user_business_behavior_async(
        self,
        request: ecs_20140526_models.ModifyUserBusinessBehaviorRequest,
    ) -> ecs_20140526_models.ModifyUserBusinessBehaviorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_business_behavior_with_options_async(request, runtime)

    def modify_virtual_border_router_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyVirtualBorderRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVirtualBorderRouterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_virtual_border_router_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyVirtualBorderRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVirtualBorderRouterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_virtual_border_router_attribute(
        self,
        request: ecs_20140526_models.ModifyVirtualBorderRouterAttributeRequest,
    ) -> ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_virtual_border_router_attribute_with_options(request, runtime)

    async def modify_virtual_border_router_attribute_async(
        self,
        request: ecs_20140526_models.ModifyVirtualBorderRouterAttributeRequest,
    ) -> ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_virtual_border_router_attribute_with_options_async(request, runtime)

    def modify_vpc_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVpcAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVpcAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vpc_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVpcAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVpcAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vpc_attribute(
        self,
        request: ecs_20140526_models.ModifyVpcAttributeRequest,
    ) -> ecs_20140526_models.ModifyVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_attribute_with_options(request, runtime)

    async def modify_vpc_attribute_async(
        self,
        request: ecs_20140526_models.ModifyVpcAttributeRequest,
    ) -> ecs_20140526_models.ModifyVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_attribute_with_options_async(request, runtime)

    def modify_vrouter_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyVRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVRouterAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVRouterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vrouter_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyVRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVRouterAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVRouterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vrouter_attribute(
        self,
        request: ecs_20140526_models.ModifyVRouterAttributeRequest,
    ) -> ecs_20140526_models.ModifyVRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vrouter_attribute_with_options(request, runtime)

    async def modify_vrouter_attribute_async(
        self,
        request: ecs_20140526_models.ModifyVRouterAttributeRequest,
    ) -> ecs_20140526_models.ModifyVRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vrouter_attribute_with_options_async(request, runtime)

    def modify_vswitch_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyVSwitchAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVSwitchAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVSwitchAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVSwitchAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vswitch_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyVSwitchAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVSwitchAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVSwitchAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVSwitchAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vswitch_attribute(
        self,
        request: ecs_20140526_models.ModifyVSwitchAttributeRequest,
    ) -> ecs_20140526_models.ModifyVSwitchAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vswitch_attribute_with_options(request, runtime)

    async def modify_vswitch_attribute_async(
        self,
        request: ecs_20140526_models.ModifyVSwitchAttributeRequest,
    ) -> ecs_20140526_models.ModifyVSwitchAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vswitch_attribute_with_options_async(request, runtime)

    def purchase_reserved_instances_offering_with_options(
        self,
        request: ecs_20140526_models.PurchaseReservedInstancesOfferingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.PurchaseReservedInstancesOfferingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.PurchaseReservedInstancesOfferingResponse().from_map(
            self.do_rpcrequest('PurchaseReservedInstancesOffering', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def purchase_reserved_instances_offering_with_options_async(
        self,
        request: ecs_20140526_models.PurchaseReservedInstancesOfferingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.PurchaseReservedInstancesOfferingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.PurchaseReservedInstancesOfferingResponse().from_map(
            await self.do_rpcrequest_async('PurchaseReservedInstancesOffering', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def purchase_reserved_instances_offering(
        self,
        request: ecs_20140526_models.PurchaseReservedInstancesOfferingRequest,
    ) -> ecs_20140526_models.PurchaseReservedInstancesOfferingResponse:
        runtime = util_models.RuntimeOptions()
        return self.purchase_reserved_instances_offering_with_options(request, runtime)

    async def purchase_reserved_instances_offering_async(
        self,
        request: ecs_20140526_models.PurchaseReservedInstancesOfferingRequest,
    ) -> ecs_20140526_models.PurchaseReservedInstancesOfferingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purchase_reserved_instances_offering_with_options_async(request, runtime)

    def purchase_storage_capacity_unit_with_options(
        self,
        request: ecs_20140526_models.PurchaseStorageCapacityUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.PurchaseStorageCapacityUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.PurchaseStorageCapacityUnitResponse().from_map(
            self.do_rpcrequest('PurchaseStorageCapacityUnit', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def purchase_storage_capacity_unit_with_options_async(
        self,
        request: ecs_20140526_models.PurchaseStorageCapacityUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.PurchaseStorageCapacityUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.PurchaseStorageCapacityUnitResponse().from_map(
            await self.do_rpcrequest_async('PurchaseStorageCapacityUnit', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def purchase_storage_capacity_unit(
        self,
        request: ecs_20140526_models.PurchaseStorageCapacityUnitRequest,
    ) -> ecs_20140526_models.PurchaseStorageCapacityUnitResponse:
        runtime = util_models.RuntimeOptions()
        return self.purchase_storage_capacity_unit_with_options(request, runtime)

    async def purchase_storage_capacity_unit_async(
        self,
        request: ecs_20140526_models.PurchaseStorageCapacityUnitRequest,
    ) -> ecs_20140526_models.PurchaseStorageCapacityUnitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purchase_storage_capacity_unit_with_options_async(request, runtime)

    def re_activate_instances_with_options(
        self,
        request: ecs_20140526_models.ReActivateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReActivateInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReActivateInstancesResponse().from_map(
            self.do_rpcrequest('ReActivateInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def re_activate_instances_with_options_async(
        self,
        request: ecs_20140526_models.ReActivateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReActivateInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReActivateInstancesResponse().from_map(
            await self.do_rpcrequest_async('ReActivateInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def re_activate_instances(
        self,
        request: ecs_20140526_models.ReActivateInstancesRequest,
    ) -> ecs_20140526_models.ReActivateInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.re_activate_instances_with_options(request, runtime)

    async def re_activate_instances_async(
        self,
        request: ecs_20140526_models.ReActivateInstancesRequest,
    ) -> ecs_20140526_models.ReActivateInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.re_activate_instances_with_options_async(request, runtime)

    def reboot_instance_with_options(
        self,
        request: ecs_20140526_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RebootInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RebootInstanceResponse().from_map(
            self.do_rpcrequest('RebootInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reboot_instance_with_options_async(
        self,
        request: ecs_20140526_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RebootInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RebootInstanceResponse().from_map(
            await self.do_rpcrequest_async('RebootInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_instance(
        self,
        request: ecs_20140526_models.RebootInstanceRequest,
    ) -> ecs_20140526_models.RebootInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_instance_with_options(request, runtime)

    async def reboot_instance_async(
        self,
        request: ecs_20140526_models.RebootInstanceRequest,
    ) -> ecs_20140526_models.RebootInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instance_with_options_async(request, runtime)

    def reboot_instances_with_options(
        self,
        request: ecs_20140526_models.RebootInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RebootInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RebootInstancesResponse().from_map(
            self.do_rpcrequest('RebootInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reboot_instances_with_options_async(
        self,
        request: ecs_20140526_models.RebootInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RebootInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RebootInstancesResponse().from_map(
            await self.do_rpcrequest_async('RebootInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_instances(
        self,
        request: ecs_20140526_models.RebootInstancesRequest,
    ) -> ecs_20140526_models.RebootInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_instances_with_options(request, runtime)

    async def reboot_instances_async(
        self,
        request: ecs_20140526_models.RebootInstancesRequest,
    ) -> ecs_20140526_models.RebootInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instances_with_options_async(request, runtime)

    def recover_virtual_border_router_with_options(
        self,
        request: ecs_20140526_models.RecoverVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RecoverVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RecoverVirtualBorderRouterResponse().from_map(
            self.do_rpcrequest('RecoverVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recover_virtual_border_router_with_options_async(
        self,
        request: ecs_20140526_models.RecoverVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RecoverVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RecoverVirtualBorderRouterResponse().from_map(
            await self.do_rpcrequest_async('RecoverVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recover_virtual_border_router(
        self,
        request: ecs_20140526_models.RecoverVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.RecoverVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.recover_virtual_border_router_with_options(request, runtime)

    async def recover_virtual_border_router_async(
        self,
        request: ecs_20140526_models.RecoverVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.RecoverVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recover_virtual_border_router_with_options_async(request, runtime)

    def redeploy_dedicated_host_with_options(
        self,
        request: ecs_20140526_models.RedeployDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RedeployDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RedeployDedicatedHostResponse().from_map(
            self.do_rpcrequest('RedeployDedicatedHost', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def redeploy_dedicated_host_with_options_async(
        self,
        request: ecs_20140526_models.RedeployDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RedeployDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RedeployDedicatedHostResponse().from_map(
            await self.do_rpcrequest_async('RedeployDedicatedHost', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def redeploy_dedicated_host(
        self,
        request: ecs_20140526_models.RedeployDedicatedHostRequest,
    ) -> ecs_20140526_models.RedeployDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.redeploy_dedicated_host_with_options(request, runtime)

    async def redeploy_dedicated_host_async(
        self,
        request: ecs_20140526_models.RedeployDedicatedHostRequest,
    ) -> ecs_20140526_models.RedeployDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.redeploy_dedicated_host_with_options_async(request, runtime)

    def redeploy_instance_with_options(
        self,
        request: ecs_20140526_models.RedeployInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RedeployInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RedeployInstanceResponse().from_map(
            self.do_rpcrequest('RedeployInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def redeploy_instance_with_options_async(
        self,
        request: ecs_20140526_models.RedeployInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RedeployInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RedeployInstanceResponse().from_map(
            await self.do_rpcrequest_async('RedeployInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def redeploy_instance(
        self,
        request: ecs_20140526_models.RedeployInstanceRequest,
    ) -> ecs_20140526_models.RedeployInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.redeploy_instance_with_options(request, runtime)

    async def redeploy_instance_async(
        self,
        request: ecs_20140526_models.RedeployInstanceRequest,
    ) -> ecs_20140526_models.RedeployInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.redeploy_instance_with_options_async(request, runtime)

    def re_init_disk_with_options(
        self,
        request: ecs_20140526_models.ReInitDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReInitDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReInitDiskResponse().from_map(
            self.do_rpcrequest('ReInitDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def re_init_disk_with_options_async(
        self,
        request: ecs_20140526_models.ReInitDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReInitDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReInitDiskResponse().from_map(
            await self.do_rpcrequest_async('ReInitDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def re_init_disk(
        self,
        request: ecs_20140526_models.ReInitDiskRequest,
    ) -> ecs_20140526_models.ReInitDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.re_init_disk_with_options(request, runtime)

    async def re_init_disk_async(
        self,
        request: ecs_20140526_models.ReInitDiskRequest,
    ) -> ecs_20140526_models.ReInitDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.re_init_disk_with_options_async(request, runtime)

    def release_capacity_reservation_with_options(
        self,
        request: ecs_20140526_models.ReleaseCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseCapacityReservationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseCapacityReservationResponse().from_map(
            self.do_rpcrequest('ReleaseCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_capacity_reservation_with_options_async(
        self,
        request: ecs_20140526_models.ReleaseCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseCapacityReservationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseCapacityReservationResponse().from_map(
            await self.do_rpcrequest_async('ReleaseCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_capacity_reservation(
        self,
        request: ecs_20140526_models.ReleaseCapacityReservationRequest,
    ) -> ecs_20140526_models.ReleaseCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_capacity_reservation_with_options(request, runtime)

    async def release_capacity_reservation_async(
        self,
        request: ecs_20140526_models.ReleaseCapacityReservationRequest,
    ) -> ecs_20140526_models.ReleaseCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_capacity_reservation_with_options_async(request, runtime)

    def release_dedicated_host_with_options(
        self,
        request: ecs_20140526_models.ReleaseDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseDedicatedHostResponse().from_map(
            self.do_rpcrequest('ReleaseDedicatedHost', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_dedicated_host_with_options_async(
        self,
        request: ecs_20140526_models.ReleaseDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseDedicatedHostResponse().from_map(
            await self.do_rpcrequest_async('ReleaseDedicatedHost', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_dedicated_host(
        self,
        request: ecs_20140526_models.ReleaseDedicatedHostRequest,
    ) -> ecs_20140526_models.ReleaseDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_dedicated_host_with_options(request, runtime)

    async def release_dedicated_host_async(
        self,
        request: ecs_20140526_models.ReleaseDedicatedHostRequest,
    ) -> ecs_20140526_models.ReleaseDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_dedicated_host_with_options_async(request, runtime)

    def release_eip_address_with_options(
        self,
        request: ecs_20140526_models.ReleaseEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseEipAddressResponse().from_map(
            self.do_rpcrequest('ReleaseEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_eip_address_with_options_async(
        self,
        request: ecs_20140526_models.ReleaseEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseEipAddressResponse().from_map(
            await self.do_rpcrequest_async('ReleaseEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_eip_address(
        self,
        request: ecs_20140526_models.ReleaseEipAddressRequest,
    ) -> ecs_20140526_models.ReleaseEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_eip_address_with_options(request, runtime)

    async def release_eip_address_async(
        self,
        request: ecs_20140526_models.ReleaseEipAddressRequest,
    ) -> ecs_20140526_models.ReleaseEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_eip_address_with_options_async(request, runtime)

    def release_public_ip_address_with_options(
        self,
        request: ecs_20140526_models.ReleasePublicIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleasePublicIpAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleasePublicIpAddressResponse().from_map(
            self.do_rpcrequest('ReleasePublicIpAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_public_ip_address_with_options_async(
        self,
        request: ecs_20140526_models.ReleasePublicIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleasePublicIpAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleasePublicIpAddressResponse().from_map(
            await self.do_rpcrequest_async('ReleasePublicIpAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_public_ip_address(
        self,
        request: ecs_20140526_models.ReleasePublicIpAddressRequest,
    ) -> ecs_20140526_models.ReleasePublicIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_public_ip_address_with_options(request, runtime)

    async def release_public_ip_address_async(
        self,
        request: ecs_20140526_models.ReleasePublicIpAddressRequest,
    ) -> ecs_20140526_models.ReleasePublicIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_public_ip_address_with_options_async(request, runtime)

    def remove_bandwidth_package_ips_with_options(
        self,
        request: ecs_20140526_models.RemoveBandwidthPackageIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RemoveBandwidthPackageIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RemoveBandwidthPackageIpsResponse().from_map(
            self.do_rpcrequest('RemoveBandwidthPackageIps', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_bandwidth_package_ips_with_options_async(
        self,
        request: ecs_20140526_models.RemoveBandwidthPackageIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RemoveBandwidthPackageIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RemoveBandwidthPackageIpsResponse().from_map(
            await self.do_rpcrequest_async('RemoveBandwidthPackageIps', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_bandwidth_package_ips(
        self,
        request: ecs_20140526_models.RemoveBandwidthPackageIpsRequest,
    ) -> ecs_20140526_models.RemoveBandwidthPackageIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_bandwidth_package_ips_with_options(request, runtime)

    async def remove_bandwidth_package_ips_async(
        self,
        request: ecs_20140526_models.RemoveBandwidthPackageIpsRequest,
    ) -> ecs_20140526_models.RemoveBandwidthPackageIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_bandwidth_package_ips_with_options_async(request, runtime)

    def remove_tags_with_options(
        self,
        request: ecs_20140526_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RemoveTagsResponse().from_map(
            self.do_rpcrequest('RemoveTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_tags_with_options_async(
        self,
        request: ecs_20140526_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RemoveTagsResponse().from_map(
            await self.do_rpcrequest_async('RemoveTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_tags(
        self,
        request: ecs_20140526_models.RemoveTagsRequest,
    ) -> ecs_20140526_models.RemoveTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    async def remove_tags_async(
        self,
        request: ecs_20140526_models.RemoveTagsRequest,
    ) -> ecs_20140526_models.RemoveTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_tags_with_options_async(request, runtime)

    def renew_dedicated_hosts_with_options(
        self,
        request: ecs_20140526_models.RenewDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RenewDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RenewDedicatedHostsResponse().from_map(
            self.do_rpcrequest('RenewDedicatedHosts', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_dedicated_hosts_with_options_async(
        self,
        request: ecs_20140526_models.RenewDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RenewDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RenewDedicatedHostsResponse().from_map(
            await self.do_rpcrequest_async('RenewDedicatedHosts', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_dedicated_hosts(
        self,
        request: ecs_20140526_models.RenewDedicatedHostsRequest,
    ) -> ecs_20140526_models.RenewDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_dedicated_hosts_with_options(request, runtime)

    async def renew_dedicated_hosts_async(
        self,
        request: ecs_20140526_models.RenewDedicatedHostsRequest,
    ) -> ecs_20140526_models.RenewDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_dedicated_hosts_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: ecs_20140526_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RenewInstanceResponse().from_map(
            self.do_rpcrequest('RenewInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: ecs_20140526_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RenewInstanceResponse().from_map(
            await self.do_rpcrequest_async('RenewInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(
        self,
        request: ecs_20140526_models.RenewInstanceRequest,
    ) -> ecs_20140526_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: ecs_20140526_models.RenewInstanceRequest,
    ) -> ecs_20140526_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def replace_system_disk_with_options(
        self,
        request: ecs_20140526_models.ReplaceSystemDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReplaceSystemDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReplaceSystemDiskResponse().from_map(
            self.do_rpcrequest('ReplaceSystemDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def replace_system_disk_with_options_async(
        self,
        request: ecs_20140526_models.ReplaceSystemDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReplaceSystemDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReplaceSystemDiskResponse().from_map(
            await self.do_rpcrequest_async('ReplaceSystemDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_system_disk(
        self,
        request: ecs_20140526_models.ReplaceSystemDiskRequest,
    ) -> ecs_20140526_models.ReplaceSystemDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_system_disk_with_options(request, runtime)

    async def replace_system_disk_async(
        self,
        request: ecs_20140526_models.ReplaceSystemDiskRequest,
    ) -> ecs_20140526_models.ReplaceSystemDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_system_disk_with_options_async(request, runtime)

    def report_instances_status_with_options(
        self,
        request: ecs_20140526_models.ReportInstancesStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReportInstancesStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReportInstancesStatusResponse().from_map(
            self.do_rpcrequest('ReportInstancesStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_instances_status_with_options_async(
        self,
        request: ecs_20140526_models.ReportInstancesStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReportInstancesStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReportInstancesStatusResponse().from_map(
            await self.do_rpcrequest_async('ReportInstancesStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_instances_status(
        self,
        request: ecs_20140526_models.ReportInstancesStatusRequest,
    ) -> ecs_20140526_models.ReportInstancesStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_instances_status_with_options(request, runtime)

    async def report_instances_status_async(
        self,
        request: ecs_20140526_models.ReportInstancesStatusRequest,
    ) -> ecs_20140526_models.ReportInstancesStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_instances_status_with_options_async(request, runtime)

    def reset_disk_with_options(
        self,
        request: ecs_20140526_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResetDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResetDiskResponse().from_map(
            self.do_rpcrequest('ResetDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_disk_with_options_async(
        self,
        request: ecs_20140526_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResetDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResetDiskResponse().from_map(
            await self.do_rpcrequest_async('ResetDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_disk(
        self,
        request: ecs_20140526_models.ResetDiskRequest,
    ) -> ecs_20140526_models.ResetDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_disk_with_options(request, runtime)

    async def reset_disk_async(
        self,
        request: ecs_20140526_models.ResetDiskRequest,
    ) -> ecs_20140526_models.ResetDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_disk_with_options_async(request, runtime)

    def reset_disks_with_options(
        self,
        request: ecs_20140526_models.ResetDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResetDisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResetDisksResponse().from_map(
            self.do_rpcrequest('ResetDisks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_disks_with_options_async(
        self,
        request: ecs_20140526_models.ResetDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResetDisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResetDisksResponse().from_map(
            await self.do_rpcrequest_async('ResetDisks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_disks(
        self,
        request: ecs_20140526_models.ResetDisksRequest,
    ) -> ecs_20140526_models.ResetDisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_disks_with_options(request, runtime)

    async def reset_disks_async(
        self,
        request: ecs_20140526_models.ResetDisksRequest,
    ) -> ecs_20140526_models.ResetDisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_disks_with_options_async(request, runtime)

    def resize_disk_with_options(
        self,
        request: ecs_20140526_models.ResizeDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResizeDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResizeDiskResponse().from_map(
            self.do_rpcrequest('ResizeDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_disk_with_options_async(
        self,
        request: ecs_20140526_models.ResizeDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResizeDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResizeDiskResponse().from_map(
            await self.do_rpcrequest_async('ResizeDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resize_disk(
        self,
        request: ecs_20140526_models.ResizeDiskRequest,
    ) -> ecs_20140526_models.ResizeDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_disk_with_options(request, runtime)

    async def resize_disk_async(
        self,
        request: ecs_20140526_models.ResizeDiskRequest,
    ) -> ecs_20140526_models.ResizeDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_disk_with_options_async(request, runtime)

    def revoke_security_group_with_options(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RevokeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RevokeSecurityGroupResponse().from_map(
            self.do_rpcrequest('RevokeSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_security_group_with_options_async(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RevokeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RevokeSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('RevokeSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_security_group(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupRequest,
    ) -> ecs_20140526_models.RevokeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_with_options(request, runtime)

    async def revoke_security_group_async(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupRequest,
    ) -> ecs_20140526_models.RevokeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_security_group_with_options_async(request, runtime)

    def revoke_security_group_egress_with_options(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RevokeSecurityGroupEgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RevokeSecurityGroupEgressResponse().from_map(
            self.do_rpcrequest('RevokeSecurityGroupEgress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_security_group_egress_with_options_async(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RevokeSecurityGroupEgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RevokeSecurityGroupEgressResponse().from_map(
            await self.do_rpcrequest_async('RevokeSecurityGroupEgress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_security_group_egress(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupEgressRequest,
    ) -> ecs_20140526_models.RevokeSecurityGroupEgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_egress_with_options(request, runtime)

    async def revoke_security_group_egress_async(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupEgressRequest,
    ) -> ecs_20140526_models.RevokeSecurityGroupEgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_security_group_egress_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        tmp_req: ecs_20140526_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RunCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = ecs_20140526_models.RunCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RunCommandResponse().from_map(
            self.do_rpcrequest('RunCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_command_with_options_async(
        self,
        tmp_req: ecs_20140526_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RunCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = ecs_20140526_models.RunCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RunCommandResponse().from_map(
            await self.do_rpcrequest_async('RunCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_command(
        self,
        request: ecs_20140526_models.RunCommandRequest,
    ) -> ecs_20140526_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: ecs_20140526_models.RunCommandRequest,
    ) -> ecs_20140526_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def run_instances_with_options(
        self,
        request: ecs_20140526_models.RunInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RunInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RunInstancesResponse().from_map(
            self.do_rpcrequest('RunInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_instances_with_options_async(
        self,
        request: ecs_20140526_models.RunInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RunInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RunInstancesResponse().from_map(
            await self.do_rpcrequest_async('RunInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_instances(
        self,
        request: ecs_20140526_models.RunInstancesRequest,
    ) -> ecs_20140526_models.RunInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_instances_with_options(request, runtime)

    async def run_instances_async(
        self,
        request: ecs_20140526_models.RunInstancesRequest,
    ) -> ecs_20140526_models.RunInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_instances_with_options_async(request, runtime)

    def send_file_with_options(
        self,
        request: ecs_20140526_models.SendFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.SendFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.SendFileResponse().from_map(
            self.do_rpcrequest('SendFile', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_file_with_options_async(
        self,
        request: ecs_20140526_models.SendFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.SendFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.SendFileResponse().from_map(
            await self.do_rpcrequest_async('SendFile', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_file(
        self,
        request: ecs_20140526_models.SendFileRequest,
    ) -> ecs_20140526_models.SendFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_file_with_options(request, runtime)

    async def send_file_async(
        self,
        request: ecs_20140526_models.SendFileRequest,
    ) -> ecs_20140526_models.SendFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_file_with_options_async(request, runtime)

    def start_elasticity_assurance_with_options(
        self,
        request: ecs_20140526_models.StartElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartElasticityAssuranceResponse().from_map(
            self.do_rpcrequest('StartElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_elasticity_assurance_with_options_async(
        self,
        request: ecs_20140526_models.StartElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartElasticityAssuranceResponse().from_map(
            await self.do_rpcrequest_async('StartElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_elasticity_assurance(
        self,
        request: ecs_20140526_models.StartElasticityAssuranceRequest,
    ) -> ecs_20140526_models.StartElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_elasticity_assurance_with_options(request, runtime)

    async def start_elasticity_assurance_async(
        self,
        request: ecs_20140526_models.StartElasticityAssuranceRequest,
    ) -> ecs_20140526_models.StartElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_elasticity_assurance_with_options_async(request, runtime)

    def start_image_pipeline_execution_with_options(
        self,
        request: ecs_20140526_models.StartImagePipelineExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartImagePipelineExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartImagePipelineExecutionResponse().from_map(
            self.do_rpcrequest('StartImagePipelineExecution', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_image_pipeline_execution_with_options_async(
        self,
        request: ecs_20140526_models.StartImagePipelineExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartImagePipelineExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartImagePipelineExecutionResponse().from_map(
            await self.do_rpcrequest_async('StartImagePipelineExecution', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_image_pipeline_execution(
        self,
        request: ecs_20140526_models.StartImagePipelineExecutionRequest,
    ) -> ecs_20140526_models.StartImagePipelineExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_image_pipeline_execution_with_options(request, runtime)

    async def start_image_pipeline_execution_async(
        self,
        request: ecs_20140526_models.StartImagePipelineExecutionRequest,
    ) -> ecs_20140526_models.StartImagePipelineExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_image_pipeline_execution_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: ecs_20140526_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartInstanceResponse().from_map(
            self.do_rpcrequest('StartInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: ecs_20140526_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartInstanceResponse().from_map(
            await self.do_rpcrequest_async('StartInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(
        self,
        request: ecs_20140526_models.StartInstanceRequest,
    ) -> ecs_20140526_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: ecs_20140526_models.StartInstanceRequest,
    ) -> ecs_20140526_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def start_instances_with_options(
        self,
        request: ecs_20140526_models.StartInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartInstancesResponse().from_map(
            self.do_rpcrequest('StartInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_instances_with_options_async(
        self,
        request: ecs_20140526_models.StartInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartInstancesResponse().from_map(
            await self.do_rpcrequest_async('StartInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instances(
        self,
        request: ecs_20140526_models.StartInstancesRequest,
    ) -> ecs_20140526_models.StartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instances_with_options(request, runtime)

    async def start_instances_async(
        self,
        request: ecs_20140526_models.StartInstancesRequest,
    ) -> ecs_20140526_models.StartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instances_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: ecs_20140526_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInstanceResponse().from_map(
            self.do_rpcrequest('StopInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: ecs_20140526_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInstanceResponse().from_map(
            await self.do_rpcrequest_async('StopInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_instance(
        self,
        request: ecs_20140526_models.StopInstanceRequest,
    ) -> ecs_20140526_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: ecs_20140526_models.StopInstanceRequest,
    ) -> ecs_20140526_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def stop_instances_with_options(
        self,
        request: ecs_20140526_models.StopInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInstancesResponse().from_map(
            self.do_rpcrequest('StopInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_instances_with_options_async(
        self,
        request: ecs_20140526_models.StopInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInstancesResponse().from_map(
            await self.do_rpcrequest_async('StopInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_instances(
        self,
        request: ecs_20140526_models.StopInstancesRequest,
    ) -> ecs_20140526_models.StopInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instances_with_options(request, runtime)

    async def stop_instances_async(
        self,
        request: ecs_20140526_models.StopInstancesRequest,
    ) -> ecs_20140526_models.StopInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instances_with_options_async(request, runtime)

    def stop_invocation_with_options(
        self,
        request: ecs_20140526_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInvocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInvocationResponse().from_map(
            self.do_rpcrequest('StopInvocation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_invocation_with_options_async(
        self,
        request: ecs_20140526_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInvocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInvocationResponse().from_map(
            await self.do_rpcrequest_async('StopInvocation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_invocation(
        self,
        request: ecs_20140526_models.StopInvocationRequest,
    ) -> ecs_20140526_models.StopInvocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    async def stop_invocation_async(
        self,
        request: ecs_20140526_models.StopInvocationRequest,
    ) -> ecs_20140526_models.StopInvocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_invocation_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ecs_20140526_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ecs_20140526_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: ecs_20140526_models.TagResourcesRequest,
    ) -> ecs_20140526_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ecs_20140526_models.TagResourcesRequest,
    ) -> ecs_20140526_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def terminate_physical_connection_with_options(
        self,
        request: ecs_20140526_models.TerminatePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TerminatePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TerminatePhysicalConnectionResponse().from_map(
            self.do_rpcrequest('TerminatePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def terminate_physical_connection_with_options_async(
        self,
        request: ecs_20140526_models.TerminatePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TerminatePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TerminatePhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('TerminatePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_physical_connection(
        self,
        request: ecs_20140526_models.TerminatePhysicalConnectionRequest,
    ) -> ecs_20140526_models.TerminatePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_physical_connection_with_options(request, runtime)

    async def terminate_physical_connection_async(
        self,
        request: ecs_20140526_models.TerminatePhysicalConnectionRequest,
    ) -> ecs_20140526_models.TerminatePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_physical_connection_with_options_async(request, runtime)

    def terminate_virtual_border_router_with_options(
        self,
        request: ecs_20140526_models.TerminateVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TerminateVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TerminateVirtualBorderRouterResponse().from_map(
            self.do_rpcrequest('TerminateVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def terminate_virtual_border_router_with_options_async(
        self,
        request: ecs_20140526_models.TerminateVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TerminateVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TerminateVirtualBorderRouterResponse().from_map(
            await self.do_rpcrequest_async('TerminateVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_virtual_border_router(
        self,
        request: ecs_20140526_models.TerminateVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.TerminateVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_virtual_border_router_with_options(request, runtime)

    async def terminate_virtual_border_router_async(
        self,
        request: ecs_20140526_models.TerminateVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.TerminateVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_virtual_border_router_with_options_async(request, runtime)

    def unassign_ipv_6addresses_with_options(
        self,
        request: ecs_20140526_models.UnassignIpv6AddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassignIpv6AddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassignIpv6AddressesResponse().from_map(
            self.do_rpcrequest('UnassignIpv6Addresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassign_ipv_6addresses_with_options_async(
        self,
        request: ecs_20140526_models.UnassignIpv6AddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassignIpv6AddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassignIpv6AddressesResponse().from_map(
            await self.do_rpcrequest_async('UnassignIpv6Addresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassign_ipv_6addresses(
        self,
        request: ecs_20140526_models.UnassignIpv6AddressesRequest,
    ) -> ecs_20140526_models.UnassignIpv6AddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassign_ipv_6addresses_with_options(request, runtime)

    async def unassign_ipv_6addresses_async(
        self,
        request: ecs_20140526_models.UnassignIpv6AddressesRequest,
    ) -> ecs_20140526_models.UnassignIpv6AddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassign_ipv_6addresses_with_options_async(request, runtime)

    def unassign_private_ip_addresses_with_options(
        self,
        request: ecs_20140526_models.UnassignPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassignPrivateIpAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassignPrivateIpAddressesResponse().from_map(
            self.do_rpcrequest('UnassignPrivateIpAddresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassign_private_ip_addresses_with_options_async(
        self,
        request: ecs_20140526_models.UnassignPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassignPrivateIpAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassignPrivateIpAddressesResponse().from_map(
            await self.do_rpcrequest_async('UnassignPrivateIpAddresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassign_private_ip_addresses(
        self,
        request: ecs_20140526_models.UnassignPrivateIpAddressesRequest,
    ) -> ecs_20140526_models.UnassignPrivateIpAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassign_private_ip_addresses_with_options(request, runtime)

    async def unassign_private_ip_addresses_async(
        self,
        request: ecs_20140526_models.UnassignPrivateIpAddressesRequest,
    ) -> ecs_20140526_models.UnassignPrivateIpAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassign_private_ip_addresses_with_options_async(request, runtime)

    def unassociate_eip_address_with_options(
        self,
        request: ecs_20140526_models.UnassociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassociateEipAddressResponse().from_map(
            self.do_rpcrequest('UnassociateEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_eip_address_with_options_async(
        self,
        request: ecs_20140526_models.UnassociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassociateEipAddressResponse().from_map(
            await self.do_rpcrequest_async('UnassociateEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_eip_address(
        self,
        request: ecs_20140526_models.UnassociateEipAddressRequest,
    ) -> ecs_20140526_models.UnassociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_eip_address_with_options(request, runtime)

    async def unassociate_eip_address_async(
        self,
        request: ecs_20140526_models.UnassociateEipAddressRequest,
    ) -> ecs_20140526_models.UnassociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_eip_address_with_options_async(request, runtime)

    def unassociate_ha_vip_with_options(
        self,
        request: ecs_20140526_models.UnassociateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassociateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassociateHaVipResponse().from_map(
            self.do_rpcrequest('UnassociateHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_ha_vip_with_options_async(
        self,
        request: ecs_20140526_models.UnassociateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassociateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassociateHaVipResponse().from_map(
            await self.do_rpcrequest_async('UnassociateHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_ha_vip(
        self,
        request: ecs_20140526_models.UnassociateHaVipRequest,
    ) -> ecs_20140526_models.UnassociateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_ha_vip_with_options(request, runtime)

    async def unassociate_ha_vip_async(
        self,
        request: ecs_20140526_models.UnassociateHaVipRequest,
    ) -> ecs_20140526_models.UnassociateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_ha_vip_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ecs_20140526_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ecs_20140526_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: ecs_20140526_models.UntagResourcesRequest,
    ) -> ecs_20140526_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ecs_20140526_models.UntagResourcesRequest,
    ) -> ecs_20140526_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
