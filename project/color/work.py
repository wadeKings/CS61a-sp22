from tkinter import Tk

from icon import Icon, Pixel, Color
from display_frame import DisplayFrame

# Initialize the Tkinter frame and canvas
root = Tk()
  

icon = Icon(2, 2, [Pixel(0, 0, 255, 0, 0),
    Pixel(0, 1, 255, 50, 0),
    Pixel(1, 0, 255, 100, 0),
    Pixel(1, 1, 255, 150, 0)])

display = DisplayFrame()
display.draw_icon(icon)

# Run Tkinter loop
root.mainloop()