import sys


def bubble_sort(array, VERBOSE):
    if VERBOSE:
        print("Received array => " + str(array))

    for i in range(len(array)):
        if VERBOSE:
            print("Currently at [" + str(i) + "] -> " + str(array[i]))

        for j in range(i + 1, len(array)):
            if VERBOSE:
                print("Comparing [" + str(j - 1) + "] -> " + str(array[j - 1]) + "  with [" + str(j) + "] -> " + str(array[j]))

            if array[j - 1] > array[j]:
                if VERBOSE:
                    print("Swapping [" + str(j - 1) + "] -> " + str(array[j - 1]) + " with [" + str(j) + "] -> " + str(array[j]))
                array[j - 1], array[j] = array[j], array[j - 1]

        # Swap method
        if VERBOSE:
            print("Result of " + str(i + 1) + " iteration => " + str(array))

    print("Sorted Array => " + str(array))


if __name__ == '__main__':
    bubble_sort([64, 25, 12, 22, 11], True)
