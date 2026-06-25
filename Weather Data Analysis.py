import numpy as np

temps = np.array([32, 35, 30, 28, 36, 34, 31])

print("Temperature Data:", temps)

avg_temp = np.mean(temps)
print("Average Temperature:", avg_temp)

print("Maximum Temperature:", np.max(temps))
print("Minimum Temperature:", np.min(temps))

print("Hottest Day:", np.argmax(temps) + 1)
print("Coldest Day:", np.argmin(temps) + 1)

above_avg = temps[temps > avg_temp]
print("Temperatures Above Average:", above_avg)