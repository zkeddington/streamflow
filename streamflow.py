# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


"""### Part 3 - Provo River Streamflow Data

You will now create a graph using streamflow data of the Provo River in June 2021.

### Numpy Array Creation & Slicing

Create and slice the array to create the x and y-axis values. These will correspond to the following columns in the CSV linked on the HW instructions page:

*   x - Date
*   y_1 - Site 10163000
*   y_2 - Site 10155200
*   y_3 - Site 10155500
*   y_4 - Site 10154200
*   y_5 - Site 10155000
"""

array2 = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv', delimiter=',',dtype=str,skip_header=1)
x = array2[:, 0]
y_1 = array2[:,1].astype(float)
y_2 = array2[:,2].astype(float)
y_3 = array2[:,3].astype(float)
y_4 = array2[:,4].astype(float)
y_5 = array2[:,5].astype(float)

"""### Graphing the Data

Plot x, y_1, y_2, y_3, y_4, and y_5 with the elements shown in the instructions in the code block below.
"""

plt.figure(figsize=(10, 6))
plt.plot(x, y_1, color='purple', label='10163000')
plt.plot(x, y_2, color='blue', label='10155200')
plt.plot(x, y_3, color='green', label='10155500')
plt.plot(x, y_4, color='yellow', label='10154200')
plt.plot(x, y_5, color='red', label='10155000')

# AI made this to adjust the density of dates on the x-axis so they are legible
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
plt.xticks(rotation=45)

plt.title('Provo River Streamflow Data (2021)')
plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')
plt.legend(loc='upper right', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
