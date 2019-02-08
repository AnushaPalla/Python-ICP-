
import statistics
from statistics import mode
import numpy as np
randnums = np.random.randint(0,21,15)
print(randnums)
print("Most repeated value is:",statistics.mode(randnums))


