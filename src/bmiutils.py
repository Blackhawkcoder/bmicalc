def bmi_float(value):
    """ Converts input to float

    Args:
        value - The value to be converted
    Return:
        float of value if conversion was possible, 0.0 otherwise
    """

    try:
        return float(value)
    except:
        return 0.0


def bmi(length, weight):
    """ Calculates BMI Metric

    Args:
        length - length in cm
        weight - weight in kg
    Return:
        Result of calculation or 0 if division by zero would have occured
    """

    l = (bmi_float(length) / 100) # cm -> m conversion
    w = bmi_float(weight)

    # Test if we would have done division by zero
    if(l == 0):
        return 0
    else:
        return (w / (l * l))

    
def bmi2(lengthft,lengthinch, weightlb):
    """ Calculates BMI Imperial

    Args:
        lengthft - length in ft
        lengthinch - length in inch
        weight - weight in lb
    Return:
        Result of calculation or 0 if division by zero would have occured
    """

    l = ((bmi_float(lengthft) * 12) + (bmi_float(lengthinch))) * 0.0254 #Already in m
         
    w = (bmi_float(weightlb) * 0.45359237)

        # Test if we would have done division by zero
    if (l == 0):
        return 0
    else:
        return (w / (l * l))


def bmi_verdict(bmi):
    if(bmi < 18.5):
        verdict = "You are underweight"
    elif(18.5 <= bmi <= 24.9):
        verdict = "You are of normal weight"
    elif(24.9 < bmi < 30):
        verdict = "You are overweight"
    else:
        verdict = "You are obese"

    return verdict
