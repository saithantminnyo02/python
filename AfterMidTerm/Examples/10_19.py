import numpy as np
data = np.loadtxt('/home/saithantminnyo/python/Python/AfterMidTerm/Examples/sales.tsv', delimiter='\t', dtype=float)
print(data)
print(np.sum(data[0, 1:]))
