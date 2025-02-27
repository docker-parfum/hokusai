import os
import httpretty
import sys
from unittest.mock import patch

from test import HokusaiIntegrationTestCase

from hokusai import CWD
from hokusai.commands.namespace import create_new_app_yaml

class TestReviewApp(HokusaiIntegrationTestCase):
    @patch('hokusai.lib.command.sys.exit')
    @httpretty.activate
    def test_create_review_app_yaml_file(self, mocked_sys_exit):
        httpretty.register_uri(httpretty.POST, "https://sts.amazonaws.com/",
                                body=self.fixture('sts-get-caller-identity-response.xml'),
                                content_type="application/xml")
        httpretty.register_uri(httpretty.POST, "https://api.ecr.us-east-1.amazonaws.com/",
                                body=self.fixture('ecr-repositories-response.json'),
                                content_type="application/x-amz-json-1.1")

        review_app_yaml_file = os.path.join(CWD, 'hokusai', 'a-review-app.yml')
        try:
            create_new_app_yaml(os.path.abspath(os.path.join(CWD, 'test/fixtures/project/hokusai/minikube.yml')), 'a-review-app')
            self.assertTrue(os.path.isfile(review_app_yaml_file))
        finally:
            os.remove(review_app_yaml_file)
