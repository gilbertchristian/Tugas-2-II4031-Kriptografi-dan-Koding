plainteks = input("Enter your plaintext: ")
key = input("Enter your key: ")
key_bit = list(''.join(format(ord(i), '08b') for i in key))

print("key", key_bit)


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

# def KSA ():


S = []
for i in range(256):
    S.append(i)

j = 0
for i in range(256):
    k = int(key_bit[i % len(key_bit)])
    j = (j + S[i] + k) % 256
    swapPositions(S, i, j)

print(S)
