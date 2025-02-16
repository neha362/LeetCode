#Invalid Tweets, solved Feb 15 2025
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets["content"].astype(str, copy = False).str.len() > 15][["tweet_id"]]
