# Algorithm: A procedure a formula for solving a problem..
'''Why should we compare algorithms ??
    Imaging two guys are asked to do a task like sum of n numbers... Both the guys may have different approaches
    to do this. How would we say which one is the best ??
    Say the two solutions are below how would we comapare them ??
'''
import timeit

def sum_n(n):
    final_sum = 0
    for i in range(n+1):
        final_sum += i
    return final_sum

def sum_of_n(n):
    return (n * (n+1))/2

# You'll notice both functions have the same result, but completely different algorithms. You'll note that the 
# first function iteratively adds the numbers, while the second function makes use of some formula

# lets check the execution times..
# NOTE: for checking the execution times just install ipython with pip install ipython and just run the below statements
# %timeit sum_n(10)
# %timeit sum_of_n(10)

# so we can see from the results that the second function is faster than the first one. But the issue here is we cannot
# always use the "time to run" param as measurments because that will depend on the speed of the computer itself and 
# hardware capabilities. So we will need to use another method, Big-O!

'''
Big O Notation: It describes how fast the runtime grows with input as the input becomes arbitarily large..
Here is a table of common Big-O functions:
            Big-O	              Name
            1	                Constant
            log(n)	            Logarithmic
            n	                 Linear
            nlog(n)	            Log Linear
            n^2	                Quadratic
            n^3	                 Cubic
            2^n	                Exponential

The original sum_n function will create an assignment n+1 times, we can see this from the range based function. 
This means it will assign the final_sum variable n+1 times. We can then say that for a problem of n size 
(in this case just a number n) this function will take 1+n steps.

This n notation allows us to compare solutions and algorithms relative to the size of the problem, 
since sum_n(10) and sum_n(100000) would take very different times to run but be using the same algorithm. 
We can also note that as n grows very large, the +1 won't have much effect.
sum_n() can be said to be O(n) since its runtime grows linearly with the input size

'''