import matplotlib.pyplot as plt

time = [1, 2, 3, 4, 5, 6]
temperature = [25, 28, 31, 35, 33, 30]

plt.plot(time, temperature, marker="o")
plt.title("Temperature vs Time")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()