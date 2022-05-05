import logging

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(msg)s")

data = {
    "col1": [1, 2, 3, 4, 5],
    "col2": ["a", "b", "c", "d", "e"],
    "col3": [True, True, False, True, True],
}


def create_dataframe(data: dict) -> pd.DataFrame:
    return pd.DataFrame(data)


if __name__ == "__main__":
    df = create_dataframe(data)
    logging.info(df)
