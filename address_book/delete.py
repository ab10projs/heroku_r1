import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.show()

#print(plt.style.available)
plt.style.use('ggplot')

x = np.arange(0,10,.2)
y = np.sin(x)
z = np.cos(x)

plt.plot(y,z)
