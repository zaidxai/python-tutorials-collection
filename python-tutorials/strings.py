# Python Strings: Basics & Operations

# 1. Creating strings
single_quote_str = 'Hello'
double_quote_str = "World"
multi_line_str = """This is
a multi-line
string."""

print(single_quote_str)
print(double_quote_str)
print(multi_line_str)

# 2. Accessing characters and slicing
sample = "Python"
print("\nFirst character:", sample[0])
print("Last character:", sample[-1])
print("Slice (1:4):", sample[1:4])
print("Slice (0:6:2):", sample[0:6:2])  # Step

# 3. String length
print("\nLength of sample:", len(sample))

# 4. String concatenation and repetition
greeting = single_quote_str + " " + double_quote_str
print("\nConcatenation:", greeting)

echo = "Ha! " * 3
print("Repetition:", echo)

# 5. Changing case
text = "python programming"
print("\nUppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Capitalize:", text.capitalize())
print("Swap Case:", text.swapcase())

# 6. Stripping whitespace
whitespace_str = "   hello   "
print("\nOriginal:", repr(whitespace_str))
print("Strip:", repr(whitespace_str.strip()))
print("Left Strip:", repr(whitespace_str.lstrip()))
print("Right Strip:", repr(whitespace_str.rstrip()))

# 7. Finding and replacing
sample_text = "I love Python. Python is fun."
print("\nFind 'Python':", sample_text.find("Python"))  # first occurrence
print("Count 'Python':", sample_text.count("Python"))
print("Replace 'Python' with 'Java':", sample_text.replace("Python", "Java"))

# 8. Checking content
check_str = "Python123"
print("\nIs alphanumeric?", check_str.isalnum())
print("Is alphabetic?", check_str.isalpha())
print("Is digit?", check_str.isdigit())
print("Is lowercase?", check_str.islower())
print("Is uppercase?", check_str.isupper())
print("Starts with 'Py'?", check_str.startswith("Py"))
print("Ends with '123'?", check_str.endswith("123"))

# 9. Splitting and joining
sentence = "Python is easy to learn"
words = sentence.split()  # Split by whitespace
print("\nSplit sentence:", words)

csv = "a,b,c,d"
letters = csv.split(",")
print("Split CSV:", letters)

joined = "-".join(letters)
print("Joined with '-':", joined)

# 10. String formatting
name = "Zaid"
age = 22
print("\nOld style formatting: My name is %s and I am %d years old." % (name, age))
print("str.format(): My name is {} and I am {} years old.".format(name, age))
print("f-string: My name is {name} and I am {age} years old.")

# 11. Escaping characters
escape_str = "He said, \"Python is awesome!\""
print("\nEscaped string:", escape_str)

# 12. Raw strings (ignores escape sequences)
path = r"C:\Users\Zaid\Documents"
print("Raw string:", path)

# 13. Multiline strings and docstrings
def greet():
    """
    This function prints a greeting message.
    """
    print("Hello, World!")

greet()
print("Docstring of greet():", greet.__doc__)