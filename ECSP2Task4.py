def decode(fn="BinOutput.txt"):
    """
    Function to decode a file containing binary codes and convert them into characters.
    The decoded characters are written to a file named 'TextOutput.txt'.
    
    Args:
    fn (str): The name of the file to read the binary codes from. Defaults to 'BinOutput.txt'.
    
    Returns:
    None
    """
    try:
        # Open the file that contains the binary data (default file is 'BinOutput.txt')
        with open(fn, 'r') as bin_file:
            # Read the entire content of the file and remove any extra spaces/newlines
            binary_data = bin_file.read().strip()

        # Convert the binary data into characters
        # Each 8 bits (1 byte) represent one ASCII character
        # Using a list comprehension to process the binary data in chunks of 8 bits
        characters = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]

        # Join the list of characters into a single string (the decoded text)
        decoded_text = ''.join(characters)

        # Open the output file 'TextOutput.txt' in write mode and save the decoded text
        with open("TextOutput.txt", 'w') as text_file:
            text_file.write(decoded_text)

        # Print a success message
        print(f"Decoding completed successfully. Output written to 'TextOutput.txt'.")
    
    except FileNotFoundError:
        # Handle the case where the input file is not found
        print(f"The file '{fn}' was not found.")
    
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {e}")

# Example usage: call the function to decode the default file 'BinOutput.txt'
decode()
