from PIL import Image, ImageFont, ImageDraw
from matplotlib.pyplot import imshow


filename = "Fuji.jpg"
im = Image.open(filename)
imshow(im)


print(im.size)
print(im.format_description)
print(im.mode)



crop = (200,200,600,600)
cropped_image = im.crop(crop)
imshow(cropped_image)


resized_image = im.resize((200,400))
imshow(resized_image)


gray_scale = im.convert("LA")
imshow(gray_scale)


from PIL import ImageFilter
effect = im.filter(ImageFilter.GaussianBlur(radius = 2))
imshow(effect)



draw = ImageDraw.Draw(im)
font = ImageFont.truetype('arial.ttf', 70)
draw.text((100,100),"Prabhat's photo", font = font)
imshow(im)
