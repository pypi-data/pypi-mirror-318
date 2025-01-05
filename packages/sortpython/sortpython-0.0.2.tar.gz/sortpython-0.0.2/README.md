# sortpython

[![PyPI version](https://img.shields.io/pypi/v/sortpython.svg)](https://pypi.org/project/sortpython/)

sortpython is a Python library that implements a variety of sorting algorithms. It provides an easy-to-use interface for sorting data using popular algorithms like Quick Sort, Merge Sort, and Bubble Sort.

## Features

## Features

- **Quick Sort**: Fast and efficient for most cases.
- **Merge Sort**: Stable and reliable for large datasets.
- **Bubble Sort**: Simple and easy to understand.
- **Counting Sort**: Efficient for sorting integers within a limited range.
- **Insertion Sort**: Simple and efficient for small or nearly sorted datasets.
- **Tim Sort**: A hybrid sorting algorithm optimized for real-world data.
- Other algorithms will be release in future
- There is a simple visualization also.

## Installation

Install sortpython using pip:

```bash
pip install sortpython
```

## Usage
```bash
from algorithms.TimSort import TimSort
from visualize.SortVisualizer import SortVisualizer

data = [64, 34, 25, 12, 22, 11, 90]
visualize = input("Do you want to visualize the sorting process? (y/n): ").strip().lower() == 'y'
if visualize:
    visualizer = SortVisualizer(data, 500)
    steps_generator = TimSort.sort_with_visualization(data)
    visualizer.capture_steps(steps_generator)
    visualizer.animate()
    print("Sorted Array:", data)
else:
    TimSort.sort(data)
    print("Sorted Array:", data)
```

