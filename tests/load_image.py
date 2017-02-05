#!/usr/bin/python
"""Test pco_reader.load():
Load a PCO image
"""

from pco_tools import pco_reader as pco
import matplotlib.pyplot as plt


def main():
    """Main function"""

    filename = 'images/dotmatrix.b16'
    image = pco.load(filename)
    plt.imshow(image,
               cmap=plt.cm.jet,
               interpolation='none',
              )
    plt.show()


if __name__ == '__main__':
    main()
