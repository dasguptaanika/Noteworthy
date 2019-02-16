from PIL import Image
import pytesseract
import cv2
import os
import io
numFiles = int(input("Enter the number of images to be processed: "))
for image in range(0, numFiles) :
    fileName = input("Enter a filename: ")
    #fileName = "book_text.JPG"

    image = cv2.imread(fileName)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    gray = cv2.medianBlur(gray, 3)

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)

    file = io.open("output_python.txt", 'w', encoding='utf8') 
    #text = text.encode("utf-8")
    file.write(text)
    file.close()

    # show the output images
    #cv2.imshow("Image", image)
    #cv2.imshow("Output", gray)
    #cv2.waitKey(0)