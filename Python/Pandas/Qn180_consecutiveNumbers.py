import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    df = logs.copy()
    df['pre1'] = df['num'].shift(1)
    df['pre2'] = df['num'].shift(2)
    df['three_in_a_row'] = (df['num'] == df['pre1']) & (df['num'] == df['pre2'])

    result = df.loc[df['three_in_a_row'], 'num'].unique()
    final_df = pd.DataFrame(result, columns=['ConsecutiveNums'])

    return final_df