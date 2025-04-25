# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0
import os

from huaweicloud_common import BaseTest

class CcTest(BaseTest):

    def test_search_cc(self):
        factory = self.replay_flight_data('cc_request')
        p = self.load_policy({
            "name": "search-cloud-connections",
            "resource": "huaweicloud.cc-cloudconnection",
            "filters": [{
                "type": "value",
                "key": "name",
                "value": "test-custodian-123"
            }],
        }, session_factory=factory)
        resources = p.run()
        self.assertEqual(len(resources), 1)
        self.assertEqual(resources[0]['id'], "03ac5131da4f460e8792ce0b9a1ac5e5")
        self.assertEqual(resources[0]['name'], "test-custodian-123")

