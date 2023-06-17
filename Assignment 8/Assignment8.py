# Part A

myList = [1, 2, 3, 4, 5, 6, 7, 8]
myList2 = myList[1:]
myList3 = myList2.copy()
myList3.append(9)
myList3.pop(2)

print("Part A:")
print("myList:", myList)
print("myList2:", myList2)
print("myList3:", myList3)
print()

# Part B

sample_text = "Hello, world! How are you today?"
print("Part B:")
print("count('o'):", sample_text.count('o'))
print("endswith('today?'):", sample_text.endswith('today?'))
print("find('world'):", sample_text.find('world'))
print("join(['Hello', 'world', 'How', 'are', 'you', 'today?']):", '-'.join(['Hello', 'world', 'How', 'are', 'you', 'today?']))
print("replace('o', 'x'):", sample_text.replace('o', 'x'))
print("split(', '):", sample_text.split(', '))
print("splitlines():", sample_text.splitlines())
print("startswith('Hello'):", sample_text.startswith('Hello'))
print("strip('H!'):", sample_text.strip('H!'))
print()

# Part C

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

user_input = int(input("Enter a number to check if it's prime: "))
if is_prime(user_input):
    print(user_input, "is a prime number.")
else:
    print(user_input, "is not a prime number.")
print()

# Part D

def disStuInfo(schoolID, *args, **kwargs):
    print("Part D:")
    for i, arg in enumerate(args):
        if i % 2 == 0:
            print(schoolID)
            print(arg)
        else:
            print(arg)
    for key, value in kwargs.items():
        if value:
            print(schoolID)
            print("'unmatched'")
            print(key)
            print(value)
    print()

disStuInfo(10001, 'John', 'Petter', Smith='jSmith@gmail.com', Potter="Petter@yahoo.com", Doe="j@gmail.com")
