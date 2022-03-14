from tkinter import Canvas, Frame, BOTH, font

class DisplayFrame(Frame):

    def __init__(self):
        super().__init__()
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)

    def draw_icon(self, icon):
        x_offset = 50
        y_offset = 50
        pixel_size = 20

        for pixel in icon.pixels:
            top_left_x = x_offset + pixel.x * pixel_size
            top_left_y = y_offset + pixel.y * pixel_size
            self.canvas.create_rectangle(
                top_left_x,
                top_left_y,
                top_left_x + pixel_size,
                top_left_y + pixel_size,
                outline="",
                fill=pixel.color.to_hex())