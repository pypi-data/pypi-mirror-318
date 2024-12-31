import pytest

from csu.service import HTTPService


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
