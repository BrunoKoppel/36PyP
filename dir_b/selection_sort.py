import sys


def selection_sort(array, VERBOSE):
    if VERBOSE:
        print("Received array => " + str(array))

    for i in range(len(array)):
        if VERBOSE:
            print("Currently at [" + str(i) + "] -> " + str(array[i]))

        minimum_index = i
        for j in range(i + 1, len(array)):
            if VERBOSE:
                print("Comparing [" + str(i) + "] -> " + str(array[i]) + "  with [" + str(j) + "] -> " + str(array[j]))
            if array[minimum_index] > array[j]:
                minimum_index = j
                if VERBOSE:
                    print("found minimum index at index => [" + str(minimum_index) + "]")

        # Swap method
        if VERBOSE:
            print("Swapping [" + str(i) + "] -> " + str(array[i]) + " with [" + str(minimum_index) + "] -> " + str(array[minimum_index]))
        array[i], array[minimum_index] = array[minimum_index], array[i]

    print("Sorted Array => " + str(array))


if __name__ == '__main__':
    selection_sort([64, 25, 12, 22, 11], True)
