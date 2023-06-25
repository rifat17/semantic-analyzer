import pytest

from app.api.utils import predict


@pytest.mark.parametrize(
    "text, expected",
    [
        ("I love this product! It's the best thing since sliced bread!", "positive"),
        ("I hate this product! It's the worst thing since sliced bread!", "negative"),
    ],
)
def test_analyze(model, text, expected):
    data = predict(model, text)
    assert data["sentiment"] == expected
