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
    # path for the folder for getting the raw images
    path = "images/edited"

    # link to the file in which output needs to be kept
    fullTempPath = "output/out.txt"

    # iterating the images inside the folder
    for imageName in os.listdir(path):
        inputPath = os.path.join(path, imageName)

        # applying ocr using pytesseract for python
        text = get_text(inputPath)

        # saving the  text for appending it to the output.txt file
        # a + parameter used for creating the file if not present
        # and if present then append the text content
        file1 = open(fullTempPath, "a+")

        # providing the name of the image
        file1.write(imageName+"\n")

        # providing the content in the image
        file1.write(text+"\n")
        file1.close()

    # for printing the output file
    file2 = open(fullTempPath, 'r')
    print(file2.read())
    file2.close()


main()
