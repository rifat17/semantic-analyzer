import pytest

from app.api.utils import preprocess_text


@pytest.mark.parametrize(
    "text, expected",
    [
        ("This is a test", "test"),
        (
            "This food is worst thing since sliced bread!",
            "food worst thing sinc slice bread",
        ),
    ],
)
def test_pre_process(text, expected):
    assert preprocess_text(text) == expected


if __name__ == "__main__":
    pytest.main()
