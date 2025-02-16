#Reshape Data: Pivot, solved Feb 13 2025
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index = "month", columns = "city", values = "temperature")
