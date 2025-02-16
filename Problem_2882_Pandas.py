#Drop Duplicate Rows, Feb 13 2025
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset = ["email"], inplace = True)
    return customers
