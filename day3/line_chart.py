import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("sales_data.xlsx")

xaxis_data = df["Month"]
yaxis_data = df["Revenue"]

plt.figure(figsize=(12, 12))

plt.plot(
    xaxis_data,
    yaxis_data,
    marker='o',
    linestyle='-',
    color='b',
    label='Monthly Sales'
)

plt.title("Monthly Revenues")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.grid(True, linestyle='--')
plt.show()
