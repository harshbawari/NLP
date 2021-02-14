import cv2
import numpy as np
import pytesseract as pt
from PIL import Image
from pytesseract import image_to_string
import os


def get_text(img):
    img = cv2.imread(img)

    print('img: ', img)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    tessdata_dir_config = '--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata"'

    text = pt.image_to_string(img, lang="hin", config=tessdata_dir_config)

    return text


def main():
    # path for images
    path = "images"

    # output file
    outputPath = "output/out.txt"

    open(outputPath, 'w').close()
    outFile = open(outputPath, "a+")

    # iterating the images inside the folder
    for imageName in os.listdir(path):
        inputPath = os.path.join(path, imageName)

        text = get_text(inputPath)

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
