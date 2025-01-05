from abc import ABC
from shared.Sort import Sort


class BubbleSort(Sort, ABC):

    @staticmethod
    def sort(arr):
        n = len(arr)
        for i in range(n):
            # Last i elements are already sorted
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    # Swap if the element found is greater than the next element
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def sort_with_visualization(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                yield arr.copy()  # Yield current state before comparing
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    yield arr.copy()  # Yield state after swapping
        yield arr.copy()  # Final sorted state
