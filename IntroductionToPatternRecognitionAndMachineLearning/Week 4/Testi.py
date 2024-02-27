def selectionSort(list):
  for i in range(len(list)):
    for j in range(i+1, len(list)):
      min_idx = i
      if list[min_idx] > list[j]:
        min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
  return list


def binarySearch(list, l, r, x):

  if r >= 1:
    mid = l + (r - l) // 2
    if list[mid] == x:
        return mid
    elif list[mid] > x:
      return binarySearch(list, l, mid-1, x)
    else:
      return binarySearch(list, mid + 1, r, x)
  else:
    return -1







arr = [4,2,8,9,7,1,3]
sorted = selectionSort(arr)
print(sorted)
#[1, 4, 0], 0, 2, 1
#[2, 3, 8, 10, 12, 15, 30], 0, 6, 12
print(binarySearch([0, 4, 8, 9, 7, 5, 3], 0, 6, 5))
