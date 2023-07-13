alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt():
    end_process = ""
    for letters in text:
        postional = alphabet.index(letters)
        new_postional = (postional + shift) % 26
        add_letter = alphabet[new_postional]
        end_process += add_letter
    print(f"This encoded message: {end_process}")

def decrypt():
    decode_cipher = ""
    for letter in text:
        postion = alphabet.index(letter)
        new_pos = (postion - shift) % 26
        shifter = alphabet[new_pos]
        decode_cipher += shifter
    print(f"This Message decoded: {decode_cipher}")

if direction == "encode":
    encrypt()
elif direction == "decode":
    decrypt()
else:
    print("You enter the invalid option")