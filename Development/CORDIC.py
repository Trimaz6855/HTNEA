# Imports the square root function from the math library
from math import sqrt, atan2, radians, pi

# Scaling factor, recalculate if number of iterations changes
k = 0.6072529350088814

# Number of iterations
n = 40

# Stores a list of arctan values
thetaTable = [atan2(1, 2**i) for i in range(n)]

# Defines the CORDIC function
def CORDIC(theta):

    #Code to convert input angle in radians to between 0 and pi/2
    while (theta >= (2*pi)):
	    theta -= (2*pi)

    #Assigns a marker to determine the quadrant of the unit circle that the angle lies within
    #Converts the angle to the first quadrant of the unit circle
    if theta >= 0 and theta < (pi/2):
        quadrant = 1
        theta = theta
    elif theta >= (pi/2) and theta < pi:
    	quadrant = 2
    	theta = pi - theta
    elif theta >= pi and theta < ((3*pi)/2):
        quadrant = 3
        theta = theta - pi 
    elif theta >= ((3*pi)/2) and theta < (2*pi):
        quadrant = 4
        theta = (2*pi) - theta 
    else:
        quadrant = 1
        theta = theta

    # Defines x and y to have the (x, y) values of the initial vector (1, 0)
    x = 1
    y = 0
    # Starting angle of 0
    z = 0
    # Used as the value of 2**-i to reduce the number of loops required
    v2i = 1
    # Loops through values in the thetaTable
    for value in thetaTable:
        # Checks if the initial angle is smaller than the desired angle
        if z < theta:
            # Makes d positive for an anticlockwise rotation
            d = +1
        else:
            # Makes d negative for a clockwise rotation
            d = -1
        # Temporarily stores the value of x
        x1 = x
        # Rotates z by the first value in the thetaTable
        z = z + (d * value)
        # Adjusts the value of x
        x = x - (d * y * v2i)
        # Adjusts the value of y
        y = y + (d * x1 * v2i)
        # Increments i (calculates 2**-(i+1))
        v2i = v2i / 2

    cosine = x*k
    sine = y*k

    #Code to convert the answer to the correct quadrant
    try:
        match quadrant:
            case 2:
                    cosine = 0 - cosine
            case 3:
                    sine = 0 - sine
                    cosine = 0 - cosine
            case 4:
                    sine = 0 - sine
    except UnboundLocalError:
        pass

    if (theta%(pi/2)) == 0 and (theta%(pi)) != 0:
        tangent = "Undefined"
        cosine = 0
    else:
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
    a = float(input("Enter angle: "))
    cosine, sine, tangent = CORDIC(radians(a))
    if tangent == "Undefined":
        print(f"Sin({a}) = {sine:.10f}, Cos({a}) = {cosine:.10f}, Tan({a}) = {tangent}")
    else:
        print(f"Sin({a}) = {sine:.10f}, Cos({a}) = {cosine:.10f}, Tan({a}) = {tangent:.10f}")
