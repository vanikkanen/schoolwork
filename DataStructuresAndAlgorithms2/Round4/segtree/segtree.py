import math
import sys


def create_segtree(V, off):
    S = [0] * 2 * off

    for i in range(0, len(V)):
        S[off + i] = V[i]

    for i in range(0, len(S), 2):
        parent = S[-(i + 1)] + S[-(i + 2)]
        location = (len(S) - (i + 2)) // 2
        if (location != 0):
            S[location] = parent

    return S


def query(S, par1, par2, off):
    print(f"Querying interval {par1}...{par2}")
    not_same_cell = True
    L = off + par1
    R = off + par2
    result = 0
    while not_same_cell:
        print(f"  left and right positions: {L} {R}")
        if L % 2 != 0:
            new_result = result + S[L]
            print(f"    updated result from {result} to {new_result} using "
                  f"S[{L}]={S[L]}")
            result = new_result
        if R % 2 == 0:
            new_result = result + S[R]
            print(f"    updated result from {result} to {new_result} using "
                  f"S[{R}]={S[R]}")
            result = new_result

        L = (L+1)//2
        R = (R-1)//2
        if R < 0:
            R = 1
        if R < L:
            not_same_cell = False
            continue

    print()
    print(f"Sum({par1}...{par2}) = {result}")


def main():
    #args = sys.argv
    #input_file = args[1]
    #command_file = args[2]
    input_file = "input1.txt"
    command_file = "commands1.txt"

    input = open(input_file)
    V = [eval(i) for i in input.read().split()]
    n = len(V)
    a = int(math.log2(n))
    off = 0
    if 2 ** a == n:
        off = n
    else:
        off = 2 ** (a + 1)

    S = create_segtree(V, off)

    print("Segment tree levels:")
    n = int(math.log2(off)) + 1
    prev_segment = 0
    tempS = S[1:len(S)]

    for i in range(n):
        segment = 2 ** i
        print("",*tempS[prev_segment: prev_segment + segment])
        prev_segment += segment

    #print(*S[1:len(S)], sep=" ")

    commands = open(command_file)
    for line in commands:
        print()
        cmd, par1, par2 = line.split()
        if cmd == "query":
            query(S, int(par1), int(par2), off)
        elif cmd == "set":
            print(f"Updating V[{par1}] = {par2}")
            V[int(par1)] = int(par2)
            S = create_segtree(V, off)

if __name__ == "__main__":
    main()
