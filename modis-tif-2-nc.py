from libtiff import TIFF
from scipy import misc
from PIL import Image, ImageFilter
import numpy as np

folder = '/home/scr/Downloads/'
sfname = folder + 'MOD17A2_GPP.A2000001.tif'
dfname = folder + 'resized-MOD17A2_GPP.A2000001.tif'
# im = Image.open(fname)
# w, h = im.size
# matrix = misc.imread(dfname)
# lt0 = (matrix[matrix<0])
# gt10000 = (matrix[matrix>10000])

out_tiff = TIFF.open(dfname, mode = 'w')
im = Image.open(sfname)
# im = im.filter(ImageFilter.MinFilter(0))
# im = im.filter(ImageFilter.MaxFilter(15000))
resized = im.resize((720, 360), Image.LANCZOS)
croped = resized.crop((0, 15, 720, 290))
out_tiff.write_image(croped, compression=None)
out_tiff.close()



# tif = TIFF.open(fname, mode='r')
# for im in list(tif.iter_images()):
#     im
