import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.nonparametric.smoothers_lowess as sm



# getting data from file
data = pd.read_csv("data.csv", sep = ",", skiprows = 1)

# curve fitting
smooth_line = pd.DataFrame(sm.lowess( data["Land_Annual"], data["Year"]))

#legend
fig, ax = plt.subplots()
ax.plot(data["Year"], data["Land_Annual"],  '-ro', label= 'Land Surface',linewidth = 1, markersize = 3)
ax.plot(data["Year"], data["Ocean_Annual"], '-bo', label= 'Ocean', linewidth = 1, markersize = 3)
ax.plot(smooth_line.loc[:,0],smooth_line.loc[:,1], '-go', label= 'Smoothed', linewidth = 1, markersize = 3)

legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

# plotting data
plt.title("Temperature Anomalies over Land and over Ocean")
plt.xlabel("Years")
plt.ylabel("Temperatures (Degrees Celsius)")

# showing the data
plt.show()
