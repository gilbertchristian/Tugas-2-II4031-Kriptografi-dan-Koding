def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def convert_ascii(text):
    result = []
    for letter in text:
        result.append(ord(letter))

    return result


def repeat(text):
    length = len(text)
    if len(text) == 256:
        return text
    else:
        for i in range(256):
            text.append(text[i % length])
    return(text)


def KSA(key):
    S = []
    for i in range(256):
        S.append(i)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i]) % 256
        swap(S, i, j)

    return S


def PRGA(text, S):
    i = 0
    j = 0
    keystream = []

    for idx in range(len(text)):
        i = (i+1) % 256
        j = (j + S[i]) % 256
        swap(S, i, j)
        t = (S[i] + S[j]) % 256
        u = S[t]
        keystream.append(u)

    return keystream


# def encrypt_decrypt(text, keystream):
#     result = []
#     for i in range(len(text)):
#         ct = text[i] ^ keystream[i]
#         result.append(ct)
#     return(result)

def encrypt_decrypt(text, keystream):
    for i, value in enumerate(text):
        text[i] = value ^ keystream[i]
    return(text)


def convert_string(text):
    result = []
    for idx in text:
        result.append(chr(idx))
    result = ''.join(result)
    return (result)


# # plaintext = list(input("Enter your plaintext: "))
# # plaintext_ascii = list(convert_ascii(plaintext))

# f = open('audio.mp3', 'rb')
# plaintext_ascii = bytearray(f.read())
# f.close()

# key = input("Enter your key: ")
# key_ascii = list(convert_ascii(key))
# repeated_key = repeat(key_ascii)

# ksa = KSA(repeated_key)

# # prga = PRGA(plaintext, ksa)

# prga = PRGA(plaintext_ascii, ksa)

# encrypted = encrypt_decrypt(plaintext_ascii, prga)
# # print("Ciphertext:", convert_string(encrypted))

# print(encrypted)

# f = open('audio.mp3', 'wb')
# f.write(encrypted)
# f.close()

# # decrypted = encrypt_decrypt(encrypted, prga)
# # print("Decrypted ciphertext:", convert_string(decrypted))


def rc4_Process(text, key):
    plaintext_ascii = list(convert_ascii(text))
    key_ascii = list(convert_ascii(key))
    repeated_key = repeat(key_ascii)
    ksa = KSA(repeated_key)
    prga = PRGA(text, ksa)
    # print(plaintext_ascii, prga)
    encrypted = encrypt_decrypt(plaintext_ascii, prga)
    # decrypted = encrypt_decrypt(encrypted, prga)
    # return(convert_string(encrypted), convert_string(decrypted))
    return(convert_string(encrypted))


def rc4_file(file, key):
    f = open(file, 'rb')
    text = bytearray(f.read())
    f.close()

    key_ascii = list(convert_ascii(key))
    repeated_key = repeat(key_ascii)
    ksa = KSA(repeated_key)
    prga = PRGA(text, ksa)
    encrypted = encrypt_decrypt(text, prga)

    f = open('image.jpg', 'wb')
    f.write(encrypted)
    f.close()

    # decrypted = encrypt_decrypt(encrypted, prga)
    return("Check your files!")


def rc4_Export(text, key):
    cipher = rc4_Process(text, key)
    txt = open('ciphertext.txt', 'w')
    cipher = txt.write(cipher[0])
    txt.close()
