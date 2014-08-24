# Copyright 2012 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import xml.etree.ElementTree as XML


def gitlab_merge_request(parser, xml_parent, data):
    """yaml: gitlab-pull-request
    Build pull requests in github and report results.
    Requires the Jenkins `GitHub Pull Request Builder Plugin.
    <https://wiki.jenkins-ci.org/display/JENKINS/
    GitHub+pull+request+builder+plugin>`_

    :arg list admin-list: the users with admin rights (optional)
    :arg list white-list: users whose pull requests build (optional)
    :arg list org-list: orgs whose users should be white listed (optional)
    :arg string cron: cron syntax of when to run (optional)
    :arg string trigger-phrase: when filled, commenting this phrase
        in the pull request will trigger a build (optional)
    :arg bool only-trigger-phrase: only commenting the trigger phrase
        in the pull request will trigger a build (default false)
    :arg bool github-hooks: use github hook (default false)
    :arg bool permit-all: build every pull request automatically
        without asking (default false)
    :arg bool auto-close-on-fail: close failed pull request automatically
        (default false)

    Example:

    .. literalinclude:: /../../tests/triggers/fixtures/github-pull-request.yaml
    """
    ghprb = XML.SubElement(xml_parent, 'org.jenkinsci.plugins.gitlab.'
                           'GitlabBuildTrigger')
    XML.SubElement(ghprb, 'spec').text = data.get('cron', '')
    XML.SubElement(ghprb, '_cron').text = data.get('cron', '')
    XML.SubElement(ghprb, '_projectPath').text = data.get('project-path', '')
