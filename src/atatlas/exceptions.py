class AtTrendsException(Exception):
    """Base exception class for AT-Trends."""


class IncorrectConfigError(AtTrendsException):
    """AT Trends was incorrectly configured."""
