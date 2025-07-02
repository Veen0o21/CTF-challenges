# List of ASCII codes => "ciphertext"
numbers = [99, 114, 121, 112, 116, 111, 123,65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Initialize an empty string to build the flag
flag = ""

# Convert each ASCII number to its corresponding character
for num in numbers:
    flag += chr(num)  # chr() converts number to ASCII character

# Print the final flag
print("The flag is:", flag)
