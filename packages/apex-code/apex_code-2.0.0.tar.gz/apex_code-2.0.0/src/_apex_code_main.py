from apex_code.utils.random import RandomNumberGenerator
from apex_code.utils.random import shuffle

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
    neural_network.SGD(inputs, outputs, 10, 120, test_inputs=inputs, test_outputs=outputs)

    w, a = neural_network.feed_forward(inputs[0])
    print(f'activation = {a[-1]}')
    w, a = neural_network.feed_forward(inputs[1])
    print(f'activation = {a[-1]}')
    w, a = neural_network.feed_forward(inputs[2])
    print(f'activation = {a[-1]}')
    w, a = neural_network.feed_forward(inputs[3])
    print(f'activation = {a[-1]}')

def shuffle_test():
    l = [[1,[1]],[2],[3],[4],[5],[6],[7],[8],[9]]
    s = shuffle(l)
    print(l)
    print(s)


def matrix_shuffle_test():
    m = Matrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
    print(m)
    m.shuffle()
    print(m)
if __name__ == '__main__':
    feed_forward_test()

