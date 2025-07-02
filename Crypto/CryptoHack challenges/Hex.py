# Hex string => "ciphertext"
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convert the hex string to bytes (each pair of hex digits becomes one byte)
flag = bytes.fromhex(hex_string)

# Print the resulting bytes
print("The flag is:", flag)
