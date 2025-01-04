from apex_code.math.linear_algebra.matrix import Matrix

class Activation:
    """
    Base class for neural network activation functions.

    Use this class as an interface for creating neural network activation functions. Subclasses must override the
    _activation() method with an activation function and _derivative() with the derivative of the activation function.
    """

    def __call__(self, x):
        """
        Applies the activation function to the parameter x.

        If x is a `Matrix`, the activation function will be applied to each element in the matrix.

        :param x: Variable that the activation function will be applied to.
        :return: Result of the activation function.
        """

        if type(x) == Matrix:
            return self._handle_matrices(x, self._activation)

        return self._activation(x)

    def derivative(self, x):
        """
        Applies the derivative of the activation function to the parameter x.

        If x is a `Matrix`, the activation function will be applied to each element in the matrix.

        :param x: Variable that the derivative of the activation function will be applied to.
        :return: Result of the activation function derivative.
        """

        if type(x) == Matrix:
            return self._handle_matrices(x, self._derivative)

        return self._derivative(x)

    def _activation(self, x):
        """
        Abstract method for the activation function.

        Subclasses must implement this method to define the activation function.

        :param x: Variable that the activation function will be applied to.
        :type x: apex_code.math.linear_algebra.matrix.Matrix or scalar e.g. (int, float)
        :return: Result of the activation function.
        :raises NotImplementedError: If the activation function has not been implemented in the subclass.
        """

        raise NotImplementedError('Activation function has not been implemented')

    def _derivative(self, x):
        """
        Abstract method for the derivative of the activation function.

        Subclasses must implement this method to define the activation function.

        :param x: Variable that the activation derivative function will be applied to.
        :type x: apex_code.math.linear_algebra.matrix.Matrix or scalar e.g. (int, float)
        :return: The result of the activation derivative when applied to x.
        :raises NotImplementedError: If the activation function has not been implemented in the subclass.
        """

        raise NotImplementedError('Activation derivative function has not been implemented')

    def _handle_matrices(self, matrix, func):
        """
        Passes each element in the matrix to function func and replaces the element with the result of func.

        :param matrix: A standard matrix
        :type matrix: apex_code.math.linear_algebra.matrix.Matrix
        :param func: The activation or activation derivative method.
        :type func: function
        :return: New matrix where each element is replaced with the value returned by func
        """

        new_matrix = Matrix.zero((matrix.rows, matrix.columns))
        for row in range(matrix.rows):
            for column in range(matrix.columns):
                new_matrix[row][column] = func(matrix[row][column])
        return new_matrix


class _Sigmoid(Activation):
    """
    A sigmoid activation class for neural networks

    use the __call__() method to calculate the activation of the input and derivative to calculate the derivative
    of the activation function
    """

    def _activation(self, x):
        return 1 / (1 + 2.718281828**-x)

    def _derivative(self, x):
        return self.__call__(x) * (1 - self.__call__(x))

sigmoid = _Sigmoid()
