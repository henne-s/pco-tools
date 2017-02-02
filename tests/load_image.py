#!/usr/bin/python

import pco_tools as pco
import matplotlib.pyplot as plt

def main():
    filename = 'images/dotmatrix.b16'
    image = pco.load(filename)
    plt.imshow(image, cmap=plt.cm.jet)
    plt.show()

if __name__ == '__main__':
    main()
