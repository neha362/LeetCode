#Customers Who Never Order, solved Feb 15 2025
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers[~customers["id"].isin(orders["customerId"])][["name"]].rename(columns={"name":"Customers"})
