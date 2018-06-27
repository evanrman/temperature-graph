import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", sep = ",", skiprows = 1)

plt.title("Temperature Anomalies over Land and over Ocean")
plt.xlabel("Years")
plt.ylabel("Temperatures (Degrees Celsius)")
plt.plot(data["Year"],data["Land_Annual"], '-ro', linewidth = 1, markersize = 3)
plt.plot(data["Year"],data["Ocean_Annual"], '-bo', linewidth = 1, markersize = 3)
plt.show()

