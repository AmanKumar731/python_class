print("Hello world")

# Conditional statements

age = 18

if age >= 18:
    print("You can vote")

age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Pass")


# Loops in Python

for i in range(5):
    print(i)

i = 1

while i <= 5:
    print(i)
    i += 1

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

# Functions in Python


def greet():
    print("Hello, Aman!")

greet()



def add(a, b):
    return a + b

result = add(10, 20)
print(result)



def test1():
    print("Hello")

def test2():
    return "Hello"

x = test1()
y = test2()

print(x)
print(y)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
# Output:
# I like apple
# I like banana
# I like cherry
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)
for i in range(2, 10, 2): # 2, 4, 6, 8
    print(i)