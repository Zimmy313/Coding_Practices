import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts()
    unique = counts[counts == 1].index

    if len(unique) == 0:
        return pd.DataFrame({'num': [None]})
    else:
        return pd.DataFrame({'num': [unique.max()]})