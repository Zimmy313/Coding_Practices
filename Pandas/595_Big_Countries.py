import pandas as pd
import typings

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    result = df[['name','population','area']]

    return result