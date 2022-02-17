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
        # c = u ^ int(plaintext[idx])
        keystream.append(u)

    # ciphertext = ' '.join(c)

    return keystream


# def convert_binary(text):
#     result = []

#     for idx in text:
#         result.append(format(ord(idx), 'b'))

#     return result

def convert_binary(n):
    return int(bin(n).replace("0b", ""))


def encrypt(plaintext, keystream):
    result = []
    for i in range(len(plaintext)):
        pt = convert_binary(plaintext[i])
        ks = convert_binary(keystream[i])
        print(pt, ks)
        ct = pt ^ ks
        result.append(ct)
    return result
    # print(convert_binary(plaintext))
    # print(convert_binary(keystream))


plaintext = list(input("Enter your plaintext: "))
plaintext_ascii = list(convert_ascii(plaintext))
key = input("Enter your key: ")
key_ascii = list(convert_ascii(key))

print("key", key_ascii, "\n")

repeated_key = repeat(key_ascii)

# print("repeat", repeated_key, "\n")
# print(repeat(key_ascii))

ksa = KSA(repeated_key)
# print(ksa, "\n")
prga = PRGA(plaintext, ksa)
# print(prga)

encrypted_text = encrypt(plaintext_ascii, prga)
print(encrypted_text)
