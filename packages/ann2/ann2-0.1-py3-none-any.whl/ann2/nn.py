import numpy as np

INPUTS = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])

def step_function(sum):
    return 1 if sum >= 0 else -1

def calculate_output(weights, instance, bias):
    return step_function(np.dot(instance, weights) + bias)

def hebb(outputs):
    weights, bias = np.zeros(2), 0 
    for i in range(len(outputs)):
        weights += INPUTS[i] * outputs[i]
        bias += outputs[i]
    return weights, bias

def train_and_print(gate_name, outputs):
    weights, bias = hebb(outputs)
    print(f"\n{gate_name.upper()} Gate:")
    for input_vec in INPUTS:
        output = calculate_output(weights, input_vec, bias)
        print(f"Input: {input_vec}, Output: {output}")

and_outputs = np.array([1, -1, -1, -1])
or_outputs = np.array([1, 1, 1, -1])

train_and_print("AND", and_outputs)
train_and_print("OR", or_outputs)
