# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cudo_compute.api_client import ApiClient


class MachineTypesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_machine_type(self, data_center_id, machine_type, **kwargs):  # noqa: E501
        """Get a machine type in a data center  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_machine_type(data_center_id, machine_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_center_id: (required)
        :param str machine_type: (required)
        :return: GetMachineTypeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_machine_type_with_http_info(data_center_id, machine_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_machine_type_with_http_info(data_center_id, machine_type, **kwargs)  # noqa: E501
            return data

    def get_machine_type_with_http_info(self, data_center_id, machine_type, **kwargs):  # noqa: E501
        """Get a machine type in a data center  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_machine_type_with_http_info(data_center_id, machine_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_center_id: (required)
        :param str machine_type: (required)
        :return: GetMachineTypeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_center_id', 'machine_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_machine_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_center_id' is set
        if self.api_client.client_side_validation and ('data_center_id' not in params or
                                                       params['data_center_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_center_id` when calling `get_machine_type`")  # noqa: E501
        # verify the required parameter 'machine_type' is set
        if self.api_client.client_side_validation and ('machine_type' not in params or
                                                       params['machine_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `machine_type` when calling `get_machine_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_center_id' in params:
            path_params['dataCenterId'] = params['data_center_id']  # noqa: E501
        if 'machine_type' in params:
            path_params['machineType'] = params['machine_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/data-centers/{dataCenterId}/machine-types/{machineType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetMachineTypeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_machine_type_live_utilization(self, data_center_id, machine_type, **kwargs):  # noqa: E501
        """Get the utilization for a machine type in a data center  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_machine_type_live_utilization(data_center_id, machine_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_center_id: (required)
        :param str machine_type: (required)
        :return: GetMachineTypeLiveUtilizationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_machine_type_live_utilization_with_http_info(data_center_id, machine_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_machine_type_live_utilization_with_http_info(data_center_id, machine_type, **kwargs)  # noqa: E501
            return data

    def get_machine_type_live_utilization_with_http_info(self, data_center_id, machine_type, **kwargs):  # noqa: E501
        """Get the utilization for a machine type in a data center  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_machine_type_live_utilization_with_http_info(data_center_id, machine_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_center_id: (required)
        :param str machine_type: (required)
        :return: GetMachineTypeLiveUtilizationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_center_id', 'machine_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_machine_type_live_utilization" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_center_id' is set
        if self.api_client.client_side_validation and ('data_center_id' not in params or
                                                       params['data_center_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_center_id` when calling `get_machine_type_live_utilization`")  # noqa: E501
        # verify the required parameter 'machine_type' is set
        if self.api_client.client_side_validation and ('machine_type' not in params or
                                                       params['machine_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `machine_type` when calling `get_machine_type_live_utilization`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_center_id' in params:
            path_params['dataCenterId'] = params['data_center_id']  # noqa: E501
        if 'machine_type' in params:
            path_params['machineType'] = params['machine_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/data-centers/{dataCenterId}/machine-types/{machineType}/live-utilization', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetMachineTypeLiveUtilizationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_machine_types(self, data_center_id, **kwargs):  # noqa: E501
        """List machine types for a data center  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_machine_types(data_center_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_center_id: (required)
        :return: ListMachineTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_machine_types_with_http_info(data_center_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_machine_types_with_http_info(data_center_id, **kwargs)  # noqa: E501
            return data

    def list_machine_types_with_http_info(self, data_center_id, **kwargs):  # noqa: E501
        """List machine types for a data center  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_machine_types_with_http_info(data_center_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_center_id: (required)
        :return: ListMachineTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_center_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_machine_types" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_center_id' is set
        if self.api_client.client_side_validation and ('data_center_id' not in params or
                                                       params['data_center_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_center_id` when calling `list_machine_types`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_center_id' in params:
            path_params['dataCenterId'] = params['data_center_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/data-centers/{dataCenterId}/machine-types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListMachineTypesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
