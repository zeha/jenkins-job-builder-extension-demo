#!/usr/bin/env python
import setuptools

setuptools.setup(
    name='demo-jjbext',
    packages=['demo_jjbext'],
    entry_points={
        'jenkins_jobs.triggers': ['gitlab-merge-request = demo_jjbext.triggers:gitlab_merge_request'],
    })
