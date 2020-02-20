"""
We are gonna start with simple
and powerful activation function.
Later on I am gonna add more functions
"""
from bearx.tensor import Tensor

import numpy as np

# TODO: change sigmoid function 
def relu(inputs: Tensor) -> Tensor:
    assert type(inputs) == np.ndarray, "Inputs have to be a Tensor(np.array)!"
    return np.maximum(inputs, 0, inputs) 



def relu_prime(inputs: Tensor) -> Tensor:
    assert type(inputs) == np.ndarray, "Inputs have to be a Tensor(np.array)!"
    return (inputs>0).astype(inputs.dtype)


def sigmoid(inputs: Tensor) -> Tensor:
    assert type(inputs) == np.ndarray, "Inputs have to be a Tensor(np.array)!"
    inputs = [1 / (1 + np.exp(-inputs[node])) for node in range(len(inputs))]
    return np.array(inputs)


def sigmoid_prime(inputs: Tensor) -> Tensor:
    assert type(inputs) == np.ndarray, "Inputs have to be a Tensor(np.array)!"
    inputs = [sigmoid(node) * (1 - sigmoid(node)) for node in range(len(inputs))]
    return np.array(inputs)


def tanh(x: Tensor) -> Tensor:
    return np.tanh(x)


def tanh_prime(x: Tensor) -> Tensor:
    y = tanh(x)
    return 1 - y ** 2