# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Unit Tests for ResourceControllerV2
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.resource_controller_v2 import *


_service = ResourceControllerV2(authenticator=NoAuthAuthenticator())

_base_url = 'https://resource-controller.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: ResourceInstances
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ResourceControllerV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ResourceControllerV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ResourceControllerV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListResourceInstances:
    """
    Test Class for list_resource_instances
    """

    @responses.activate
    def test_list_resource_instances_all_params(self):
        """
        list_resource_instances()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        guid = 'testString'
        name = 'testString'
        resource_group_id = 'testString'
        resource_id = 'testString'
        resource_plan_id = 'testString'
        type = 'testString'
        sub_type = 'testString'
        limit = 100
        start = 'testString'
        state = 'active'
        updated_from = '2021-01-01'
        updated_to = '2021-01-01'

        # Invoke method
        response = _service.list_resource_instances(
            guid=guid,
            name=name,
            resource_group_id=resource_group_id,
            resource_id=resource_id,
            resource_plan_id=resource_plan_id,
            type=type,
            sub_type=sub_type,
            limit=limit,
            start=start,
            state=state,
            updated_from=updated_from,
            updated_to=updated_to,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'guid={}'.format(guid) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'resource_plan_id={}'.format(resource_plan_id) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'sub_type={}'.format(sub_type) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'state={}'.format(state) in query_string
        assert 'updated_from={}'.format(updated_from) in query_string
        assert 'updated_to={}'.format(updated_to) in query_string

    def test_list_resource_instances_all_params_with_retries(self):
        # Enable retries and run test_list_resource_instances_all_params.
        _service.enable_retries()
        self.test_list_resource_instances_all_params()

        # Disable retries and run test_list_resource_instances_all_params.
        _service.disable_retries()
        self.test_list_resource_instances_all_params()

    @responses.activate
    def test_list_resource_instances_required_params(self):
        """
        test_list_resource_instances_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.list_resource_instances()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_resource_instances_required_params_with_retries(self):
        # Enable retries and run test_list_resource_instances_required_params.
        _service.enable_retries()
        self.test_list_resource_instances_required_params()

        # Disable retries and run test_list_resource_instances_required_params.
        _service.disable_retries()
        self.test_list_resource_instances_required_params()

    @responses.activate
    def test_list_resource_instances_with_pager_get_next(self):
        """
        test_list_resource_instances_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_instances')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","scheduled_reclaim_at":"2019-01-01T12:00:00.000Z","restored_at":"2019-01-01T12:00:00.000Z","restored_by":"restored_by","scheduled_reclaim_by":"scheduled_reclaim_by","name":"name","region_id":"region_id","account_id":"account_id","reseller_channel_id":"reseller_channel_id","resource_plan_id":"resource_plan_id","resource_group_id":"resource_group_id","resource_group_crn":"resource_group_crn","target_crn":"target_crn","parameters":{"anyKey":"anyValue"},"allow_cleanup":false,"crn":"crn","state":"active","type":"type","sub_type":"sub_type","resource_id":"resource_id","dashboard_url":"dashboard_url","last_operation":{"type":"type","state":"in progress","sub_type":"sub_type","async":true,"description":"description","reason_code":"reason_code","poll_after":10,"cancelable":true,"poll":true},"resource_aliases_url":"resource_aliases_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url","plan_history":[{"resource_plan_id":"resource_plan_id","start_date":"2019-01-01T12:00:00.000Z","requestor_id":"requestor_id"}],"migrated":true,"extensions":{"anyKey":"anyValue"},"controlled_by":"controlled_by","locked":true}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","scheduled_reclaim_at":"2019-01-01T12:00:00.000Z","restored_at":"2019-01-01T12:00:00.000Z","restored_by":"restored_by","scheduled_reclaim_by":"scheduled_reclaim_by","name":"name","region_id":"region_id","account_id":"account_id","reseller_channel_id":"reseller_channel_id","resource_plan_id":"resource_plan_id","resource_group_id":"resource_group_id","resource_group_crn":"resource_group_crn","target_crn":"target_crn","parameters":{"anyKey":"anyValue"},"allow_cleanup":false,"crn":"crn","state":"active","type":"type","sub_type":"sub_type","resource_id":"resource_id","dashboard_url":"dashboard_url","last_operation":{"type":"type","state":"in progress","sub_type":"sub_type","async":true,"description":"description","reason_code":"reason_code","poll_after":10,"cancelable":true,"poll":true},"resource_aliases_url":"resource_aliases_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url","plan_history":[{"resource_plan_id":"resource_plan_id","start_date":"2019-01-01T12:00:00.000Z","requestor_id":"requestor_id"}],"migrated":true,"extensions":{"anyKey":"anyValue"},"controlled_by":"controlled_by","locked":true}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = ResourceInstancesPager(
            client=_service,
            guid='testString',
            name='testString',
            resource_group_id='testString',
            resource_id='testString',
            resource_plan_id='testString',
            type='testString',
            sub_type='testString',
            limit=10,
            state='active',
            updated_from='2021-01-01',
            updated_to='2021-01-01',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_resource_instances_with_pager_get_all(self):
        """
        test_list_resource_instances_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_instances')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","scheduled_reclaim_at":"2019-01-01T12:00:00.000Z","restored_at":"2019-01-01T12:00:00.000Z","restored_by":"restored_by","scheduled_reclaim_by":"scheduled_reclaim_by","name":"name","region_id":"region_id","account_id":"account_id","reseller_channel_id":"reseller_channel_id","resource_plan_id":"resource_plan_id","resource_group_id":"resource_group_id","resource_group_crn":"resource_group_crn","target_crn":"target_crn","parameters":{"anyKey":"anyValue"},"allow_cleanup":false,"crn":"crn","state":"active","type":"type","sub_type":"sub_type","resource_id":"resource_id","dashboard_url":"dashboard_url","last_operation":{"type":"type","state":"in progress","sub_type":"sub_type","async":true,"description":"description","reason_code":"reason_code","poll_after":10,"cancelable":true,"poll":true},"resource_aliases_url":"resource_aliases_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url","plan_history":[{"resource_plan_id":"resource_plan_id","start_date":"2019-01-01T12:00:00.000Z","requestor_id":"requestor_id"}],"migrated":true,"extensions":{"anyKey":"anyValue"},"controlled_by":"controlled_by","locked":true}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","scheduled_reclaim_at":"2019-01-01T12:00:00.000Z","restored_at":"2019-01-01T12:00:00.000Z","restored_by":"restored_by","scheduled_reclaim_by":"scheduled_reclaim_by","name":"name","region_id":"region_id","account_id":"account_id","reseller_channel_id":"reseller_channel_id","resource_plan_id":"resource_plan_id","resource_group_id":"resource_group_id","resource_group_crn":"resource_group_crn","target_crn":"target_crn","parameters":{"anyKey":"anyValue"},"allow_cleanup":false,"crn":"crn","state":"active","type":"type","sub_type":"sub_type","resource_id":"resource_id","dashboard_url":"dashboard_url","last_operation":{"type":"type","state":"in progress","sub_type":"sub_type","async":true,"description":"description","reason_code":"reason_code","poll_after":10,"cancelable":true,"poll":true},"resource_aliases_url":"resource_aliases_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url","plan_history":[{"resource_plan_id":"resource_plan_id","start_date":"2019-01-01T12:00:00.000Z","requestor_id":"requestor_id"}],"migrated":true,"extensions":{"anyKey":"anyValue"},"controlled_by":"controlled_by","locked":true}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = ResourceInstancesPager(
            client=_service,
            guid='testString',
            name='testString',
            resource_group_id='testString',
            resource_id='testString',
            resource_plan_id='testString',
            type='testString',
            sub_type='testString',
            limit=10,
            state='active',
            updated_from='2021-01-01',
            updated_to='2021-01-01',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateResourceInstance:
    """
    Test Class for create_resource_instance
    """

    @responses.activate
    def test_create_resource_instance_all_params(self):
        """
        create_resource_instance()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        name = 'ExampleResourceInstance'
        target = 'global'
        resource_group = '13aa3ee48c3b44ddb64c05c79f7ab8ef'
        resource_plan_id = 'a10e4960-3685-11e9-b210-d663bd873d93'
        tags = ['testString']
        allow_cleanup = False
        parameters = {'foo': 'bar'}
        entity_lock = False

        # Invoke method
        response = _service.create_resource_instance(
            name,
            target,
            resource_group,
            resource_plan_id,
            tags=tags,
            allow_cleanup=allow_cleanup,
            parameters=parameters,
            entity_lock=entity_lock,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'ExampleResourceInstance'
        assert req_body['target'] == 'global'
        assert req_body['resource_group'] == '13aa3ee48c3b44ddb64c05c79f7ab8ef'
        assert req_body['resource_plan_id'] == 'a10e4960-3685-11e9-b210-d663bd873d93'
        assert req_body['tags'] == ['testString']
        assert req_body['allow_cleanup'] == False
        assert req_body['parameters'] == {'foo': 'bar'}

    def test_create_resource_instance_all_params_with_retries(self):
        # Enable retries and run test_create_resource_instance_all_params.
        _service.enable_retries()
        self.test_create_resource_instance_all_params()

        # Disable retries and run test_create_resource_instance_all_params.
        _service.disable_retries()
        self.test_create_resource_instance_all_params()

    @responses.activate
    def test_create_resource_instance_required_params(self):
        """
        test_create_resource_instance_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        name = 'ExampleResourceInstance'
        target = 'global'
        resource_group = '13aa3ee48c3b44ddb64c05c79f7ab8ef'
        resource_plan_id = 'a10e4960-3685-11e9-b210-d663bd873d93'
        tags = ['testString']
        allow_cleanup = False
        parameters = {'foo': 'bar'}

        # Invoke method
        response = _service.create_resource_instance(
            name,
            target,
            resource_group,
            resource_plan_id,
            tags=tags,
            allow_cleanup=allow_cleanup,
            parameters=parameters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'ExampleResourceInstance'
        assert req_body['target'] == 'global'
        assert req_body['resource_group'] == '13aa3ee48c3b44ddb64c05c79f7ab8ef'
        assert req_body['resource_plan_id'] == 'a10e4960-3685-11e9-b210-d663bd873d93'
        assert req_body['tags'] == ['testString']
        assert req_body['allow_cleanup'] == False
        assert req_body['parameters'] == {'foo': 'bar'}

    def test_create_resource_instance_required_params_with_retries(self):
        # Enable retries and run test_create_resource_instance_required_params.
        _service.enable_retries()
        self.test_create_resource_instance_required_params()

        # Disable retries and run test_create_resource_instance_required_params.
        _service.disable_retries()
        self.test_create_resource_instance_required_params()

    @responses.activate
    def test_create_resource_instance_value_error(self):
        """
        test_create_resource_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        name = 'ExampleResourceInstance'
        target = 'global'
        resource_group = '13aa3ee48c3b44ddb64c05c79f7ab8ef'
        resource_plan_id = 'a10e4960-3685-11e9-b210-d663bd873d93'
        tags = ['testString']
        allow_cleanup = False
        parameters = {'foo': 'bar'}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "target": target,
            "resource_group": resource_group,
            "resource_plan_id": resource_plan_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_resource_instance(**req_copy)

    def test_create_resource_instance_value_error_with_retries(self):
        # Enable retries and run test_create_resource_instance_value_error.
        _service.enable_retries()
        self.test_create_resource_instance_value_error()

        # Disable retries and run test_create_resource_instance_value_error.
        _service.disable_retries()
        self.test_create_resource_instance_value_error()


class TestGetResourceInstance:
    """
    Test Class for get_resource_instance
    """

    @responses.activate
    def test_get_resource_instance_all_params(self):
        """
        get_resource_instance()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_resource_instance(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_instance_all_params_with_retries(self):
        # Enable retries and run test_get_resource_instance_all_params.
        _service.enable_retries()
        self.test_get_resource_instance_all_params()

        # Disable retries and run test_get_resource_instance_all_params.
        _service.disable_retries()
        self.test_get_resource_instance_all_params()

    @responses.activate
    def test_get_resource_instance_value_error(self):
        """
        test_get_resource_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_resource_instance(**req_copy)

    def test_get_resource_instance_value_error_with_retries(self):
        # Enable retries and run test_get_resource_instance_value_error.
        _service.enable_retries()
        self.test_get_resource_instance_value_error()

        # Disable retries and run test_get_resource_instance_value_error.
        _service.disable_retries()
        self.test_get_resource_instance_value_error()


class TestDeleteResourceInstance:
    """
    Test Class for delete_resource_instance
    """

    @responses.activate
    def test_delete_resource_instance_all_params(self):
        """
        delete_resource_instance()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString')
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        id = 'testString'
        recursive = False

        # Invoke method
        response = _service.delete_resource_instance(id, recursive=recursive, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'recursive={}'.format('true' if recursive else 'false') in query_string

    def test_delete_resource_instance_all_params_with_retries(self):
        # Enable retries and run test_delete_resource_instance_all_params.
        _service.enable_retries()
        self.test_delete_resource_instance_all_params()

        # Disable retries and run test_delete_resource_instance_all_params.
        _service.disable_retries()
        self.test_delete_resource_instance_all_params()

    @responses.activate
    def test_delete_resource_instance_required_params(self):
        """
        test_delete_resource_instance_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString')
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_resource_instance(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_resource_instance_required_params_with_retries(self):
        # Enable retries and run test_delete_resource_instance_required_params.
        _service.enable_retries()
        self.test_delete_resource_instance_required_params()

        # Disable retries and run test_delete_resource_instance_required_params.
        _service.disable_retries()
        self.test_delete_resource_instance_required_params()

    @responses.activate
    def test_delete_resource_instance_value_error(self):
        """
        test_delete_resource_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString')
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_resource_instance(**req_copy)

    def test_delete_resource_instance_value_error_with_retries(self):
        # Enable retries and run test_delete_resource_instance_value_error.
        _service.enable_retries()
        self.test_delete_resource_instance_value_error()

        # Disable retries and run test_delete_resource_instance_value_error.
        _service.disable_retries()
        self.test_delete_resource_instance_value_error()


class TestUpdateResourceInstance:
    """
    Test Class for update_resource_instance
    """

    @responses.activate
    def test_update_resource_instance_all_params(self):
        """
        update_resource_instance()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        name = 'UpdatedExampleResourceInstance'
        parameters = {'foo': 'bar'}
        resource_plan_id = 'testString'
        allow_cleanup = True

        # Invoke method
        response = _service.update_resource_instance(
            id,
            name=name,
            parameters=parameters,
            resource_plan_id=resource_plan_id,
            allow_cleanup=allow_cleanup,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'UpdatedExampleResourceInstance'
        assert req_body['parameters'] == {'foo': 'bar'}
        assert req_body['resource_plan_id'] == 'testString'
        assert req_body['allow_cleanup'] == True

    def test_update_resource_instance_all_params_with_retries(self):
        # Enable retries and run test_update_resource_instance_all_params.
        _service.enable_retries()
        self.test_update_resource_instance_all_params()

        # Disable retries and run test_update_resource_instance_all_params.
        _service.disable_retries()
        self.test_update_resource_instance_all_params()

    @responses.activate
    def test_update_resource_instance_value_error(self):
        """
        test_update_resource_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        name = 'UpdatedExampleResourceInstance'
        parameters = {'foo': 'bar'}
        resource_plan_id = 'testString'
        allow_cleanup = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_resource_instance(**req_copy)

    def test_update_resource_instance_value_error_with_retries(self):
        # Enable retries and run test_update_resource_instance_value_error.
        _service.enable_retries()
        self.test_update_resource_instance_value_error()

        # Disable retries and run test_update_resource_instance_value_error.
        _service.disable_retries()
        self.test_update_resource_instance_value_error()


class TestListResourceAliasesForInstance:
    """
    Test Class for list_resource_aliases_for_instance
    """

    @responses.activate
    def test_list_resource_aliases_for_instance_all_params(self):
        """
        list_resource_aliases_for_instance()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/resource_aliases')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "name": "name", "resource_instance_id": "resource_instance_id", "target_crn": "target_crn", "account_id": "account_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "crn": "crn", "region_instance_id": "region_instance_id", "region_instance_crn": "region_instance_crn", "state": "state", "migrated": true, "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_resource_aliases_for_instance(id, limit=limit, start=start, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_resource_aliases_for_instance_all_params_with_retries(self):
        # Enable retries and run test_list_resource_aliases_for_instance_all_params.
        _service.enable_retries()
        self.test_list_resource_aliases_for_instance_all_params()

        # Disable retries and run test_list_resource_aliases_for_instance_all_params.
        _service.disable_retries()
        self.test_list_resource_aliases_for_instance_all_params()

    @responses.activate
    def test_list_resource_aliases_for_instance_required_params(self):
        """
        test_list_resource_aliases_for_instance_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/resource_aliases')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "name": "name", "resource_instance_id": "resource_instance_id", "target_crn": "target_crn", "account_id": "account_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "crn": "crn", "region_instance_id": "region_instance_id", "region_instance_crn": "region_instance_crn", "state": "state", "migrated": true, "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.list_resource_aliases_for_instance(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_resource_aliases_for_instance_required_params_with_retries(self):
        # Enable retries and run test_list_resource_aliases_for_instance_required_params.
        _service.enable_retries()
        self.test_list_resource_aliases_for_instance_required_params()

        # Disable retries and run test_list_resource_aliases_for_instance_required_params.
        _service.disable_retries()
        self.test_list_resource_aliases_for_instance_required_params()

    @responses.activate
    def test_list_resource_aliases_for_instance_value_error(self):
        """
        test_list_resource_aliases_for_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/resource_aliases')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "name": "name", "resource_instance_id": "resource_instance_id", "target_crn": "target_crn", "account_id": "account_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "crn": "crn", "region_instance_id": "region_instance_id", "region_instance_crn": "region_instance_crn", "state": "state", "migrated": true, "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_resource_aliases_for_instance(**req_copy)

    def test_list_resource_aliases_for_instance_value_error_with_retries(self):
        # Enable retries and run test_list_resource_aliases_for_instance_value_error.
        _service.enable_retries()
        self.test_list_resource_aliases_for_instance_value_error()

        # Disable retries and run test_list_resource_aliases_for_instance_value_error.
        _service.disable_retries()
        self.test_list_resource_aliases_for_instance_value_error()

    @responses.activate
    def test_list_resource_aliases_for_instance_with_pager_get_next(self):
        """
        test_list_resource_aliases_for_instance_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_instances/testString/resource_aliases')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","name":"name","resource_instance_id":"resource_instance_id","target_crn":"target_crn","account_id":"account_id","resource_id":"resource_id","resource_group_id":"resource_group_id","crn":"crn","region_instance_id":"region_instance_id","region_instance_crn":"region_instance_crn","state":"state","migrated":true,"resource_instance_url":"resource_instance_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","name":"name","resource_instance_id":"resource_instance_id","target_crn":"target_crn","account_id":"account_id","resource_id":"resource_id","resource_group_id":"resource_group_id","crn":"crn","region_instance_id":"region_instance_id","region_instance_crn":"region_instance_crn","state":"state","migrated":true,"resource_instance_url":"resource_instance_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = ResourceAliasesForInstancePager(
            client=_service,
            id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_resource_aliases_for_instance_with_pager_get_all(self):
        """
        test_list_resource_aliases_for_instance_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_instances/testString/resource_aliases')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","name":"name","resource_instance_id":"resource_instance_id","target_crn":"target_crn","account_id":"account_id","resource_id":"resource_id","resource_group_id":"resource_group_id","crn":"crn","region_instance_id":"region_instance_id","region_instance_crn":"region_instance_crn","state":"state","migrated":true,"resource_instance_url":"resource_instance_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","name":"name","resource_instance_id":"resource_instance_id","target_crn":"target_crn","account_id":"account_id","resource_id":"resource_id","resource_group_id":"resource_group_id","crn":"crn","region_instance_id":"region_instance_id","region_instance_crn":"region_instance_crn","state":"state","migrated":true,"resource_instance_url":"resource_instance_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = ResourceAliasesForInstancePager(
            client=_service,
            id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestListResourceKeysForInstance:
    """
    Test Class for list_resource_keys_for_instance
    """

    @responses.activate
    def test_list_resource_keys_for_instance_all_params(self):
        """
        list_resource_keys_for_instance()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/resource_keys')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "name": "name", "crn": "crn", "state": "state", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_id": "resource_id", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "migrated": true, "resource_instance_url": "resource_instance_url", "resource_alias_url": "resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_resource_keys_for_instance(id, limit=limit, start=start, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_resource_keys_for_instance_all_params_with_retries(self):
        # Enable retries and run test_list_resource_keys_for_instance_all_params.
        _service.enable_retries()
        self.test_list_resource_keys_for_instance_all_params()

        # Disable retries and run test_list_resource_keys_for_instance_all_params.
        _service.disable_retries()
        self.test_list_resource_keys_for_instance_all_params()

    @responses.activate
    def test_list_resource_keys_for_instance_required_params(self):
        """
        test_list_resource_keys_for_instance_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/resource_keys')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "name": "name", "crn": "crn", "state": "state", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_id": "resource_id", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "migrated": true, "resource_instance_url": "resource_instance_url", "resource_alias_url": "resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.list_resource_keys_for_instance(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_resource_keys_for_instance_required_params_with_retries(self):
        # Enable retries and run test_list_resource_keys_for_instance_required_params.
        _service.enable_retries()
        self.test_list_resource_keys_for_instance_required_params()

        # Disable retries and run test_list_resource_keys_for_instance_required_params.
        _service.disable_retries()
        self.test_list_resource_keys_for_instance_required_params()

    @responses.activate
    def test_list_resource_keys_for_instance_value_error(self):
        """
        test_list_resource_keys_for_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/resource_keys')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "name": "name", "crn": "crn", "state": "state", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_id": "resource_id", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "migrated": true, "resource_instance_url": "resource_instance_url", "resource_alias_url": "resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_resource_keys_for_instance(**req_copy)

    def test_list_resource_keys_for_instance_value_error_with_retries(self):
        # Enable retries and run test_list_resource_keys_for_instance_value_error.
        _service.enable_retries()
        self.test_list_resource_keys_for_instance_value_error()

        # Disable retries and run test_list_resource_keys_for_instance_value_error.
        _service.disable_retries()
        self.test_list_resource_keys_for_instance_value_error()

    @responses.activate
    def test_list_resource_keys_for_instance_with_pager_get_next(self):
        """
        test_list_resource_keys_for_instance_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_instances/testString/resource_keys')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","name":"name","crn":"crn","state":"state","account_id":"account_id","resource_group_id":"resource_group_id","resource_id":"resource_id","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"migrated":true,"resource_instance_url":"resource_instance_url","resource_alias_url":"resource_alias_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","name":"name","crn":"crn","state":"state","account_id":"account_id","resource_group_id":"resource_group_id","resource_id":"resource_id","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"migrated":true,"resource_instance_url":"resource_instance_url","resource_alias_url":"resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = ResourceKeysForInstancePager(
            client=_service,
            id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_resource_keys_for_instance_with_pager_get_all(self):
        """
        test_list_resource_keys_for_instance_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_instances/testString/resource_keys')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","name":"name","crn":"crn","state":"state","account_id":"account_id","resource_group_id":"resource_group_id","resource_id":"resource_id","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"migrated":true,"resource_instance_url":"resource_instance_url","resource_alias_url":"resource_alias_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","name":"name","crn":"crn","state":"state","account_id":"account_id","resource_group_id":"resource_group_id","resource_id":"resource_id","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"migrated":true,"resource_instance_url":"resource_instance_url","resource_alias_url":"resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = ResourceKeysForInstancePager(
            client=_service,
            id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestLockResourceInstance:
    """
    Test Class for lock_resource_instance
    """

    @responses.activate
    def test_lock_resource_instance_all_params(self):
        """
        lock_resource_instance()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/lock')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.lock_resource_instance(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_lock_resource_instance_all_params_with_retries(self):
        # Enable retries and run test_lock_resource_instance_all_params.
        _service.enable_retries()
        self.test_lock_resource_instance_all_params()

        # Disable retries and run test_lock_resource_instance_all_params.
        _service.disable_retries()
        self.test_lock_resource_instance_all_params()

    @responses.activate
    def test_lock_resource_instance_value_error(self):
        """
        test_lock_resource_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/lock')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.lock_resource_instance(**req_copy)

    def test_lock_resource_instance_value_error_with_retries(self):
        # Enable retries and run test_lock_resource_instance_value_error.
        _service.enable_retries()
        self.test_lock_resource_instance_value_error()

        # Disable retries and run test_lock_resource_instance_value_error.
        _service.disable_retries()
        self.test_lock_resource_instance_value_error()


class TestUnlockResourceInstance:
    """
    Test Class for unlock_resource_instance
    """

    @responses.activate
    def test_unlock_resource_instance_all_params(self):
        """
        unlock_resource_instance()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/lock')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.DELETE, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.unlock_resource_instance(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_unlock_resource_instance_all_params_with_retries(self):
        # Enable retries and run test_unlock_resource_instance_all_params.
        _service.enable_retries()
        self.test_unlock_resource_instance_all_params()

        # Disable retries and run test_unlock_resource_instance_all_params.
        _service.disable_retries()
        self.test_unlock_resource_instance_all_params()

    @responses.activate
    def test_unlock_resource_instance_value_error(self):
        """
        test_unlock_resource_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/lock')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.DELETE, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.unlock_resource_instance(**req_copy)

    def test_unlock_resource_instance_value_error_with_retries(self):
        # Enable retries and run test_unlock_resource_instance_value_error.
        _service.enable_retries()
        self.test_unlock_resource_instance_value_error()

        # Disable retries and run test_unlock_resource_instance_value_error.
        _service.disable_retries()
        self.test_unlock_resource_instance_value_error()


class TestCancelLastopResourceInstance:
    """
    Test Class for cancel_lastop_resource_instance
    """

    @responses.activate
    def test_cancel_lastop_resource_instance_all_params(self):
        """
        cancel_lastop_resource_instance()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/last_operation')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.DELETE, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.cancel_lastop_resource_instance(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_cancel_lastop_resource_instance_all_params_with_retries(self):
        # Enable retries and run test_cancel_lastop_resource_instance_all_params.
        _service.enable_retries()
        self.test_cancel_lastop_resource_instance_all_params()

        # Disable retries and run test_cancel_lastop_resource_instance_all_params.
        _service.disable_retries()
        self.test_cancel_lastop_resource_instance_all_params()

    @responses.activate
    def test_cancel_lastop_resource_instance_value_error(self):
        """
        test_cancel_lastop_resource_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_instances/testString/last_operation')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "scheduled_reclaim_at": "2019-01-01T12:00:00.000Z", "restored_at": "2019-01-01T12:00:00.000Z", "restored_by": "restored_by", "scheduled_reclaim_by": "scheduled_reclaim_by", "name": "name", "region_id": "region_id", "account_id": "account_id", "reseller_channel_id": "reseller_channel_id", "resource_plan_id": "resource_plan_id", "resource_group_id": "resource_group_id", "resource_group_crn": "resource_group_crn", "target_crn": "target_crn", "parameters": {"anyKey": "anyValue"}, "allow_cleanup": false, "crn": "crn", "state": "active", "type": "type", "sub_type": "sub_type", "resource_id": "resource_id", "dashboard_url": "dashboard_url", "last_operation": {"type": "type", "state": "in progress", "sub_type": "sub_type", "async": true, "description": "description", "reason_code": "reason_code", "poll_after": 10, "cancelable": true, "poll": true}, "resource_aliases_url": "resource_aliases_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url", "plan_history": [{"resource_plan_id": "resource_plan_id", "start_date": "2019-01-01T12:00:00.000Z", "requestor_id": "requestor_id"}], "migrated": true, "extensions": {"anyKey": "anyValue"}, "controlled_by": "controlled_by", "locked": true}'
        responses.add(responses.DELETE, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.cancel_lastop_resource_instance(**req_copy)

    def test_cancel_lastop_resource_instance_value_error_with_retries(self):
        # Enable retries and run test_cancel_lastop_resource_instance_value_error.
        _service.enable_retries()
        self.test_cancel_lastop_resource_instance_value_error()

        # Disable retries and run test_cancel_lastop_resource_instance_value_error.
        _service.disable_retries()
        self.test_cancel_lastop_resource_instance_value_error()


# endregion
##############################################################################
# End of Service: ResourceInstances
##############################################################################

##############################################################################
# Start of Service: ResourceKeys
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ResourceControllerV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ResourceControllerV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ResourceControllerV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListResourceKeys:
    """
    Test Class for list_resource_keys
    """

    @responses.activate
    def test_list_resource_keys_all_params(self):
        """
        list_resource_keys()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_keys')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "name": "name", "crn": "crn", "state": "state", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_id": "resource_id", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "migrated": true, "resource_instance_url": "resource_instance_url", "resource_alias_url": "resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        guid = 'testString'
        name = 'testString'
        resource_group_id = 'testString'
        resource_id = 'testString'
        limit = 100
        start = 'testString'
        updated_from = '2021-01-01'
        updated_to = '2021-01-01'

        # Invoke method
        response = _service.list_resource_keys(
            guid=guid,
            name=name,
            resource_group_id=resource_group_id,
            resource_id=resource_id,
            limit=limit,
            start=start,
            updated_from=updated_from,
            updated_to=updated_to,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'guid={}'.format(guid) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'updated_from={}'.format(updated_from) in query_string
        assert 'updated_to={}'.format(updated_to) in query_string

    def test_list_resource_keys_all_params_with_retries(self):
        # Enable retries and run test_list_resource_keys_all_params.
        _service.enable_retries()
        self.test_list_resource_keys_all_params()

        # Disable retries and run test_list_resource_keys_all_params.
        _service.disable_retries()
        self.test_list_resource_keys_all_params()

    @responses.activate
    def test_list_resource_keys_required_params(self):
        """
        test_list_resource_keys_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_keys')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "name": "name", "crn": "crn", "state": "state", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_id": "resource_id", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "migrated": true, "resource_instance_url": "resource_instance_url", "resource_alias_url": "resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.list_resource_keys()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_resource_keys_required_params_with_retries(self):
        # Enable retries and run test_list_resource_keys_required_params.
        _service.enable_retries()
        self.test_list_resource_keys_required_params()

        # Disable retries and run test_list_resource_keys_required_params.
        _service.disable_retries()
        self.test_list_resource_keys_required_params()

    @responses.activate
    def test_list_resource_keys_with_pager_get_next(self):
        """
        test_list_resource_keys_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_keys')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","name":"name","crn":"crn","state":"state","account_id":"account_id","resource_group_id":"resource_group_id","resource_id":"resource_id","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"migrated":true,"resource_instance_url":"resource_instance_url","resource_alias_url":"resource_alias_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","name":"name","crn":"crn","state":"state","account_id":"account_id","resource_group_id":"resource_group_id","resource_id":"resource_id","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"migrated":true,"resource_instance_url":"resource_instance_url","resource_alias_url":"resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = ResourceKeysPager(
            client=_service,
            guid='testString',
            name='testString',
            resource_group_id='testString',
            resource_id='testString',
            limit=10,
            updated_from='2021-01-01',
            updated_to='2021-01-01',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_resource_keys_with_pager_get_all(self):
        """
        test_list_resource_keys_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_keys')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","name":"name","crn":"crn","state":"state","account_id":"account_id","resource_group_id":"resource_group_id","resource_id":"resource_id","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"migrated":true,"resource_instance_url":"resource_instance_url","resource_alias_url":"resource_alias_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","name":"name","crn":"crn","state":"state","account_id":"account_id","resource_group_id":"resource_group_id","resource_id":"resource_id","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"migrated":true,"resource_instance_url":"resource_instance_url","resource_alias_url":"resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = ResourceKeysPager(
            client=_service,
            guid='testString',
            name='testString',
            resource_group_id='testString',
            resource_id='testString',
            limit=10,
            updated_from='2021-01-01',
            updated_to='2021-01-01',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateResourceKey:
    """
    Test Class for create_resource_key
    """

    @responses.activate
    def test_create_resource_key_all_params(self):
        """
        create_resource_key()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_keys')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "name": "name", "crn": "crn", "state": "state", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_id": "resource_id", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "migrated": true, "resource_instance_url": "resource_instance_url", "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Construct a dict representation of a ResourceKeyPostParameters model
        resource_key_post_parameters_model = {}
        resource_key_post_parameters_model[
            'serviceid_crn'
        ] = 'crn:v1:bluemix:public:iam-identity::a/9fceaa56d1ab84893af6b9eec5ab81bb::serviceid:ServiceId-fe4c29b5-db13-410a-bacc-b5779a03d393'
        resource_key_post_parameters_model['exampleParameter'] = 'exampleValue'

        # Set up parameter values
        name = 'ExampleResourceKey'
        source = '381fd51a-f251-4f95-aff4-2b03fa8caa63'
        parameters = resource_key_post_parameters_model
        role = 'Writer'

        # Invoke method
        response = _service.create_resource_key(name, source, parameters=parameters, role=role, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'ExampleResourceKey'
        assert req_body['source'] == '381fd51a-f251-4f95-aff4-2b03fa8caa63'
        assert req_body['parameters'] == resource_key_post_parameters_model
        assert req_body['role'] == 'Writer'

    def test_create_resource_key_all_params_with_retries(self):
        # Enable retries and run test_create_resource_key_all_params.
        _service.enable_retries()
        self.test_create_resource_key_all_params()

        # Disable retries and run test_create_resource_key_all_params.
        _service.disable_retries()
        self.test_create_resource_key_all_params()

    @responses.activate
    def test_create_resource_key_value_error(self):
        """
        test_create_resource_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_keys')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "name": "name", "crn": "crn", "state": "state", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_id": "resource_id", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "migrated": true, "resource_instance_url": "resource_instance_url", "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Construct a dict representation of a ResourceKeyPostParameters model
        resource_key_post_parameters_model = {}
        resource_key_post_parameters_model[
            'serviceid_crn'
        ] = 'crn:v1:bluemix:public:iam-identity::a/9fceaa56d1ab84893af6b9eec5ab81bb::serviceid:ServiceId-fe4c29b5-db13-410a-bacc-b5779a03d393'
        resource_key_post_parameters_model['exampleParameter'] = 'exampleValue'

        # Set up parameter values
        name = 'ExampleResourceKey'
        source = '381fd51a-f251-4f95-aff4-2b03fa8caa63'
        parameters = resource_key_post_parameters_model
        role = 'Writer'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "source": source,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_resource_key(**req_copy)

    def test_create_resource_key_value_error_with_retries(self):
        # Enable retries and run test_create_resource_key_value_error.
        _service.enable_retries()
        self.test_create_resource_key_value_error()

        # Disable retries and run test_create_resource_key_value_error.
        _service.disable_retries()
        self.test_create_resource_key_value_error()


class TestGetResourceKey:
    """
    Test Class for get_resource_key
    """

    @responses.activate
    def test_get_resource_key_all_params(self):
        """
        get_resource_key()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_keys/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "name": "name", "crn": "crn", "state": "state", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_id": "resource_id", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "migrated": true, "resource_instance_url": "resource_instance_url", "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_resource_key(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_key_all_params_with_retries(self):
        # Enable retries and run test_get_resource_key_all_params.
        _service.enable_retries()
        self.test_get_resource_key_all_params()

        # Disable retries and run test_get_resource_key_all_params.
        _service.disable_retries()
        self.test_get_resource_key_all_params()

    @responses.activate
    def test_get_resource_key_value_error(self):
        """
        test_get_resource_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_keys/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "name": "name", "crn": "crn", "state": "state", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_id": "resource_id", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "migrated": true, "resource_instance_url": "resource_instance_url", "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_resource_key(**req_copy)

    def test_get_resource_key_value_error_with_retries(self):
        # Enable retries and run test_get_resource_key_value_error.
        _service.enable_retries()
        self.test_get_resource_key_value_error()

        # Disable retries and run test_get_resource_key_value_error.
        _service.disable_retries()
        self.test_get_resource_key_value_error()


class TestDeleteResourceKey:
    """
    Test Class for delete_resource_key
    """

    @responses.activate
    def test_delete_resource_key_all_params(self):
        """
        delete_resource_key()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_keys/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_resource_key(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_resource_key_all_params_with_retries(self):
        # Enable retries and run test_delete_resource_key_all_params.
        _service.enable_retries()
        self.test_delete_resource_key_all_params()

        # Disable retries and run test_delete_resource_key_all_params.
        _service.disable_retries()
        self.test_delete_resource_key_all_params()

    @responses.activate
    def test_delete_resource_key_value_error(self):
        """
        test_delete_resource_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_keys/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_resource_key(**req_copy)

    def test_delete_resource_key_value_error_with_retries(self):
        # Enable retries and run test_delete_resource_key_value_error.
        _service.enable_retries()
        self.test_delete_resource_key_value_error()

        # Disable retries and run test_delete_resource_key_value_error.
        _service.disable_retries()
        self.test_delete_resource_key_value_error()


class TestUpdateResourceKey:
    """
    Test Class for update_resource_key
    """

    @responses.activate
    def test_update_resource_key_all_params(self):
        """
        update_resource_key()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_keys/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "name": "name", "crn": "crn", "state": "state", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_id": "resource_id", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "migrated": true, "resource_instance_url": "resource_instance_url", "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        name = 'UpdatedExampleResourceKey'

        # Invoke method
        response = _service.update_resource_key(id, name, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'UpdatedExampleResourceKey'

    def test_update_resource_key_all_params_with_retries(self):
        # Enable retries and run test_update_resource_key_all_params.
        _service.enable_retries()
        self.test_update_resource_key_all_params()

        # Disable retries and run test_update_resource_key_all_params.
        _service.disable_retries()
        self.test_update_resource_key_all_params()

    @responses.activate
    def test_update_resource_key_value_error(self):
        """
        test_update_resource_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_keys/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "name": "name", "crn": "crn", "state": "state", "account_id": "account_id", "resource_group_id": "resource_group_id", "resource_id": "resource_id", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "migrated": true, "resource_instance_url": "resource_instance_url", "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        name = 'UpdatedExampleResourceKey'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_resource_key(**req_copy)

    def test_update_resource_key_value_error_with_retries(self):
        # Enable retries and run test_update_resource_key_value_error.
        _service.enable_retries()
        self.test_update_resource_key_value_error()

        # Disable retries and run test_update_resource_key_value_error.
        _service.disable_retries()
        self.test_update_resource_key_value_error()


# endregion
##############################################################################
# End of Service: ResourceKeys
##############################################################################

##############################################################################
# Start of Service: ResourceBindings
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ResourceControllerV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ResourceControllerV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ResourceControllerV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListResourceBindings:
    """
    Test Class for list_resource_bindings
    """

    @responses.activate
    def test_list_resource_bindings_all_params(self):
        """
        list_resource_bindings()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_bindings')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "target_crn": "target_crn", "crn": "crn", "region_binding_id": "region_binding_id", "region_binding_crn": "region_binding_crn", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "state": "state", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_id": "resource_id", "migrated": true, "resource_alias_url": "resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        guid = 'testString'
        name = 'testString'
        resource_group_id = 'testString'
        resource_id = 'testString'
        region_binding_id = 'testString'
        limit = 100
        start = 'testString'
        updated_from = '2021-01-01'
        updated_to = '2021-01-01'

        # Invoke method
        response = _service.list_resource_bindings(
            guid=guid,
            name=name,
            resource_group_id=resource_group_id,
            resource_id=resource_id,
            region_binding_id=region_binding_id,
            limit=limit,
            start=start,
            updated_from=updated_from,
            updated_to=updated_to,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'guid={}'.format(guid) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'region_binding_id={}'.format(region_binding_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'updated_from={}'.format(updated_from) in query_string
        assert 'updated_to={}'.format(updated_to) in query_string

    def test_list_resource_bindings_all_params_with_retries(self):
        # Enable retries and run test_list_resource_bindings_all_params.
        _service.enable_retries()
        self.test_list_resource_bindings_all_params()

        # Disable retries and run test_list_resource_bindings_all_params.
        _service.disable_retries()
        self.test_list_resource_bindings_all_params()

    @responses.activate
    def test_list_resource_bindings_required_params(self):
        """
        test_list_resource_bindings_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_bindings')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "target_crn": "target_crn", "crn": "crn", "region_binding_id": "region_binding_id", "region_binding_crn": "region_binding_crn", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "state": "state", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_id": "resource_id", "migrated": true, "resource_alias_url": "resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.list_resource_bindings()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_resource_bindings_required_params_with_retries(self):
        # Enable retries and run test_list_resource_bindings_required_params.
        _service.enable_retries()
        self.test_list_resource_bindings_required_params()

        # Disable retries and run test_list_resource_bindings_required_params.
        _service.disable_retries()
        self.test_list_resource_bindings_required_params()

    @responses.activate
    def test_list_resource_bindings_with_pager_get_next(self):
        """
        test_list_resource_bindings_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_bindings')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","target_crn":"target_crn","crn":"crn","region_binding_id":"region_binding_id","region_binding_crn":"region_binding_crn","name":"name","account_id":"account_id","resource_group_id":"resource_group_id","state":"state","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"resource_id":"resource_id","migrated":true,"resource_alias_url":"resource_alias_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","target_crn":"target_crn","crn":"crn","region_binding_id":"region_binding_id","region_binding_crn":"region_binding_crn","name":"name","account_id":"account_id","resource_group_id":"resource_group_id","state":"state","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"resource_id":"resource_id","migrated":true,"resource_alias_url":"resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = ResourceBindingsPager(
            client=_service,
            guid='testString',
            name='testString',
            resource_group_id='testString',
            resource_id='testString',
            region_binding_id='testString',
            limit=10,
            updated_from='2021-01-01',
            updated_to='2021-01-01',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_resource_bindings_with_pager_get_all(self):
        """
        test_list_resource_bindings_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_bindings')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","target_crn":"target_crn","crn":"crn","region_binding_id":"region_binding_id","region_binding_crn":"region_binding_crn","name":"name","account_id":"account_id","resource_group_id":"resource_group_id","state":"state","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"resource_id":"resource_id","migrated":true,"resource_alias_url":"resource_alias_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","target_crn":"target_crn","crn":"crn","region_binding_id":"region_binding_id","region_binding_crn":"region_binding_crn","name":"name","account_id":"account_id","resource_group_id":"resource_group_id","state":"state","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"resource_id":"resource_id","migrated":true,"resource_alias_url":"resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = ResourceBindingsPager(
            client=_service,
            guid='testString',
            name='testString',
            resource_group_id='testString',
            resource_id='testString',
            region_binding_id='testString',
            limit=10,
            updated_from='2021-01-01',
            updated_to='2021-01-01',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateResourceBinding:
    """
    Test Class for create_resource_binding
    """

    @responses.activate
    def test_create_resource_binding_all_params(self):
        """
        create_resource_binding()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_bindings')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "target_crn": "target_crn", "crn": "crn", "region_binding_id": "region_binding_id", "region_binding_crn": "region_binding_crn", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "state": "state", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_id": "resource_id", "migrated": true, "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Construct a dict representation of a ResourceBindingPostParameters model
        resource_binding_post_parameters_model = {}
        resource_binding_post_parameters_model[
            'serviceid_crn'
        ] = 'crn:v1:bluemix:public:iam-identity::a/9fceaa56d1ab84893af6b9eec5ab81bb::serviceid:ServiceId-fe4c29b5-db13-410a-bacc-b5779a03d393'
        resource_binding_post_parameters_model['exampleParameter'] = 'exampleValue'

        # Set up parameter values
        source = 'faaec9d8-ec64-44d8-ab83-868632fac6a2'
        target = 'crn:v1:staging:public:bluemix:us-south:s/e1773b6e-17b4-40c8-b5ed-d2a1c4b620d7::cf-application:8d9457e0-1303-4f32-b4b3-5525575f6205'
        name = 'ExampleResourceBinding'
        parameters = resource_binding_post_parameters_model
        role = 'Writer'

        # Invoke method
        response = _service.create_resource_binding(
            source, target, name=name, parameters=parameters, role=role, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source'] == 'faaec9d8-ec64-44d8-ab83-868632fac6a2'
        assert (
            req_body['target']
            == 'crn:v1:staging:public:bluemix:us-south:s/e1773b6e-17b4-40c8-b5ed-d2a1c4b620d7::cf-application:8d9457e0-1303-4f32-b4b3-5525575f6205'
        )
        assert req_body['name'] == 'ExampleResourceBinding'
        assert req_body['parameters'] == resource_binding_post_parameters_model
        assert req_body['role'] == 'Writer'

    def test_create_resource_binding_all_params_with_retries(self):
        # Enable retries and run test_create_resource_binding_all_params.
        _service.enable_retries()
        self.test_create_resource_binding_all_params()

        # Disable retries and run test_create_resource_binding_all_params.
        _service.disable_retries()
        self.test_create_resource_binding_all_params()

    @responses.activate
    def test_create_resource_binding_value_error(self):
        """
        test_create_resource_binding_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_bindings')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "target_crn": "target_crn", "crn": "crn", "region_binding_id": "region_binding_id", "region_binding_crn": "region_binding_crn", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "state": "state", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_id": "resource_id", "migrated": true, "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Construct a dict representation of a ResourceBindingPostParameters model
        resource_binding_post_parameters_model = {}
        resource_binding_post_parameters_model[
            'serviceid_crn'
        ] = 'crn:v1:bluemix:public:iam-identity::a/9fceaa56d1ab84893af6b9eec5ab81bb::serviceid:ServiceId-fe4c29b5-db13-410a-bacc-b5779a03d393'
        resource_binding_post_parameters_model['exampleParameter'] = 'exampleValue'

        # Set up parameter values
        source = 'faaec9d8-ec64-44d8-ab83-868632fac6a2'
        target = 'crn:v1:staging:public:bluemix:us-south:s/e1773b6e-17b4-40c8-b5ed-d2a1c4b620d7::cf-application:8d9457e0-1303-4f32-b4b3-5525575f6205'
        name = 'ExampleResourceBinding'
        parameters = resource_binding_post_parameters_model
        role = 'Writer'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "source": source,
            "target": target,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_resource_binding(**req_copy)

    def test_create_resource_binding_value_error_with_retries(self):
        # Enable retries and run test_create_resource_binding_value_error.
        _service.enable_retries()
        self.test_create_resource_binding_value_error()

        # Disable retries and run test_create_resource_binding_value_error.
        _service.disable_retries()
        self.test_create_resource_binding_value_error()


class TestGetResourceBinding:
    """
    Test Class for get_resource_binding
    """

    @responses.activate
    def test_get_resource_binding_all_params(self):
        """
        get_resource_binding()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_bindings/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "target_crn": "target_crn", "crn": "crn", "region_binding_id": "region_binding_id", "region_binding_crn": "region_binding_crn", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "state": "state", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_id": "resource_id", "migrated": true, "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_resource_binding(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_binding_all_params_with_retries(self):
        # Enable retries and run test_get_resource_binding_all_params.
        _service.enable_retries()
        self.test_get_resource_binding_all_params()

        # Disable retries and run test_get_resource_binding_all_params.
        _service.disable_retries()
        self.test_get_resource_binding_all_params()

    @responses.activate
    def test_get_resource_binding_value_error(self):
        """
        test_get_resource_binding_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_bindings/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "target_crn": "target_crn", "crn": "crn", "region_binding_id": "region_binding_id", "region_binding_crn": "region_binding_crn", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "state": "state", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_id": "resource_id", "migrated": true, "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_resource_binding(**req_copy)

    def test_get_resource_binding_value_error_with_retries(self):
        # Enable retries and run test_get_resource_binding_value_error.
        _service.enable_retries()
        self.test_get_resource_binding_value_error()

        # Disable retries and run test_get_resource_binding_value_error.
        _service.disable_retries()
        self.test_get_resource_binding_value_error()


class TestDeleteResourceBinding:
    """
    Test Class for delete_resource_binding
    """

    @responses.activate
    def test_delete_resource_binding_all_params(self):
        """
        delete_resource_binding()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_bindings/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_resource_binding(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_resource_binding_all_params_with_retries(self):
        # Enable retries and run test_delete_resource_binding_all_params.
        _service.enable_retries()
        self.test_delete_resource_binding_all_params()

        # Disable retries and run test_delete_resource_binding_all_params.
        _service.disable_retries()
        self.test_delete_resource_binding_all_params()

    @responses.activate
    def test_delete_resource_binding_value_error(self):
        """
        test_delete_resource_binding_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_bindings/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_resource_binding(**req_copy)

    def test_delete_resource_binding_value_error_with_retries(self):
        # Enable retries and run test_delete_resource_binding_value_error.
        _service.enable_retries()
        self.test_delete_resource_binding_value_error()

        # Disable retries and run test_delete_resource_binding_value_error.
        _service.disable_retries()
        self.test_delete_resource_binding_value_error()


class TestUpdateResourceBinding:
    """
    Test Class for update_resource_binding
    """

    @responses.activate
    def test_update_resource_binding_all_params(self):
        """
        update_resource_binding()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_bindings/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "target_crn": "target_crn", "crn": "crn", "region_binding_id": "region_binding_id", "region_binding_crn": "region_binding_crn", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "state": "state", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_id": "resource_id", "migrated": true, "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        name = 'UpdatedExampleResourceBinding'

        # Invoke method
        response = _service.update_resource_binding(id, name, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'UpdatedExampleResourceBinding'

    def test_update_resource_binding_all_params_with_retries(self):
        # Enable retries and run test_update_resource_binding_all_params.
        _service.enable_retries()
        self.test_update_resource_binding_all_params()

        # Disable retries and run test_update_resource_binding_all_params.
        _service.disable_retries()
        self.test_update_resource_binding_all_params()

    @responses.activate
    def test_update_resource_binding_value_error(self):
        """
        test_update_resource_binding_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_bindings/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "target_crn": "target_crn", "crn": "crn", "region_binding_id": "region_binding_id", "region_binding_crn": "region_binding_crn", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "state": "state", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_id": "resource_id", "migrated": true, "resource_alias_url": "resource_alias_url"}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        name = 'UpdatedExampleResourceBinding'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_resource_binding(**req_copy)

    def test_update_resource_binding_value_error_with_retries(self):
        # Enable retries and run test_update_resource_binding_value_error.
        _service.enable_retries()
        self.test_update_resource_binding_value_error()

        # Disable retries and run test_update_resource_binding_value_error.
        _service.disable_retries()
        self.test_update_resource_binding_value_error()


# endregion
##############################################################################
# End of Service: ResourceBindings
##############################################################################

##############################################################################
# Start of Service: ResourceAliases
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ResourceControllerV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ResourceControllerV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ResourceControllerV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListResourceAliases:
    """
    Test Class for list_resource_aliases
    """

    @responses.activate
    def test_list_resource_aliases_all_params(self):
        """
        list_resource_aliases()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "name": "name", "resource_instance_id": "resource_instance_id", "target_crn": "target_crn", "account_id": "account_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "crn": "crn", "region_instance_id": "region_instance_id", "region_instance_crn": "region_instance_crn", "state": "state", "migrated": true, "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        guid = 'testString'
        name = 'testString'
        resource_instance_id = 'testString'
        region_instance_id = 'testString'
        resource_id = 'testString'
        resource_group_id = 'testString'
        limit = 100
        start = 'testString'
        updated_from = '2021-01-01'
        updated_to = '2021-01-01'

        # Invoke method
        response = _service.list_resource_aliases(
            guid=guid,
            name=name,
            resource_instance_id=resource_instance_id,
            region_instance_id=region_instance_id,
            resource_id=resource_id,
            resource_group_id=resource_group_id,
            limit=limit,
            start=start,
            updated_from=updated_from,
            updated_to=updated_to,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'guid={}'.format(guid) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'resource_instance_id={}'.format(resource_instance_id) in query_string
        assert 'region_instance_id={}'.format(region_instance_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'updated_from={}'.format(updated_from) in query_string
        assert 'updated_to={}'.format(updated_to) in query_string

    def test_list_resource_aliases_all_params_with_retries(self):
        # Enable retries and run test_list_resource_aliases_all_params.
        _service.enable_retries()
        self.test_list_resource_aliases_all_params()

        # Disable retries and run test_list_resource_aliases_all_params.
        _service.disable_retries()
        self.test_list_resource_aliases_all_params()

    @responses.activate
    def test_list_resource_aliases_required_params(self):
        """
        test_list_resource_aliases_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "name": "name", "resource_instance_id": "resource_instance_id", "target_crn": "target_crn", "account_id": "account_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "crn": "crn", "region_instance_id": "region_instance_id", "region_instance_crn": "region_instance_crn", "state": "state", "migrated": true, "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.list_resource_aliases()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_resource_aliases_required_params_with_retries(self):
        # Enable retries and run test_list_resource_aliases_required_params.
        _service.enable_retries()
        self.test_list_resource_aliases_required_params()

        # Disable retries and run test_list_resource_aliases_required_params.
        _service.disable_retries()
        self.test_list_resource_aliases_required_params()

    @responses.activate
    def test_list_resource_aliases_with_pager_get_next(self):
        """
        test_list_resource_aliases_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_aliases')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","name":"name","resource_instance_id":"resource_instance_id","target_crn":"target_crn","account_id":"account_id","resource_id":"resource_id","resource_group_id":"resource_group_id","crn":"crn","region_instance_id":"region_instance_id","region_instance_crn":"region_instance_crn","state":"state","migrated":true,"resource_instance_url":"resource_instance_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","name":"name","resource_instance_id":"resource_instance_id","target_crn":"target_crn","account_id":"account_id","resource_id":"resource_id","resource_group_id":"resource_group_id","crn":"crn","region_instance_id":"region_instance_id","region_instance_crn":"region_instance_crn","state":"state","migrated":true,"resource_instance_url":"resource_instance_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = ResourceAliasesPager(
            client=_service,
            guid='testString',
            name='testString',
            resource_instance_id='testString',
            region_instance_id='testString',
            resource_id='testString',
            resource_group_id='testString',
            limit=10,
            updated_from='2021-01-01',
            updated_to='2021-01-01',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_resource_aliases_with_pager_get_all(self):
        """
        test_list_resource_aliases_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_aliases')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","name":"name","resource_instance_id":"resource_instance_id","target_crn":"target_crn","account_id":"account_id","resource_id":"resource_id","resource_group_id":"resource_group_id","crn":"crn","region_instance_id":"region_instance_id","region_instance_crn":"region_instance_crn","state":"state","migrated":true,"resource_instance_url":"resource_instance_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","name":"name","resource_instance_id":"resource_instance_id","target_crn":"target_crn","account_id":"account_id","resource_id":"resource_id","resource_group_id":"resource_group_id","crn":"crn","region_instance_id":"region_instance_id","region_instance_crn":"region_instance_crn","state":"state","migrated":true,"resource_instance_url":"resource_instance_url","resource_bindings_url":"resource_bindings_url","resource_keys_url":"resource_keys_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = ResourceAliasesPager(
            client=_service,
            guid='testString',
            name='testString',
            resource_instance_id='testString',
            region_instance_id='testString',
            resource_id='testString',
            resource_group_id='testString',
            limit=10,
            updated_from='2021-01-01',
            updated_to='2021-01-01',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateResourceAlias:
    """
    Test Class for create_resource_alias
    """

    @responses.activate
    def test_create_resource_alias_all_params(self):
        """
        create_resource_alias()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "name": "name", "resource_instance_id": "resource_instance_id", "target_crn": "target_crn", "account_id": "account_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "crn": "crn", "region_instance_id": "region_instance_id", "region_instance_crn": "region_instance_crn", "state": "state", "migrated": true, "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        name = 'ExampleResourceAlias'
        source = '381fd51a-f251-4f95-aff4-2b03fa8caa63'
        target = 'crn:v1:bluemix:public:bluemix:us-south:o/d35d4f0e-5076-4c89-9361-2522894b6548::cf-space:e1773b6e-17b4-40c8-b5ed-d2a1c4b620d7'

        # Invoke method
        response = _service.create_resource_alias(name, source, target, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'ExampleResourceAlias'
        assert req_body['source'] == '381fd51a-f251-4f95-aff4-2b03fa8caa63'
        assert (
            req_body['target']
            == 'crn:v1:bluemix:public:bluemix:us-south:o/d35d4f0e-5076-4c89-9361-2522894b6548::cf-space:e1773b6e-17b4-40c8-b5ed-d2a1c4b620d7'
        )

    def test_create_resource_alias_all_params_with_retries(self):
        # Enable retries and run test_create_resource_alias_all_params.
        _service.enable_retries()
        self.test_create_resource_alias_all_params()

        # Disable retries and run test_create_resource_alias_all_params.
        _service.disable_retries()
        self.test_create_resource_alias_all_params()

    @responses.activate
    def test_create_resource_alias_value_error(self):
        """
        test_create_resource_alias_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "name": "name", "resource_instance_id": "resource_instance_id", "target_crn": "target_crn", "account_id": "account_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "crn": "crn", "region_instance_id": "region_instance_id", "region_instance_crn": "region_instance_crn", "state": "state", "migrated": true, "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        name = 'ExampleResourceAlias'
        source = '381fd51a-f251-4f95-aff4-2b03fa8caa63'
        target = 'crn:v1:bluemix:public:bluemix:us-south:o/d35d4f0e-5076-4c89-9361-2522894b6548::cf-space:e1773b6e-17b4-40c8-b5ed-d2a1c4b620d7'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "source": source,
            "target": target,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_resource_alias(**req_copy)

    def test_create_resource_alias_value_error_with_retries(self):
        # Enable retries and run test_create_resource_alias_value_error.
        _service.enable_retries()
        self.test_create_resource_alias_value_error()

        # Disable retries and run test_create_resource_alias_value_error.
        _service.disable_retries()
        self.test_create_resource_alias_value_error()


class TestGetResourceAlias:
    """
    Test Class for get_resource_alias
    """

    @responses.activate
    def test_get_resource_alias_all_params(self):
        """
        get_resource_alias()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "name": "name", "resource_instance_id": "resource_instance_id", "target_crn": "target_crn", "account_id": "account_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "crn": "crn", "region_instance_id": "region_instance_id", "region_instance_crn": "region_instance_crn", "state": "state", "migrated": true, "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_resource_alias(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_alias_all_params_with_retries(self):
        # Enable retries and run test_get_resource_alias_all_params.
        _service.enable_retries()
        self.test_get_resource_alias_all_params()

        # Disable retries and run test_get_resource_alias_all_params.
        _service.disable_retries()
        self.test_get_resource_alias_all_params()

    @responses.activate
    def test_get_resource_alias_value_error(self):
        """
        test_get_resource_alias_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "name": "name", "resource_instance_id": "resource_instance_id", "target_crn": "target_crn", "account_id": "account_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "crn": "crn", "region_instance_id": "region_instance_id", "region_instance_crn": "region_instance_crn", "state": "state", "migrated": true, "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_resource_alias(**req_copy)

    def test_get_resource_alias_value_error_with_retries(self):
        # Enable retries and run test_get_resource_alias_value_error.
        _service.enable_retries()
        self.test_get_resource_alias_value_error()

        # Disable retries and run test_get_resource_alias_value_error.
        _service.disable_retries()
        self.test_get_resource_alias_value_error()


class TestDeleteResourceAlias:
    """
    Test Class for delete_resource_alias
    """

    @responses.activate
    def test_delete_resource_alias_all_params(self):
        """
        delete_resource_alias()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        id = 'testString'
        recursive = False

        # Invoke method
        response = _service.delete_resource_alias(id, recursive=recursive, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'recursive={}'.format('true' if recursive else 'false') in query_string

    def test_delete_resource_alias_all_params_with_retries(self):
        # Enable retries and run test_delete_resource_alias_all_params.
        _service.enable_retries()
        self.test_delete_resource_alias_all_params()

        # Disable retries and run test_delete_resource_alias_all_params.
        _service.disable_retries()
        self.test_delete_resource_alias_all_params()

    @responses.activate
    def test_delete_resource_alias_required_params(self):
        """
        test_delete_resource_alias_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_resource_alias(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_resource_alias_required_params_with_retries(self):
        # Enable retries and run test_delete_resource_alias_required_params.
        _service.enable_retries()
        self.test_delete_resource_alias_required_params()

        # Disable retries and run test_delete_resource_alias_required_params.
        _service.disable_retries()
        self.test_delete_resource_alias_required_params()

    @responses.activate
    def test_delete_resource_alias_value_error(self):
        """
        test_delete_resource_alias_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_resource_alias(**req_copy)

    def test_delete_resource_alias_value_error_with_retries(self):
        # Enable retries and run test_delete_resource_alias_value_error.
        _service.enable_retries()
        self.test_delete_resource_alias_value_error()

        # Disable retries and run test_delete_resource_alias_value_error.
        _service.disable_retries()
        self.test_delete_resource_alias_value_error()


class TestUpdateResourceAlias:
    """
    Test Class for update_resource_alias
    """

    @responses.activate
    def test_update_resource_alias_all_params(self):
        """
        update_resource_alias()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "name": "name", "resource_instance_id": "resource_instance_id", "target_crn": "target_crn", "account_id": "account_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "crn": "crn", "region_instance_id": "region_instance_id", "region_instance_crn": "region_instance_crn", "state": "state", "migrated": true, "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url"}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        name = 'UpdatedExampleResourceAlias'

        # Invoke method
        response = _service.update_resource_alias(id, name, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'UpdatedExampleResourceAlias'

    def test_update_resource_alias_all_params_with_retries(self):
        # Enable retries and run test_update_resource_alias_all_params.
        _service.enable_retries()
        self.test_update_resource_alias_all_params()

        # Disable retries and run test_update_resource_alias_all_params.
        _service.disable_retries()
        self.test_update_resource_alias_all_params()

    @responses.activate
    def test_update_resource_alias_value_error(self):
        """
        test_update_resource_alias_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases/testString')
        mock_response = '{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "name": "name", "resource_instance_id": "resource_instance_id", "target_crn": "target_crn", "account_id": "account_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "crn": "crn", "region_instance_id": "region_instance_id", "region_instance_crn": "region_instance_crn", "state": "state", "migrated": true, "resource_instance_url": "resource_instance_url", "resource_bindings_url": "resource_bindings_url", "resource_keys_url": "resource_keys_url"}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        name = 'UpdatedExampleResourceAlias'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_resource_alias(**req_copy)

    def test_update_resource_alias_value_error_with_retries(self):
        # Enable retries and run test_update_resource_alias_value_error.
        _service.enable_retries()
        self.test_update_resource_alias_value_error()

        # Disable retries and run test_update_resource_alias_value_error.
        _service.disable_retries()
        self.test_update_resource_alias_value_error()


class TestListResourceBindingsForAlias:
    """
    Test Class for list_resource_bindings_for_alias
    """

    @responses.activate
    def test_list_resource_bindings_for_alias_all_params(self):
        """
        list_resource_bindings_for_alias()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases/testString/resource_bindings')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "target_crn": "target_crn", "crn": "crn", "region_binding_id": "region_binding_id", "region_binding_crn": "region_binding_crn", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "state": "state", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_id": "resource_id", "migrated": true, "resource_alias_url": "resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_resource_bindings_for_alias(id, limit=limit, start=start, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_resource_bindings_for_alias_all_params_with_retries(self):
        # Enable retries and run test_list_resource_bindings_for_alias_all_params.
        _service.enable_retries()
        self.test_list_resource_bindings_for_alias_all_params()

        # Disable retries and run test_list_resource_bindings_for_alias_all_params.
        _service.disable_retries()
        self.test_list_resource_bindings_for_alias_all_params()

    @responses.activate
    def test_list_resource_bindings_for_alias_required_params(self):
        """
        test_list_resource_bindings_for_alias_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases/testString/resource_bindings')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "target_crn": "target_crn", "crn": "crn", "region_binding_id": "region_binding_id", "region_binding_crn": "region_binding_crn", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "state": "state", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_id": "resource_id", "migrated": true, "resource_alias_url": "resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.list_resource_bindings_for_alias(id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_resource_bindings_for_alias_required_params_with_retries(self):
        # Enable retries and run test_list_resource_bindings_for_alias_required_params.
        _service.enable_retries()
        self.test_list_resource_bindings_for_alias_required_params()

        # Disable retries and run test_list_resource_bindings_for_alias_required_params.
        _service.disable_retries()
        self.test_list_resource_bindings_for_alias_required_params()

    @responses.activate
    def test_list_resource_bindings_for_alias_value_error(self):
        """
        test_list_resource_bindings_for_alias_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/resource_aliases/testString/resource_bindings')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "guid": "guid", "url": "url", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "deleted_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_by": "updated_by", "deleted_by": "deleted_by", "source_crn": "source_crn", "target_crn": "target_crn", "crn": "crn", "region_binding_id": "region_binding_id", "region_binding_crn": "region_binding_crn", "name": "name", "account_id": "account_id", "resource_group_id": "resource_group_id", "state": "state", "credentials": {"REDACTED": "REDACTED", "apikey": "apikey", "iam_apikey_description": "iam_apikey_description", "iam_apikey_name": "iam_apikey_name", "iam_role_crn": "iam_role_crn", "iam_serviceid_crn": "iam_serviceid_crn"}, "iam_compatible": true, "resource_id": "resource_id", "migrated": true, "resource_alias_url": "resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_resource_bindings_for_alias(**req_copy)

    def test_list_resource_bindings_for_alias_value_error_with_retries(self):
        # Enable retries and run test_list_resource_bindings_for_alias_value_error.
        _service.enable_retries()
        self.test_list_resource_bindings_for_alias_value_error()

        # Disable retries and run test_list_resource_bindings_for_alias_value_error.
        _service.disable_retries()
        self.test_list_resource_bindings_for_alias_value_error()

    @responses.activate
    def test_list_resource_bindings_for_alias_with_pager_get_next(self):
        """
        test_list_resource_bindings_for_alias_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_aliases/testString/resource_bindings')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","target_crn":"target_crn","crn":"crn","region_binding_id":"region_binding_id","region_binding_crn":"region_binding_crn","name":"name","account_id":"account_id","resource_group_id":"resource_group_id","state":"state","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"resource_id":"resource_id","migrated":true,"resource_alias_url":"resource_alias_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","target_crn":"target_crn","crn":"crn","region_binding_id":"region_binding_id","region_binding_crn":"region_binding_crn","name":"name","account_id":"account_id","resource_group_id":"resource_group_id","state":"state","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"resource_id":"resource_id","migrated":true,"resource_alias_url":"resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = ResourceBindingsForAliasPager(
            client=_service,
            id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_resource_bindings_for_alias_with_pager_get_all(self):
        """
        test_list_resource_bindings_for_alias_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v2/resource_aliases/testString/resource_bindings')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","target_crn":"target_crn","crn":"crn","region_binding_id":"region_binding_id","region_binding_crn":"region_binding_crn","name":"name","account_id":"account_id","resource_group_id":"resource_group_id","state":"state","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"resource_id":"resource_id","migrated":true,"resource_alias_url":"resource_alias_url"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","guid":"guid","url":"url","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","deleted_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_by":"updated_by","deleted_by":"deleted_by","source_crn":"source_crn","target_crn":"target_crn","crn":"crn","region_binding_id":"region_binding_id","region_binding_crn":"region_binding_crn","name":"name","account_id":"account_id","resource_group_id":"resource_group_id","state":"state","credentials":{"REDACTED":"REDACTED","apikey":"apikey","iam_apikey_description":"iam_apikey_description","iam_apikey_name":"iam_apikey_name","iam_role_crn":"iam_role_crn","iam_serviceid_crn":"iam_serviceid_crn"},"iam_compatible":true,"resource_id":"resource_id","migrated":true,"resource_alias_url":"resource_alias_url"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = ResourceBindingsForAliasPager(
            client=_service,
            id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


# endregion
##############################################################################
# End of Service: ResourceAliases
##############################################################################

##############################################################################
# Start of Service: ResourceReclamations
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ResourceControllerV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ResourceControllerV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ResourceControllerV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListReclamations:
    """
    Test Class for list_reclamations
    """

    @responses.activate
    def test_list_reclamations_all_params(self):
        """
        list_reclamations()
        """
        # Set up mock
        url = preprocess_url('/v1/reclamations')
        mock_response = '{"resources": [{"id": "id", "entity_id": "entity_id", "entity_type_id": "entity_type_id", "entity_crn": "entity_crn", "resource_instance_id": "resource_instance_id", "resource_group_id": "resource_group_id", "account_id": "account_id", "policy_id": "policy_id", "state": "state", "target_time": "target_time", "custom_properties": {"anyKey": "anyValue"}, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_instance_id = 'testString'

        # Invoke method
        response = _service.list_reclamations(
            account_id=account_id, resource_instance_id=resource_instance_id, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'resource_instance_id={}'.format(resource_instance_id) in query_string

    def test_list_reclamations_all_params_with_retries(self):
        # Enable retries and run test_list_reclamations_all_params.
        _service.enable_retries()
        self.test_list_reclamations_all_params()

        # Disable retries and run test_list_reclamations_all_params.
        _service.disable_retries()
        self.test_list_reclamations_all_params()

    @responses.activate
    def test_list_reclamations_required_params(self):
        """
        test_list_reclamations_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/reclamations')
        mock_response = '{"resources": [{"id": "id", "entity_id": "entity_id", "entity_type_id": "entity_type_id", "entity_crn": "entity_crn", "resource_instance_id": "resource_instance_id", "resource_group_id": "resource_group_id", "account_id": "account_id", "policy_id": "policy_id", "state": "state", "target_time": "target_time", "custom_properties": {"anyKey": "anyValue"}, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.list_reclamations()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_reclamations_required_params_with_retries(self):
        # Enable retries and run test_list_reclamations_required_params.
        _service.enable_retries()
        self.test_list_reclamations_required_params()

        # Disable retries and run test_list_reclamations_required_params.
        _service.disable_retries()
        self.test_list_reclamations_required_params()


class TestRunReclamationAction:
    """
    Test Class for run_reclamation_action
    """

    @responses.activate
    def test_run_reclamation_action_all_params(self):
        """
        run_reclamation_action()
        """
        # Set up mock
        url = preprocess_url('/v1/reclamations/testString/actions/testString')
        mock_response = '{"id": "id", "entity_id": "entity_id", "entity_type_id": "entity_type_id", "entity_crn": "entity_crn", "resource_instance_id": "resource_instance_id", "resource_group_id": "resource_group_id", "account_id": "account_id", "policy_id": "policy_id", "state": "state", "target_time": "target_time", "custom_properties": {"anyKey": "anyValue"}, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        action_name = 'testString'
        request_by = 'testString'
        comment = 'testString'

        # Invoke method
        response = _service.run_reclamation_action(id, action_name, request_by=request_by, comment=comment, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['request_by'] == 'testString'
        assert req_body['comment'] == 'testString'

    def test_run_reclamation_action_all_params_with_retries(self):
        # Enable retries and run test_run_reclamation_action_all_params.
        _service.enable_retries()
        self.test_run_reclamation_action_all_params()

        # Disable retries and run test_run_reclamation_action_all_params.
        _service.disable_retries()
        self.test_run_reclamation_action_all_params()

    @responses.activate
    def test_run_reclamation_action_required_params(self):
        """
        test_run_reclamation_action_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/reclamations/testString/actions/testString')
        mock_response = '{"id": "id", "entity_id": "entity_id", "entity_type_id": "entity_type_id", "entity_crn": "entity_crn", "resource_instance_id": "resource_instance_id", "resource_group_id": "resource_group_id", "account_id": "account_id", "policy_id": "policy_id", "state": "state", "target_time": "target_time", "custom_properties": {"anyKey": "anyValue"}, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        action_name = 'testString'

        # Invoke method
        response = _service.run_reclamation_action(id, action_name, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_run_reclamation_action_required_params_with_retries(self):
        # Enable retries and run test_run_reclamation_action_required_params.
        _service.enable_retries()
        self.test_run_reclamation_action_required_params()

        # Disable retries and run test_run_reclamation_action_required_params.
        _service.disable_retries()
        self.test_run_reclamation_action_required_params()

    @responses.activate
    def test_run_reclamation_action_value_error(self):
        """
        test_run_reclamation_action_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/reclamations/testString/actions/testString')
        mock_response = '{"id": "id", "entity_id": "entity_id", "entity_type_id": "entity_type_id", "entity_crn": "entity_crn", "resource_instance_id": "resource_instance_id", "resource_group_id": "resource_group_id", "account_id": "account_id", "policy_id": "policy_id", "state": "state", "target_time": "target_time", "custom_properties": {"anyKey": "anyValue"}, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = 'testString'
        action_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "action_name": action_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.run_reclamation_action(**req_copy)

    def test_run_reclamation_action_value_error_with_retries(self):
        # Enable retries and run test_run_reclamation_action_value_error.
        _service.enable_retries()
        self.test_run_reclamation_action_value_error()

        # Disable retries and run test_run_reclamation_action_value_error.
        _service.disable_retries()
        self.test_run_reclamation_action_value_error()


# endregion
##############################################################################
# End of Service: ResourceReclamations
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_Credentials:
    """
    Test Class for Credentials
    """

    def test_credentials_serialization(self):
        """
        Test serialization/deserialization for Credentials
        """

        # Construct a json representation of a Credentials model
        credentials_model_json = {}
        credentials_model_json['REDACTED'] = 'REDACTED'
        credentials_model_json['apikey'] = 'testString'
        credentials_model_json['iam_apikey_description'] = 'testString'
        credentials_model_json['iam_apikey_name'] = 'testString'
        credentials_model_json['iam_role_crn'] = 'testString'
        credentials_model_json['iam_serviceid_crn'] = 'testString'
        credentials_model_json['foo'] = 'testString'

        # Construct a model instance of Credentials by calling from_dict on the json representation
        credentials_model = Credentials.from_dict(credentials_model_json)
        assert credentials_model != False

        # Construct a model instance of Credentials by calling from_dict on the json representation
        credentials_model_dict = Credentials.from_dict(credentials_model_json).__dict__
        credentials_model2 = Credentials(**credentials_model_dict)

        # Verify the model instances are equivalent
        assert credentials_model == credentials_model2

        # Convert model instance back to dict and verify no loss of data
        credentials_model_json2 = credentials_model.to_dict()
        assert credentials_model_json2 == credentials_model_json

        # Test get_properties and set_properties methods.
        credentials_model.set_properties({})
        actual_dict = credentials_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        credentials_model.set_properties(expected_dict)
        actual_dict = credentials_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_PlanHistoryItem:
    """
    Test Class for PlanHistoryItem
    """

    def test_plan_history_item_serialization(self):
        """
        Test serialization/deserialization for PlanHistoryItem
        """

        # Construct a json representation of a PlanHistoryItem model
        plan_history_item_model_json = {}
        plan_history_item_model_json['resource_plan_id'] = 'testString'
        plan_history_item_model_json['start_date'] = '2019-01-01T12:00:00Z'
        plan_history_item_model_json['requestor_id'] = 'testString'

        # Construct a model instance of PlanHistoryItem by calling from_dict on the json representation
        plan_history_item_model = PlanHistoryItem.from_dict(plan_history_item_model_json)
        assert plan_history_item_model != False

        # Construct a model instance of PlanHistoryItem by calling from_dict on the json representation
        plan_history_item_model_dict = PlanHistoryItem.from_dict(plan_history_item_model_json).__dict__
        plan_history_item_model2 = PlanHistoryItem(**plan_history_item_model_dict)

        # Verify the model instances are equivalent
        assert plan_history_item_model == plan_history_item_model2

        # Convert model instance back to dict and verify no loss of data
        plan_history_item_model_json2 = plan_history_item_model.to_dict()
        assert plan_history_item_model_json2 == plan_history_item_model_json


class TestModel_Reclamation:
    """
    Test Class for Reclamation
    """

    def test_reclamation_serialization(self):
        """
        Test serialization/deserialization for Reclamation
        """

        # Construct a json representation of a Reclamation model
        reclamation_model_json = {}
        reclamation_model_json['id'] = 'testString'
        reclamation_model_json['entity_id'] = 'testString'
        reclamation_model_json['entity_type_id'] = 'testString'
        reclamation_model_json['entity_crn'] = 'testString'
        reclamation_model_json['resource_instance_id'] = 'testString'
        reclamation_model_json['resource_group_id'] = 'testString'
        reclamation_model_json['account_id'] = 'testString'
        reclamation_model_json['policy_id'] = 'testString'
        reclamation_model_json['state'] = 'testString'
        reclamation_model_json['target_time'] = 'testString'
        reclamation_model_json['custom_properties'] = {'foo': 'bar'}
        reclamation_model_json['created_at'] = '2019-01-01T12:00:00Z'
        reclamation_model_json['created_by'] = 'testString'
        reclamation_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        reclamation_model_json['updated_by'] = 'testString'

        # Construct a model instance of Reclamation by calling from_dict on the json representation
        reclamation_model = Reclamation.from_dict(reclamation_model_json)
        assert reclamation_model != False

        # Construct a model instance of Reclamation by calling from_dict on the json representation
        reclamation_model_dict = Reclamation.from_dict(reclamation_model_json).__dict__
        reclamation_model2 = Reclamation(**reclamation_model_dict)

        # Verify the model instances are equivalent
        assert reclamation_model == reclamation_model2

        # Convert model instance back to dict and verify no loss of data
        reclamation_model_json2 = reclamation_model.to_dict()
        assert reclamation_model_json2 == reclamation_model_json


class TestModel_ReclamationsList:
    """
    Test Class for ReclamationsList
    """

    def test_reclamations_list_serialization(self):
        """
        Test serialization/deserialization for ReclamationsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        reclamation_model = {}  # Reclamation
        reclamation_model['id'] = 'testString'
        reclamation_model['entity_id'] = 'testString'
        reclamation_model['entity_type_id'] = 'testString'
        reclamation_model['entity_crn'] = 'testString'
        reclamation_model['resource_instance_id'] = 'testString'
        reclamation_model['resource_group_id'] = 'testString'
        reclamation_model['account_id'] = 'testString'
        reclamation_model['policy_id'] = 'testString'
        reclamation_model['state'] = 'testString'
        reclamation_model['target_time'] = 'testString'
        reclamation_model['custom_properties'] = {'foo': 'bar'}
        reclamation_model['created_at'] = '2019-01-01T12:00:00Z'
        reclamation_model['created_by'] = 'testString'
        reclamation_model['updated_at'] = '2019-01-01T12:00:00Z'
        reclamation_model['updated_by'] = 'testString'

        # Construct a json representation of a ReclamationsList model
        reclamations_list_model_json = {}
        reclamations_list_model_json['resources'] = [reclamation_model]

        # Construct a model instance of ReclamationsList by calling from_dict on the json representation
        reclamations_list_model = ReclamationsList.from_dict(reclamations_list_model_json)
        assert reclamations_list_model != False

        # Construct a model instance of ReclamationsList by calling from_dict on the json representation
        reclamations_list_model_dict = ReclamationsList.from_dict(reclamations_list_model_json).__dict__
        reclamations_list_model2 = ReclamationsList(**reclamations_list_model_dict)

        # Verify the model instances are equivalent
        assert reclamations_list_model == reclamations_list_model2

        # Convert model instance back to dict and verify no loss of data
        reclamations_list_model_json2 = reclamations_list_model.to_dict()
        assert reclamations_list_model_json2 == reclamations_list_model_json


class TestModel_ResourceAlias:
    """
    Test Class for ResourceAlias
    """

    def test_resource_alias_serialization(self):
        """
        Test serialization/deserialization for ResourceAlias
        """

        # Construct a json representation of a ResourceAlias model
        resource_alias_model_json = {}
        resource_alias_model_json['id'] = 'testString'
        resource_alias_model_json['guid'] = 'testString'
        resource_alias_model_json['url'] = 'testString'
        resource_alias_model_json['created_at'] = '2019-01-01T12:00:00Z'
        resource_alias_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        resource_alias_model_json['deleted_at'] = '2019-01-01T12:00:00Z'
        resource_alias_model_json['created_by'] = 'testString'
        resource_alias_model_json['updated_by'] = 'testString'
        resource_alias_model_json['deleted_by'] = 'testString'
        resource_alias_model_json['name'] = 'testString'
        resource_alias_model_json['resource_instance_id'] = 'testString'
        resource_alias_model_json['target_crn'] = 'testString'
        resource_alias_model_json['account_id'] = 'testString'
        resource_alias_model_json['resource_id'] = 'testString'
        resource_alias_model_json['resource_group_id'] = 'testString'
        resource_alias_model_json['crn'] = 'testString'
        resource_alias_model_json['region_instance_id'] = 'testString'
        resource_alias_model_json['region_instance_crn'] = 'testString'
        resource_alias_model_json['state'] = 'testString'
        resource_alias_model_json['migrated'] = True
        resource_alias_model_json['resource_instance_url'] = 'testString'
        resource_alias_model_json['resource_bindings_url'] = 'testString'
        resource_alias_model_json['resource_keys_url'] = 'testString'

        # Construct a model instance of ResourceAlias by calling from_dict on the json representation
        resource_alias_model = ResourceAlias.from_dict(resource_alias_model_json)
        assert resource_alias_model != False

        # Construct a model instance of ResourceAlias by calling from_dict on the json representation
        resource_alias_model_dict = ResourceAlias.from_dict(resource_alias_model_json).__dict__
        resource_alias_model2 = ResourceAlias(**resource_alias_model_dict)

        # Verify the model instances are equivalent
        assert resource_alias_model == resource_alias_model2

        # Convert model instance back to dict and verify no loss of data
        resource_alias_model_json2 = resource_alias_model.to_dict()
        assert resource_alias_model_json2 == resource_alias_model_json


class TestModel_ResourceAliasesList:
    """
    Test Class for ResourceAliasesList
    """

    def test_resource_aliases_list_serialization(self):
        """
        Test serialization/deserialization for ResourceAliasesList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_alias_model = {}  # ResourceAlias
        resource_alias_model['id'] = 'testString'
        resource_alias_model['guid'] = 'testString'
        resource_alias_model['url'] = 'testString'
        resource_alias_model['created_at'] = '2019-01-01T12:00:00Z'
        resource_alias_model['updated_at'] = '2019-01-01T12:00:00Z'
        resource_alias_model['deleted_at'] = '2019-01-01T12:00:00Z'
        resource_alias_model['created_by'] = 'testString'
        resource_alias_model['updated_by'] = 'testString'
        resource_alias_model['deleted_by'] = 'testString'
        resource_alias_model['name'] = 'testString'
        resource_alias_model['resource_instance_id'] = 'testString'
        resource_alias_model['target_crn'] = 'testString'
        resource_alias_model['account_id'] = 'testString'
        resource_alias_model['resource_id'] = 'testString'
        resource_alias_model['resource_group_id'] = 'testString'
        resource_alias_model['crn'] = 'testString'
        resource_alias_model['region_instance_id'] = 'testString'
        resource_alias_model['region_instance_crn'] = 'testString'
        resource_alias_model['state'] = 'testString'
        resource_alias_model['migrated'] = True
        resource_alias_model['resource_instance_url'] = 'testString'
        resource_alias_model['resource_bindings_url'] = 'testString'
        resource_alias_model['resource_keys_url'] = 'testString'

        # Construct a json representation of a ResourceAliasesList model
        resource_aliases_list_model_json = {}
        resource_aliases_list_model_json['rows_count'] = 38
        resource_aliases_list_model_json['next_url'] = 'testString'
        resource_aliases_list_model_json['resources'] = [resource_alias_model]

        # Construct a model instance of ResourceAliasesList by calling from_dict on the json representation
        resource_aliases_list_model = ResourceAliasesList.from_dict(resource_aliases_list_model_json)
        assert resource_aliases_list_model != False

        # Construct a model instance of ResourceAliasesList by calling from_dict on the json representation
        resource_aliases_list_model_dict = ResourceAliasesList.from_dict(resource_aliases_list_model_json).__dict__
        resource_aliases_list_model2 = ResourceAliasesList(**resource_aliases_list_model_dict)

        # Verify the model instances are equivalent
        assert resource_aliases_list_model == resource_aliases_list_model2

        # Convert model instance back to dict and verify no loss of data
        resource_aliases_list_model_json2 = resource_aliases_list_model.to_dict()
        assert resource_aliases_list_model_json2 == resource_aliases_list_model_json


class TestModel_ResourceBinding:
    """
    Test Class for ResourceBinding
    """

    def test_resource_binding_serialization(self):
        """
        Test serialization/deserialization for ResourceBinding
        """

        # Construct dict forms of any model objects needed in order to build this model.

        credentials_model = {}  # Credentials
        credentials_model['REDACTED'] = 'REDACTED'
        credentials_model['apikey'] = 'testString'
        credentials_model['iam_apikey_description'] = 'testString'
        credentials_model['iam_apikey_name'] = 'testString'
        credentials_model['iam_role_crn'] = 'testString'
        credentials_model['iam_serviceid_crn'] = 'testString'
        credentials_model['foo'] = 'testString'

        # Construct a json representation of a ResourceBinding model
        resource_binding_model_json = {}
        resource_binding_model_json['id'] = 'testString'
        resource_binding_model_json['guid'] = 'testString'
        resource_binding_model_json['url'] = 'testString'
        resource_binding_model_json['created_at'] = '2019-01-01T12:00:00Z'
        resource_binding_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        resource_binding_model_json['deleted_at'] = '2019-01-01T12:00:00Z'
        resource_binding_model_json['created_by'] = 'testString'
        resource_binding_model_json['updated_by'] = 'testString'
        resource_binding_model_json['deleted_by'] = 'testString'
        resource_binding_model_json['source_crn'] = 'testString'
        resource_binding_model_json['target_crn'] = 'testString'
        resource_binding_model_json['crn'] = 'testString'
        resource_binding_model_json['region_binding_id'] = 'testString'
        resource_binding_model_json['region_binding_crn'] = 'testString'
        resource_binding_model_json['name'] = 'testString'
        resource_binding_model_json['account_id'] = 'testString'
        resource_binding_model_json['resource_group_id'] = 'testString'
        resource_binding_model_json['state'] = 'testString'
        resource_binding_model_json['credentials'] = credentials_model
        resource_binding_model_json['iam_compatible'] = True
        resource_binding_model_json['resource_id'] = 'testString'
        resource_binding_model_json['migrated'] = True
        resource_binding_model_json['resource_alias_url'] = 'testString'

        # Construct a model instance of ResourceBinding by calling from_dict on the json representation
        resource_binding_model = ResourceBinding.from_dict(resource_binding_model_json)
        assert resource_binding_model != False

        # Construct a model instance of ResourceBinding by calling from_dict on the json representation
        resource_binding_model_dict = ResourceBinding.from_dict(resource_binding_model_json).__dict__
        resource_binding_model2 = ResourceBinding(**resource_binding_model_dict)

        # Verify the model instances are equivalent
        assert resource_binding_model == resource_binding_model2

        # Convert model instance back to dict and verify no loss of data
        resource_binding_model_json2 = resource_binding_model.to_dict()
        assert resource_binding_model_json2 == resource_binding_model_json


class TestModel_ResourceBindingPostParameters:
    """
    Test Class for ResourceBindingPostParameters
    """

    def test_resource_binding_post_parameters_serialization(self):
        """
        Test serialization/deserialization for ResourceBindingPostParameters
        """

        # Construct a json representation of a ResourceBindingPostParameters model
        resource_binding_post_parameters_model_json = {}
        resource_binding_post_parameters_model_json[
            'serviceid_crn'
        ] = 'crn:v1:bluemix:public:iam-identity::a/9fceaa56d1ab84893af6b9eec5ab81bb::serviceid:ServiceId-fe4c29b5-db13-410a-bacc-b5779a03d393'
        resource_binding_post_parameters_model_json['foo'] = 'testString'

        # Construct a model instance of ResourceBindingPostParameters by calling from_dict on the json representation
        resource_binding_post_parameters_model = ResourceBindingPostParameters.from_dict(
            resource_binding_post_parameters_model_json
        )
        assert resource_binding_post_parameters_model != False

        # Construct a model instance of ResourceBindingPostParameters by calling from_dict on the json representation
        resource_binding_post_parameters_model_dict = ResourceBindingPostParameters.from_dict(
            resource_binding_post_parameters_model_json
        ).__dict__
        resource_binding_post_parameters_model2 = ResourceBindingPostParameters(
            **resource_binding_post_parameters_model_dict
        )

        # Verify the model instances are equivalent
        assert resource_binding_post_parameters_model == resource_binding_post_parameters_model2

        # Convert model instance back to dict and verify no loss of data
        resource_binding_post_parameters_model_json2 = resource_binding_post_parameters_model.to_dict()
        assert resource_binding_post_parameters_model_json2 == resource_binding_post_parameters_model_json

        # Test get_properties and set_properties methods.
        resource_binding_post_parameters_model.set_properties({})
        actual_dict = resource_binding_post_parameters_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        resource_binding_post_parameters_model.set_properties(expected_dict)
        actual_dict = resource_binding_post_parameters_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_ResourceBindingsList:
    """
    Test Class for ResourceBindingsList
    """

    def test_resource_bindings_list_serialization(self):
        """
        Test serialization/deserialization for ResourceBindingsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        credentials_model = {}  # Credentials
        credentials_model['REDACTED'] = 'REDACTED'
        credentials_model['apikey'] = 'testString'
        credentials_model['iam_apikey_description'] = 'testString'
        credentials_model['iam_apikey_name'] = 'testString'
        credentials_model['iam_role_crn'] = 'testString'
        credentials_model['iam_serviceid_crn'] = 'testString'
        credentials_model['foo'] = 'testString'

        resource_binding_model = {}  # ResourceBinding
        resource_binding_model['id'] = 'testString'
        resource_binding_model['guid'] = 'testString'
        resource_binding_model['url'] = 'testString'
        resource_binding_model['created_at'] = '2019-01-01T12:00:00Z'
        resource_binding_model['updated_at'] = '2019-01-01T12:00:00Z'
        resource_binding_model['deleted_at'] = '2019-01-01T12:00:00Z'
        resource_binding_model['created_by'] = 'testString'
        resource_binding_model['updated_by'] = 'testString'
        resource_binding_model['deleted_by'] = 'testString'
        resource_binding_model['source_crn'] = 'testString'
        resource_binding_model['target_crn'] = 'testString'
        resource_binding_model['crn'] = 'testString'
        resource_binding_model['region_binding_id'] = 'testString'
        resource_binding_model['region_binding_crn'] = 'testString'
        resource_binding_model['name'] = 'testString'
        resource_binding_model['account_id'] = 'testString'
        resource_binding_model['resource_group_id'] = 'testString'
        resource_binding_model['state'] = 'testString'
        resource_binding_model['credentials'] = credentials_model
        resource_binding_model['iam_compatible'] = True
        resource_binding_model['resource_id'] = 'testString'
        resource_binding_model['migrated'] = True
        resource_binding_model['resource_alias_url'] = 'testString'

        # Construct a json representation of a ResourceBindingsList model
        resource_bindings_list_model_json = {}
        resource_bindings_list_model_json['rows_count'] = 38
        resource_bindings_list_model_json['next_url'] = 'testString'
        resource_bindings_list_model_json['resources'] = [resource_binding_model]

        # Construct a model instance of ResourceBindingsList by calling from_dict on the json representation
        resource_bindings_list_model = ResourceBindingsList.from_dict(resource_bindings_list_model_json)
        assert resource_bindings_list_model != False

        # Construct a model instance of ResourceBindingsList by calling from_dict on the json representation
        resource_bindings_list_model_dict = ResourceBindingsList.from_dict(resource_bindings_list_model_json).__dict__
        resource_bindings_list_model2 = ResourceBindingsList(**resource_bindings_list_model_dict)

        # Verify the model instances are equivalent
        assert resource_bindings_list_model == resource_bindings_list_model2

        # Convert model instance back to dict and verify no loss of data
        resource_bindings_list_model_json2 = resource_bindings_list_model.to_dict()
        assert resource_bindings_list_model_json2 == resource_bindings_list_model_json


class TestModel_ResourceInstance:
    """
    Test Class for ResourceInstance
    """

    def test_resource_instance_serialization(self):
        """
        Test serialization/deserialization for ResourceInstance
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_instance_last_operation_model = {}  # ResourceInstanceLastOperation
        resource_instance_last_operation_model['type'] = 'testString'
        resource_instance_last_operation_model['state'] = 'in progress'
        resource_instance_last_operation_model['sub_type'] = 'testString'
        resource_instance_last_operation_model['async'] = True
        resource_instance_last_operation_model['description'] = 'testString'
        resource_instance_last_operation_model['reason_code'] = 'testString'
        resource_instance_last_operation_model['poll_after'] = 72.5
        resource_instance_last_operation_model['cancelable'] = True
        resource_instance_last_operation_model['poll'] = True
        resource_instance_last_operation_model['foo'] = 'testString'

        plan_history_item_model = {}  # PlanHistoryItem
        plan_history_item_model['resource_plan_id'] = 'testString'
        plan_history_item_model['start_date'] = '2019-01-01T12:00:00Z'
        plan_history_item_model['requestor_id'] = 'testString'

        # Construct a json representation of a ResourceInstance model
        resource_instance_model_json = {}
        resource_instance_model_json['id'] = 'testString'
        resource_instance_model_json['guid'] = 'testString'
        resource_instance_model_json['url'] = 'testString'
        resource_instance_model_json['created_at'] = '2019-01-01T12:00:00Z'
        resource_instance_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        resource_instance_model_json['deleted_at'] = '2019-01-01T12:00:00Z'
        resource_instance_model_json['created_by'] = 'testString'
        resource_instance_model_json['updated_by'] = 'testString'
        resource_instance_model_json['deleted_by'] = 'testString'
        resource_instance_model_json['scheduled_reclaim_at'] = '2019-01-01T12:00:00Z'
        resource_instance_model_json['restored_at'] = '2019-01-01T12:00:00Z'
        resource_instance_model_json['restored_by'] = 'testString'
        resource_instance_model_json['scheduled_reclaim_by'] = 'testString'
        resource_instance_model_json['name'] = 'testString'
        resource_instance_model_json['region_id'] = 'testString'
        resource_instance_model_json['account_id'] = 'testString'
        resource_instance_model_json['reseller_channel_id'] = 'testString'
        resource_instance_model_json['resource_plan_id'] = 'testString'
        resource_instance_model_json['resource_group_id'] = 'testString'
        resource_instance_model_json['resource_group_crn'] = 'testString'
        resource_instance_model_json['target_crn'] = 'testString'
        resource_instance_model_json['parameters'] = {'foo': 'bar'}
        resource_instance_model_json['allow_cleanup'] = True
        resource_instance_model_json['crn'] = 'testString'
        resource_instance_model_json['state'] = 'active'
        resource_instance_model_json['type'] = 'testString'
        resource_instance_model_json['sub_type'] = 'testString'
        resource_instance_model_json['resource_id'] = 'testString'
        resource_instance_model_json['dashboard_url'] = 'testString'
        resource_instance_model_json['last_operation'] = resource_instance_last_operation_model
        resource_instance_model_json['resource_aliases_url'] = 'testString'
        resource_instance_model_json['resource_bindings_url'] = 'testString'
        resource_instance_model_json['resource_keys_url'] = 'testString'
        resource_instance_model_json['plan_history'] = [plan_history_item_model]
        resource_instance_model_json['migrated'] = True
        resource_instance_model_json['extensions'] = {'foo': 'bar'}
        resource_instance_model_json['controlled_by'] = 'testString'
        resource_instance_model_json['locked'] = True

        # Construct a model instance of ResourceInstance by calling from_dict on the json representation
        resource_instance_model = ResourceInstance.from_dict(resource_instance_model_json)
        assert resource_instance_model != False

        # Construct a model instance of ResourceInstance by calling from_dict on the json representation
        resource_instance_model_dict = ResourceInstance.from_dict(resource_instance_model_json).__dict__
        resource_instance_model2 = ResourceInstance(**resource_instance_model_dict)

        # Verify the model instances are equivalent
        assert resource_instance_model == resource_instance_model2

        # Convert model instance back to dict and verify no loss of data
        resource_instance_model_json2 = resource_instance_model.to_dict()
        assert resource_instance_model_json2 == resource_instance_model_json


class TestModel_ResourceInstanceLastOperation:
    """
    Test Class for ResourceInstanceLastOperation
    """

    def test_resource_instance_last_operation_serialization(self):
        """
        Test serialization/deserialization for ResourceInstanceLastOperation
        """

        # Construct a json representation of a ResourceInstanceLastOperation model
        resource_instance_last_operation_model_json = {}
        resource_instance_last_operation_model_json['type'] = 'testString'
        resource_instance_last_operation_model_json['state'] = 'in progress'
        resource_instance_last_operation_model_json['sub_type'] = 'testString'
        resource_instance_last_operation_model_json['async'] = True
        resource_instance_last_operation_model_json['description'] = 'testString'
        resource_instance_last_operation_model_json['reason_code'] = 'testString'
        resource_instance_last_operation_model_json['poll_after'] = 72.5
        resource_instance_last_operation_model_json['cancelable'] = True
        resource_instance_last_operation_model_json['poll'] = True
        resource_instance_last_operation_model_json['foo'] = 'testString'

        # Construct a model instance of ResourceInstanceLastOperation by calling from_dict on the json representation
        resource_instance_last_operation_model = ResourceInstanceLastOperation.from_dict(
            resource_instance_last_operation_model_json
        )
        assert resource_instance_last_operation_model != False

        # Construct a model instance of ResourceInstanceLastOperation by calling from_dict on the json representation
        resource_instance_last_operation_model_dict = ResourceInstanceLastOperation.from_dict(
            resource_instance_last_operation_model_json
        ).__dict__
        resource_instance_last_operation_model2 = ResourceInstanceLastOperation(
            **resource_instance_last_operation_model_dict
        )

        # Verify the model instances are equivalent
        assert resource_instance_last_operation_model == resource_instance_last_operation_model2

        # Convert model instance back to dict and verify no loss of data
        resource_instance_last_operation_model_json2 = resource_instance_last_operation_model.to_dict()
        assert resource_instance_last_operation_model_json2 == resource_instance_last_operation_model_json

        # Test get_properties and set_properties methods.
        resource_instance_last_operation_model.set_properties({})
        actual_dict = resource_instance_last_operation_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        resource_instance_last_operation_model.set_properties(expected_dict)
        actual_dict = resource_instance_last_operation_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_ResourceInstancesList:
    """
    Test Class for ResourceInstancesList
    """

    def test_resource_instances_list_serialization(self):
        """
        Test serialization/deserialization for ResourceInstancesList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_instance_last_operation_model = {}  # ResourceInstanceLastOperation
        resource_instance_last_operation_model['type'] = 'testString'
        resource_instance_last_operation_model['state'] = 'in progress'
        resource_instance_last_operation_model['sub_type'] = 'testString'
        resource_instance_last_operation_model['async'] = True
        resource_instance_last_operation_model['description'] = 'testString'
        resource_instance_last_operation_model['reason_code'] = 'testString'
        resource_instance_last_operation_model['poll_after'] = 72.5
        resource_instance_last_operation_model['cancelable'] = True
        resource_instance_last_operation_model['poll'] = True
        resource_instance_last_operation_model['foo'] = 'testString'

        plan_history_item_model = {}  # PlanHistoryItem
        plan_history_item_model['resource_plan_id'] = 'testString'
        plan_history_item_model['start_date'] = '2019-01-01T12:00:00Z'
        plan_history_item_model['requestor_id'] = 'testString'

        resource_instance_model = {}  # ResourceInstance
        resource_instance_model['id'] = 'testString'
        resource_instance_model['guid'] = 'testString'
        resource_instance_model['url'] = 'testString'
        resource_instance_model['created_at'] = '2019-01-01T12:00:00Z'
        resource_instance_model['updated_at'] = '2019-01-01T12:00:00Z'
        resource_instance_model['deleted_at'] = '2019-01-01T12:00:00Z'
        resource_instance_model['created_by'] = 'testString'
        resource_instance_model['updated_by'] = 'testString'
        resource_instance_model['deleted_by'] = 'testString'
        resource_instance_model['scheduled_reclaim_at'] = '2019-01-01T12:00:00Z'
        resource_instance_model['restored_at'] = '2019-01-01T12:00:00Z'
        resource_instance_model['restored_by'] = 'testString'
        resource_instance_model['scheduled_reclaim_by'] = 'testString'
        resource_instance_model['name'] = 'testString'
        resource_instance_model['region_id'] = 'testString'
        resource_instance_model['account_id'] = 'testString'
        resource_instance_model['reseller_channel_id'] = 'testString'
        resource_instance_model['resource_plan_id'] = 'testString'
        resource_instance_model['resource_group_id'] = 'testString'
        resource_instance_model['resource_group_crn'] = 'testString'
        resource_instance_model['target_crn'] = 'testString'
        resource_instance_model['parameters'] = {'foo': 'bar'}
        resource_instance_model['allow_cleanup'] = True
        resource_instance_model['crn'] = 'testString'
        resource_instance_model['state'] = 'active'
        resource_instance_model['type'] = 'testString'
        resource_instance_model['sub_type'] = 'testString'
        resource_instance_model['resource_id'] = 'testString'
        resource_instance_model['dashboard_url'] = 'testString'
        resource_instance_model['last_operation'] = resource_instance_last_operation_model
        resource_instance_model['resource_aliases_url'] = 'testString'
        resource_instance_model['resource_bindings_url'] = 'testString'
        resource_instance_model['resource_keys_url'] = 'testString'
        resource_instance_model['plan_history'] = [plan_history_item_model]
        resource_instance_model['migrated'] = True
        resource_instance_model['extensions'] = {'foo': 'bar'}
        resource_instance_model['controlled_by'] = 'testString'
        resource_instance_model['locked'] = True

        # Construct a json representation of a ResourceInstancesList model
        resource_instances_list_model_json = {}
        resource_instances_list_model_json['rows_count'] = 38
        resource_instances_list_model_json['next_url'] = 'testString'
        resource_instances_list_model_json['resources'] = [resource_instance_model]

        # Construct a model instance of ResourceInstancesList by calling from_dict on the json representation
        resource_instances_list_model = ResourceInstancesList.from_dict(resource_instances_list_model_json)
        assert resource_instances_list_model != False

        # Construct a model instance of ResourceInstancesList by calling from_dict on the json representation
        resource_instances_list_model_dict = ResourceInstancesList.from_dict(
            resource_instances_list_model_json
        ).__dict__
        resource_instances_list_model2 = ResourceInstancesList(**resource_instances_list_model_dict)

        # Verify the model instances are equivalent
        assert resource_instances_list_model == resource_instances_list_model2

        # Convert model instance back to dict and verify no loss of data
        resource_instances_list_model_json2 = resource_instances_list_model.to_dict()
        assert resource_instances_list_model_json2 == resource_instances_list_model_json


class TestModel_ResourceKey:
    """
    Test Class for ResourceKey
    """

    def test_resource_key_serialization(self):
        """
        Test serialization/deserialization for ResourceKey
        """

        # Construct dict forms of any model objects needed in order to build this model.

        credentials_model = {}  # Credentials
        credentials_model['REDACTED'] = 'REDACTED'
        credentials_model['apikey'] = 'testString'
        credentials_model['iam_apikey_description'] = 'testString'
        credentials_model['iam_apikey_name'] = 'testString'
        credentials_model['iam_role_crn'] = 'testString'
        credentials_model['iam_serviceid_crn'] = 'testString'
        credentials_model['foo'] = 'testString'

        # Construct a json representation of a ResourceKey model
        resource_key_model_json = {}
        resource_key_model_json['id'] = 'testString'
        resource_key_model_json['guid'] = 'testString'
        resource_key_model_json['url'] = 'testString'
        resource_key_model_json['created_at'] = '2019-01-01T12:00:00Z'
        resource_key_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        resource_key_model_json['deleted_at'] = '2019-01-01T12:00:00Z'
        resource_key_model_json['created_by'] = 'testString'
        resource_key_model_json['updated_by'] = 'testString'
        resource_key_model_json['deleted_by'] = 'testString'
        resource_key_model_json['source_crn'] = 'testString'
        resource_key_model_json['name'] = 'testString'
        resource_key_model_json['crn'] = 'testString'
        resource_key_model_json['state'] = 'testString'
        resource_key_model_json['account_id'] = 'testString'
        resource_key_model_json['resource_group_id'] = 'testString'
        resource_key_model_json['resource_id'] = 'testString'
        resource_key_model_json['credentials'] = credentials_model
        resource_key_model_json['iam_compatible'] = True
        resource_key_model_json['migrated'] = True
        resource_key_model_json['resource_instance_url'] = 'testString'
        resource_key_model_json['resource_alias_url'] = 'testString'

        # Construct a model instance of ResourceKey by calling from_dict on the json representation
        resource_key_model = ResourceKey.from_dict(resource_key_model_json)
        assert resource_key_model != False

        # Construct a model instance of ResourceKey by calling from_dict on the json representation
        resource_key_model_dict = ResourceKey.from_dict(resource_key_model_json).__dict__
        resource_key_model2 = ResourceKey(**resource_key_model_dict)

        # Verify the model instances are equivalent
        assert resource_key_model == resource_key_model2

        # Convert model instance back to dict and verify no loss of data
        resource_key_model_json2 = resource_key_model.to_dict()
        assert resource_key_model_json2 == resource_key_model_json


class TestModel_ResourceKeyPostParameters:
    """
    Test Class for ResourceKeyPostParameters
    """

    def test_resource_key_post_parameters_serialization(self):
        """
        Test serialization/deserialization for ResourceKeyPostParameters
        """

        # Construct a json representation of a ResourceKeyPostParameters model
        resource_key_post_parameters_model_json = {}
        resource_key_post_parameters_model_json[
            'serviceid_crn'
        ] = 'crn:v1:bluemix:public:iam-identity::a/9fceaa56d1ab84893af6b9eec5ab81bb::serviceid:ServiceId-fe4c29b5-db13-410a-bacc-b5779a03d393'
        resource_key_post_parameters_model_json['foo'] = 'testString'

        # Construct a model instance of ResourceKeyPostParameters by calling from_dict on the json representation
        resource_key_post_parameters_model = ResourceKeyPostParameters.from_dict(
            resource_key_post_parameters_model_json
        )
        assert resource_key_post_parameters_model != False

        # Construct a model instance of ResourceKeyPostParameters by calling from_dict on the json representation
        resource_key_post_parameters_model_dict = ResourceKeyPostParameters.from_dict(
            resource_key_post_parameters_model_json
        ).__dict__
        resource_key_post_parameters_model2 = ResourceKeyPostParameters(**resource_key_post_parameters_model_dict)

        # Verify the model instances are equivalent
        assert resource_key_post_parameters_model == resource_key_post_parameters_model2

        # Convert model instance back to dict and verify no loss of data
        resource_key_post_parameters_model_json2 = resource_key_post_parameters_model.to_dict()
        assert resource_key_post_parameters_model_json2 == resource_key_post_parameters_model_json

        # Test get_properties and set_properties methods.
        resource_key_post_parameters_model.set_properties({})
        actual_dict = resource_key_post_parameters_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        resource_key_post_parameters_model.set_properties(expected_dict)
        actual_dict = resource_key_post_parameters_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_ResourceKeysList:
    """
    Test Class for ResourceKeysList
    """

    def test_resource_keys_list_serialization(self):
        """
        Test serialization/deserialization for ResourceKeysList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        credentials_model = {}  # Credentials
        credentials_model['REDACTED'] = 'REDACTED'
        credentials_model['apikey'] = 'testString'
        credentials_model['iam_apikey_description'] = 'testString'
        credentials_model['iam_apikey_name'] = 'testString'
        credentials_model['iam_role_crn'] = 'testString'
        credentials_model['iam_serviceid_crn'] = 'testString'
        credentials_model['foo'] = 'testString'

        resource_key_model = {}  # ResourceKey
        resource_key_model['id'] = 'testString'
        resource_key_model['guid'] = 'testString'
        resource_key_model['url'] = 'testString'
        resource_key_model['created_at'] = '2019-01-01T12:00:00Z'
        resource_key_model['updated_at'] = '2019-01-01T12:00:00Z'
        resource_key_model['deleted_at'] = '2019-01-01T12:00:00Z'
        resource_key_model['created_by'] = 'testString'
        resource_key_model['updated_by'] = 'testString'
        resource_key_model['deleted_by'] = 'testString'
        resource_key_model['source_crn'] = 'testString'
        resource_key_model['name'] = 'testString'
        resource_key_model['crn'] = 'testString'
        resource_key_model['state'] = 'testString'
        resource_key_model['account_id'] = 'testString'
        resource_key_model['resource_group_id'] = 'testString'
        resource_key_model['resource_id'] = 'testString'
        resource_key_model['credentials'] = credentials_model
        resource_key_model['iam_compatible'] = True
        resource_key_model['migrated'] = True
        resource_key_model['resource_instance_url'] = 'testString'
        resource_key_model['resource_alias_url'] = 'testString'

        # Construct a json representation of a ResourceKeysList model
        resource_keys_list_model_json = {}
        resource_keys_list_model_json['rows_count'] = 38
        resource_keys_list_model_json['next_url'] = 'testString'
        resource_keys_list_model_json['resources'] = [resource_key_model]

        # Construct a model instance of ResourceKeysList by calling from_dict on the json representation
        resource_keys_list_model = ResourceKeysList.from_dict(resource_keys_list_model_json)
        assert resource_keys_list_model != False

        # Construct a model instance of ResourceKeysList by calling from_dict on the json representation
        resource_keys_list_model_dict = ResourceKeysList.from_dict(resource_keys_list_model_json).__dict__
        resource_keys_list_model2 = ResourceKeysList(**resource_keys_list_model_dict)

        # Verify the model instances are equivalent
        assert resource_keys_list_model == resource_keys_list_model2

        # Convert model instance back to dict and verify no loss of data
        resource_keys_list_model_json2 = resource_keys_list_model.to_dict()
        assert resource_keys_list_model_json2 == resource_keys_list_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
