import logging
import sys
from datetime import datetime
from os import getpid
from pathlib import Path
from types import SimpleNamespace

import pytest

from csu import exceptions
from csu import service
from csu.exceptions import DecodeError
from csu.exceptions import OpenServiceError
from csu.exceptions import UnexpectedStatusError
from csu.service import HTTPService
from csu.views import exception_handler

PYTHON311 = sys.version_info >= (3, 11)


class OkError(OpenServiceError):
    message = "It's ok."
    error_code = "ok"
    status_code = 200


class BingoService(HTTPService):
    def __init__(self):
        super().__init__(config={"BASE_URL": "https://httpbingo.org"})

    def run(self):
        with self.context() as ctx:
            resp = ctx.request(
                "GET",
                "redirect-to",
                params={
                    "status_code": 307,
                    "url": "https://httpbingo.org/json",
                },
                follow_redirects=True,
            )
            return resp.json

    def error(self):
        with self.context() as ctx:
            try:
                return ctx.request("GET", "status/599", expect_json=False)
            except UnexpectedStatusError as exc:
                if exc.status_code == 599:
                    raise OkError(event_id=ctx.event_id) from exc
                else:
                    raise

    def json(self):
        with self.context() as ctx:
            return ctx.request("GET", "status/418", accept_statuses=[418]).json


@pytest.mark.vcr
def test_redirects():
    service = BingoService()
    data = service.run()
    assert data == {
        "slideshow": {
            "author": "Yours Truly",
            "date": "date of publication",
            "slides": [
                {"title": "Wake up to WonderWidgets!", "type": "all"},
                {"items": ["Why <em>WonderWidgets</em> are great", "Who <em>buys</em> WonderWidgets"], "title": "Overview", "type": "all"},
            ],
            "title": "Sample Slide Show",
        }
    }


@pytest.fixture
def fake_accident_id(monkeypatch):
    calls = []

    def fake_urandom(_):
        frame = sys._getframe().f_back.f_back
        filename = Path(frame.f_code.co_filename).name
        calls.append(f"{filename}:{frame.f_lineno}")
        return bytes([len(calls)])

    monkeypatch.setattr(exceptions, "naivenow", lambda: datetime(2024, 12, 12))  # noqa: DTZ001
    monkeypatch.setattr(exceptions, "urandom", fake_urandom)
    return SimpleNamespace(
        calls=calls,
    )


@pytest.fixture
def capall(capsys, caplog):
    def get_logs():
        for record in caplog.records:
            print("(\n", repr(record.levelname), ",", sep="")
            print('"""', record.message, '"""), ', sep="")
        return [(record.levelname, record.message) for record in caplog.records]

    with caplog.at_level(logging.INFO, logger="service"):
        yield SimpleNamespace(
            std=capsys.readouterr,
            log=get_logs,
        )


@pytest.mark.vcr
def test_error(fake_accident_id, capall):
    bingo = BingoService()
    with pytest.raises(OkError) as exc:
        bingo.error()
    assert exc.value.message == "It's ok."
    api_exc = exc.value.as_api_service_error()
    assert api_exc.status_code == 200
    assert api_exc.detail == {"accident_id": "20241212:01:79200.00", "code": "ok", "detail": "It's ok."}

    assert fake_accident_id.calls == [
        "service.py:55",
    ]
    std = capall.std()
    assert std.out == ""
    assert std.err == ""
    assert capall.log() == [
        ("INFO", f"""[pid:{getpid()}] Setting up BingoService with BASE_URL='https://httpbingo.org' TIMEOUT=60 RETRIES=3 VERIFY=True"""),
        ("INFO", """[01:79200.00] GET https://httpbingo.org/status/599 +[]"""),
        (
            "INFO",
            """[01:79200.00] GET https://httpbingo.org/status/599 => 599
--------------------------------------------------- response body utf-8: utf-8 - 0 bytes----------------------------------------------------
  b''
============================================================================================================================================""",
        ),
        (
            "ERROR",
            """[01:79200.00] GET https://httpbingo.org/status/599 !> failed: UnexpectedStatusError(599, event_id=20241212:01:79200.00)""",
        ),
        ("ERROR", """[01:79200.00] Servicing error: OkError(event_id=20241212:01:79200.00) """),
    ]


@pytest.mark.vcr
def test_decoding(fake_accident_id, capall):
    bingo = BingoService()
    with pytest.raises(DecodeError) as exc:
        bingo.json()
    exception_handler(exc.value, {})
    assert fake_accident_id.calls == [
        "service.py:55",
    ]
    std = capall.std()
    assert std.out == ""
    assert std.err == ""
    assert capall.log() == [
        ("INFO", f"""[pid:{getpid()}] Setting up BingoService with BASE_URL='https://httpbingo.org' TIMEOUT=60 RETRIES=3 VERIFY=True"""),
        ("INFO", """[01:79200.00] GET https://httpbingo.org/status/418 +[]"""),
        (
            "INFO",
            """[01:79200.00] GET https://httpbingo.org/status/418 => 418
--------------------------------------------------- response body utf-8: utf-8 - 13 bytes---------------------------------------------------
  b"I'm a teapot!"
============================================================================================================================================""",
        ),
        ("ERROR", """[01:79200.00] GET https://httpbingo.org/status/418 !> failed: DecodeError(418, event_id=20241212:01:79200.00)"""),
        ("ERROR", """[01:79200.00] Servicing error: DecodeError(418, event_id=20241212:01:79200.00) """),
        (
            "ERROR",
            f""" (renderer: NoneType)
----------------------------------------------------------------- context ------------------------------------------------------------------
  {{}}
---------------------------------------------------------------- traceback -----------------------------------------------------------------
Traceback (most recent call last):
  File "{__file__}", line 146, in test_decoding
    bingo.json()
  File "{__file__}", line 56, in json
    return ctx.request("GET", "status/418", accept_statuses=[418]).json"""
            + (
                """
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
                if PYTHON311
                else ""
            )
            + f"""
  File "{service.__file__}", line 163, in request
    return self.handle_process_response("""
            + (
                """
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
                if PYTHON311
                else ""
            )
            + f"""
  File "{service.__file__}", line 136, in handle_process_response
    raise DecodeError(status_code=response.status_code, error=exc, event_id=self.event_id) from None
csu.exceptions.DecodeError: JSONDecodeError('Expecting value: line 1 column 1 (char 0)') (status: 418)
------------------------------------------------------------ response exception ------------------------------------------------------------
  {{'detail': 'Internal server error', 'code': 'server', 'accident_id': '20241212:01:79200.00'}}
============================================================================================================================================""",
        ),
    ]


@pytest.mark.vcr
def test_logging(fake_accident_id, capall):
    bingo = BingoService()
    with pytest.raises(OkError) as exc:
        bingo.error()
    exception_handler(exc.value, {})
    assert fake_accident_id.calls == [
        "service.py:55",
    ]
    std = capall.std()
    assert std.out == ""
    assert std.err == ""
    assert capall.log() == [
        ("INFO", f"""[pid:{getpid()}] Setting up BingoService with BASE_URL='https://httpbingo.org' TIMEOUT=60 RETRIES=3 VERIFY=True"""),
        ("INFO", """[01:79200.00] GET https://httpbingo.org/status/599 +[]"""),
        (
            "INFO",
            """[01:79200.00] GET https://httpbingo.org/status/599 => 599
--------------------------------------------------- response body utf-8: utf-8 - 0 bytes----------------------------------------------------
  b''
============================================================================================================================================""",
        ),
        (
            "ERROR",
            """[01:79200.00] GET https://httpbingo.org/status/599 !> failed: UnexpectedStatusError(599, event_id=20241212:01:79200.00)""",
        ),
        ("ERROR", """[01:79200.00] Servicing error: OkError(event_id=20241212:01:79200.00) """),
        (
            "WARNING",
            f""" (renderer: NoneType)
----------------------------------------------------------------- context ------------------------------------------------------------------
  {{}}
---------------------------------------------------------------- traceback -----------------------------------------------------------------
Traceback (most recent call last):
  File "{__file__}", line 47, in error
    return ctx.request("GET", "status/599", expect_json=False)"""
            + (
                """
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
                if PYTHON311
                else ""
            )
            + f"""
  File "{service.__file__}", line 163, in request
    return self.handle_process_response("""
            + (
                """
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
                if PYTHON311
                else ""
            )
            + f"""
  File "{service.__file__}", line 130, in handle_process_response
    raise UnexpectedStatusError(status_code=response.status_code, accept_statuses=accept_statuses, event_id=self.event_id)
csu.exceptions.UnexpectedStatusError: Expected(200,) (status: 599)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "{__file__}", line 207, in test_logging
    bingo.error()
  File "{__file__}", line 50, in error
    raise OkError(event_id=ctx.event_id) from exc
test_service.OkError: OkError()

The above exception was the direct cause of the following exception:

csu.exceptions.APIServiceError: {{'accident_id': '20241212:01:79200.00', 'detail': "It's ok.", 'code': 'ok'}}
------------------------------------------------------------ response exception ------------------------------------------------------------
  {{'accident_id': '20241212:01:79200.00', 'detail': "It's ok.", 'code': 'ok'}}
============================================================================================================================================""",
        ),
    ]
