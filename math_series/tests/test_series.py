# here we can import any thing from the file using import *
# here we can import only the function from the file using from file_name import function_name
from math_series.math_series import fibonacci
from math_series.math_series import lucas
from math_series.math_series import sum_series

def test_fibonacci():
    """
    Test for the fibonacci function
    """

    # arrange => what output do i expect to get
    expected = 2
    # assign => what is the output that i resive
    actual = fibonacci(3)
    # assert => check if the output is as expected
    assert expected == actual



def test_lucas():
    """
    Test for the lucas function
    """
    # arrange => what output do i expect to get
    expected = 11
    # assign => what is the output that i resive
    actual = lucas(5)
    # assert => check if the output is as expected
    assert expected == actual  

def test_sum_series():
    """
    Test for the test_other_series function
    """
    # arrange => what output do i expect to get
    expected = 2
    # assign => what is the output that i resive
    actual = sum_series(3, 0 ,1)
    # assert => check if the output is as expected
    assert expected == actual      

    # test lucas using the sum_series
    assert sum_series(5,2,1) == lucas(5)

    #  test others using the sum_series
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12