"""
author: Yuval Haimov

This code gets 6 examples of a xnor b xnor c and the resaults of those examples
and tries to learn how to anticipate the resaults of the 2 left possibilities
"""


import numpy as np

    
def sigmoid(sigma):
    
    return 1 / (1 + np.exp(-sigma))  


def sigmoid_derivative(output):
    
    return output * (1 - output)


training_set_inputs = np.array([[0, 0, 0],
                                [0, 0, 1],
                                [0, 1, 0],
                                [0, 1, 1],
                                [1, 0, 0],
                                [1, 0, 1]])
num_weights = (len(training_set_inputs[0]))
training_set_outputs = np.array([[0, 1, 1, 0, 1, 0]]).T
np.random.seed(1)
weights = np.array([])
for count in range(num_weights):
    weights = np.append(weights, [np.random.uniform(-1, 1)])

for iteration in range(5000):
    
    sigma = np.dot(training_set_inputs, weights)
    output = sigmoid(sigma)
    error = training_set_outputs - output
    weights += np.dot(training_set_inputs, error * output * (1 - output))
    
sigma = np.dot(training_set_inputs, weights)
print (sigmoid(sigma))
