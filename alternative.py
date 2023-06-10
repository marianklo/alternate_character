# Program that reads in a string and makes each alternate character an UPPERCASE character and each other alternate character a lowercase character 

# creating a string
string = "I am learning Phyton, the best programming language! "

upated_string = " "   # Store updated string

for i in range(len(string)): # Taking index value of the string
    # Using % to find is odd or even index
    if i % 2 == 1: 
        upated_string += string[i].upper()   # Concatonate
    else:
        upated_string += string[i].lower()  # Concatonate
print(upated_string)

# Now,the same string but making each alternative word lower and upper case 

new_string = string     
split_string = new_string.split()  # To store the split string -creates a list
final_string = " "

for i in range(len(split_string)):  # Taking index value of the string
    if i % 2 == 1: 
        final_string += split_string[i].upper() + " " # If item index divides by 2 then convert to uppercase
    else:
        final_string += split_string[i].lower()  + " " # Otherwise convert to lowercase
print(final_string)
