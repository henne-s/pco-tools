
PCO Tools
=========

A Python module to read images that have been recorded using a PCO camera and
the software PCO CamWare.

Tested cameras
--------------

* SensiCam qe

The module should also work for other PCO cameras.

Examples
--------

Load an image and show it using matplotlib::

    from pco_tools import pco_reader as pco
    import matplotlib.pyplot as plt
    
    img = pco.load('myimage.b16')
    plt.imshow(img)
