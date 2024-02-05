from numpy.random import Generator
from randomgen import Xoroshiro128

# Create a random number generator
rng = Xoroshiro128()

result = rng.random(size=1)  # Generate a random float in the half-open interval [0.0, 1.0)
die_roll = int(1 + 6 * result)  # Scale the float to the range [1, 6]
print(die_roll)