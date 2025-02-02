class ImageProcessor:
    def __init__(self, image):
        self.image = image  # 3D array representing RGB pixels

    def apply_grayscale(self):
        for i in range(len(self.image)):
            for j in range(len(self.image[i])):
                r, g, b = self.image[i][j]
                gray = (r + g + b) // 3
                self.image[i][j] = [gray, gray, gray]  # Apply grayscale

    def display_image(self):
        for row in self.image:
            print(row)


# Example usage
image = [
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 0]]
]
processor = ImageProcessor(image)
processor.apply_grayscale()
processor.display_image()
