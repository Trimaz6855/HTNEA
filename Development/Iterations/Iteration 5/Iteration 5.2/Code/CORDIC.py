# Imports the square root function from the math library.
from math import sqrt, atan2, radians, pi

# Scaling factor, recalculate if number of iterations changes.
k = 0.6072529350088814

# Number of iterations.
n = 40

# Stores a list of arctan values.
thetaTable = [atan2(1, 2**i) for i in range(n)]

# Defines the CORDIC function.
def CORDIC(theta):

    # Checks that the angle is a number.
    try:
        # Tries to convert the angle to a number
        theta = float(theta)
    # Catches any value errors.
    except ValueError:
        # Returns an error message.
        return "Invalid Angle"

    #Code to convert input angle in radians to between 0 and pi/2.
    while (theta >= (2*pi)):
        theta -= (2*pi)

    #Assigns a marker to determine the quadrant of the unit circle that the angle lies within.
    #Converts the angle to the first quadrant of the unit circle.
    if theta >= 0 and theta < (pi/2):
        quadrant = 1
        theta = theta
    # Converts from second quadrant to first.
    elif theta >= (pi/2) and theta < pi:
        quadrant = 2
        theta = pi - theta
    # Converts from third quadrant to first.
    elif theta >= pi and theta < ((3*pi)/2):
        quadrant = 3
        theta = theta - pi
    # Converts from fourth quadrant to first.
    elif theta >= ((3*pi)/2) and theta < (2*pi):
        quadrant = 4
        theta = (2*pi) - theta
    # Defaults to first quadrant.
    else:
        quadrant = 1
        theta = theta

    # Defines x and y to have the (x, y) values of the initial vector (1, 0).
    x = 1
    y = 0
    # Starting angle of 0
    z = 0
    # Used as the value of 2**-i to reduce the number of loops required.
    v2i = 1
    # Loops through values in the thetaTable.
    for value in thetaTable:
        # Checks if the initial angle is smaller than the desired angle.
        if z < theta:
            # Makes d positive for an anticlockwise rotation.
            d = +1
        else:
            # Makes d negative for a clockwise rotation.
            d = -1
        # Temporarily stores the value of x.
        x1 = x
        # Rotates z by the first value in the thetaTable.
        z = z + (d * value)
        # Adjusts the value of x.
        x = x - (d * y * v2i)
        # Adjusts the value of y.
        y = y + (d * x1 * v2i)
        # Increments i (calculates 2**-(i+1)).
        v2i = v2i / 2

    # Applies the scaling factor to the sine and cosine values.
    cosine = x*k
    sine = y*k

    #Code to convert the answer to the correct quadrant.
    try:
        # Checks the quadrant the angle is in.
        match quadrant:
            # Angle is in second quadrant.
            case 2:
                # Converts the cosine value to be in the second quadrant.
                cosine = 0 - cosine
            # Angle is in the third quadrant.
            case 3:
                # Converts the sine value to be in the third quadrant.
                sine = 0 - sine
                # Converts the cosine value to be in the third quadrant.
                cosine = 0 - cosine
            # Angle is in the fourth quadrant.
            case 4:
                # Converts the sine value to be in the fourth quadrant.
                sine = 0 - sine
    # Catches any errors where the quadrant is not defied.
    except UnboundLocalError:
        # Terminates the function by returning the error.
        return UnboundLocalError

    # Rounds the sine and cosine values.
    sine = round(sine, 10)
    cosine = round(cosine, 10)

    # Checks if the cosine value
    if (theta%(pi/2)) == 0 and (theta%(pi)) != 0:
        # Defines tangent as undefined to avoid a zero division error.
        tangent = "Undefined"
    else:
        # Calculates the tangent value for the sine and cosine values
         tangent = sine / cosine

    # Returns the coordinates adjusted by the scaling factor
    return cosine, sine, tangent

# Function to calculate the scaling factor, only used if number of iterations changes
def calcK(n):
    # Initialises k as 1
    k = 1
    # Calculates the product of k_i
    for i in range(0, n):
        k = k * (1 / sqrt(1+2**(-2*i)))
    # Returns k
    return k

# Runs the program
if __name__ == "__main__":
    results = CORDIC(pi)
    if len(results) == 1:
        print(results)
    else:
        print(f"Cosine: {results[0]}\n",
              f"Sine: {results[1]}\n",
              f"Tangent: {results[2]}", sep="")
