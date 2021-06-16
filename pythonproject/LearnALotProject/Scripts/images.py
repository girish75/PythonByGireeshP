from PIL import Image, ImageFilter, ImageDraw, ImageFont

"""
To read files from disk, use the open() function in the Image module. You don’t have to know the file format to open a
file. The library automatically determines the format based on the contents of the file.
"""


def add_cross_to(im, color):
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=color, width=10)  # 0,0 are xy coordinates of both the ends
    draw.line((0,im.size[1], im.size[0], 0), fill=color, width=10) # x and y coordinates of both the ends
    return im
def add_rectangle_to(im, topleft, bottomright, color):
    draw = ImageDraw.Draw(im)
    draw.rectangle((topleft, bottomright), fill=color)
    return im

def add_ellipse_to(im, topleft, size, color):
    draw = ImageDraw.Draw(im)
    draw.ellipse((topleft, (topleft[0] +size[0], topleft[1]+ size[1])), fill=color)
    return im

def add_text(im: object, text, topleft, size, color):
    font = ImageFont.truetype("C:/Users/GIRISHPAREEK/Desktop/Amity/PythonByGirishPareek/Resources/font/arial.ttf", size)
    draw = ImageDraw.Draw(im)
    draw.text(topleft, text, font=font, fill=color)
    return im


# Draw shapes - x and rectangle(Same for square), ellipse(same for circle).
# with Image.open("../../Resources/Images/space.jpg") as im:
#     print(im.format)
#     print(im.size)
#     print(im.mode)
#     im_cross = add_cross_to(im, (255, 0, 0))
#     im_cross.save("./ProcessedImageFolder/Crossed_space.jpg")
#     im_rectangle = add_rectangle_to(im, (50, 50), (1500, 700), (0, 255, 0))
#     im_rectangle.save("./ProcessedImageFolder/Rectangle_space.jpg")
#     im_ellipse = add_ellipse_to(im, (650, 650), (1500, 700), (0, 0, 255))
#     im_rectangle.save("./ProcessedImageFolder/ellipse_space.jpg")
#
# # Draw shapes - x and rectangle(Same for square), ellipse(same for circle).
# with Image.open("../../Resources/Images/space.jpg") as im:
#     print(im.format)
#     print(im.size)
#     print(im.mode)
#     im_cross = add_cross_to(im, (255, 0, 0))
#     im_cross.save("./ProcessedImageFolder/Crossed_space.jpg")
#     im_rectangle = add_rectangle_to(im, (50, 50), (1500, 700), (0, 255, 0))
#     im_rectangle.save("./ProcessedImageFolder/Rectangle_space.jpg")
#     im_ellipse = add_ellipse_to(im, (650, 650), (1500, 700), (0, 0, 255))
#     im_rectangle.save("./ProcessedImageFolder/ellipse_space.jpg")

# ====Drawing text - Image manipulation with python ==========
# with Image.open("../../Resources/Images/spaceman.jpg") as imtext:
#     imagewithtext = add_text(imtext, "Hello Girish! \n Welcome at Mars", (100,100), 200, (255,255,255))
#     imagewithtext.save("./ProcessedImageFolder/Spaceman_with_text.jpg")

# ====Using Filters - Image manipulation with python ==========

filters= {
    "Blur": ImageFilter.BLUR,
    "Contour": ImageFilter.CONTOUR,
    "Detail": ImageFilter.DETAIL,
    "Edge Enhanced": ImageFilter.EDGE_ENHANCE,
    "Edge Enhanced More": ImageFilter.EDGE_ENHANCE_MORE,
    "Emboss": ImageFilter.EMBOSS,
    "Find Edges": ImageFilter.FIND_EDGES,
    "Sharpen": ImageFilter.SHARPEN,
    "Smooth": ImageFilter.SMOOTH,
    "Smooth More": ImageFilter.SMOOTH_MORE,
    "Box Blur": ImageFilter.BoxBlur(1),
    "Gaussian Blur": ImageFilter.GaussianBlur(2),
    "Gaussian Blur": ImageFilter.GaussianBlur(25),
    "Unsharp Mask": ImageFilter.UnsharpMask
}

for key,value in filters.items():
    with Image.open("SourceFolder/Resized_space.jpeg") as img:
        img1 = img.filter(value)
        img1.save(f"./ProcessedImageFolder/{key}.jpg")

# # print(im) # This does not print image itself but just show all of its meta data.
# # im.show() # this will open the file and show the image.
# Filtered_image = im.filter(ImageFilter.BLUR)
# Filtered_image.save("Pikachu_blur.png", "png")
# print(Filtered_image)
# # Filtered_image.show() # this will show the new image file.
# Filtered_image = im.filter(ImageFilter.SMOOTH)
# Filtered_image.save("Pikachu_Smooth.png", "png")
# Filtered_image = im.filter(ImageFilter.SHARPEN)
# Filtered_image.save("Pikachu_Smooth.png", "png")
# Filtered_image = im.convert('L')
# Filtered_image.save("Pikachu_grey.jpeg", "jpeg")
# crooked = Filtered_image.rotate(90, expand = True)
# crooked.save("90Degree_Pikachu_grey.jpeg", "jpeg")
# crooked.show()
#
# Resize = Filtered_image.resize((300, 300))
# Resize.save("Resized_Pikachu_grey.jpeg", "jpeg")
# Resize.show()
#
# box=(100,100,400,400) # coordinates of images to crop it.
# region = Filtered_image.crop(box)
# region.save("Cropped_PikachuForFace.png", "png")
# region.show()

# Resize = im.resize((300, 300)) # aspect ratio. But this will have impact on image clarity.
# Resize.save("Resized_space.jpeg", "jpeg")
# Resize.show()
# im.thumbnail((300, 300)) # but Thumbnail do not return a value rather it do in place (current) image.
# im.save('spaceThumbnail.jpg') #it will not impact the aspect ratio and keep the image as much clean.
# im.show()


