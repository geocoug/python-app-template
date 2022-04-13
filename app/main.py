import pandas as pd

data = {
    "col1": [1, 2, 3, 4, 5],
    "col2": ["a", "b", "c", "d", "e"],
    "col3": [True, True, False, True, True],
}
df = pd.DataFrame(data)
print(df)
