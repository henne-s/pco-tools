#!/usr/bin/python
"""Test pco_reader.info():
Show information about a PCO image
"""

from pco_tools import pco_reader as pco


def main():
    """Main function"""

    filename = 'images/dotmatrix.b16'
    pco.info(filename)


if __name__ == '__main__':
    main()
