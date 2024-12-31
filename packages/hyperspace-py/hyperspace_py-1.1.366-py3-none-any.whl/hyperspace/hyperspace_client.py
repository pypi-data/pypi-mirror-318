# coding: utf-8
"""
    Vector Similarity Demo

    The test functionality and Query testing  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@hyper-space.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
from __future__ import absolute_import

from typing import Optional, List, Dict
import msgpack
from types import MethodType
from hyperspace.rest import RESTResponse
import logging
from urllib.parse import urlencode
import re
import hyperspace.models
from hyperspace.api.hyperspace_api import HyperspaceApi
from hyperspace.api_client import *
import os
import stat
# python 2 and python 3 compatibility library
from hyperspace.rest import ApiException

import types
import tempfile
import inspect


try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')

logger = logging.getLogger(__name__)


class HyperspaceClientApi(HyperspaceApi):
    """Generic API client for Swagger client library builds.

    Swagger generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the Swagger
    templates.

    NOTE: This class is auto generated by the swagger code generator program.
    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    """
    def __init__(self, host, username, password, token=None):
        self.configuration = hyperspace.configuration.Configuration()
        self.configuration.host = host
        if token is not None:
            self._token = token
        else:
            self.username = username
            self.password = password
            api_client = hyperspace.api_client.ApiClient(configuration=self.configuration)
            super().__init__(api_client=api_client)
            body = {"username": username, "password": password}
            login_response = self.login(body)
            self._token = "Bearer " + login_response.token
        api_client = hyperspace.api_client.ApiClient(configuration=self.configuration, header_name='Authorization',
                                                     header_value=self._token)
        super().__init__(api_client=api_client)
        old_func_call_api = self.api_client.call_api
        self.api_client.rest_client.request = MethodType(better_request, self.api_client.rest_client)

        def retry_jwt(*args, **kwargs):
            try:
                return old_func_call_api(*args, **kwargs)
            except ApiException as e:
                if "token expired" in str(e.body):
                    login_body = {"username": username, "password": password}
                    login_response = self.login(login_body)
                    self._token = "Bearer " + login_response.token
                    api_client.set_default_header('Authorization', self._token)
                    return old_func_call_api(*args, **kwargs)
                else:
                    raise

        self.api_client.call_api = retry_jwt


    def search(self, body, size, collection_name, function_name: Optional[str] = None, fields: Optional[List[str]] = None, source=False, **kwargs):  # noqa: E501
        source = "true" if source is True else "false"
        new_body = msgpack.packb({"query": body, "fields": fields})
        if function_name is None:
            return super().search(new_body, size, collection_name, source=source, **kwargs)
        else:
            return super().search(new_body, size, collection_name, function_name=function_name, source=source, **kwargs)

    def dsl_search(self, body, size, collection_name, source=False, **kwargs):  # noqa: E501
        source = "true" if source is True else "false"
        return super().dsl_search(body=body, size=size, collection_name=collection_name, source=source, **kwargs)

    def add_batch(self, batch: List[Dict], collection_name: str, **kwargs):
        msgpack_docs = []
        for doc in batch:
            doc_id = doc.get("_id")  # Safely get "_id" with default value as None
            if doc_id is not None:
                msgpack_docs.append({"_id": doc_id, "doc_data": msgpack.packb(doc)})
            else:
                msgpack_docs.append({"_id": "", "doc_data": msgpack.packb(doc)})
        packed_batch = msgpack.packb(msgpack_docs)

        return super().add_batch(packed_batch, collection_name, **kwargs)

    def add_document(self, body, collection_name, **kwargs):
        packed_row = msgpack.packb(body)

        return super().add_document(packed_row, collection_name, **kwargs)

    def get_document(self, collection_name, document_id, metadata_only=False, **kwargs):
        metadata_only = "true" if metadata_only is True else "false"
        vec_to_get = super().get_document(collection_name, document_id, metadata_only=metadata_only, **kwargs)
        vector = msgpack.unpackb(vec_to_get, raw=False)
        return vector

    def update_document(self, body, collection_name, partial_update=False, doc_as_upsert=False, **kwargs):
        partial_update = "true" if partial_update is True else "false"
        doc_as_upsert = "true" if doc_as_upsert is True else "false"
        packed_row_to_update = msgpack.packb(body, use_bin_type=True)
        return super().update_document(body=packed_row_to_update,
                                       collection_name=collection_name,
                                       partial_update=partial_update,
                                       doc_as_upsert=doc_as_upsert, **kwargs)

    def update_by_query(self, body, collection_name, **kwargs):
        packed_row = msgpack.packb(body)
        return super().update_by_query(packed_row, collection_name, **kwargs)

    def set_function(self, function, collection_name, function_name = None, **kwargs):
        if isinstance(function, types.FunctionType):
            if function_name is None:
                function_name = function.__name__
            body = inspect.getsource(function)
        else:
            with open(function) as f:
                body = f.read()
        return super().set_function(body=body, collection_name=collection_name, function_name=function_name, **kwargs)

    def create_collection(self, schema, collection_name, **kwargs):
        if isinstance(schema, dict):
            body = schema
        else:
            with open(schema) as json_file:
                body = json.load(json_file)
        return super().create_collection(body=body, collection_name=collection_name, **kwargs)

    def get_function(self, collection_name, function_name, **kwargs):
        function =super().get_function(collection_name=collection_name, function_name=function_name, **kwargs)
        return function.decode("utf-8")





def better_request(self, method, url, query_params=None, headers=None,
                   body=None, post_params=None, _preload_content=True,
                   _request_timeout=None):
    """Perform requests.

    :param method: http request method
    :param url: http request url
    :param query_params: query parameters in the url
    :param headers: http request headers
    :param body: request json body, for `application/json`
    :param post_params: request post parameters,
                        `application/x-www-form-urlencoded`
                        and `multipart/form-data`
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                             be returned without reading/decoding response
                             data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                             number provided, it will be total request
                             timeout. It can also be a pair (tuple) of
                             (connection, read) timeouts.

    source: hyperspace_api.py request function
    change: add case of binary data with 'Content-Type' of 'application/msgpack'
    """
    method = method.upper()
    assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                      'PATCH', 'OPTIONS']

    if post_params and body:
        raise ValueError(
            "body parameter cannot be used with post_params parameter."
        )

    post_params = post_params or {}
    headers = headers or {}

    timeout = None
    if _request_timeout:
        if isinstance(_request_timeout, (int, ) if six.PY3 else (int, long)):  # noqa: E501,F821
            timeout = urllib3.Timeout(total=_request_timeout)
        elif (isinstance(_request_timeout, tuple) and
              len(_request_timeout) == 2):
            timeout = urllib3.Timeout(
                connect=_request_timeout[0], read=_request_timeout[1])

    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'

    try:
        # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
        if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
            if query_params:
                url += '?' + urlencode(query_params)
            if re.search('json', headers['Content-Type'], re.IGNORECASE):
                request_body = '{}'
                if body is not None:
                    request_body = json.dumps(body)
                r = self.pool_manager.request(
                    method, url,
                    body=request_body,
                    preload_content=_preload_content,
                    timeout=timeout,
                    headers=headers)
            elif headers['Content-Type'] == 'application/x-www-form-urlencoded':  # noqa: E501
                r = self.pool_manager.request(
                    method, url,
                    fields=post_params,
                    encode_multipart=False,
                    preload_content=_preload_content,
                    timeout=timeout,
                    headers=headers)
            elif headers['Content-Type'] == 'multipart/form-data':
                # must del headers['Content-Type'], or the correct
                # Content-Type which generated by urllib3 will be
                # overwritten.
                del headers['Content-Type']
                r = self.pool_manager.request(
                    method, url,
                    fields=post_params,
                    encode_multipart=True,
                    preload_content=_preload_content,
                    timeout=timeout,
                    headers=headers)
            # Pass a `string` parameter directly in the body to support
            # other content types than Json when `body` argument is
            # provided in serialized form
            elif isinstance(body, str) or isinstance(body, bytes):  # new case for binary data
                headers['Content-Type'] = 'application/msgpack'
                request_body = body
                r = self.pool_manager.request(
                    method, url,
                    body=request_body,
                    preload_content=_preload_content,
                    timeout=timeout,
                    headers=headers)
            else:
                # Cannot generate the request from given parameters
                msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                raise ApiException(status=0, reason=msg)
        # For `GET`, `HEAD`
        else:
            r = self.pool_manager.request(method, url,
                                          fields=query_params,
                                          preload_content=_preload_content,
                                          timeout=timeout,
                                          headers=headers)
    except urllib3.exceptions.SSLError as e:
        msg = "{0}\n{1}".format(type(e).__name__, str(e))
        raise ApiException(status=0, reason=msg)

    if _preload_content:
        r = RESTResponse(r)

        # log response body
        logger.debug("response body: %s", r.data)

    if not 200 <= r.status <= 299:
        raise ApiException(http_resp=r)

    return r

