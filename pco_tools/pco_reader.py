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
Initial version: 2014-04-03
"""

import struct
import numpy as np

PCO_STRING = 0x2d4f4350  # String 'PCO-'


def info(filename):
    """Read information from PCO file header."""

    # read image file
    imgfile = open(filename, 'rb')  # read binary
    buf = imgfile.read()
    imgfile.close()

    # read header
    # 32 bit values (long)
    header = struct.unpack_from('<' + 'L' * 6, buf)

    if header[0] != PCO_STRING:
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
        header = struct.unpack_from('<' + 'L' * 32, buf)

        color_mode = header[6]
        if color_mode == 1:
            print("  Color mode: color")
        else:
            print("  Color mode: b/w")

    return


def load(filename):
    """Load image file in .b16 format
    as used by PCO CamWare
    and return image data as numpy array.
    """

    # read image file
    imgfile = open(filename, 'rb')  # read binary
    buf = imgfile.read()
    imgfile.close()

    # read header
    # 32 bit values (long)
    header = struct.unpack_from('<' + 'L' * 6, buf)

    if header[0] != PCO_STRING:
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
        img = np.frombuffer(buf,
                            dtype=np.dtype('<u2'),
                            count=imgsize_x * imgsize_y,
                            offset=headersize,
                           )
        img = img.reshape(imgsize_y, imgsize_x)

        return img
