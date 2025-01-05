from abc import ABC
from shared.Sort import Sort


class MergeSort(Sort, ABC):

    @staticmethod
    def sort(arr):
        return MergeSort.merge_sort(arr, 0, len(arr) - 1)

    @staticmethod
    def sort_with_visualization(arr):
        yield from MergeSort.merge_sort_with_visualization(arr, 0, len(arr) - 1)

    @staticmethod
    def merge_sort(arr, left, right):
        if left < right:
            mid = (left + right) // 2

            MergeSort.merge_sort(arr, left, mid)
            MergeSort.merge_sort(arr, mid + 1, right)
            MergeSort.merge(arr, left, mid, right)

    @staticmethod
    def merge_sort_with_visualization(arr, left, right):
        if left < right:
            mid = (left + right) // 2

            # Recursively sort first and second halves with visualization
            yield from MergeSort.merge_sort_with_visualization(arr, left, mid)
            yield from MergeSort.merge_sort_with_visualization(arr, mid + 1, right)

            # Merge the sorted halves with visualization
            yield from MergeSort.merge_with_visualization(arr, left, mid, right)

    @staticmethod
    def merge(arr, left, mid, right):
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]

        # Merge the temporary arrays back into arr
        i = 0
        j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1

    @staticmethod
    def merge_with_visualization(arr, left, mid, right):
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]

        i = 0
        j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
            yield arr.copy()  # Yield the array state after each merge step

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
            yield arr.copy()  # Yield the array state

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
            yield arr.copy()  # Yield the array state
