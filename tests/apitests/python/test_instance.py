# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest
import v2_swagger_client
from library.base import _assert_status_code
from v2_swagger_client.models.instance_created_resp import InstanceCreatedResp  # noqa: E501
from v2_swagger_client.rest import ApiException
from v2_swagger_client.api import PreheatApi

class TestInstance(unittest.TestCase):

    def setUp(self):
        self.preheat=PreheatApi()
        self.instances=[]

    def tearDown(self):
        for i in self.instances:
            print "Remove {}".format(i)
            self.delete(i)

    def create(self, instance):
        rsp, code, headers=self.preheat.create_instance_with_http_info(instance)
        self.assertEqual(201, code)
        print rsp
        self.instances.append(rsp.id)
        return rsp.id

    def delete(self, id):
        rsp, code, headers=self.preheat.delete_instance_with_http_info(id)
        print rsp
        self.assertEqual(200, code)
        self.instances.remove(id)

    def testInstanceCreate(self):
        self.create({
           "auth_mode": "NONE",
           "enabled": True,
           "endpoint": "http://127.0.0.1:8000",
           "name": "test",
           "provider": "dragonfly"
        })

    def testInstanceGet(self):
        id=self.create({
           "auth_mode": "NONE",
           "enabled": True,
           "endpoint": "http://127.0.0.1:8001",
           "name": "test",
           "provider": "dragonfly"
        })
        rsp, code, headers=self.preheat.get_instance_with_http_info(id)
        self.assertEqual(200, code)
        self.assertEqual(rsp.endpoint, "http://127.0.0.1:8001")

    def testInstanceUpdate(self):
        id=self.create({
           "auth_mode": "NONE",
           "enabled": True,
           "endpoint": "http://127.0.0.1:8002",
           "name": "test",
           "provider": "dragonfly"
        })
        rsp, code, headers=self.preheat.update_instance_with_http_info(id, {"endpoint": "http://127.0.0.1:8888"})
        self.assertEqual(200, code)
        rsp, code, headers=self.preheat.get_instance_with_http_info(id)
        self.assertEqual(200, code)
        self.assertEqual(rsp.endpoint, "http://127.0.0.1:8888")

    def testInstanceDelete(self):
        id=self.create({
           "auth_mode": "NONE",
           "enabled": True,
           "endpoint": "http://127.0.0.1:8003",
           "name": "test",
           "provider": "dragonfly"
        })
        self.delete(id)

    def testListInstances(self):
        self.create({
           "auth_mode": "NONE",
           "enabled": True,
           "endpoint": "http://127.0.0.1",
           "name": "default",
           "provider": "dragonfly"
        })
        rsp, code, headers=self.preheat.list_instances_with_http_info(page=1,page_size=10,q="nonexist")
        self.assertEqual(200, code)
        self.assertEqual(0, len(rsp))
        self.assertEqual("0", headers["X-Total-Count"])

        rsp, code, headers=self.preheat.list_instances_with_http_info(page=1,page_size=10,q="default")
        self.assertEqual("1", headers["X-Total-Count"])
        self.assertEqual(200, code)
        self.assertEqual(1, len(rsp))
        self.assertEqual("http://127.0.0.1", rsp[0].endpoint)

if __name__ == '__main__':
    unittest.main()