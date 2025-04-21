# Data Types in Python
# Variables are used to store data that can be used later in the program.

name = "boris petrov"
print(name.title())


first_name = "Boris"
last_name = "Petrov"
print(f"hello {first_name} {last_name} good luck!")


# String are immutable, meaning they cannot be changed.
# To change a string, you must create a new string with the desired changes.

name = "boris petrov"
favroite_language = "python "
print(favroite_language.rstrip())
# String methods
other_language = '   java'   
print(other_language.lstrip())

# String concatenation
quote_person = "Albert Einstein"
quote_message = "A person who never made a mistake never tried anything new."
print(f"{quote_person} once said, '{quote_message}'")


# NUMBERS

# Multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)

# CONSTANTS
# Constants are variables that should not be changed.
# Constants are usually written in all uppercase letters.
PI = 3.14159
print(f"The value of PI is {PI}")
# Constants are usually defined at the top of the file.
# Constants are usually defined in a separate file.
