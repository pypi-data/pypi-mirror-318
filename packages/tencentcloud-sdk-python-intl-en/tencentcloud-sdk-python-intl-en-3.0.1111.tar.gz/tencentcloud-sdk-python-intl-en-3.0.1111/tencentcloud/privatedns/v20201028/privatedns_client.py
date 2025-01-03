# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.privatedns.v20201028 import models


class PrivatednsClient(AbstractClient):
    _apiVersion = '2020-10-28'
    _endpoint = 'privatedns.tencentcloudapi.com'
    _service = 'privatedns'


    def CreateEndPoint(self, request):
        """This API is used to create an endpoint.

        :param request: Request instance for CreateEndPoint.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreateEndPointRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreateEndPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEndPoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEndPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEndPointAndEndPointService(self, request):
        """This API is used to create an endpoint and an endpoint service simultaneously.

        :param request: Request instance for CreateEndPointAndEndPointService.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreateEndPointAndEndPointServiceRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreateEndPointAndEndPointServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEndPointAndEndPointService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEndPointAndEndPointServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateForwardRule(self, request):
        """This API is used to create a custom forwarding rule.

        :param request: Request instance for CreateForwardRule.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreateForwardRuleRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreateForwardRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateForwardRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateForwardRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateDNSAccount(self, request):
        """This API is used to create a Private DNS account.

        :param request: Request instance for CreatePrivateDNSAccount.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateDNSAccountRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateDNSAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateDNSAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateDNSAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateZone(self, request):
        """This API is used to create a private domain.

        :param request: Request instance for CreatePrivateZone.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateZone", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateZoneRecord(self, request):
        """This API is used to add a DNS record for a private domain.

        :param request: Request instance for CreatePrivateZoneRecord.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneRecordRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.CreatePrivateZoneRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateZoneRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateZoneRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivateZoneRecord(self, request):
        """This API is used to delete a DNS record for a private domain.

        :param request: Request instance for DeletePrivateZoneRecord.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateZoneRecordRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DeletePrivateZoneRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateZoneRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivateZoneRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountVpcList(self, request):
        """This API is used to get the VPC list of a Private DNS account.

        :param request: Request instance for DescribeAccountVpcList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeAccountVpcListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeAccountVpcListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountVpcList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountVpcListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditLog(self, request):
        """This API is used to get the list of operation logs.

        :param request: Request instance for DescribeAuditLog.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeAuditLogRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeAuditLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDashboard(self, request):
        """This API is used to get the overview of private DNS records.

        :param request: Request instance for DescribeDashboard.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeDashboardRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEndPointList(self, request):
        """This API is used to obtain the endpoint list.

        :param request: Request instance for DescribeEndPointList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeEndPointListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeEndPointListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEndPointList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEndPointListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeForwardRuleList(self, request):
        """This API is used to query the forwarding rule list.

        :param request: Request instance for DescribeForwardRuleList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeForwardRuleListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeForwardRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeForwardRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeForwardRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateDNSAccountList(self, request):
        """This API is used to get the list of Private DNS accounts.

        :param request: Request instance for DescribePrivateDNSAccountList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateDNSAccountListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateDNSAccountListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateDNSAccountList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateDNSAccountListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateZoneList(self, request):
        """This API is used to obtain the private domain list.

        :param request: Request instance for DescribePrivateZoneList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateZoneList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateZoneListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateZoneRecordList(self, request):
        """This API is used to get the list of records for a private domain.

        :param request: Request instance for DescribePrivateZoneRecordList.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneRecordListRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateZoneRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateZoneRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateZoneService(self, request):
        """This API is used to query the Private DNS activation status.

        :param request: Request instance for DescribePrivateZoneService.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneServiceRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribePrivateZoneServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateZoneService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateZoneServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuotaUsage(self, request):
        """This API is used to query quota usage.

        :param request: Request instance for DescribeQuotaUsage.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeQuotaUsageRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeQuotaUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuotaUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuotaUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRequestData(self, request):
        """This API is used to get the DNS request volume of a private domain.

        :param request: Request instance for DescribeRequestData.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.DescribeRequestDataRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.DescribeRequestDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRequestData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRequestDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateZone(self, request):
        """This API is used to modify a private domain.

        :param request: Request instance for ModifyPrivateZone.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateZone", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateZoneRecord(self, request):
        """This API is used to modify a DNS record for a private domain.

        :param request: Request instance for ModifyPrivateZoneRecord.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneRecordRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateZoneRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateZoneRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateZoneVpc(self, request):
        """This API is used to modify the VPC associated with a private domain.

        :param request: Request instance for ModifyPrivateZoneVpc.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneVpcRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyPrivateZoneVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateZoneVpc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateZoneVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordsStatus(self, request):
        """This API is used to modify the DNS record status.

        :param request: Request instance for ModifyRecordsStatus.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.ModifyRecordsStatusRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ModifyRecordsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubscribePrivateZoneService(self, request):
        """This API is used to activate the Private DNS service.

        :param request: Request instance for SubscribePrivateZoneService.
        :type request: :class:`tencentcloud.privatedns.v20201028.models.SubscribePrivateZoneServiceRequest`
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.SubscribePrivateZoneServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubscribePrivateZoneService", params, headers=headers)
            response = json.loads(body)
            model = models.SubscribePrivateZoneServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))