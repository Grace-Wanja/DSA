i = 1
while i <= 7:
    i += 1
    if i == 3:
        continue
    print(i)
a = 3
b = 5
if a == b:
    print("a is greater than b")
def add_numbers(num1,num2):
    return num1 + num2

r = add_numbers(3,7)
print(r)

# a=2
# b=3
# tmp_a = a
# a=b
# b=tmp_a
# (a,b)=(b,a)
# print(b)

# x=3
# y=x=20
# print(y)
# print(x)

##mutability of data types

# num = input('enter value: ')
# if num.isdigit():
#     num=int(num)

#     if num % 2 == 0:
#         print(num, "is even")
#     else:
#         print(num, "is odd")
# else:
#     print("invalid input")

# def greet(name):
#     print(f"Hello,{'name'}")
# greet(4)


# def greet(name):
#     if not isinstance(name, str):
#         raise TypeError("Name must be a string")
#     print(f"Hello, {name}")

# if len(items) == 0:
#     print("List is empty.")
#     # Check if the list is empty after the loop