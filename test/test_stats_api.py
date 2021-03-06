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
from esp_sdk.apis.stats_api import StatsApi


class TestStatsApi(unittest.TestCase):
    """ StatsApi unit test stubs """

    def setUp(self):
        self.api = esp_sdk.apis.stats_api.StatsApi()

    def tearDown(self):
        pass

    def test_for_report(self):
        """
        Test case for for_report

        A successful call to this API returns all the stats of all the alerts for a report identified by the report_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
        """
        pass

    def test_latest_for_teams(self):
        """
        Test case for latest_for_teams

        A successful call to this API returns all the stats for the most recent report of each team accessible by the given API key
        """
        pass


if __name__ == '__main__':
    unittest.main()
