import timeit


def power2(n):
    
    return 2 ** n


first_time = timeit.timeit('power2(10000)', globals=globals(), number=10000)

print("Time taken for 10000 times of pow2(10000):", first_time)


def power2_loop():
    
    for n in range(1001):
        
        result = power2(n)


second_time = timeit.timeit('power2_loop()', globals=globals(), number=1000)

print("Time taken for 1000 times of power2_loop:", second_time)


def power2_list_comprehension():
    
    result2 = [power2(n) for n in range(1001)]


third_time = timeit.timeit('power2_list_comprehension()', globals=globals(), number=1000)

print("Time taken for 1000 times of power2_list_comprehension:", third_time)
