# coding: utf-8

"""
    JobSet SDK

    Python SDK for the JobSet API

    The version of the OpenAPI document: v0.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from jobset.models.io_k8s_api_core_v1_env_from_source import IoK8sApiCoreV1EnvFromSource

class TestIoK8sApiCoreV1EnvFromSource(unittest.TestCase):
    """IoK8sApiCoreV1EnvFromSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoK8sApiCoreV1EnvFromSource:
        """Test IoK8sApiCoreV1EnvFromSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoK8sApiCoreV1EnvFromSource`
        """
        model = IoK8sApiCoreV1EnvFromSource()
        if include_optional:
            return IoK8sApiCoreV1EnvFromSource(
                config_map_ref = jobset.models.io/k8s/api/core/v1/config_map_env_source.io.k8s.api.core.v1.ConfigMapEnvSource(
                    name = '', 
                    optional = True, ),
                prefix = '',
                secret_ref = jobset.models.io/k8s/api/core/v1/secret_env_source.io.k8s.api.core.v1.SecretEnvSource(
                    name = '', 
                    optional = True, )
            )
        else:
            return IoK8sApiCoreV1EnvFromSource(
        )
        """

    def testIoK8sApiCoreV1EnvFromSource(self):
        """Test IoK8sApiCoreV1EnvFromSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
