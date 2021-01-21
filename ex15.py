from sys import argv

# Assiging argument from command line to variables.
script, filename = argv

# Opening file.
txt = open(filename)

# Printing name of the file and reading what's inside.
print(f"Here's your {filename}.")
print(txt.read())
txt.close()  # Closing file after reading.

# Taking filename as an input argument from command line while script is working.
print("Type the filename again:")
file_again = input("> ")

# Opening file.
txt_again = open(file_again)

# Reading file and printing its content.
print(txt_again.read())
txt_again.close()
