import pandas as pd

df = pd.read_csv("employees.csv")
high_earners = df[   df["Salary"] >= 50000   ]
high_earners.to_csv("high_earners.csv", index=False)
print("Filtered data saved successfully!")
print(high_earners)
print(type(high_earners))