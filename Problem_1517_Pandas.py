#Find Users With Valid E-Mails, solved Feb 16 2025
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users["mail"].astype(str).str.match("^[a-zA-Z][a-zA-Z0-9\-._]*@leetcode\.com$")]
