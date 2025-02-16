#Change Data Type, solved Feb 13 2025
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int, copy = True, errors = "raise")
    return students
