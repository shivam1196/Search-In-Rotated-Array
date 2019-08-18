def rotated_array_search(input_list, number):
    if len(input_list) is 0:
        return -1
    pivot = find_pivot(input_list, 0, len(input_list))
    index = binary_search(input_list, 0, pivot, number)
    if index is not -1:
        return index
    else:
        last = len(input_list)
        return binary_search(input_list, pivot+1, last-1, number)


def find_pivot(input_list, first, last):
    if first > last:
        return -1
    mid = int((first + last) / 2)
    if input_list[mid] > input_list[mid+1]:
        return mid
    elif input_list[mid] < input_list[mid-1]:
        return mid-1
    elif input_list[mid] < input_list[0]:
        return find_pivot(input_list, 0, mid-1)
    else:
        return find_pivot(input_list, mid+1, last)


def binary_search(input_list, first, last, number):
    if first > last:
        return -1
    mid = int((first+last)/2)
    if input_list[mid] == number:
        return mid
    elif input_list[mid] < number:
        return binary_search(input_list, mid+1, last, number)
    else:
        return binary_search(input_list, first, mid-1, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    test_function([[], 10])
