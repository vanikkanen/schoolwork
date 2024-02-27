import sys


def suffix_array(T):
    sa = []
    for i in range(0, len(T)):
        sa.append(i)
    return sorted(sa, key=lambda x: T[x:])


def lcp(A, B):
    x = 0

    max = min(len(A), len(B))

    for i in range(0, max):
        if A[i] == B[i]:
            x += 1
        else:
            break
    return x


def lcp_arr(sa, T):
    lcp_array = []
    for i in range(0, len(sa)):
        lo = -1
        hi = len(sa)
        while lo < hi:
            mid = (lo + hi) // 2
            if mid == i:

                if hi >= len(sa):
                    lcp_high = 0
                else:
                    lcp_high = lcp(T[sa[mid]:], T[sa[hi]:])
                if lo == -1:
                    lcp_low = 0
                else:
                    lcp_low = lcp(T[sa[lo]:], T[sa[mid]:])

                lcp_array.append((lcp_low, lcp_high))
                break
            elif mid < i:
                lo = mid
            else:
                hi = mid

    return lcp_array


def bin_search(sa, T, P):
    print(f"Binary search for {P}")
    low = -1
    high = len(sa)
    while (high-low) > 1:
        mid = (low+high)//2
        found = False
        if high >= len(sa):
            lcp_high = 0
            lcp_high_mid = 0
        else:
            lcp_high = lcp(T[sa[high]:], P)
            lcp_high_mid = lcp(T[sa[mid]:], T[sa[high]:])

        if low == -1:
            lcp_low = 0
            lcp_low_mid = 0
        else:
            lcp_low = lcp(T[sa[low]:], P)
            lcp_low_mid = lcp(T[sa[low]:], T[sa[mid]:])

        print(f"({low}, {mid}, {high}, {lcp_low}, {lcp_high}):", end="")

        if lcp_low >= lcp_high:
            if lcp_low < lcp_low_mid:
                low = mid
                print(f" LCP(low, P) = {lcp_low} < LCP(low, mid) ="
                      f" {lcp_low_mid}")
            elif lcp_low > lcp_low_mid:
                high = mid
                print(f" LCP(low, P) = {lcp_low} > LCP(low, mid) ="
                      f" {lcp_low_mid}")
            else:
                matching = lcp(P[lcp_low:], T[sa[mid]+lcp_low:])
                if matching != len(P[lcp_low:]):
                    if matching >= len(T[sa[mid] + lcp_low:]):
                        low = mid
                        matching -= 1
                    elif T[sa[mid] + lcp_low:][matching] < P[lcp_low:][matching]:
                        low = mid
                    else:
                        high = mid

                    print(f" {P[lcp_low:lcp_low + matching + 1]} <=>"
                          f" {T[sa[mid] + lcp_low:sa[mid] + lcp_low + matching + 1]}")
                else:
                    found = True
                    print(f" {P[lcp_low:lcp_low + matching]} <=>"
                          f" {T[sa[mid] + lcp_low:sa[mid] + lcp_low + matching]}")

        else:
            if lcp_high > lcp_high_mid:
                low = mid
                print(f" LCP(high, P) = {lcp_high} > LCP(mid, high) = "
                      f"{lcp_high_mid}")
            elif lcp_high < lcp_high_mid:
                high = mid
                print(f" LCP(high, P) = {lcp_high} < LCP(mid, high) = "
                      f"{lcp_high_mid}")
            else:
                matching = lcp(P[lcp_high:], T[sa[mid]+lcp_high:])
                if matching != len(P[lcp_high:]):
                    if matching != len(P[lcp_high:]):
                        if matching >= len(T[sa[mid] + lcp_high:]):
                            high = mid
                            matching -= 1
                        elif T[sa[mid]+lcp_high:][matching] < P[lcp_high:][
                            matching]:
                            low = mid
                        else:
                            high = mid

                    print(f" {P[lcp_high:lcp_high + matching + 1]} <=>"
                          f" {T[sa[mid] + lcp_high:sa[mid] + lcp_high + matching + 1]}")
                else:
                    found = True
                    print(f" {P[lcp_high:lcp_high + matching]} <=>"
                          f" {T[sa[mid] + lcp_high:sa[mid] + lcp_high + matching]}")
        if found:
            print(f"Found the pattern at location {sa[mid]}")
            break


args = sys.argv
if len(args) > 1:
    input_file = args[1]
else:
    input_file = "input5.txt"

text, pattern = open(input_file).read().splitlines()
sa = suffix_array(text)
print("SA: ", end="")
print(*sa, sep=" ")

lcp_array = lcp_arr(sa, text)
print("LCP:", end="")
for ele in lcp_array:
    print(f" [{ele[0]}, {ele[1]}]", end="")
print()
bin_search(sa, text, pattern)
