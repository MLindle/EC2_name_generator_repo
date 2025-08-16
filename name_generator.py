import random
import sys

"""""
Using ASCII uppercase range and lowercase range, combining with randint generator to create a unique string of characters and numbers. ASCII reference below:

Uppercase letters:

A → 65

Z → 90

Range: 65 - 90

Lowercase letters:

a → 97

z → 122

Range: 97 - 122
"""""
def ec2_name_generator():

    #Both inputs below are nested in try-except blocks, which will exit the script upon a ValueError.

    #Entry for number of EC2 names, with a try-except block to catch non-integer entries
    try:
        total_names = int(input("Please enter the number of random EC2 names you require here. Valid entries are case sensitive, and include:\n Marketing\n Accounting\n FinOps\n"))
    except ValueError:
        print ("Please enter a valid number value.")
        sys.exit()

    #Entry for department name, to be concatenated with the randomizer for-loop below this. Added a try-except block to catch casing issues.
    try:
        department_name = input("Your department name will be added to this instance name. Please enter here:\n")
        if department_name[0].islower() or (department_name == "FinOps" and department_name[0].islower() or (department_name == "FinOps" and department_name[3].islower())):
            raise ValueError
    except ValueError as e:
        print("Entry is case sensitive. Please use correct casing.")
        sys.exit()

    #Condition to check for correct entries. Will also catch casing issues as well is invalid entries.

    if department_name == "FinOps" or department_name == "Marketing" or department_name == "Accounting":

    #For loop to generate a random set of uppercase characters, lowercase characters, and numbers.

        for x in range(int(total_names)):

            new_name_randomizer = ''

            for x in range(3):

                random_numbers = random.randint(1, 9)
                random_characters_uppercase = chr(random.randint(65, 90))
                random_characters_lowercase = chr(random.randint(97, 122))

                
                name_gen = str(random_numbers) + random_characters_uppercase + random_characters_lowercase
                new_name_randomizer = name_gen + new_name_randomizer

            print (department_name + "-EC2-" + new_name_randomizer)
    else:
        print("Department name invalid. Please enter a valid department name.")

ec2_name_generator()