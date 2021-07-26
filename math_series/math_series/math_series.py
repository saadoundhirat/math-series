# functions folder 
def fibonacci(n):
    """
    This function calculates the nth value of the Fibonacci series
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# lucas function
def lucas(n):
    """
    This function calculates the nth value of the Lucas series
    """
    if n==0:
        return 2
    if n==1:
        return 1
    return lucas(n-1) + lucas(n-2)

#another function
# if sum_series(n,n0:3,n1:2 ) 
def other_series(n,n0,n1):
    pass


# sum_series
def sum_series(n, n0=0 , n1=1 ):
    """
compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).

    sum_series(n, 3, 2) should generate antoehr series with no specific name

    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci sercies
    """
    if n0==0 and n1==1:
        return fibonacci(n)    
    elif n0 == 2 and n1==1:
        return lucas(n)
    else:
        return other_series(n,n0,n1)











