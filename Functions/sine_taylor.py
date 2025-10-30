import math 

def taylor_sine(order, radians):

    expansion = 0

    for n in range(order):
        exponent = 2 * n+ 1
        
        x_power = radians ** exponent
        
        denominator = math.factorial(exponent)
        
        sign = (-1) ** n
        
        # Add the term to the sum
        term = sign * (x_power / denominator)
        expansion += term
        
    return expansion

