import pandas as pd

amazon = pd.read_csv("amazon.csv")
customer = pd.read_csv("customer_data(1).csv")

merged = amazon.merge(customer, on="user_id", how="left")
