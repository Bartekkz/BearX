import sys
sys.path.append("..")

from bearx.layers import RNN
import numpy as np

x = np.array([1,1])
rnn = RNN(1, 2, 1)
rnn
x = rnn.forward(x, rnn.state)
print(x)
