import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    return(followers.groupby("user_id", as_index = False)['follower_id'].nunique().
           rename(columns={'follower_id' : 'followers_count'}).
           sort_values("user_id"))
    
    
