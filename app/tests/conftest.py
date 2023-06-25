import pytest


@pytest.fixture
def client():
    from app.api.app import app

    with app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def model():
    from app.api.app import load_your_model

    return load_your_model()
