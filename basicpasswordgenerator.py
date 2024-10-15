# goal: to create a pasword generator
# requires paswords lengths
# requires pasword criteria
# does ir include numbers?
# does it include special charchters 
# generate a paswords with the given constraints 
# output the generated pasword

import random

#program introduction
print("welcome to our pasword genetrating app")
#set pasword length
pwd_length = int(input("enter the legnth of the password"))
#password criteria 
lowercase = list(range(1,10))
uppercase = list(range(65,91)) #the range never icludes the last value; 65-91 from the ascii table
digits=list(range(48,58))
special = list(range(33,48)) + list(range(58,65)) + list(range(91,97)) + list(range(123,127))

pwd_symbols = lowercase.copy # a list of possible charchters for our pasword

has_upper = input("include uppercase characters?(y/n)")
if has_upper == "Y" or has_upper == "y":
    pwd_symbols.extend(uppercase)
    # you can also do: pwd_symbols = pwd_symbols+uppercase
    
has_special = input("include special characters?(y/n)")
if has_special == "Y" or has_special == "y":
    pwd_symbols.extend(special)
    #pwd_symbols = pwd_symbls + uppercase

has_digits = input("include digits characters?(y/n)")
if has_digits == "Y" or has_digits == "y":
    pwd_symbols.extend(digits)
    #pwd_symbols = pwd_symbls + uppercase

    new_pasword = " " #empty string to hold our new pasword 

    while len(new_pasword) != pwd_length:
        random_symbol = chr(random (choice(pwd_symbols))) # chr() converts the random integers to its encoded value in the ASCII
        new_pasword = new_pasword + random_symbol
    #end of while loop

    print(f"{new_pasword} has been generated")
