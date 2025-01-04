from apex_code.math.linear_algebra.matrix import Matrix
from apex_code.ai.neural_networks import activations
from apex_code.utils.random import RandomNumberGenerator, shuffle

class FeedForward:
    """
    Feed Forward Neural Network
    """


    _RANDOM_NUMBER_GENERATORS = ['uniform', 'gaussian']

    def __init__(self, layers, activation=activations.sigmoid, weight_initialization='gaussian', bias_initialization='gaussian'):
        """
        Initializes a feed forward neural network with customizable activations functions and
        weight/bias initialization methods.

        Layers:
        The first element in layers will be the number of inputs in the first layer and the last layer will be the
        number of outputs in the output layer. Everything inbetween is the number of neurons in the hidden layers.

        Activation:
        The activation function used in the neural network. Can be imported from apex_code.ai.neural_networks.activations.

        Weight and Bias Initialization
        The random number generator used to initialize the weights and biases, must be one of the
        following ['uniform', 'gaussian']. Defaults to 'gaussian'


        :param layers: list of integers where each element is a layer and the value inside the element is the number of
        neurons in that layer.
        :type layers: list[int].
        :param activation: The activation function
        :type activation: apex_code.ai.neural_networks.activations.*
        :param weight_initialization: The random number generator used to initialize the weights.
        :type weight_initialization: string, must be one of the following ('uniform', 'gaussian') defaults to 'gaussian'
        :param bias_initialization: The random number generator used to initialize the biases.
        :type bias_initialization: string, must be one of the following ('uniform', 'gaussian') defaults to 'gaussian'
        """

        self.layers = layers
        self.activation = activation
        self.number_of_layers = len(layers)
        self.weights = self.initialize_weights(rng=weight_initialization)
        self.biases = self.randomize_biases(rng=bias_initialization)

    def initialize_weights(self, rng='gaussian'):
        """
        Randomly initialize weights based on the type of random number generator defined in rng.
        Creates a list matrices of randomized weights of CurrentLayerNeuron x PreviousLayerNeuron

        :param rng: Random number generator type. Defaults to 'gaussian'.
        :return: Matrix of randomized weights.
        """

        if rng == 'uniform':
            rng = RandomNumberGenerator().uniform
        elif rng == 'gaussian':
            rng = RandomNumberGenerator().gaussian
        else:
            raise ValueError(
                f'{rng} is not a valid random number generator. Expected one of the following '
                f'{', '.join(FeedForward._RANDOM_NUMBER_GENERATORS)}')

        list_of_weights = []

        for layer in range(1, self.number_of_layers):
            weights_matrix = Matrix.zero((self.layers[layer], self.layers[layer - 1]))
            for row in range(weights_matrix.rows):
                for col in range(weights_matrix.columns):
                    weights_matrix[row][col] = rng()
            list_of_weights.append(weights_matrix)

        return list_of_weights

    def randomize_biases(self, rng='gaussian'):
        """
        Randomly initialize biases based on the type of random number generator defined in rng.
        returns a list of matrices of randomized biases per layer

        :param rng: Random number generator type. Defaults to 'gaussian'.
        :return: Matrix of randomized biases.
        """

        if rng == 'uniform':
            rng = RandomNumberGenerator().uniform
        elif rng == 'gaussian':
            rng = RandomNumberGenerator().gaussian
        else:
            raise ValueError(
                f'{rng} is not a valid random number generator. Expected one of the following '
                f'{', '.join(FeedForward._RANDOM_NUMBER_GENERATORS)}')

        list_of_biases = []

        for layer_size in self.layers[1:]:
            bias_matrix = Matrix.zero((layer_size, 1))

            for row in range(bias_matrix.rows):
                bias_matrix[row][0] = rng()

            list_of_biases.append(bias_matrix)

        return list_of_biases


    def feed_forward(self, inputs):
        """
        Pass inputs through the neural network

        :param inputs: the input data for the neural network.
        :type inputs: apex_code.math.linear_algebra.matrix.Matrix of dimension Nx1 where N is the number of
        neurons in the input layer.
        :return: a tuple of (weighted_sums, activations) per layer.
        """

        weighted_sums = []
        activations = []
        activation = inputs

        activations.append(inputs)
        for layer in range(len(self.weights)):
            weighted_sum = (self.weights[layer] * activation) + self.biases[layer]
            weighted_sums.append(weighted_sum)
            activation = self.activation(weighted_sum)
            activations.append(activation)

        return weighted_sums, activations


    def SGD(self, inputs, outputs, learning_rate, epoch, batch_size=None, test_inputs=None, test_outputs=None):
        """
        Stochastic gradient descent

        Trains the neural network using stochastic gradient descent

        :param inputs: list of inputs [Matrix]
        :param outputs: list of outputs [Matrix]
        :param learning_rate: learning rate of the neural network
        :param epoch: Number of training cycles
        :param batch_size: Size the data will be split into
        :param test_inputs: test inputs
        :param test_outputs: test outputs
        """

        if not batch_size:
            batch_size = len(inputs)

        for _ in range(epoch):
            # TODO: shuffle does not create a deep copy. It alters the current list.
            #  this could cause hard to trace bugs. Update shuffle function to create a deep copy
            shuffle(inputs)
            shuffle(outputs)

            input_batches = [inputs[i:i + batch_size] for i in range(0, len(inputs), batch_size)]
            output_batches = [outputs[i:i + batch_size] for i in range(0, len(outputs), batch_size)]

            for input_batch, output_batch in zip(input_batches, output_batches):
                self.mini_batch(input_batch, output_batch, learning_rate)
            if test_inputs and test_outputs:
                self.evaluate(test_inputs, test_outputs, _)

    def cost_derivate(self, output, expected_output):
        return 2 * (output - expected_output)

    def mini_batch(self, inputs, expected_outputs, learning_rate):
        """
        Calculate the gradients for the current batch and update the weights and biases based on the gradient

        :param inputs: input batch
        :param expected_outputs: output batch
        :param learning_rate: learning rate of the neural network
        """


        w_gradients_sum = [Matrix.zero((weight.rows,weight.columns)) for weight in self.weights]
        b_gradients_sum = [Matrix.zero((bias.rows,bias.columns)) for bias in self.biases]
        n = len(inputs)

        for x, y in zip(inputs, expected_outputs):
            w_gradients, b_gradients = self.back_prop(x, y)

            for i in range(len(w_gradients)):
                w_gradients_sum[i] += w_gradients[i]
                b_gradients_sum[i] += b_gradients[i]

        for i in range(len(w_gradients_sum)):
            w_gradients_sum[i] *= 1/n
            b_gradients_sum[i] *= 1/n
            self.weights[i] -= learning_rate * w_gradients_sum[i]
            self.biases[i] -= learning_rate * b_gradients_sum[i]



    def back_prop(self, x, y):
        """
        Calculate the gradient for inputs x using y as the expected outputs

        :param x: inputs
        :param y: expected outputs
        :return: tuple of the weighted sums and activations
        """

        weighted_sums, activations = self.feed_forward(x)
        w_gradients = []
        b_gradients = []

        delta = self.cost_derivate(activations[-1], y)
        sigmoid_derivative = self.activation.derivative(weighted_sums[-1])

        delta = delta.element_wise_product(sigmoid_derivative)

        w_gradient = delta * activations[-2].transpose()
        w_gradients.append(w_gradient)
        b_gradient = delta
        b_gradients.append(b_gradient)

        for layer in range(2, len(activations)):
            sigmoid_derivative = self.activation.derivative(weighted_sums[-layer])

            delta =  self.weights[-layer+1].transpose() * delta
            delta = sigmoid_derivative.element_wise_product(delta)

            w_gradient = delta * activations[-layer-1].transpose()
            w_gradients.append(w_gradient)
            b_gradient = delta
            b_gradients.append(b_gradient)


        w_gradients.reverse()
        b_gradients.reverse()

        return w_gradients, b_gradients

    def evaluate(self, test_inputs, test_outputs, epoch):
        """
        Evaluates the accuracy of the neural network using test inputs and outputs and
        prints the results to STDOUT.

        :param test_inputs: test inputs
        :param test_outputs: expected outputs for test inputs
        :param epoch: The current epoch in the neural networks training session
        """
        correct = 0
        for x, y in zip(test_inputs, test_outputs):
            w, a = self.feed_forward(x)
            predicted_vector = a[-1].transpose()[0]
            expected_vector = y.transpose()[0]

            predicted_index = predicted_vector.index(max(predicted_vector))
            expected_index = expected_vector.index(max(expected_vector))

            if predicted_index == expected_index:
                correct += 1

        accuracy = (correct / len(test_inputs)) * 100
        print(f'epoch {epoch}: {accuracy}')
