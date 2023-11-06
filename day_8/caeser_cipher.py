def encrypt(text, shift):
    encrypted_text = ''
    for letter in text:
        position = alphabet.index(letter)   
        new_position = position + shift
        if new_position > 25:
            new_position = new_position % 26
        new_letter = alphabet[new_position]
        encrypted_text += new_letter
    print(f"The encoded text is {encrypted_text}")


def decrypt(text, shift):
    decrypted_text = ''
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        if new_position < 0:
            new_position = new_position % 26
        new_letter = alphabet[new_position]
        decrypted_text += new_letter
    print(f"The decoded text is {decrypted_text}")

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]


while True:
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'exit' to quit:\n").lower()

    if action == 'exit':
        break

    if action == 'encode' or action == 'decode':
        text = input("Enter your message: ").lower()
        shift = int(input('Type the shift number: '))
        shift = shift % 26

        if action == 'encode':
            encrypt(text, shift)
        elif action == 'decode':
            decrypt(text, shift)
    else:
        print('You typed a wrong action')