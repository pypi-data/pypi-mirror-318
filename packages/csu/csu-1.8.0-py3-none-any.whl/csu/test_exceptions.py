import pytest

from . import exceptions
from .exceptions import APIServiceError
from .exceptions import OpenServiceError


class OpenFooError(OpenServiceError):
    pass


class ProperOpenFooError(OpenServiceError):
    default_message = "proper foo"


def test_open_service_error():
    with pytest.raises(TypeError) as exc:
        OpenServiceError(event_id=None)
    assert exc.value.args == ("OpenServiceError.__init__() missing 1 required positional argument: 'message'.",)


def test_open_service_error_bad_subclass():
    with pytest.raises(TypeError) as exc:
        OpenFooError(event_id=None)
    assert exc.value.args == (
        "OpenServiceError.__init__() missing 1 required positional argument: 'message'. "
        "Set OpenFooError.default_message to avoid this error.",
    )


def test_open_service_error_proper_subclass(monkeypatch):
    exc = ProperOpenFooError(event_id=None)
    assert exc.message == "proper foo"
    monkeypatch.setattr(exceptions, "get_accident_id", lambda: 123)
    api_exc = exc.as_api_service_error()
    assert isinstance(api_exc, APIServiceError)
    assert api_exc.detail == {
        "accident_id": 123,
        "code": "unknown",
        "detail": "proper foo",
    }
