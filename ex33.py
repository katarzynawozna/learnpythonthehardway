def fillingup_list(operator, incremention):
    numbers = []
    while operator < 6:
        print(f"At the top i is {operator}.")
        numbers.append(operator)

        operator += incremention
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {operator}.")
    return numbers

numbers = fillingup_list(0, 2)
print("The numbers: ")

for num in numbers:
    print(num)