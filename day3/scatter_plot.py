import matplotlib.pyplot as plt
load =        [13,  9, 15, 7, 20, 15, 5, 12, 18, 14]
deformation = [20, 10,  5, 2, 10, 15, 20, 10, 15, 6]
plt.scatter(load, deformation)
plt.title("Load vs Deformation")
plt.xlabel("Load (kN)")
plt.ylabel("Deformation (mm)")
plt.show()