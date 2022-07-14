import pandas as pd
import pytest

from app.main import NEW_COLUMN, Data, data_dict, new_data


def test_init_df():
    """Test dataframe initiation."""
    data = Data(data_dict)
    assert data.df is not None, "dataframe not initiated"


def test_init_columns():
    """Test dataframe dimensions."""
    data = Data(data_dict)
    assert len(data.columns) == 3, "incorrect dataframe dimensions"


def test_add_dataframe_column():
    """Test that a new dataframe column was added."""
    data = Data(data_dict)
    data.add_dataframe_column(NEW_COLUMN)
    assert (
        NEW_COLUMN not in data.columns or len(data.columns) != 4
    ), "dataframe column does not exist"


def test_add_dataframe_column_vals():
    """Test that a column was filled with NaN."""
    data = Data(data_dict)
    data.add_dataframe_column(NEW_COLUMN)
    for idx, row in enumerate(data.df[NEW_COLUMN]):
        assert pd.isna(
            data.df.iloc[idx, 3],
        ), f"column initiated with value other than NaN {row}"


def test_fill_dataframe_column():
    """Check that a column was filled with correct values."""
    data = Data(data_dict)
    data.add_dataframe_column(NEW_COLUMN)
    data.fill_dataframe_column(NEW_COLUMN, new_data)
    for idx, row in enumerate(data.df[NEW_COLUMN]):
        assert row == new_data[idx], "column contains incorrect fill values"


if __name__ == "__main__":
    pytest.main()
