import math
from apex_code.math.constants import PI

class RandomNumberGenerator:
    """
    Pseudo random number generator

    Generates a pseudo random number using the linear congruential generator algorithm (LCG). The results of the
    generator are deterministic and depend on the initial value of the seed.
    """

    def __init__(self, seed=None):
        """
        Creates a pseudo random number generator

        The sequence of numbers generated is deterministic and depends on the initial value of the seed.
        If a seed is not provided the seed will default to 4815162342.

        :param seed: starting value in the generators sequence of pseudo random numbers. Defaults to 4815162342.
        :type seed: int
        :raises TypeError: If the seed is not of type int.
        """

        if seed is None:
            self.seed = 4815162342
        else:
            if not isinstance(seed, int):
                raise TypeError(f'Seed must be of type int. Received {type(seed)}')
            self.seed = seed

        self.m = 2**32
        self.a = 1664525
        self.c = 1013904223
        self.x = self.seed

    def uniform(self):
        """
        Generates the next value in the sequence of pseudo random numbers in the range [0, 1].

        :return: pseudo randomly generated number
        """

        self.x = (self.a * self.x + self.c) % self.m

        return self.x / self.m

    def uniform_integers(self, low=0, high=2**32-1):
        """
        Generates the next value in the sequence of pseudo random numbers.

        Use low and high to generate a number in a specific range.

        :param low: The start of inclusive range, must be greater than or equal to 0 (defaults to 0)
        :type low: int
        :param high: The end of the inclusive range, must be less than 2**32 (defaults to 2**32 - 1)
        :type high: int
        :return: pseudo randomly generated number
        :raises TypeError: If low or high are not of type int.
        :raises ValueError: If low < 0 or high >= 2**32.
        :raises ValueError: If low > high.
        """

        if not isinstance(low, int):
            raise TypeError(f'low must be of type int. Received {type(low)}')

        if not isinstance(high, int):
            raise TypeError(f'high must be of type int. Received {type(high)}')

        if low < 0:
            raise ValueError(f'low must be greater than or equal to 0. Received {low}')

        if high >= 2**32:
            raise ValueError(f'high must be less than 2**32. Received {high}')

        if low > high:
            raise ValueError(f'low must be less than or equal to high. low = {low}, high = {high}')

        self.x = (self.a * self.x + self.c) % self.m

        range_size = high - low + 1

        return (self.x % range_size) + low

    def gaussian(self, mean=0, sigma=1):
        """
        Generates a random number in a gaussian distribution

        :param mean: the mean of the distribution.
        :type mean: int, float
        :param sigma: Controls the variation of the distribution
        :type sigma: int, float
        :return: A randomly generated number in a gaussian distribution
        """

        if not isinstance(mean, int) and not isinstance(mean, float):
            raise ValueError(f'mean must be of type float or int: Received {type(mean)}')
        if not isinstance(sigma, int) and not isinstance(sigma, float):
            raise ValueError(f'sigma must be of type float or int: Received {type(mean)}')

        x = self.uniform()
        y = self.uniform()
        z1 = math.sqrt(-2*math.log2(x)) * math.cos(2*PI*y)

        return mean + (sigma * z1)