# Copyright 2017 Hendrik Soehnholz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""PCO tools

Read image files as written by PCO CamWare

Hendrik Soehnholz
3.4.14
"""

import struct
import numpy as np
#import matplotlib.pyplot as plt

pco_string = 0x2d4f4350  # String 'PCO-'


def info(filename):
    """Read information from PCO file header."""

    # read image file
    imgfile = open(filename, 'rb') # read binary
    buf = imgfile.read()
    imgfile.close()

    # read header
    # 32 bit values (long)
#    header = range(6)
#    for i in range(6):
#        header[i] = struct.unpack_from('<L', buf[4 * i:4 * i + 4])[0]
    header = struct.unpack_from('<' + 'L' * 6, buf)

    if header[0] != pco_string:
        print("Error: Not a PCO file!")
        return

    filesize = header[1]
    print("File size: " + repr(filesize) + " Bytes")
    headersize = header[2]
    print("Header size: " + repr(headersize) + " Bytes")
    imgsize_x = header[3]
    print("Width: " + repr(imgsize_x) + " Pixels")
    imgsize_y = header[4]
    print("Height: " + repr(imgsize_y) + " Pixels")

    if np.int32(header[5]) == -1:
        # extended header
        print("Extended header:")
        # read extended header
        # 32 bit values (long)
#        header = range(32)
#        for i in range(32):
#            header[i] = struct.unpack_from('<L', buf[4 * i:4 * i + 4])[0]
        header = struct.unpack_from('<' + 'L' * 32, buf)

        color_mode = header[6]
        if color_mode == 1:
            print("  Color mode: color")
        else:
            print("  Color mode: b/w")

    return


#@profile
def load(filename):
    """Load image file in .b16 format
    as used by PCO CamWare
    and return image data as numpy array.
    """

    # read image file
    imgfile = open(filename, 'rb') # read binary
    buf = imgfile.read()
    imgfile.close()



    # read header
    # 32 bit values (long)
#    header = range(6)
#    for i in range(6):
#        header[i] = struct.unpack_from('<L', buf[4 * i:4 * i + 4])[0]
    header = struct.unpack_from('<' + 'L' * 6, buf)

    if header[0] != pco_string:
        print("Error: Not a PCO file!")
        return

    headersize = header[2]
    imgsize_x = header[3]
    imgsize_y = header[4]

    # read image data
    # 16 bit values (short)
    if len(buf[headersize:]) < imgsize_x * imgsize_y * 2:
        print("Error: Not enough pixel data!")
        return
    else:
#        img = np.arange(imgsize_x * imgsize_y)
#        for i in range(imgsize_x * imgsize_y):
#            img[i] = struct.unpack_from('<H', buf,
#                                        offset = headersize + 2 * i)[0]

#        daten = struct.unpack_from('<' + 'H' * imgsize_x * imgsize_y,
#                                   buf, offset = headersize)
#        img = np.array(daten)

        img = np.frombuffer(buf, \
                                dtype=np.dtype('<u2'), \
                                count=imgsize_x * imgsize_y, \
                                offset=headersize)
        img = img.reshape(imgsize_y, imgsize_x)
        return img


if __name__ == '__main__':
    print("PCO tools")
