#!/usr/bin/python3
import cv2
import matplotlib.pyplot as plt
from astropy.io import fits
import argparse, sys

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

parser = argparse.ArgumentParser(description='input fits image filename')
parser.add_argument("filename", help='input bayered fits image filename and create jpg color image')
parser.add_argument("-o", action='store_true', help='save file')
args = parser.parse_args()
hdul = fits.open(args.filename)
imgRGGB = hdul[0].data
imgRGB = cv2.cvtColor(imgRGGB, cv2.COLOR_BAYER_RG2RGB)
#debayered_image = cv2.cvtColor(imgRGGB, cv2.COLOR_BayerRGGB2BGR )
normalised_image = cv2.normalize(imgRGB, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
#imgplot = plt.imshow(normalised_image)
#plt.show()
b,g,r = cv2.split(imgRGB)
tiles = 128  #int(readpar('tiles'))
clahe = cv2.createCLAHE(clipLimit=4., tileGridSize=(tiles,tiles))
cr=clahe.apply(r)
cg=clahe.apply(g)
cb=clahe.apply(b)
crgb = cv2.merge((cb,cg,cr))
if args.o: 
    cv2.imwrite(args.filename[:-5]+".jpg", crgb, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    print("file "+args.filename[:-5]+".jpg created")
#imgplot = plt.imshow(normalised_image)
#plt.show()

#img = cv2.imread( args.filename[:-5]+".jpg", cv2.IMREAD_ANYCOLOR)

resize = ResizeWithAspectRatio(crgb, height=900) # Resize by width OR

#cv2.imshow('resize', resize)
#cv2.waitKey()

while True:
    cv2.imshow(args.filename[:-5]+".jpg", resize)
    cv2.waitKey(0)
    sys.exit() # to exit from all the processes

#cv2.destroyAllWindows() # destroy all windows
