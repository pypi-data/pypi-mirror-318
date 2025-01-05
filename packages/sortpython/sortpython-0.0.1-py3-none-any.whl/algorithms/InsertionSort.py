from abc import ABC
from shared.Sort import Sort


class InsertionSort(Sort, ABC):

    @staticmethod
    def sort(arr):
        # Sort the entire array using insertion_sort
        InsertionSort.insertion_sort(arr, 0, len(arr) - 1)
        return arr

    @staticmethod
    def sort_with_visualization(arr):
        arr = arr.copy()
        # Use insertion sort with visualization
        yield from InsertionSort.insertion_sort_with_visualization(arr, 0, len(arr) - 1)

    @staticmethod
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    @staticmethod
    def insertion_sort_with_visualization(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                yield arr.copy()  # Yield intermediate steps
            arr[j + 1] = key
            yield arr.copy()  # Yield final state of this step