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

# Defines the combination function.
def combination(binTrials, binSuccesses):
    # Calculates the factorial of the number of successes.
    binSuccessesFac = factorial(binSuccesses)
    # Calculates the factorial of the number of trials.
    binTrialsFac = factorial(binTrials)
    # Calculates the factorial of the difference.
    binDiffFac = factorial(binTrials - binSuccesses)
    # Calculates the combination.
    binCombination = binTrialsFac / (binSuccessesFac * binDiffFac)
    # Tries to return the combination as an integer.
    try:
        # Returns the combination.
        return int(binCombination)
    # Catches any value errors if the combination is not an integer.
    except ValueError:
        return ValueError

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

# Defines the binomial probability function.
def binProbability(binTrials, binSuccesses, binPValue):
    # Calculates the combination for the input number of trials and successes.
    binCombination = combination(binTrials, binSuccesses)
    # Calculates the probability.
    binProb = binCombination * ((binPValue) ** binSuccesses) * ((1 - binPValue) ** (binTrials - binSuccesses))
    # Returns the probability.
    return round(binProb, 10)

# Defines the binomial cumulative probability function.
def binCProbability(binTrials, binSuccesses, binPValue):
    # Defines the count variable.
    count = 0
    # Defines the variable to store the cumulative probability.
    binTotalProb = 0
    # Calculates each individual probability and adds them to the total.
    while count <= binSuccesses:
        # Calculates the probability.
        binProb = binProbability(binTrials, count, binPValue)
        # Adds the probability to the total.
        binTotalProb += binProb
        # Increments the count variable.
        count += 1
    # Returns the probability.
    return round(binTotalProb, 10)
