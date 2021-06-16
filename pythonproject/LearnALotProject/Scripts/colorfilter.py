
from PIL import Image, ImageDraw


def greyscale(img):
    return img.convert("L")  # luminous


def draw_gradient(im, *colors, direction="diagonal"):
    def _interpolate(start, end):
        diffs = [(t - f) / lines for f, t in zip(start, end)]
        for i in range(lines):
            yield [round(value + (diff * i)) for value, diff in zip(start, diffs)]

    draw = ImageDraw.Draw(im)

    if direction == "horizontal":
        lines = im.width // (len(colors) - 1)
    elif direction == "vertical":
        lines = im.height // (len(colors) - 1)
    else:
        lines = (im.width * 2) // len(colors)

    line_number = 0
    for i in range(len(colors) - 1):
        for color in _interpolate(colors[i], colors[i + 1]):
            if direction == "horizontal":
                draw.line([(line_number, 0), (line_number, im.height)], tuple(color), width=1)
            elif direction == "vertical":
                draw.line([(0, line_number), (im.width, line_number)], tuple(color), width=1)
            else:
                draw.line([(line_number, 0), (0, line_number)], tuple(color), width=1)
            line_number += 1
    return im


def pride(im, direction="diagonal"):
    grad = Image.new("RGBA", size=im.size, color=(0, 0, 0, 0))
    colors = (
        (240, 1, 0),
        (255, 128, 0),
        (255, 255, 0),
        (0, 121, 64),
        (64, 65, 255),
        (161, 0, 193)
    )

    grad = draw_gradient(grad, *colors, direction=direction)
    grad.putalpha(127)
    return Image.alpha_composite(im, grad)


def trans_pride(im, direction="diagonal"):
    grad = Image.new("RGBA", size=im.size,
                     color=(0, 0, 0, 0))  # creates a new image with the given mode and size. Size is
    # given as a (width, height)-tuple, in pixels. The color is given as a single value for single-band images,
    # and a tuple for multi-band images (with one value for each band).
    colors = (
        (91, 206, 251),  # blue
        (245, 168, 184),  #
        (255, 255, 255),
        (245, 168, 184),
        (91, 206, 251),
    )
    grad = draw_gradient(grad, *colors, direction=direction)
    grad.putalpha(127)
    return Image.alpha_composite(im, grad)


if __name__ == "__main__":
    with Image.open("SourceFolder/peacock1.jpg") as img:
        print(img.size)
        img = img.convert("RGBA")
        # img.show()
        greyscale_img = greyscale(img)
        # greyscale_img.show()
# creating a image object (new image object) with
# RGB mode and size 200x200
pride_im = pride(img)
pride_im.show()

trans_im = trans_pride(img)
trans_im.show()
