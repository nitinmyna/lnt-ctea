import pandas as pd

data = {
    "Machine": ["A", "B", "C", "D"],
    "Temperature": [72, 80, 75, 90],
    "Pressure": [30, 35, 32, 40],
    "Output": [85, 110, 95, 125]
}
df = pd.DataFrame(data)

print(df)