def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def KSA(key):
    S = []
    for i in range(256):
        S.append(i)

    j = 0
    for i in range(256):
        k = int(key[i % len(key_bit)])
        j = (j + S[i] + k) % 256
        swapPositions(S, i, j)

    return S


def PRGA(plaintext, S):
    i = 0
    j = 0
    ciphertext = []

    for idx in range(len(plaintext)):
        i = (i+1) % 256
        j = (j + S[i]) % 256
        swapPositions(S, i, j)
        t = (S[i] + S[j]) % 256
        u = S[t]
        c = u ^ int(plaintext[idx])
        ciphertext.append(c)

    # ciphertext = ' '.join(c)

    return ciphertext


plaintext = list(input("Enter your plaintext: "))
plaintext_bit = list(''.join(format(ord(i), '08b') for i in plaintext))
key = input("Enter your key: ")
key_bit = list(''.join(format(ord(i), '08b') for i in key))

print("key", key_bit)
ksa_S = KSA(key_bit)
prga = PRGA(plaintext_bit, ksa_S)
print(prga)
