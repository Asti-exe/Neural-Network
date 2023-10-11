import numpy as np
def tanh_function(x):
    z = (2/(1 + np.exp(-2*x))) -1
    return z

output = tanh_function(0.5)

print(output)