# Assignment 12 - Task 3
# Bubble Sort Algorithm

def bubble_sort(numbers):
    result = numbers.copy()
    comparisons = 0
    n = len(result)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparisons += 1

            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result, comparisons


# Testing different lists

test_lists = [
    [5, 2, 8, 1, 3],

    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],

    [42, 8, -3, 17, 0, 91, 23, 5, 68, 12,
     -10, 34, 7, 56, 19, 2, 80, -5, 41, 15]
]

for numbers in test_lists:
    sorted_list, comparisons = bubble_sort(numbers)

    n = len(numbers)

    print("\n--- Sorting experiment ---")
    print("List length:", n)
    print("Original list:", numbers)
    print("Sorted list:", sorted_list)
    print("Comparisons:", comparisons)
    print("Expected comparisons:", n * (n - 1) // 2)