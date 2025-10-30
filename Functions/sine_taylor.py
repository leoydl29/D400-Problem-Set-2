import math 

def taylor_sine(order, radians):

    """
    This function approximates sine by using the taylor expansion. 

    Param: 
        order(int): This parameter determines the order of the expansion for the taylor series 
        radians(float): This parameter determines the x value in the taylor expansion
    
    Output: 
        expansion(float): This is where the output of the taylor expansion is stored
    
    """
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

