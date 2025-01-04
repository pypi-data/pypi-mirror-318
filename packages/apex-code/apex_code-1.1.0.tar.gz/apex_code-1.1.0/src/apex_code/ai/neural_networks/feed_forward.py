from apex_code.math.linear_algebra.matrix import Matrix
from apex_code.ai.neural_networks.activations import sigmoid
from apex_code.utils.random import RandomNumberGenerator

class FeedForward:

    def __init__(self, layers, activation=sigmoid):
        self.layers = layers
        self.activation = activation
        self.number_of_layers = len(layers)
        self.rng = RandomNumberGenerator().random
        self.weights = self.randomize_weights()
        self.biases = self.randomize_biases()


    def randomize_weights(self):
        # Creates a list matrices of randomized weights of CurrentLayerNeuron x PreviousLayerNeuron

        list_of_weights = []

        for layer in range(1, self.number_of_layers):
            weights_matrix = Matrix.zero((self.layers[layer], self.layers[layer - 1]))
            for row in range(weights_matrix.rows):
                for col in range(weights_matrix.columns):
                    weights_matrix[row][col] = self.rng()
            list_of_weights.append(weights_matrix)

        return list_of_weights

    def randomize_biases(self):
        # returns a list of matrices of randomized biases per layer

        list_of_biases = []

        for layer_size in self.layers[1:]:
            bias_matrix = Matrix.zero((layer_size, 1))

            for row in range(bias_matrix.rows):
                bias_matrix[row][0] = self.rng()

            list_of_biases.append(bias_matrix)

        return list_of_biases


    def feed_forward(self, inputs):
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
        if not batch_size:
            batch_size = len(inputs)

        input_batches = [inputs[i:i + batch_size] for i in range(0, len(inputs), batch_size)]
        output_batches = [outputs[i:i + batch_size] for i in range(0, len(outputs), batch_size)]

        for _ in range(epoch):
            for input_batch, output_batch in zip(input_batches, output_batches):
                self.mini_batch(input_batch, output_batch, learning_rate)
            if test_inputs and test_outputs:
                self.evaluate(test_inputs, test_outputs, _)

    def cost_derivate(self, output, expected_output):
        return 2 * (output - expected_output)

    def mini_batch(self, inputs, expected_outputs, learning_rate):
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
