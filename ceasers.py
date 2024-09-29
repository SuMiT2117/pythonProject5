alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get user input
direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n ").lower()
text = input("Type your message:\n").lower()
shift = int(input("How many letters do you want to shift?\n"))

# Encrypt function
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabets:  # Check if the letter is in alphabets
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)  # Wrap around using modulus
            cipher_text += alphabets[shifted_position]
        else:
            cipher_text += letter  # Leave spaces and punctuation as is
    print(f"Your encoded result is: {cipher_text}")

# Decrypt function
def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        if letter in alphabets:
            shifted_position = alphabets.index(letter) - shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
        else:
            output_text += letter  # Leave spaces and punctuation as is
    print(f"Your decoded result is: {output_text}")

# General Caesar cipher function
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""


    if encode_or_decode == "decode":
        shift_amount *= -1  # Reverse the shift for decoding

    for letter in original_text:
        if letter in alphabets:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
        else:
            output_text += letter  # Handle spaces or punctuation

    print(f"Your {encode_or_decode}d result is: {output_text}")

# Call the Caesar cipher function
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
