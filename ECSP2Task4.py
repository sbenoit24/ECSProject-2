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
