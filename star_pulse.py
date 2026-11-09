import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(0, 10, 100)
brightness = 1.0 + 0.1 * np.sin(time)  # A star that pulses!

plt.plot(time, brightness)
plt.xlabel("Time (days)")
plt.ylabel("Brightness")
plt.title("My Star's Pulse")
plt.show()