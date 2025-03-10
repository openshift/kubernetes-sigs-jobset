# coding: utf-8

"""
    JobSet SDK

    Python SDK for the JobSet API

    The version of the OpenAPI document: v0.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from jobset.models.jobset_v1alpha2_job_set_list import JobsetV1alpha2JobSetList

class TestJobsetV1alpha2JobSetList(unittest.TestCase):
    """JobsetV1alpha2JobSetList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobsetV1alpha2JobSetList:
        """Test JobsetV1alpha2JobSetList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobsetV1alpha2JobSetList`
        """
        model = JobsetV1alpha2JobSetList()
        if include_optional:
            return JobsetV1alpha2JobSetList(
                api_version = '',
                items = [
                    jobset.models.jobset_v1alpha2_job_set.JobsetV1alpha2JobSet(
                        api_version = '', 
                        kind = '', 
                        metadata = None, 
                        spec = jobset.models.jobset_v1alpha2_job_set_spec.JobsetV1alpha2JobSetSpec(
                            coordinator = jobset.models.jobset_v1alpha2_coordinator.JobsetV1alpha2Coordinator(
                                job_index = 56, 
                                pod_index = 56, 
                                replicated_job = '', ), 
                            failure_policy = jobset.models.jobset_v1alpha2_failure_policy.JobsetV1alpha2FailurePolicy(
                                max_restarts = 56, 
                                restart_strategy = '', 
                                rules = [
                                    jobset.models.jobset_v1alpha2_failure_policy_rule.JobsetV1alpha2FailurePolicyRule(
                                        action = '', 
                                        name = '', 
                                        on_job_failure_reasons = [
                                            ''
                                            ], 
                                        target_replicated_jobs = [
                                            ''
                                            ], )
                                    ], ), 
                            managed_by = '', 
                            network = jobset.models.jobset_v1alpha2_network.JobsetV1alpha2Network(
                                enable_dns_hostnames = True, 
                                publish_not_ready_addresses = True, 
                                subdomain = '', ), 
                            replicated_jobs = [
                                jobset.models.jobset_v1alpha2_replicated_job.JobsetV1alpha2ReplicatedJob(
                                    depends_on = [
                                        jobset.models.jobset_v1alpha2_depends_on.JobsetV1alpha2DependsOn(
                                            name = '', 
                                            status = '', )
                                        ], 
                                    name = '', 
                                    replicas = 56, 
                                    template = V1JobTemplateSpec(), )
                                ], 
                            startup_policy = jobset.models.jobset_v1alpha2_startup_policy.JobsetV1alpha2StartupPolicy(
                                startup_policy_order = '', ), 
                            success_policy = jobset.models.jobset_v1alpha2_success_policy.JobsetV1alpha2SuccessPolicy(
                                operator = '', ), 
                            suspend = True, 
                            ttl_seconds_after_finished = 56, ), 
                        status = jobset.models.jobset_v1alpha2_job_set_status.JobsetV1alpha2JobSetStatus(
                            conditions = [
                                None
                                ], 
                            replicated_jobs_status = [
                                jobset.models.jobset_v1alpha2_replicated_job_status.JobsetV1alpha2ReplicatedJobStatus(
                                    active = 56, 
                                    failed = 56, 
                                    name = '', 
                                    ready = 56, 
                                    succeeded = 56, 
                                    suspended = 56, )
                                ], 
                            restarts = 56, 
                            restarts_count_towards_max = 56, 
                            terminal_state = '', ), )
                    ],
                kind = '',
                metadata = None
            )
        else:
            return JobsetV1alpha2JobSetList(
                items = [
                    jobset.models.jobset_v1alpha2_job_set.JobsetV1alpha2JobSet(
                        api_version = '', 
                        kind = '', 
                        metadata = None, 
                        spec = jobset.models.jobset_v1alpha2_job_set_spec.JobsetV1alpha2JobSetSpec(
                            coordinator = jobset.models.jobset_v1alpha2_coordinator.JobsetV1alpha2Coordinator(
                                job_index = 56, 
                                pod_index = 56, 
                                replicated_job = '', ), 
                            failure_policy = jobset.models.jobset_v1alpha2_failure_policy.JobsetV1alpha2FailurePolicy(
                                max_restarts = 56, 
                                restart_strategy = '', 
                                rules = [
                                    jobset.models.jobset_v1alpha2_failure_policy_rule.JobsetV1alpha2FailurePolicyRule(
                                        action = '', 
                                        name = '', 
                                        on_job_failure_reasons = [
                                            ''
                                            ], 
                                        target_replicated_jobs = [
                                            ''
                                            ], )
                                    ], ), 
                            managed_by = '', 
                            network = jobset.models.jobset_v1alpha2_network.JobsetV1alpha2Network(
                                enable_dns_hostnames = True, 
                                publish_not_ready_addresses = True, 
                                subdomain = '', ), 
                            replicated_jobs = [
                                jobset.models.jobset_v1alpha2_replicated_job.JobsetV1alpha2ReplicatedJob(
                                    depends_on = [
                                        jobset.models.jobset_v1alpha2_depends_on.JobsetV1alpha2DependsOn(
                                            name = '', 
                                            status = '', )
                                        ], 
                                    name = '', 
                                    replicas = 56, 
                                    template = V1JobTemplateSpec(), )
                                ], 
                            startup_policy = jobset.models.jobset_v1alpha2_startup_policy.JobsetV1alpha2StartupPolicy(
                                startup_policy_order = '', ), 
                            success_policy = jobset.models.jobset_v1alpha2_success_policy.JobsetV1alpha2SuccessPolicy(
                                operator = '', ), 
                            suspend = True, 
                            ttl_seconds_after_finished = 56, ), 
                        status = jobset.models.jobset_v1alpha2_job_set_status.JobsetV1alpha2JobSetStatus(
                            conditions = [
                                None
                                ], 
                            replicated_jobs_status = [
                                jobset.models.jobset_v1alpha2_replicated_job_status.JobsetV1alpha2ReplicatedJobStatus(
                                    active = 56, 
                                    failed = 56, 
                                    name = '', 
                                    ready = 56, 
                                    succeeded = 56, 
                                    suspended = 56, )
                                ], 
                            restarts = 56, 
                            restarts_count_towards_max = 56, 
                            terminal_state = '', ), )
                    ],
        )
        """

    def testJobsetV1alpha2JobSetList(self):
        """Test JobsetV1alpha2JobSetList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
