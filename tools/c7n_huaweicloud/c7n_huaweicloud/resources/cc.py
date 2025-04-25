# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0

import logging

from huaweicloudsdkcore.exceptions import exceptions

from c7n_huaweicloud.provider import resources
from c7n_huaweicloud.query import QueryResourceManager, TypeInfo


log = logging.getLogger("custodian.huaweicloud.resources.cc")

@resources.register('cc-cloudconnection')
class CloudConnection(QueryResourceManager):
    class resource_type(TypeInfo):
        service = 'cc'
        enum_spec = ("list_cloud_connections","cloud_connections","marker")
        id = 'id'
        tag_resource_type = 'cc'
