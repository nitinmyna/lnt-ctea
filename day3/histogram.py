import matplotlib.pyplot as plt
diameter = [10.1, 10.2, 10.0, 10.3, 10.1, 9.9, 10.2, 10.0, 10.1, 10.4]
plt.hist(diameter, bins=5)
plt.title("Component Diameter Distribution")
plt.xlabel("Diameter (mm)")
plt.ylabel("Frequency")
plt.show()