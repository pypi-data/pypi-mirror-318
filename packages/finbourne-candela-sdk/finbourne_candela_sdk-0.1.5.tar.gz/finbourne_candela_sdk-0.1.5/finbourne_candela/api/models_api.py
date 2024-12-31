# coding: utf-8

"""
    FINBOURNE Candela Platform Web API

    FINBOURNE Technology  # noqa: E501

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic.v1 import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from pydantic.v1 import StrictBool, StrictStr

from typing import List, Optional

from finbourne_candela.models.object_metadata import ObjectMetadata

from finbourne_candela.api_client import ApiClient
from finbourne_candela.api_response import ApiResponse
from finbourne_candela.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from finbourne_candela.extensions.configuration_options import ConfigurationOptions


class ModelsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def add_model(self, hf_url : StrictStr, scope : StrictStr, identifier : StrictStr, quantisation : StrictStr, description : StrictStr, version_bump : Optional[StrictStr] = None, system_level : Optional[StrictBool] = None, **kwargs) -> None:  # noqa: E501
        ...

    @overload
    def add_model(self, hf_url : StrictStr, scope : StrictStr, identifier : StrictStr, quantisation : StrictStr, description : StrictStr, version_bump : Optional[StrictStr] = None, system_level : Optional[StrictBool] = None, async_req: Optional[bool]=True, **kwargs) -> None:  # noqa: E501
        ...

    @validate_arguments
    def add_model(self, hf_url : StrictStr, scope : StrictStr, identifier : StrictStr, quantisation : StrictStr, description : StrictStr, version_bump : Optional[StrictStr] = None, system_level : Optional[StrictBool] = None, async_req: Optional[bool]=None, **kwargs) -> Union[None, Awaitable[None]]:  # noqa: E501
        """Add an LLM model to Candela.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_model(hf_url, scope, identifier, quantisation, description, version_bump, system_level, async_req=True)
        >>> result = thread.get()

        :param hf_url: (required)
        :type hf_url: str
        :param scope: (required)
        :type scope: str
        :param identifier: (required)
        :type identifier: str
        :param quantisation: (required)
        :type quantisation: str
        :param description: (required)
        :type description: str
        :param version_bump:
        :type version_bump: str
        :param system_level:
        :type system_level: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the add_model_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.add_model_with_http_info(hf_url, scope, identifier, quantisation, description, version_bump, system_level, **kwargs)  # noqa: E501

    @validate_arguments
    def add_model_with_http_info(self, hf_url : StrictStr, scope : StrictStr, identifier : StrictStr, quantisation : StrictStr, description : StrictStr, version_bump : Optional[StrictStr] = None, system_level : Optional[StrictBool] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Add an LLM model to Candela.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_model_with_http_info(hf_url, scope, identifier, quantisation, description, version_bump, system_level, async_req=True)
        >>> result = thread.get()

        :param hf_url: (required)
        :type hf_url: str
        :param scope: (required)
        :type scope: str
        :param identifier: (required)
        :type identifier: str
        :param quantisation: (required)
        :type quantisation: str
        :param description: (required)
        :type description: str
        :param version_bump:
        :type version_bump: str
        :param system_level:
        :type system_level: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'hf_url',
            'scope',
            'identifier',
            'quantisation',
            'description',
            'version_bump',
            'system_level'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_model" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('hf_url') is not None:  # noqa: E501
            _query_params.append(('hf_url', _params['hf_url']))

        if _params.get('scope') is not None:  # noqa: E501
            _query_params.append(('scope', _params['scope']))

        if _params.get('identifier') is not None:  # noqa: E501
            _query_params.append(('identifier', _params['identifier']))

        if _params.get('quantisation') is not None:  # noqa: E501
            _query_params.append(('quantisation', _params['quantisation']))

        if _params.get('description') is not None:  # noqa: E501
            _query_params.append(('description', _params['description']))

        if _params.get('version_bump') is not None:  # noqa: E501
            _query_params.append(('version_bump', _params['version_bump']))

        if _params.get('system_level') is not None:  # noqa: E501
            _query_params.append(('system_level', _params['system_level']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['HTTPBearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/models/', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def delete_model(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, **kwargs) -> List[ObjectMetadata]:  # noqa: E501
        ...

    @overload
    def delete_model(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, async_req: Optional[bool]=True, **kwargs) -> List[ObjectMetadata]:  # noqa: E501
        ...

    @validate_arguments
    def delete_model(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, async_req: Optional[bool]=None, **kwargs) -> Union[List[ObjectMetadata], Awaitable[List[ObjectMetadata]]]:  # noqa: E501
        """Delete a model in Candela.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_model(scope, identifier, version, async_req=True)
        >>> result = thread.get()

        :param scope: (required)
        :type scope: str
        :param identifier: (required)
        :type identifier: str
        :param version:
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[ObjectMetadata]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the delete_model_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.delete_model_with_http_info(scope, identifier, version, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_model_with_http_info(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Delete a model in Candela.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_model_with_http_info(scope, identifier, version, async_req=True)
        >>> result = thread.get()

        :param scope: (required)
        :type scope: str
        :param identifier: (required)
        :type identifier: str
        :param version:
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[ObjectMetadata], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'scope',
            'identifier',
            'version'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_model" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('scope') is not None:  # noqa: E501
            _query_params.append(('scope', _params['scope']))

        if _params.get('identifier') is not None:  # noqa: E501
            _query_params.append(('identifier', _params['identifier']))

        if _params.get('version') is not None:  # noqa: E501
            _query_params.append(('version', _params['version']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['HTTPBearer']  # noqa: E501

        _response_types_map = {
            '200': "List[ObjectMetadata]",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/models/', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def get_model_metadata(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, **kwargs) -> ObjectMetadata:  # noqa: E501
        ...

    @overload
    def get_model_metadata(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, async_req: Optional[bool]=True, **kwargs) -> ObjectMetadata:  # noqa: E501
        ...

    @validate_arguments
    def get_model_metadata(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, async_req: Optional[bool]=None, **kwargs) -> Union[ObjectMetadata, Awaitable[ObjectMetadata]]:  # noqa: E501
        """Get metadata for a model in Candela.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_model_metadata(scope, identifier, version, async_req=True)
        >>> result = thread.get()

        :param scope: (required)
        :type scope: str
        :param identifier: (required)
        :type identifier: str
        :param version:
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ObjectMetadata
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_model_metadata_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_model_metadata_with_http_info(scope, identifier, version, **kwargs)  # noqa: E501

    @validate_arguments
    def get_model_metadata_with_http_info(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get metadata for a model in Candela.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_model_metadata_with_http_info(scope, identifier, version, async_req=True)
        >>> result = thread.get()

        :param scope: (required)
        :type scope: str
        :param identifier: (required)
        :type identifier: str
        :param version:
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ObjectMetadata, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'scope',
            'identifier',
            'version'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_model_metadata" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('scope') is not None:  # noqa: E501
            _query_params.append(('scope', _params['scope']))

        if _params.get('identifier') is not None:  # noqa: E501
            _query_params.append(('identifier', _params['identifier']))

        if _params.get('version') is not None:  # noqa: E501
            _query_params.append(('version', _params['version']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['HTTPBearer']  # noqa: E501

        _response_types_map = {
            '200': "ObjectMetadata",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/models/metadata', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def list_models(self, all_versions : Optional[StrictBool] = None, **kwargs) -> List[ObjectMetadata]:  # noqa: E501
        ...

    @overload
    def list_models(self, all_versions : Optional[StrictBool] = None, async_req: Optional[bool]=True, **kwargs) -> List[ObjectMetadata]:  # noqa: E501
        ...

    @validate_arguments
    def list_models(self, all_versions : Optional[StrictBool] = None, async_req: Optional[bool]=None, **kwargs) -> Union[List[ObjectMetadata], Awaitable[List[ObjectMetadata]]]:  # noqa: E501
        """List all models available to you in Candela.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_models(all_versions, async_req=True)
        >>> result = thread.get()

        :param all_versions:
        :type all_versions: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[ObjectMetadata]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_models_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.list_models_with_http_info(all_versions, **kwargs)  # noqa: E501

    @validate_arguments
    def list_models_with_http_info(self, all_versions : Optional[StrictBool] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List all models available to you in Candela.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_models_with_http_info(all_versions, async_req=True)
        >>> result = thread.get()

        :param all_versions:
        :type all_versions: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[ObjectMetadata], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'all_versions'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_models" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('all_versions') is not None:  # noqa: E501
            _query_params.append(('all_versions', _params['all_versions']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['HTTPBearer']  # noqa: E501

        _response_types_map = {
            '200': "List[ObjectMetadata]",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/models/list', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def model_exists(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, **kwargs) -> bool:  # noqa: E501
        ...

    @overload
    def model_exists(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, async_req: Optional[bool]=True, **kwargs) -> bool:  # noqa: E501
        ...

    @validate_arguments
    def model_exists(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, async_req: Optional[bool]=None, **kwargs) -> Union[bool, Awaitable[bool]]:  # noqa: E501
        """Check that a model exists in Candela.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.model_exists(scope, identifier, version, async_req=True)
        >>> result = thread.get()

        :param scope: (required)
        :type scope: str
        :param identifier: (required)
        :type identifier: str
        :param version:
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bool
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the model_exists_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.model_exists_with_http_info(scope, identifier, version, **kwargs)  # noqa: E501

    @validate_arguments
    def model_exists_with_http_info(self, scope : StrictStr, identifier : StrictStr, version : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Check that a model exists in Candela.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.model_exists_with_http_info(scope, identifier, version, async_req=True)
        >>> result = thread.get()

        :param scope: (required)
        :type scope: str
        :param identifier: (required)
        :type identifier: str
        :param version:
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(bool, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'scope',
            'identifier',
            'version'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method model_exists" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('scope') is not None:  # noqa: E501
            _query_params.append(('scope', _params['scope']))

        if _params.get('identifier') is not None:  # noqa: E501
            _query_params.append(('identifier', _params['identifier']))

        if _params.get('version') is not None:  # noqa: E501
            _query_params.append(('version', _params['version']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['HTTPBearer']  # noqa: E501

        _response_types_map = {
            '200': "bool",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/models/exists', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
