import sys


def suffix_array(T):
    sa = []
    for i in range(0, len(T)):
        sa.append(i)
    return sorted(sa, key=lambda x: T[x:])


def bin_search(sa, T, P):
    print(f"Binary search for {P}")
    l = 0
    r = len(T)
    while l < r:
        lo = l
        hi = r
        mid = (lo + hi) // 2
        print(f"({lo}, {mid}, {hi}): ", end="")
        matching_length = 0
        match = False
        for k in range(0, len(P)):
            if P[k] == T[sa[mid]+k]:
                matching_length = k + 1
            else:
                break
            if k == len(P)-1:
                match = True
        if match:
            print(f"{P[0:k+1]} <=> {T[sa[mid]:sa[mid]+matching_length]}")
        else:
            print(f"{P[0:k+1]} <=> "
                  f"{T[sa[mid]:sa[mid] + matching_length+1]}")

        if T[sa[mid]:sa[mid]+matching_length] == P:
            print(f"Found the pattern at location {sa[mid]}")
            return
        elif T[sa[mid]:] < P:
            l = mid + 1
        else:
            r = mid


args = sys.argv
if len(args) > 1:
    input_file = args[1]
else:
    input_file = "input3.txt"

text, pattern = open(input_file).read().splitlines()
sa = suffix_array(text)
print("SA: ", end="")
print(*sa, sep=" ")
bin_search(sa, text, pattern)
