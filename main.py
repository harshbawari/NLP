import cv2
import numpy as np
import pytesseract as pt
from PIL import Image
from pytesseract import image_to_string
import os


def logger(text):
    print('Log: ', text)


def edit_image(img):
    img = cv2.resize(img, None, fx=0.5, fy=0.5)
    logger('Resize complete')
    #cv2.imshow("Img", img)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    logger('Color changed')

    kernel = np.ones((1, 1), np.uint8)
    logger('kernel ')
    img = cv2.dilate(img, kernel, iterations=1)
    logger('Image dilated')
    #cv2.imshow("Img", img)
    img = cv2.erode(img, kernel, iterations=1)
    logger('Image eroded')
    #cv2.imshow("Img", img)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    logger('Threshold set')
    logger('Returning image')

    return img


def get_text(img):
    img = cv2.imread(img)

    img = edit_image(img)
    logger('Image edited')

    tessdata_dir_config = '--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata"'

    logger('Extracting text')
    text = pt.image_to_string(img, lang="hin", config=tessdata_dir_config)
    logger('Text extraction complete')

    return text


def main():
    # path for images
    path = "images"

    # output file
    outputPath = "output/out.txt"

    open(outputPath, 'w').close()
    outFile = open(outputPath, "a+")

    count = 1

    # iterating the images inside the folder
    for imageName in os.listdir(path):
        print(count)
        logger('processing ' + imageName)
        count = count+1
        inputPath = os.path.join(path, imageName)

        text = get_text(inputPath)
        logger('Text received')

        # providing the name of the image
        # file1.write(imageName+"\n")

        # providing the content in the image
        outFile.write(text+"\n")

    outFile.close()

    # for printing the output file
    file2 = open(outputPath, 'r')
    print(file2.read())
    file2.close()


main()
