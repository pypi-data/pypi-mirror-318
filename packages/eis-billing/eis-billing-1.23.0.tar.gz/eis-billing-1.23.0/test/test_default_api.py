"""
    EMIL BillingService

    The EMIL BillingService API description  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: kontakt@emil.de
    Generated by: https://openapi-generator.tech
"""


import unittest

import eis.billing
from eis.billing.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check(self):
        """Test case for check

        """
        pass


if __name__ == '__main__':
    unittest.main()
