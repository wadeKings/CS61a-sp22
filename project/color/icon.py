class Color:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return f"Color({self.r},{self.g},{self.b})"

    def to_hex(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"


red = Color(255, 0, 0)
print(red.to_hex())


class Pixel:
    def __init__(self, x, y, r, g, b):
        self.x = x
        self.y = y
        self.color = Color(r, g, b)

    def __repr__(self):
        return f"Pixel({self.x},{self.y},{self.color})"

        
pixel = Pixel(0, 7, 255, 0, 0)
print(pixel.color.to_hex())     


class Icon:

    def __init__(self, width, height, pixels=None):
        self.width = width
        self.height = height
        self.pixels = pixels
        if not self.pixels:
            self.pixels = [ Pixel(x, y, 0, 0, 0)
                for x in range(width) for y in range(height)]

    def __repr__(self):
        pixels = ",".join([repr(pixel) for pixel in self.pixels])
        return f"Icon({self.width}, {self.height}, {self.pixels})"

icon = Icon(2, 2, [Pixel(0, 0, 255, 0, 0),
    Pixel(0, 1, 255, 50, 0),
    Pixel(1, 0, 255, 100, 0),
    Pixel(1, 1, 255, 150, 0)])

for pixel in icon.pixels:
    pixel.color.g += 50        


