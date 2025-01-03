import numpy as np

inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
expected_outputs = np.array([0, 0, 0, 1])

weights = np.array([1, 1])
threshold = 1.5

def perceptron(x, weights, threshold):
    weighted_sum = np.dot(x, weights)
    return 1 if weighted_sum >= threshold else 0

print("AND Gate using McCulloch-Pitts Model:")
for i in range(len(inputs)):
    output = perceptron(inputs[i], weights, threshold)
    print(f"Input: {inputs[i]} -> Output: {output} (Expected: {expected_outputs[i]})")
