# Generators in Python are special type of functions that allow you to create an iterable sequence of values. A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it. Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.

# In Python, you can create a generator by using the yield statement in a function. The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested.

# Benefits of Generators
# Generators offer several benefits over other types of sequences, such as lists, tuples, and sets. One of the main benefits of generators is that they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory. This makes generators a powerful tool for working with large or complex data sets, as you can generate the values as you need them, rather than having to store them all in memory at once.

# Another benefit of generators is that they are lazy, which means that the values are generated only when they are requested. This allows you to generate the values in a more efficient and memory-friendly manner, as you don't have to generate all the values up front.

def my_generator():
    for i in range(5):
        yield i  # It will return a generator object. To extract its value, use next function. next will return the next value of i.

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# print(next(gen))  After 5 values, it will give error

# A generator can only be iterated over once. Once a generator has been exhausted (i.e., all its values have been yielded), it cannot be reset or reused.

def gen2(n):
    a = 0
    while a <= n:
        if a % 2 == 0:
            yield a
        a += 1

even_no = gen2(20)
for i in even_no:
    print(i)  # Here, i is not a generator object, it's just a value yielded by the generator even_no.

# Alternatively, we can also write this using next function.
even_no = gen2(20)  # Create a new generator and iterate over it with next(), bcz previous one is exhausted
while True:
    try:
        print(next(even_no))
    except StopIteration:
        break