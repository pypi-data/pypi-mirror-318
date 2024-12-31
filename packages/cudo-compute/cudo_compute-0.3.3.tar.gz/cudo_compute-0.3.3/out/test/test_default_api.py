# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cudo_compute
from cudo_compute.api.default_api import DefaultApi  # noqa: E501
from cudo_compute.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = cudo_compute.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_data_center_commitment_schedule(self):
        """Test case for get_data_center_commitment_schedule

        """
        pass

    def test_get_data_center_commitment_time_series(self):
        """Test case for get_data_center_commitment_time_series

        """
        pass

    def test_list_billing_account_projects(self):
        """Test case for list_billing_account_projects

        """
        pass

    def test_list_data_center_machine_type_prices(self):
        """Test case for list_data_center_machine_type_prices

        """
        pass

    def test_list_vm_machine_types(self):
        """Test case for list_vm_machine_types

        """
        pass

    def test_search_resources(self):
        """Test case for search_resources

        """
        pass

    def test_track(self):
        """Test case for track

        """
        pass

    def test_update_vm_expire_time(self):
        """Test case for update_vm_expire_time

        """
        pass

    def test_update_vm_password(self):
        """Test case for update_vm_password

        """
        pass


if __name__ == '__main__':
    unittest.main()
