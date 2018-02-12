i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)

# converted while-loop to a function
# def ex33(num):
#     numbers = []
#     i = 0
#     for i in range(0, num):
#         if i < num:
#             numbers.append(i)
#     return numbers

# print(ex33(10))