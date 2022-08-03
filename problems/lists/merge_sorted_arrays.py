# Given two sorted lists, merge them into one sorted list
import pdb

def merge_sorted_lsts(a: list, b: list) -> list:
    # Edge case
    if len(a) == 0 or len(b) == 0:
        return

    # Define indices
    i,j = 0,0

    result = []
    while i < len(a) and j < len(b):
        try:
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        except IndexError as e:
            pdb.set_trace()
        
    if len(a[i:]) > 0:
        result = result + a[i:]

    if len(b[j:]) > 0:
        result = result + b[j:]

    return result

if __name__ == '__main__':
    lst_one = [1,2,3,4,10,20]
    lst_two = [1,5,6,7,11,21]
    expected = [1, 1, 2, 3, 4, 5, 6, 7, 10, 11, 20, 21]
    result = merge_sorted_lsts(lst_one, lst_two)
    print(result == expected)
