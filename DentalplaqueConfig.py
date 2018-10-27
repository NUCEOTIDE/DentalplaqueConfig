from PIL import Image

#  open image
img = Image.open(r"F:\Users\user\Desktop\iGEM\2018\理论组\testpicRawFiles\testpic_10min_Range.jpg")
result = open(r"F:\Users\user\Desktop\iGEM\2018\理论组\testpicRawFiles\resultFile.txt", "w")

width = img.size[0]   # width of the image
height = img.size[1]  # height of the image

img_darkness = 0  # the measurement of darkness of target pixels
pix_range = 0  # the count of the target pixels

color_range = 82
targetPixel = [228, 47, 114]


def detectionFromRegularImg():
    global width, height
    global pix_range, img_darkness
    global targetPixel
    targetPixel_total = targetPixel[0] + targetPixel[1] + targetPixel[2]
    for i in range(0, width):
        for j in range(0, height):
            data = (img.getpixel((i, j)))
            data_total = data[0] + data[1] + data[2]
            if ((data_total - targetPixel_total) in range(-color_range, +color_range)):
                img_darkness += data[0]+data[1]+data[2]
                pix_range += 1
    result.write("The sum of image darkness: {0}\n".format(img_darkness))
    result.write("The sum of the area of colored pixes: {0}\n".format(pix_range))
    pix_range = 0
    img_darkness = 0



def detectionFromRangeImg():
    global width, height
    global pix_range, img_darkness
    for i in range(0, width):
        for j in range(0, height):
            data = (img.getpixel((i, j)))
            if (data[0] > 30):
                img_darkness += data[0]*3
                pix_range += 1
    result.write("From Range")
    result.write("The sum of image darkness: {0}\n".format(img_darkness))
    result.write("The sum of the area of colored pixes: {0}\n".format(pix_range))
    pix_range = 0
    img_darkness = 0


detectionFromRegularImg()

print("imageCount: ", img_darkness)
print("imageRange: ", pix_range)

result.close()
