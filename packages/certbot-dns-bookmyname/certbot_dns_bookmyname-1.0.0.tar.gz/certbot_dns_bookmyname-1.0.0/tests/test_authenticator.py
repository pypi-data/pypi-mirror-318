"""Tests for certbot_dns_bookmyname.dns_bookmyname."""

from unittest import mock

import pytest

from certbot import errors
from certbot.compat import os
from certbot.plugins import dns_test_common
from certbot.plugins.dns_test_common import BaseAuthenticatorTest
from certbot.plugins.dns_test_common import DOMAIN
from certbot.tests import util as test_util
from certbot.tests.util import TempDirTestCase

from certbot_dns_bookmyname.dns_bookmyname import Authenticator, Action


class AuthenticatorTest(TempDirTestCase, BaseAuthenticatorTest):

    def setUp(self):
        super().setUp()
        path = os.path.join(self.tempdir, 'file.ini')
        dns_test_common.write(
            {
                "bookmyname_user": "fake_user",
                "bookmyname_password": "fake_password",
            },
            path,
        )
        self.config = mock.MagicMock(
            bookmyname_credentials=path,
            bookmyname_propagation_seconds=0,   # don't wait during tests
        )
        self.auth = Authenticator(self.config, "bookmyname")

    @test_util.patch_display_util()
    def test_perform(self, unused_mock_get_utility):
        # _change_txt_record | pylint: disable=protected-access
        self.auth._change_txt_record = mock.MagicMock()
        self.auth.perform([self.achall])
        self.auth._change_txt_record.assert_called_once_with(
            Action.ADD,
            f"_acme-challenge.{DOMAIN}",
            mock.ANY,
        )

    def test_cleanup(self):
        # _attempt_cleanup | pylint: disable=protected-access
        self.auth._attempt_cleanup = True
        # _change_txt_record | pylint: disable=protected-access
        self.auth._change_txt_record = mock.MagicMock()
        self.auth.cleanup([self.achall])
        self.auth._change_txt_record.assert_called_once_with(
            Action.REMOVE,
            f"_acme-challenge.{DOMAIN}",
            mock.ANY,
        )

    def test_no_credentials(self):
        empty_config = {}
        dns_test_common.write(empty_config, self.config.bookmyname_credentials)

        with pytest.raises(errors.PluginError):
            self.auth.perform([self.achall])
