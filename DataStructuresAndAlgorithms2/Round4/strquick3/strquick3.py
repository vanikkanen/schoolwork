import random
import sys


def StringQuick3(V, s, e, d):

    if s < e:
        pi = int((s+e)/2)
        p = V[pi]
        V[s], V[pi] = V[pi], V[s]
        print(f"Sorting subarray {s}...{e} with depth {d} and pivot {p}")
        eqs = s
        eqe = e
        i = s+1
        while i <= eqe:
            if len(V[i]) <= d:
                V[eqs], V[i] = V[i], V[eqs]
                if V[eqs] != V[i]:
                    eqs += 1
                i += 1
            elif len(p) <= d:
                V[eqe], V[i] = V[i], V[eqe]
                eqe -= 1
            elif V[i][d] < p[d]:
                V[eqs], V[i] = V[i], V[eqs]
                eqs += 1
                i += 1
            elif V[i][d] > p[d]:
                V[eqe], V[i] = V[i], V[eqe]
                eqe -= 1
            else:
                i += 1
        StringQuick3(V, s, eqs-1, d)
        if len(p) > d:
            StringQuick3(V, eqs, eqe, d+1)
        StringQuick3(V, eqe+1, e, d)

    else:
        print(f"Immediate return from subarray {s}...{e} with depth {d}")


def main():

    #args = sys.argv
    #input_file = args[1]
    input_file = "input1.txt"

    input = open(input_file)
    V = input.read().split()

    print("Original:", end=" ")
    print(*V, sep=" ")

    StringQuick3(V, 0, len(V)-1, 0)

    print("Sorted:", end=" ")
    print(*V, sep=" ")

if __name__ == "__main__":
    main()
