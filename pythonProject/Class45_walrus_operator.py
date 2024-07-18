# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

numbers = [1,5,8,6,3,7]
while(n := len(numbers)) > 0:
    print(numbers.pop())

food = list()
while(inp := input("Enter your favourite food : ")) != "quit":
    food.append(inp)

print(food)