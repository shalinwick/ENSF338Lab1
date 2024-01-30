import timeit

# Function to compute the n-th power of 2
def pow2(n):
    return 2 ** n

# Timing the execution of 10000 instances of pow2(10000)
time1 = timeit.timeit('pow2(10000)', globals=globals(), number=10000)
print("Time taken for 10000 instances of pow2(10000):", time1)

# Function using a for loop to compute pow2(n) for n up to 1000
def pow2_with_loop():
    for n in range(1001):
        result = pow2(n)

# Timing the execution of 1000 instances of pow2_with_loop
time2 = timeit.timeit('pow2_with_loop()', globals=globals(), number=1000)
print("Time taken for 1000 instances of pow2_with_loop:", time2)

# Function using list comprehension to compute pow2(n) for n up to 1000
def pow2_with_list_comprehension():
    results = [pow2(n) for n in range(1001)]

# Timing the execution of 1000 instances of pow2_with_list_comprehension
time3 = timeit.timeit('pow2_with_list_comprehension()', globals=globals(), number=1000)
print("Time taken for 1000 instances of pow2_with_list_comprehension:", time3)
