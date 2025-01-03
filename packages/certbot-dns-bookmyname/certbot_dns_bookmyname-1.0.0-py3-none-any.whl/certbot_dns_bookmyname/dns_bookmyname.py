"""DNS Authenticator for BookMyName."""

import logging

from enum import Enum
from typing import Any
from typing import Callable

import requests

from certbot import errors
from certbot.plugins import dns_common
from certbot.plugins.dns_common import CredentialsConfiguration

logger = logging.getLogger(__name__)


class Action(Enum):
    """
    Possibles actions on a DNS TXT record.
    """

    ADD = "add"
    REMOVE = "remove"


class Authenticator(dns_common.DNSAuthenticator):
    """DNS Authenticator for BookMyName.

    This Authenticator uses the BookMyName API to fulfill a dns-01 challenge.
    """
    description = (
        "Obtain certificates using a DNS TXT record "
        "(if you are using BookMyName for DNS)."
    )
    ttl = 60

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.credentials: CredentialsConfiguration | None = None

    @classmethod
    def add_parser_arguments(
        cls,
        add: Callable[..., None],
        default_propagation_seconds=360,
    ):
        super().add_parser_arguments(add, default_propagation_seconds)
        add("credentials", help="BookMyName credentials INI file.")

    def more_info(self) -> str:
        return (
            "This plugin configures a DNS TXT record to respond to a dns-01 "
            "challenge using BookMyName API"
        )

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            "credentials",
            "BookMyName credentials INI file",
            {
                "user": "BookMyName identifier",
                "password": "BookMyName password",
            },
        )

    def _session(self) -> requests.Session:
        """
        Session for HTTP Basic authentification.

        :raises certbot.errors.Error: When not all credentials are supplied.
        """
        if not self.credentials:
            raise errors.Error("Plugin has not been prepared.")

        user = self.credentials.conf("user")
        password = self.credentials.conf("password")

        if not (user and password):
            raise errors.Error("User and password are required")

        session = requests.Session()
        session.auth = (user, password)
        return session

    def _change_txt_record(self, action: Action, record: str, value: str):
        """
        Perform change on a TXT record using the supplied information.

        :params action Action: Action to the record
        :params str record: The record name (typically
            _acme-challenge.domain.tld).
        :params str value: The record content (typically the challenge
            validation).
        :raises certbot.errors.Error: When API request fail.
        """
        bmn_url = "https://www.bookmyname.com/dyndns/"
        bmn_params = {
            "do": action.value,
            "hostname": record,
            "ttl": self.ttl,
            "type": "TXT",
            "value": f'"{value}"',
        }
        logger.debug(
            "Authenticator %(do)s: "
            "%(hostname)s. %(ttl)d IN %(type)s %(value)s",
            bmn_params,
        )
        resp = self._session().get(url=bmn_url, params=bmn_params)

        if resp.status_code == 401:
            raise errors.Error(
                "BookMyName authentication failed, "
                "please verify your credentials."
            )

        text = resp.text.strip()
        if resp.status_code != 200 or not text.startswith("good:"):
            raise errors.Error(text)

    def _perform(self, _domain: str, validation_name: str, validation: str):
        self._change_txt_record(
            Action.ADD,
            validation_name,
            validation,
        )

    def _cleanup(self, domain: str, validation_name: str, validation: str):
        self._change_txt_record(
            Action.REMOVE,
            validation_name,
            validation,
        )
