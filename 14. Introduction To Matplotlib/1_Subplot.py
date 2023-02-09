
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [5, 15, 1, 3, 5, 11]

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.scatter(x, y)


plt.show()
