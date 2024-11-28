import os
from dataclasses import dataclass

from .exceptions import IncorrectConfigError


BLUESKY_LOGIN = "ATATLAS_BLUESKY_LOGIN"
BLUESKY_PASSWORD = "ATATLAS_BLUESKY_PASSWORD"


@dataclass
class BlueskyCreds:
    """Class for Bluesky user credentials"""

    login: str
    password: str


def get_bluesky_creds() -> BlueskyCreds:
    """Get the username and password from environment variables."""
    try:
        login = os.environ[BLUESKY_LOGIN]
    except KeyError:
        raise IncorrectConfigError(
            f"You must set the {BLUESKY_LOGIN} environment variable"
        )
    try:
        password = os.environ[BLUESKY_PASSWORD]
    except KeyError:
        raise IncorrectConfigError(
            f"You must set the {BLUESKY_PASSWORD} environment variable"
        )
    return BlueskyCreds(login=login, password=password)
