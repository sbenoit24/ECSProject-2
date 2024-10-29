import pandas as pd

# Step 1: Read Excel file and extract 'Char' and 'Bin' columns.
xl = pd.read_excel("P2M010_G8.xlsx", dtype=str)  # Read Excel

chars = list(xl['Char'])  # List of characters from 'Char'
bins = list(xl["Bin"])  # List of binary codes from 'Bin'

# Replace '\\n' with '\n' per Task 2.
i = chars.index('\\n')  # Index of '\\n'
chars[i] = '\n'  # Replace '\\n' with '\n'

# Step 2: Create binary-to-character dictionary.
binsD = {}  # Binary to character mapping

for i in range(len(chars)):
    binsD[bins[i]] = chars[i]  # Map binary to character

# Step 3: Function to decode binary file with variable-length codes.
# takes a file and a place to put the file as input and 
# writes the encoded version of that file as output
strings = list
for char in chars :
    if len(char) > 1 :
        strings.append(char)

def encodeFile(inputFilePath, outputFilePath):
    try:
        with open(inputFilePath, 'r') as inputFile:
            text = inputFile.read()
        
        encodedText = ""
        i = 0
        while i < len(text):
            # string check
            checkSingles = True
            for string in strings:
                if text[i:i+len(string)] == string:
                    encodedText += bins[chars.index(string)]
                    i += len(string)
                    checkSingles = False
                    break
            
            if checkSingles:
                # single so grab from dict
                char = text[i]
                encodedText += bins[chars.index(char)] 
                # what if not in dict?
                i += 1

        with open(outputFilePath, 'w') as outputFile:
            outputFile.write(encodedText)

        print(f"encoded '{inputFilePath}' and saved it to '{outputFilePath}'.")
    
    except FileNotFoundError:
        print(f"'{inputFilePath}' doesnt exist")


def decode(fn="BinOutput.txt"):
    """
    Decode file with variable-length binary codes to characters.
    """
    try:
        # Step 4: Open binary file for reading.
        with open(fn, 'r') as bin_file:
            binary_data = bin_file.read().strip()  # Clean content

        # Step 5: Decode binary data using binsD.
        decoded_text = ""
        buffer = ""  # Buffer for accumulating bits

        for bit in binary_data:
            buffer += bit  # Accumulate bits
            if buffer in binsD:  # Check if buffer matches a code
                decoded_text += binsD[buffer]  # Add matched character
                buffer = ""  # Reset buffer

        # Step 6: Write decoded characters to output file.
        with open("TextOutput.txt", 'w') as text_file:
            text_file.write(decoded_text)

        # Step 7: Success message on completion.
        print("Decoding completed. Output in 'TextOutput.txt'.")

    except FileNotFoundError:
        # Step 8: Handle missing input file.
        print(f"File '{fn}' not found.")

    except Exception as e:
        # Step 9: Handle unexpected errors.
        print(f"An error occurred: {e}")

# Step 10: Call decode() for default file 'BinOutput.txt'.
decode()
"""
Reads Excel File, processes data by creating global variables for functions,
converts characters to binary to code and vice versa. A dictionary is used to
implement this method.
Akolda Arop
"""

# Import the pandas library to read Excel files
import pandas as pd

"""
Step 1: Open and read Excel file.
'xl' contains the data from the Excel file, with columns
formatted as strings.
"""
xl = pd.read_excel("P2M010_G8.xlsx", dtype=str)

"""
Step 2: Create lists out of 'Char' and 'Bin' in the
Excel file.
'chars' will contain all the character values from the 'Char' column.
"""
chars = list(xl['Char'])

# 'bins' contain all the binary code values from the 'Bin' column.
bins = list(xl['Bin'])

# Step 3: Modify any characters that need to be changed.
# Specifically, we replace any occurrences of '\\n' with '\n'.
i = chars.index('\\n')  # Find the index where '\\n' occurs
chars[i] = '\n'  # Replace the '\\n' at that index with '\n'

# Step 4: Create dictionaries to map chars to bin codes and vice-versa.
# 'charsD' will map each char to its corresponding bin code.
# 'binsD' will map each bin code to its corresponding char.

charsD = {}  # Initialize an empty dictionary for characters to binary codes
binsD = {}  # Initialize an empty dictionary for binary codes to characters

# Step 5: Loop through each character and its corresponding binary code.
# Assign each character
for i in range(len(chars)):
    charsD[chars[i]] = bins[i]  # Map character to binary code
    binsD[bins[i]] = chars[i]  # Map binary code to character

# 'charsD' contains a mapping of all chars to bins,
# 'binsD' contains a reverse mapping from bins to chars.


'''
Task 5: This program compares two text files to check if they are
identical.If they are not identical, it writes the difference,
including the lengths of the files and any non-matching characters,
to an "Errors.txt" file.

Akolda
'''


# Importing modules: 'filecmp' - comparing files and 'os' - file size operations
# import os
# import filecmp

# Defining function 'same' to compare two files and report difference
def same(fn1, fn2="TextOutput.txt"):
    # Open both files for reading
    with open(fn1, 'r') as file1, open(fn2, 'r') as file2:
        # Read the contents of both files
        content1 = file1.read()
        content2 = file2.read()

    # Get the lengths of both files
    len1 = len(content1)
    len2 = len(content2)

    # Check if the files are identical
    if content1 == content2:
        print("Identical Files")
    else:
        print("Different Files")
        # Create 'Errors.txt' and write the lengths and differences
        with open('Errors.txt', 'w') as error_file:
            # Write the lengths of both files to the first line
            error_file.write(f"file 1: {len1} and file 2: {len2}\n")

            # Find the length of the shorter file for character comparison
            min_len = min(len1, len2)

            # Loop through the files char by char
            for i in range(min_len):
                if content1[i] != content2[i]:
                    # Write the non-matching chars and their index to the file
                    error_file.write(f"{i}: {content1[i]}: {content2[i]}\n")

            # If file1 is longer, write the remaining chars from file1
            if len1 > len2:
                for i in range(len2, len1):
                    error_file.write(f"{i}: {content1[i]}: None\n")
            # If file2 is longer, write the remaining chars from file2
            elif len2 > len1:
                for i in range(len1, len2):
                    error_file.write(f"{i}: None: {content2[i]}\n")


# Comparing two files (fn1 and fn2)
fn1 = 'text1.txt'  # First file to compare
fn2 = 'text2.txt'  # Second file to compare against

# Call the 'same' function to compare 'fn1' and 'fn2'
# same(fn1, fn2)
'''
Task 5: This program compares two text files to check if they are
identical.If they are not identical, it writes the difference,
including the lengths of the files and any non-matching characters,
to an "Errors.txt" file.

Akolda
'''

# Defining function 'same' to compare two files and report difference
def same(fn1, fn2):
    # Open both files for reading
    with open(fn1, 'r') as file1, open(fn2, 'r') as file2:
        # Read the contents of both files
        content1 = file1.read()
        content2 = file2.read()

    # Get the lengths of both files
    len1 = len(content1)
    len2 = len(content2)

    # Check if the files are identical
    if content1 == content2:
        print("Identical Files")
    else:
        print("Different Files")
        # Create 'Errors.txt' and write the lengths and differences
        with open('Errors.txt', 'w') as error_file:
            # Write the lengths of both files to the first line
            error_file.write(f"file 1: {len1} and file 2: {len2}\n")

            # Find the length of the shorter file for character comparison
            min_len = min(len1, len2)

            # Loop through the files char by char
            for i in range(min_len):
                if content1[i] != content2[i]:
                    # Write the non-matching chars and their index to the file
                    error_file.write(f"{i}: {content1[i]}: {content2[i]}\n")

            # If file1 is longer, write the remaining chars from file1
            if len1 > len2:
                for i in range(len2, len1):
                    error_file.write(f"{i}: {content1[i]}: None\n")
            # If file2 is longer, write the remaining chars from file2
            elif len2 > len1:
                for i in range(len1, len2):
                    error_file.write(f"{i}: None: {content2[i]}\n")