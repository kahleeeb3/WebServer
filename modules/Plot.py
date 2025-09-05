import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import cv2
import numpy as np

class RandomScatterPlot():
    def __init__(self, seed:int = 42, num_points:int = 50):
        self.seed = seed
        self.num_points = num_points
        self.fig = None
        self.ax = None
        self.scatter = None
        self._setup()

    def _setup(self):
        np.random.seed(self.seed)
        self.fig = plt.figure(figsize=(6.4, 4.8)) # 640x480 figure
        self.ax = self.fig.add_subplot(111)
        self.scatter = plt.scatter([], [], s=10, c='red')
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)

    def update(self):
        x = np.random.rand(self.num_points)
        y = np.random.rand(self.num_points)
        self.scatter.set_offsets(np.c_[x, y])
    
    def get_frame_data(self, quality:int = 80) -> bytes:
        canvas = FigureCanvas(self.fig)
        canvas.draw()  # Render the figure
        buf = np.frombuffer(canvas.buffer_rgba(), dtype=np.uint8)
        width, height = self.fig.canvas.get_width_height()
        image = buf.reshape((height, width, 4))[:, :, :3]
        _, frame_data = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        return frame_data.tobytes()