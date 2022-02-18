from collections import deque

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

    j = 100
    for i in range(256):
        j = ((j + S[i] + key[i])*16) % 256
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

def LFSR(keystream, n):
    ks = []
    for idx in keystream:
        # if idx == 1:
        #     idx = len(keystream)
            
        temp = []
        binary = deque(bin(idx).replace("0b", ""))

        for i in range(n):
            pos1 = 0
            pos2 = len(binary) - 1
            temp.append(int(binary[pos1])^int(binary[pos2]))
            binary.pop()
            for idx in binary:
                temp.append(int(idx))
        ks.append(decimal(temp)%256)

    return ks

def decimal(list):
    temp = 0
    j = len(list)-1
    for i in range(len(list)):
        if list[i] == 1:
            temp += 2 ** j
        j-=1
    return temp

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


plaintext = list(input("Enter your plaintext: "))
plaintext_ascii = list(convert_ascii(plaintext))

# f = open('image.jpg', 'rb')
# plaintext_ascii = bytearray(f.read())
# f.close()

key = input("Enter your key: ")
key_ascii = list(convert_ascii(key))
repeated_key = repeat(key_ascii)

ksa = KSA(repeated_key)

prga = PRGA(plaintext, ksa)

lfsr = LFSR(prga, 4)

# prga = PRGA(plaintext_ascii, ksa)

encrypted = encrypt_decrypt(plaintext_ascii, lfsr)
print("Ciphertext:", convert_string(encrypted))

# f = open('image.jpg', 'wb')
# f.write(encrypted)
# f.close()

# decrypted = encrypt_decrypt(encrypted, prga)
# print("Decrypted ciphertext:", convert_string(decrypted))


# def rc4_Process(plaintext, key):
#     plaintext_ascii = list(convert_ascii(plaintext))
#     key_ascii = list(convert_ascii(key))
#     repeated_key = repeat(key_ascii)
#     ksa = KSA(repeated_key)
#     prga = PRGA(plaintext, ksa)
#     lfsr = LFSR(prga, 4)
#     print(plaintext_ascii, lfsr)
#     encrypted = encrypt_decrypt(plaintext_ascii, lfsr)
#     decrypted = encrypt_decrypt(encrypted, prga)
#     return(convert_string(encrypted), convert_string(decrypted))


# def rc4_file(plaintext, key):
#     f = open('image.jpg', 'rb')
#     plaintext_ascii = bytearray(f.read())
#     f.close()

#     key_ascii = list(convert_ascii(key))
#     repeated_key = repeat(key_ascii)
#     ksa = KSA(repeated_key)
#     prga = PRGA(plaintext, ksa)
#     encrypted = encrypt_decrypt(plaintext_ascii, prga)

#     f = open('image.jpg', 'wb')
#     f.write(encrypted)
#     f.close()

#     decrypted = encrypt_decrypt(encrypted, prga)
#     return(convert_string(encrypted), convert_string(decrypted))


# def rc4_Export(plaintext, key):
#     cipher = rc4_Process(plaintext, key)
#     txt = open('ciphertext.txt', 'w')
#     cipher = txt.write(cipher[0])
#     txt.close()
