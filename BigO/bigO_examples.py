# O(1)

lst = [1,2,3,4,5,6,7,8,9]

def o_1(values):
    return values[0]

o_1(lst)
# returns 1
'''
the above function is constant because regardless of the list size the function will only ever take a constant 
step size in this case 1, printing the first value from a list. so we can see here that an input list of 100 values 
will print just 1 item, a list of 10,000 values will print just 1 item, and a list of n values will print just 
1 item!
'''

# O(n)
def o_n(lst):
    for i in lst:
        print(i)

o_n(lst)

'''
This function runs in O(n) (linear time). This means that the number of operations taking place scales l
inearly with n, so we can see here that an input list of 100 values will print 100 times, a list of 10,000 values 
will print 10,000 times, and a list of n values will print n times.
'''

# O(n^2) Quadratic

def quadratic(lst):
    for i in lst:
        for j in lst:
            print(i, j)

quadratic(lst)
'''
Note how we now have two loops, one nested inside another. This means that for a list of n items, 
we will have to perform n operations for every item in the list! This means in total, we will perform n times n 
assignments, or n^2. So a list of 10 items will have 10^2, or 100 operations. You can see how dangerous this can 
get for very large inputs! This is why Big-O is so important to be aware of!
'''


'''
NOTE:::: When it comes to Big O notation we only care about the most significant terms, 
remember as the input grows larger only the fastest growing terms will matter
Let's see an example of how to drop constants:
'''
def print_once(lst):
    '''
    Prints all items once
    '''
    for val in lst:
        print(val)
print_once(lst)
# The print_once() function is O(n) since it will scale linearly with the input.

def print_3(lst): # O(3n)
    '''
    Prints all items three times
    '''
    # O(n)
    for val in lst:
        print(val)
    
    # O(n)
    for val in lst:
        print(val)
    # O(n)
    for val in lst:
        print(val)
'''
We can see that the first function will print O(n) items and the second will print O(3n) items. 
However for n going to inifinity the constant can be dropped, since it will not have a large effect, (consider 3*infinity, x*infinity)
so both functions are O(n).
'''
def comp(lst):
    '''
    This function prints the first item O(1)
    Then is prints the first 1/2 of the list O(n/2)
    Then prints a string 10 times O(10)
    '''
    # O(1)
    print lst[0]
    
    # O(n/2) i.e O(1/2 * n)
    midpoint = len(lst)/2
    
    for val in lst[:midpoint]:
        print val
    
    # O(10)
    for x in range(10):
        print 'number'
# So let's break down the operations here. We can combine each operation to get the total Big-O of the function:

# O(1 + n/2 + 10)
# We can see that as n grows larger the 1 and 10 terms become insignificant and the 1/2 term multiplied against n 
# will also not have much of an effect as n goes towards infinity. This means the function is simply O(n)!

# Worst Case vs Best Case

'''
Many times we are only concerned with the worst possible case of an algorithm, but in an interview setting its 
important to keep in mind that worst case and best case scenarios may be completely different Big-O times. 
For example, consider the following function:
'''
def matcher(lst,match):
    '''
    Given a list lst, return a boolean indicating if match item is in the list
    '''
    for item in lst:
        if item == match:
            return True
    return False
matcher(lst,1)

matcher(lst,9)
'''
Note that in the first scenario, the best case was actually O(1), since the match was found at the first element. 
In the case where there is no match, every element must be checked, this results in a worst case time of O(n).
'''

# Space Complexity
# Many times we are also concerned with how much memory/space an algorithm uses. The notation of space complexity 
# is the same, but instead of checking the time of operations, we check the size of the allocation of memory.

def printer(n):
    '''
    Prints "hello world!" n times
    '''
    for x in range(n):
        print('Hello World!')

printer(10)
'''
Note how we only assign the 'hello world!' variable once, not every time we print. So the algorithm has O(1) 
space complexity and an O(n) time complexity.
'''

def create_list(n):
    new_list = []
    
    for num in range(n):
        new_list.append('new')
    
    return 
create_list(10)
# this above function has time complexity of O(n) and space complexity of 0(n)