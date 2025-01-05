from abc import ABC
from shared.Sort import Sort
from algorithms.MergeSort import MergeSort
from algorithms.InsertionSort import InsertionSort


class TimSort(Sort, ABC):
    MIN_RUN = 32

    @staticmethod
    def sort(arr):
        n = len(arr)

        # Step 1: Sort small runs using Insertion Sort
        for start in range(0, n, TimSort.MIN_RUN):
            end = min(start + TimSort.MIN_RUN - 1, n - 1)
            InsertionSort.insertion_sort(arr, start, end)

        # Step 2: Merge runs using Merge Sort logic
        size = TimSort.MIN_RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min(n - 1, left + 2 * size - 1)

                if mid < right:
                    MergeSort.merge(arr, left, mid, right)
            size *= 2

    @staticmethod
    def sort_with_visualization(arr):
        n = len(arr)

        # Step 1: Sort small runs using Insertion Sort
        for start in range(0, n, TimSort.MIN_RUN):
            end = min(start + TimSort.MIN_RUN - 1, n - 1)
            yield from InsertionSort.insertion_sort_with_visualization(arr, start, end)  # Yield each step

        # Step 2: Merge runs using Merge Sort logic
        size = TimSort.MIN_RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min(n - 1, left + 2 * size - 1)

                if mid < right:
                    yield from MergeSort.merge_with_visualization(arr, left, mid, right)  # Yield each step
            size *= 2
