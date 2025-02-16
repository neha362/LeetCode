#Fix Names in a Table, solved Feb 15 2025
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].astype(str).str.lower().str.capitalize()
    return users.sort_values(by = ["user_id"])
