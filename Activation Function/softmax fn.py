import numpy as np

def softmax_function(x):
    z = np.exp(x)
    z = z/z.sum()
    return z

input = [0.8, 1.2, 3.3]
output = softmax_function(input)

print(output)