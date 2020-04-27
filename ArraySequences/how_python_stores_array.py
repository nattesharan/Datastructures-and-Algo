import sys
n = 100
data = []
for i in range(n):
    a = len(data)
    size = sys.getsizeof(data)
    print("Size of list with {} elements is {}".format(a, size))
    data.append(i)

# python uses dynamic array concept
# when an array is filled it allocates more memory in chunks