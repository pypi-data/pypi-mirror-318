from apex_code.utils.random import RandomNumberGenerator
from apex_code.math.linear_algebra.matrix import Matrix
from apex_code.math.constants import euler, PI
from apex_code.ai.neural_networks.feed_forward import FeedForward
from apex_code.ai.neural_networks.activations import sigmoid
import math


def feed_forward_test():
    neural_network = FeedForward([2, 3, 2], activation=sigmoid)

    inputs = [
        Matrix([[0], [0]]),
        Matrix([[1], [0]]),
        Matrix([[0], [1]]),
        Matrix([[1], [1]]),
    ]

    outputs = [
        Matrix([[1], [0]]),
        Matrix([[0], [1]]),
        Matrix([[0], [1]]),
        Matrix([[1], [0]])
    ]
    ti = [
        Matrix([[0], [0]]),
        Matrix([[1], [0]]),
        Matrix([[0], [1]]),
        Matrix([[1], [1]])
    ]
    to = [
        Matrix([[1], [0]]),
        Matrix([[0], [1]]),
        Matrix([[0], [1]]),
        Matrix([[1], [0]])
    ]
    neural_network.SGD(inputs, outputs, 10, 100, test_inputs=inputs, test_outputs=outputs)

    w, a = neural_network.feed_forward(inputs[0])
    print(f'activation = {a[-1]}')
    w, a = neural_network.feed_forward(inputs[1])
    print(f'activation = {a[-1]}')
    w, a = neural_network.feed_forward(inputs[2])
    print(f'activation = {a[-1]}')
    w, a = neural_network.feed_forward(inputs[3])



if __name__ == '__main__':
    import numpy
    r2 = RandomNumberGenerator()
    r = numpy.random.default_rng(4815162342)
    d1 = [0] * 200
    nd1 = [0] * 200
    d2 = [0] * 200
    nd2 = [0] * 200
    for i in range(100):

        g1 = r.normal()
        g2 = r2.gaussian(mean='2')
        print(f'{g1} : {g2}')

