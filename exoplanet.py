import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(0, 10, 500)
brightness = np.ones(len(time))  # Normal brightness

# Simulate a planet passing in front of the star
for i in range(len(time)):
    if 4.5 < time[i] < 5.5:  # Transit happens between day 4.5 and 5.5
        brightness[i] = 0.97  # 3% dip in brightness

plt.plot(time, brightness, linewidth=2)
plt.xlabel("Time (days)")
plt.ylabel("Relative Brightness")
plt.title("Exoplanet Transit Detection")
plt.axhline(y=0.97, color='r', linestyle='--', label='Transit depth')
plt.legend()
plt.grid(True)
plt.show()