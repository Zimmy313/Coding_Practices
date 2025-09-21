import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    df = triangle
    df['triangle'] = (
        (df['x'] + df['y'] > df['z']) &
        (df['x'] + df['z'] > df['y']) &
        (df['y'] + df['z'] > df['x'])
    )

    df['triangle'] = df['triangle'].map({
        True:'Yes',
        False:'No'
    })

    return df