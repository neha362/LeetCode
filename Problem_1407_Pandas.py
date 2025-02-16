#Top Travellers, Jan 7 2025
import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    return users.set_index("id").join(rides.groupby("user_id").sum()).fillna(0).sort_values(by = ["distance", "name"], ascending = [False, True]).rename(columns = {"distance": "travelled_distance"})[["name", "travelled_distance"]]
