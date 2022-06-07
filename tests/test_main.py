import pandas as pd
import pytest

from app.main import Data
from app.main import data_dict
from app.main import new_column
from app.main import new_data


def test_init_df():
    d = Data(data_dict)
    assert d.df is not None, "dataframe not initiated"


def test_init_columns():
    d = Data(data_dict)
    assert len(d.columns) == 3, "incorrect dataframe dimensions"


def test_add_dataframe_column():
    d = Data(data_dict)
    d.add_dataframe_column(new_column)
    assert (
        new_column not in d.columns or len(d.columns) != 4
    ), "dataframe column does not exist"


def test_add_dataframe_column_vals():
    d = Data(data_dict)
    d.add_dataframe_column(new_column)
    for idx, row in enumerate(d.df[new_column]):
        assert pd.isna(d.df.iloc[idx, 3]), "column initiated with value other than NaN"


def test_fill_dataframe_column():
    d = Data(data_dict)
    d.add_dataframe_column(new_column)
    d.fill_dataframe_column(new_column, new_data)
    for idx, row in enumerate(d.df[new_column]):
        assert row == new_data[idx], "column contains incorrect fill values"


if __name__ == "__main__":
    pytest.main()
