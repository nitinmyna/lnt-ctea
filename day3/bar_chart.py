import matplotlib.pyplot as plt

machines = ["Machine A", "Machine B", "Machine C", "Machine D"]
output = [85, 110, 95, 125]

plt.bar(machines, output)
plt.title("Machine Output Comparison")
plt.xlabel("Machines")
plt.ylabel("Output (units/hour)")
plt.show()