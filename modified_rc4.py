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


def PRGA(plaintext, S):
    i = 0
    j = 0
    keystream = []

    for idx in range(len(plaintext)):
        i = (i+1) % 256
        j = (j + S[i]) % 256
        swap(S, i, j)
        t = (S[i] + S[j]) % 256
        u = S[t]
        keystream.append(u)

    return keystream


def encrypt_decrypt(text, keystream):
    result = []
    for i in range(len(text)):
        ct = text[i] ^ keystream[i]
        result.append(ct)
    return(result)


def convert_string(text):
    result = []
    for idx in text:
        result.append(chr(idx))
    result = ''.join(result)
    return (result)


plaintext = list(input("Enter your plaintext: "))
plaintext_ascii = list(convert_ascii(plaintext))

key = input("Enter your key: ")
key_ascii = list(convert_ascii(key))
repeated_key = repeat(key_ascii)

ksa = KSA(repeated_key)
prga = PRGA(plaintext, ksa)

encrypted = encrypt_decrypt(plaintext_ascii, prga)
print("Ciphertext:", convert_string(encrypted))
decrypted = encrypt_decrypt(encrypted, prga)
print("Decrypted ciphertext:", convert_string(decrypted))
