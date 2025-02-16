#Modify Columns, Feb 13 2025
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees[["salary"]] *= 2
    return employees
