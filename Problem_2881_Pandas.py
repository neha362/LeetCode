#Create a New Column, solved Feb 13 2025
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.insert(2, "bonus", employees["salary"] * 2)
    return employees
    
