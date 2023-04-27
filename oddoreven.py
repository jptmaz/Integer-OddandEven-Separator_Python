# Write a Python program that reads a text file named numbers.txt that contains 20 integers.
# The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. 
# The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.
    
# Open the text file containing the 20 integers and have the program read it.

import sys
print(sys.path)

with open("C:/Users/HomePC/OOP_SourceCode/OddandEven/numbers.txt") as int_file:
    integers = int_file.readlines()
    
# Then create two text files, one for even numbers, the other one for odd numbers.
with open("C:/Users/HomePC/OOP_SourceCode/OddandEven/even.txt", "w") as output_even, open("C:/Users/HomePC/OOP_SourceCode/OddandEven/odd.txt", "w") as output_odd:
    for line in integers:
        int_line = int(line)
        
        # Identify the numbers if they are odd or even
        # # If the number is even, write to the even numbers text file
        
        if int_line %2 == 0:
            output_even.write(str(int_line) + "\n")
        # # If the number is odd, write to the odd numbers text file.
        else:
            output_odd.write(str(int_line) + "\n")