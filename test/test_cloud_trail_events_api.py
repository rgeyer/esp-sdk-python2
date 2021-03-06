# coding: utf-8

"""
    ESP Documentation

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import esp_sdk
from esp_sdk.rest import ApiException
from esp_sdk.apis.cloud_trail_events_api import CloudTrailEventsApi


class TestCloudTrailEventsApi(unittest.TestCase):
    """ CloudTrailEventsApi unit test stubs """

    def setUp(self):
        self.api = esp_sdk.apis.cloud_trail_events_api.CloudTrailEventsApi()

    def tearDown(self):
        pass

    def test_list(self):
        """
        Test case for list

        Get a list of Cloud Trail Events
        """
        pass

    def test_show(self):
        """
        Test case for show

        Show a single Cloud Trail Event
        """
        pass


if __name__ == '__main__':
    unittest.main()
