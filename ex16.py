from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C.")
print("If you want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Turncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write this into your file.")

target.write(f"{line1}\n{line2}\n{line3}")

print("All done. Closing it.")
target.close()
