from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2

def getSize(size, dementions):
    ratio = min(dementions[0] / size[0], dementions[1] / size[1])
    return (int(size[0] * ratio), int(size[1] * ratio))

frameArray = []
pathOut = 'video.mp4'

borderSize = 5
desiredDementions = (600,900)
fontSize = 40
text = "AMOGUS"
myImg = Image.open("image.jpg")


for i in text:
    size = getSize(myImg.size, desiredDementions)
    myImg.thumbnail(size, Image.ANTIALIAS)
    img_w, img_h = myImg.size
    word = i if type(i) == str else text
    bg = Image.new('RGB', (img_w + 44 * 2, img_h + 44 + 150), color = 'black')
    border = Image.new('RGB', (img_w + borderSize * 2, img_h + borderSize* 2), color = 'white')
    bg_w, bg_h = bg.size

    fnt = ImageFont.truetype("font.ttf", fontSize)
    d = ImageDraw.Draw(bg)

    offsetImg = ((bg_w - img_w) // 2, 44)
    offsetBorder = ((bg_w - border.size[0]) // 2, 44 - borderSize)
    textOffset = (fontSize * len(word)) // 4

    bg.paste(border, offsetBorder)
    bg.paste(myImg, offsetImg)
    d.text((bg_w//2 - textOffset, 44 + borderSize * 2 + img_h + 25),word ,(255,255,255),font=fnt)
    myImg = bg
    frame = np.array(myImg) 
    frame = frame[:, :, ::-1].copy()
    frameArray.append(frame)

size = frameArray[len(frameArray)-1].shape
videoSize = (max(i.shape[1] for i in frameArray), max(i.shape[0] for i in frameArray))
out = cv2.VideoWriter(pathOut, 0x7634706d, 8, videoSize)
for i in range(len(frameArray)):
    image = cv2.resize(frameArray[i], videoSize)
    out.write(image)
out.release()
bg.save('out.png')
