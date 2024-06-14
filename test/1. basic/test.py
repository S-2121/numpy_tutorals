import numpy as np
import timeit

print(np.__version__)

a_st= timeit.default_timer()

a = list(range(10000000))

for i, v in enumerate(a):
    a[i] = v*10

a_et= timeit.default_timer()

b_st= timeit.default_timer()

b = np.arange(0, 10000000)
b = b * 10

b_et= timeit.default_timer()

print("list :", a_et - a_st)
print("numpy :", b_et - b_st)
