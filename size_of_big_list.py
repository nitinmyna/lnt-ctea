import sys
large_generator = (x ** 2 for x in range(10_000_000))
print(f"Generator memory size: {sys.getsizeof(large_generator)} bytes")
