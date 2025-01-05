import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

matplotlib.use("TkAgg")  # Or "Qt5Agg"


class SortVisualizer:
    def __init__(self, initial_data, interval):
        self.data = initial_data
        self.interval = interval
        self.steps = []  # Store the sorting steps
        self.fig, self.ax = plt.subplots()
        self.text_boxes = []  # Store the text box objects for updates

    def capture_steps(self, generator):
        for state in generator:
            self.steps.append(state.copy())

    def update(self, frame):
        current_values = self.steps[frame]
        # Clear the current axes
        self.ax.clear()
        self.ax.axis("off")  # Turn off the axis

        spacing = 0
        box_size = 1

        for i, value in enumerate(current_values):
            # Calculate box position
            left = i * (box_size  + spacing)
            bottom = 0

            # Draw a rectangle
            self.ax.add_patch(
                plt.Rectangle((left, bottom), box_size, box_size, edgecolor='black', facecolor='lightgreen')
            )
            # Add the number as text inside the box
            self.ax.text(
                left + box_size / 2,
                bottom + box_size / 2,
                str(value),
                ha='center',
                va='center',
                fontsize=12
            )

        # Adjust the plot limits to fit all the boxes
        self.ax.set_xlim(-0.5, len(current_values) * (box_size + spacing) - spacing)
        self.ax.set_ylim(-0.5, box_size + 0.5)

    def animate(self):
        ani = animation.FuncAnimation(
            self.fig, self.update, frames=len(self.steps), repeat=False, interval=self.interval
        )
        plt.show()



