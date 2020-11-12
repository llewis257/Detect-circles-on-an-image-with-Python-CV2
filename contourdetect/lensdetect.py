import cv2
import numpy as np
from PIL import Image
import os

def circledetect(givenpath):
    outPath = "/results/" # create a folder called "results" to save the results
    path = givenpath

    ###############################KHOSHGEL######################################Here we declare the variable used to name new files created
    l= 0
    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):

        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        img = Image.open(input_path)
        width, height = img.size
        left = 0
        top = 0
        right = width / 2
        bottom = height
        img_cropped = img.crop((left, top, right, bottom)) # getting rid of the right part of the image
        img_cropped.save("D:/Summer20/contourdetect/contourdetect/images/image_cropped.png")

        # Let's blur and make it gray
        img_cr = cv2.imread("D:/Summer20/contourdetect/contourdetect/images/image_cropped.png")
        img_bl = cv2.medianBlur(img_cr, 5)
        gray = cv2.cvtColor(img_bl, cv2.COLOR_BGR2GRAY)
        # Find edges
        # img_canny = cv2.Canny(gray,300,300)

        # Find circles
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 20, 550.0,
                                   param1=50, param2=100, minRadius=0, maxRadius=0)

        circles = np.uint16(np.around(circles))
        # Find the diameter of the found circle
        for i in circles:
            for j in i:
                diameter= (j[2] * 2)
        # Draw the circle found
        for k in circles[0, :]:
            # draw the outer circle
            cv2.circle(img_cr, (k[0], k[1]), k[2], (255, 0, 0), 2)
            # draw the center of the circle
            cv2.circle(img_cr, (k[0], k[1]), 2, (0, 0, 255), 3) 
            #put the diameter of the circle on the image
        result = cv2.putText(img_cr, "The diameter is "+ str(diameter),(20, 55), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2, cv2.LINE_AA) 
            #saving result
        cv2.imwrite('results/result_image {0}.png'.format(l), result)
        l+=1
            # create full result path, 'example.jpg'
            # becomes 'result_example.jpg', save the file to disk
        #fullpath = os.path.join(outPath, 'result_{0}'.format(i)+image_path)
            #cv2.waitKey()
            #cv2.destroyAllWindows()
            






if __name__ == '__main__':
    circledetect("D:/Summer20/contourdetect/Jupiter Z/Jupiter Z/")








