import sys


def KMP(P, T, f):
    i = 0
    j = 0
    n = len(T)
    m = len(P)
    x = 0
    while i-j <= n-m:

        print(f"P at pos {i-j} with i = {i} and j = {j}")
        matches = False
        a = i
        c = j
        while j < m and T[i].upper() == P[j].upper():
            i += 1
            j += 1
            matches = True
        if matches:
            print(f"  matched T[{a}..{i-1}] = {T[a:i]} = P[{c}..{j-1}] = {P[c:j]}")
            x = i
        if not j >= len(P):
            print(f"  mismatch T[{i}] = {T[i]} != P[{j}] = {P[j]}")
        if j == m:
            print(f"  found an occurrence of P")
        if j > 0:
            print(f"  updated j from {j} to f[{j-1}] = {f[j-1]}")
            j = f[j-1]
            x += j
        else:
            print(f"  incremented i from {i} to {i+1}")
            i += 1
            x += 1


def precomputeF(P):
    f = [0]*(len(P))
    T = P[1:(len(P))]
    i = 0
    j = 0
    while i < len(T):
        while i < len(T) and T[i].upper() == P[j].upper():
            i += 1
            j += 1
            f[i] = j
        if j > 0:
            j = f[j-1]
        else:
            i += 1
    return f


args = sys.argv
if len(args) > 1:
    filename = args[1]
else:
    filename = "input1.txt"

input = open(filename)

input = input.read().splitlines()
P = input[0]
T = input[1]

print(f"P: {P}")
f = precomputeF(P)
print("Suffix function f: ", end="")
print(*f, sep=" ")

KMP(P, T, f)

