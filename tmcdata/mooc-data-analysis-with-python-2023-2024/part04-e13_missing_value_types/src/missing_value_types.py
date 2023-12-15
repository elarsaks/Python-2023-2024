#!/usr/bin/env python3

import pandas as pd
import numpy as np


def missing_value_types():
    # Create a DataFrame with the given data
    data = {
        "State": ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"],
        "Year of independence": [np.nan, 1917, 1776, 1523, np.nan, 1992],
        "President": [None, "Niinistö", "Trump", None, "Steinmeier", "Putin"]
    }
    df = pd.DataFrame(data)

    # Set the 'State' column as the index
    df.set_index("State", inplace=True)

    return df


# Test the function
df = missing_value_types()
print(df)
