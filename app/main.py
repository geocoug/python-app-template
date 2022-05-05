import logging

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(msg)s")

data_dict = {
    "col1": [1, 2, 3, 4, 5],
    "col2": ["a", "b", "c", "d", "e"],
    "col3": [True, True, False, True, True],
}

new_column = "new_col"
new_data = ["z", "y", "x", "w", "v"]


class Data:
    def __init__(self, data: dict) -> None:
        self.df = pd.DataFrame(data)
        self.columns = list(self.df.columns)

    def add_dataframe_column(self, col_name: str) -> None:
        self.df[col_name] = np.nan

    def fill_dataframe_column(self, col_name: str, data: list) -> None:
        self.df[col_name] = data


if __name__ == "__main__":
    dtable = Data(data_dict)
    dtable.add_dataframe_column(new_column)
    dtable.fill_dataframe_column(new_column, new_data)
    logging.info(dtable.columns)
    logging.info(dtable.df)
