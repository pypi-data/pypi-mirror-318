from abc import ABC
from shared.Sort import Sort


class CountingSort(Sort, ABC):

    @staticmethod
    def sort(input_array):
        # Finding the maximum element of input_array.
        M = max(input_array)

        # Initializing count_array with 0
        count_array = [0] * (M + 1)

        # Mapping each element of input_array as an index of count_array
        for num in input_array:
            count_array[num] += 1

        # Calculating prefix sum at every index of count_array
        for i in range(1, M + 1):
            count_array[i] += count_array[i - 1]

        # Creating output_array from count_array
        output_array = [0] * len(input_array)

        for i in range(len(input_array) - 1, -1, -1):
            output_array[count_array[input_array[i]] - 1] = input_array[i]
            count_array[input_array[i]] -= 1

        return output_array

    @staticmethod
    def sort_with_visualization(input_array):
        M = max(input_array)

        # Initialize count array
        count_array = [0] * (M + 1)

        # Step 1: Count occurrences
        for num in input_array:
            count_array[num] += 1
            yield count_array + [0] * (len(input_array) - len(count_array))  # For visualization

        # Step 2: Compute prefix sums
        for i in range(1, M + 1):
            count_array[i] += count_array[i - 1]
            yield count_array + [0] * (len(input_array) - len(count_array))  # For visualization

        # Step 3: Sort the array in place
        output_array = [0] * len(input_array)
        for i in range(len(input_array) - 1, -1, -1):
            output_array[count_array[input_array[i]] - 1] = input_array[i]
            count_array[input_array[i]] -= 1
            yield output_array  # For visualization

        # Copy sorted values back to input_array
        for i in range(len(input_array)):
            input_array[i] = output_array[i]

        yield input_array  # Final sorted state
