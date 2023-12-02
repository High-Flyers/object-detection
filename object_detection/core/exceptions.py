"""Module for core package exceptions, including config exceptions."""


class RequiredFieldException(Exception):
    """Indicates that there is required field missing in Config
    after initialization."""

    pass
