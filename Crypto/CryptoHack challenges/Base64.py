import base64  # Import the base64 module for encoding

# Hex string => "ciphertext"
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convert the hex string to bytes (each pair of hex digits becomes one byte)
decoded_bytes = bytes.fromhex(hex_string)

# Encode the bytes using Base64 and decode to get a readable string
encoded_base64 = base64.b64encode(decoded_bytes).decode()

# Print the flag
print("The flag is:", encoded_base64)
