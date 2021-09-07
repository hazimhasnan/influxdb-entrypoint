import matplotlib.pyplot as plt
import math
import numpy as np
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


value = []
x = 0
for i in range(65):
    x += 0.1
    value.append((2 * math.sin(x)) + 5)

plt.plot(value)
plt.show()


x_axis = np.arange(0, 10, 0.1)
amplitude = np.sin(x_axis)

plt.plot(amplitude)
plt.show()
