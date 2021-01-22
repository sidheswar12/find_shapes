import cv2
import numpy as np
import argparse


def find_shapes(file_name, min_area=2000, max_area=6000):
    color_img = cv2.imread(file_name)

    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.medianBlur(gray_img, 5)
    k_sharpen = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(blur_img, -1, k_sharpen)

    thr = cv2.threshold(sharpen,150,255, cv2.THRESH_BINARY)[1]
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

    close = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, k, iterations=2)

    contour = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cont = contour[0] if len(contour) == 2 else contour[1]

    image_number = 0
    for c in cont:    
        area = cv2.contourArea(c)   
        if area > min_area and area < max_area:
            x,y,w,h = cv2.boundingRect(c)
            ROI = color_img[y:y+h, x:x+h]
            x1 = x
            y1 = y
            x2 = x + w
            y2 = y + h
            print('X1 = {}'.format(x1))
            print('Y1 = {}'.format(y1))
            print('X2 = {}'.format(x2))
            print('Y2 = {}'.format(y2))
            cv2.imwrite('ROI_{}.bmp'.format(image_number), ROI)
            cv2.rectangle(color_img, (x, y), (x + w, y + h), (36,255,12), 2)
            image_number += 1

    cv2.imshow('image', color_img)
    cv2.waitKey()

def main():
    parser = argparse.ArgumentParser(description='Find shapes from image')
    parser.add_argument('--file','-f', type=str, default='img.bmp',
                        help='Provide full path with file name')
    parser.add_argument('--min_area', type=int, default=2000,
                        help='Provide min area of the shape to be found')
    parser.add_argument('--max_area', type=int, default=6000,
                    help='Provide max area of the shape to be found')
    args = parser.parse_args()
    find_shapes(args.file, args.min_area, args.max_area)


if __name__ == "__main__":
    main()
