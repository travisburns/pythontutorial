def squared(num): lambda num : num * num 

print(squared(2))

addTwo = lambda num : num + 2
# lambda num : num + 2


print(addTwo(12))

sum = lambda a, b : a + b 

print(sum(10, 8))


def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))