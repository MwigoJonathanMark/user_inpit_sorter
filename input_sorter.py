# get user input by prompting user to enter any text
string = input("Enter any text: ")

# sorting the user input into upper and lower case
# explicitly converting user input into set data type ie.(set()) to use set sort methods ie.upper() and lower()
lower = set(string.lower())
upper = set(string.upper())

#explicitly converting back to string data #type using str() method and  seperating #numbers and symbols from alpha #numerics by intersecting
small_letters = str(lower.difference(upper))
capital_letters = str(upper.difference(lower))
numbers = str(upper.intersection(lower))

# printing out worked on (sorted) data to console or screen for user
print("\n", "[" * 19, "SORTED DATA", "]" * 19)
print("\nUPPER CASE = ", capital_letters, "\n\vLOWER CASE = ", small_letters, "\n\vNUMBERS = ", numbers)

# getting the times a value appears in text entered by user using tye "count()" string function in for loop
print("\v", "{" * 19, "APPEARENCES", "}" * 19)
for letter in string:
    appearences = str(string.count(letter))
    print("\n\n", letter + " appears " + appearences + " in the your text.")
   