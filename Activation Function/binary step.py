def binary_step(x):
    # Check if x is less than 0
    if x < 0:
        # Return 0 if true
        return 0
    else:
        # Return 1 if false
        return 1

# Test the function
input = -1
output = binary_step(input)

print(output)