def prime_less_than_N (N):

    """
    This function returns a list of primes less than N. This function is limited for larger values of N. 

    Param: 
        N(int): This parameter defines the integer we are interested listing the primes which are lower than it. 
    
    Output: 
        prime_list(list): This is a list containing all the primes smaller than N
    
    """

    prime_list = []
    prime_true = [True for _ in range(N)]

    #For each number 'p' from 2 to the (square root of N) + 1, we will turn all positions which are a multiple of p to False
    for p in range(2, int(N**0.5) + 1):
        # We only need to update for p values, if p is prime. 
        if prime_true[p] == True:
            # Update all multiples of p
            for i in range(p * p, N, p):
                prime_true[i] = False

    # Update prime_list to only include the numbers for which the index in prime_list is True
    for p in range(2, N):
        if prime_true[p] == True:
            prime_list.append(p)

    return prime_list