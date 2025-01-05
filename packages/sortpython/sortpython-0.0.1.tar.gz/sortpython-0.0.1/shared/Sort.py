from abc import ABC, abstractmethod


class Sort(ABC):

    @abstractmethod
    def sort(self, input_array):
        pass

    @abstractmethod
    def sort_with_visualization(self, input_array):
        pass
