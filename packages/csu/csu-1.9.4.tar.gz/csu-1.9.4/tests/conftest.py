import pytest


@pytest.fixture(scope="session")
def vcr_config():
    return {
        "decode_compressed_response": True,
        "match_on": ("method", "scheme", "host", "path", "query"),  # no port because it's random
    }
