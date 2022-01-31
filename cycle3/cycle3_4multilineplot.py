# importing package
import matplotlib.pyplot as plt
import numpy as np

# create data
x = [1,2,3,4,5]
y = [3,3,3,3,3]
z = [4,4,4,4,4]
# plot lines
plt.plot(x, y, label = "line 1")
plt.plot(y, x, label = "line 2")
plt.plot(z, x, label = "line 3")
plt.legend()
plt.show()