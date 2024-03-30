
import cv2
import numpy as np

def read_image(img_path):
    return cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

def main():
    img = read_image('./opencv_logo.jpg')

    print(f'The mean pixel value is {np.mean(img)}')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
