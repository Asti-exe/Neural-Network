def leaky_relu_function(x):
    if x<0:
        return 0.02*x
    else:
        return x
input = 7
output= leaky_relu_function(input)
print(output)