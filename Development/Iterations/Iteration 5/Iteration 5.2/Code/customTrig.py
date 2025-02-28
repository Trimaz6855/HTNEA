### Custom functions Used in iteration 5 ###

# Imports the necessary constants from the math library.
from math import pi

# Defines the function to convert angles to radians.
def toRad(trigInput, trigAngle):
    # Checks that the angle is a number.
    try:
        # Tries to convert the angle to a number.
        trigInput = float(trigInput)
    # Catches any value errors.
    except ValueError:
        # Returns an error message.
        return "Invalid Angle"

    # Checks what the input angle unit is.
    match trigAngle:
        # Input angle unit is degrees.
        case "Deg":
            # Converts the angle into degrees.
            trigInput = trigInput * pi / 180.0
        # Input angle unit is gradians.
        case "Grad":
            # Converts the angle into gradians.
            trigInput = trigInput * pi / 200.0

    # Returns the converted angle.
    return trigInput

# Defines the function to convert angles to degrees.
def toDeg(trigInput, trigAngle):
    # Checks that the input angle is a number.
    try:
        # Tries to convert the angle to a number.
        trigInput = float(trigInput)
    # Catches any value errors.
    except ValueError:
        # Returns an error message.
        return "Invalid Angle"

    # Checks what the input angle unit is.
    match trigAngle:
        # Input angle is in radians.
        case "Rad":
            trigInput = trigInput * 180.0 / pi
        # Input angle is in gradians.
        case "Grad":
            trigInput = trigInput * 180.0 / 200.0

    # Returns the converted angle.
    return trigInput

# Defines the function to convert angles to gradians.
def toGrad(trigInput, trigAngle):
    # Checks that the input angle is a number.
    try:
        # Tries to convert the angle to a number.
        trigInput = float(trigInput)
    # Catches any value errors.
    except ValueError:
        # Returns an error message.
        return "Invalid Angle"

    # Checks what the input angle unit is.
    match trigAngle:
        # The input angle is in degrees.
        case "Deg":
            trigInput = trigInput * 200.0 / 180.0
        # The input angle is in radians.
        case "Rad":
            trigInput = trigInput * 200.0 / pi

    # Returns the converted angle.
    return trigInput
