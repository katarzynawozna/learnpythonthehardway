print("How old are you?", end=" ")
age = int(input())
print("How tall are you?", end=" ")
height = int(input())
print("How much do you weight?", end=" ")
weight = int(input())

all = age + height + weight

print(f"So you're {age} years old, {height} cm tall and {weight} kg heavy. All of this gives us {all}.")
