def caesar_encrypt(text, key):
    print(text,key)
    key = int(key)

    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset + key) % 26
            encrypted_char = chr(shifted + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, key):
    print(text,key)
    key = int(key)

    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset - key) % 26
            decrypted_char = chr(shifted + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def playfair_encrypt(text, key):
    print(text,key)
    # Generate the Playfair matrix based on the provided key
    def generate_matrix(key):
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        key = key.upper().replace('J', 'I')
        key += alphabet
        matrix = []
        for char in key:
            if char not in matrix:
                matrix.append(char)
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix
    # Get the position of a letter in the Playfair matrix
    def get_position(matrix, letter):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == letter:
                    return i, j
    # Encrypt a pair of letters based on the Playfair rules
    def encrypt_pair(matrix, pair):
        a, b = pair[0], pair[1]
        row_a, col_a = get_position(matrix, a)
        row_b, col_b = get_position(matrix, b)
        if row_a == row_b:
            return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
        else:
            return matrix[row_a][col_b] + matrix[row_b][col_a]
    # Remove any non-alphabetic characters from the input text
    text = ''.join(char.upper() for char in text if char.isalpha())
    # Generate the Playfair matrix based on the provided key
    matrix = generate_matrix(key)
    # Divide the input text into pairs of letters
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    # Encrypt each pair of letters using the Playfair rules
    encrypted_text = ''
    for pair in pairs:
        if len(pair) == 2:
            encrypted_text += encrypt_pair(matrix, pair)
        else:
            encrypted_text += pair[0] + 'X'  # Append 'X' for odd-length pairs
    return encrypted_text

def playfair_decrypt(text, key):
    print(text,key)
    # Generate the Playfair matrix based on the provided key
    def generate_matrix(key):
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        key = key.upper().replace('J', 'I')
        key += alphabet
        matrix = []
        for char in key:
            if char not in matrix:
                matrix.append(char)
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix
    # Get the position of a letter in the Playfair matrix
    def get_position(matrix, letter):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == letter:
                    return i, j
    # Decrypt a pair of letters based on the Playfair rules
    def decrypt_pair(matrix, pair):
        a, b = pair[0], pair[1]
        row_a, col_a = get_position(matrix, a)
        row_b, col_b = get_position(matrix, b)
        if row_a == row_b:
            return matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            return matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
        else:
            return matrix[row_a][col_b] + matrix[row_b][col_a]
    # Remove any non-alphabetic characters from the input text
    text = ''.join(char.upper() for char in text if char.isalpha())
    # Generate the Playfair matrix based on the provided key
    matrix = generate_matrix(key)
    # Divide the input text into pairs of letters
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    # Decrypt each pair of letters using the Playfair rules
    decrypted_text = ''
    for pair in pairs:
        decrypted_text += decrypt_pair(matrix, pair)
    return decrypted_text

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def aes_encrypt(text, key):
    print(text,key)
    # Convert the key to bytes
    key = key.encode()
    # Create a new AES cipher object with key and mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Pad the input text to a multiple of 16 bytes
    padded_text = pad(text.encode(), 16)
    # Encrypt the padded text
    encrypted_text = cipher.encrypt(padded_text)
    # Return the encrypted text as hex
    return encrypted_text.hex()

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def aes_decrypt(text, key):
    print(text,key)
    # Convert the key to bytes
    key = key.encode()
    # Create a new AES cipher object with key and mode
    cipher = AES.new(key, AES.MODE_ECB)
    # Convert the input text from hexadecimal to bytes
    encrypted_text = bytes.fromhex(text)
    # Decrypt the text
    decrypted_text = cipher.decrypt(encrypted_text)
    # Remove the padding from the decrypted text
    unpadded_text = unpad(decrypted_text, 16)
    # Return the decrypted text as a string
    return unpadded_text.decode()
import onetimepad
def otp_encrypt(text, key):
    print(text,key)
    return onetimepad.encrypt(text,key)


def otp_decrypt(text, key):
    print(text,key)

    return onetimepad.decrypt(text,key)

def railfence_encrypt(text, key):
    print(text,key)
    key = int(key)
    # Remove whitespaces from the text
    text = text.replace(" ", "")
    # Create the rail fence pattern
    pattern = []
    for i in range(key):
        pattern.append([])
    # Populate the pattern with the characters from the text
    row = 0
    direction = 1
    for char in text:
        pattern[row].append(char)
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    # Flatten the pattern to get the encrypted text
    encrypted_text = ""
    for row in pattern:
        encrypted_text += "".join(row)
    return encrypted_text

def railfence_decrypt(text, key):
    print(text,key)
    key = int(key)
    # Remove whitespaces from the text
    text = text.replace(" ", "")
    # Calculate the length of each rail
    rail_lengths = [0] * key
    i = 0
    direction = 1
    for _ in range(len(text)):
        rail_lengths[i] += 1
        i += direction
        if i == 0 or i == key - 1:
            direction *= -1
    # Create the rail fence pattern
    pattern = []
    for _ in range(key):
        pattern.append([])
    # Populate the pattern with the characters from the text
    row = 0
    for i in range(len(text)):
        pattern[row].append(None)
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    # Fill in the pattern with the characters from the text
    text_index = 0
    for row in pattern:
        for j in range(len(row)):
            row[j] = text[text_index]
            text_index += 1
    # Read the decrypted text from the pattern
    decrypted_text = ""
    row = 0
    direction = 1
    for _ in range(len(text)):
        decrypted_text += pattern[row].pop(0)
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    return decrypted_text

import pyperclip

def encryptMessage(text, key):
    ciphertext = [''] * key
    for col in range(key):
        position = col
        while position < len(text):
            ciphertext[col] += text[position]
            position += key
        return ''.join(ciphertext) #Cipher text
