### Contains the statistical functions used in iteration 4.

# Imports the required math functions.
from math import exp as e

# Defines the factorial function.
def factorial(n):
    # Checks if the terminating condition has been reached.
    if n == 0:
        # Returns 1 to stop the recursion.
        return 1
    # Checks if the value of n is negative.
    elif n < 0:
        # Returns a value error if n is negative.
        return ValueError
    # Continues the recursion.
    else:
        return n * factorial(n-1)

# Defines the poisson probability function.
def poiProbability(poiSuccesses, poiRate):
    # Calculates the factorial of the number of successes.
    poiSuccessesFac = factorial(poiSuccesses)
    # Calculates e to the power of the negative of the average rate.
    poiRateExp = e(-(poiRate))
    # Calculates the probability.
    poiProb = (poiRateExp * (poiRate ** poiSuccesses)) / poiSuccessesFac
    # Returns the probability.
    return round(poiProb, 10)

# Defines the poisson cumulative probability function.
def poiCProbability(poiSuccesses, poiRate):
    # Defines the count variable.
    count = 0
    # Defines the variable to keep track of the cumulative probability.
    poiTotalProb = 0
    # Calculates each individual probability.
    while count <= poiSuccesses:
        # Calculates the individual probability.
        poiProb = poiProbability(count, poiRate)
        # Adds the probability to the total.
        poiTotalProb += poiProb
        # Increments the count variable.
        count += 1
    # Returns the probability.
    return round(poiTotalProb, 10)
