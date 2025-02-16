#Calculate Special Bonus, solved Feb 15 2025
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees.insert(1, "bonus", np.where((~(employees["name"].astype(str).str.startswith("M")) & (employees["employee_id"] % 2 == 1)), employees["salary"], 0))
    return employees[["employee_id", "bonus"]].sort_values(by=["employee_id"])
