import pytest
from app import main

data = {
    "col1": [1, 2, 3, 4, 5],
    "col2": ["a", "b", "c", "d", "e"],
    "col3": [True, True, False, True, True],
}


def test_create_dataframe():
    df = main.create_dataframe(data)
    assert df is not None
    assert df.shape[0] == 5
    assert df.shape[1] == 3


if __name__ == "__main__":
    pytest.main()
