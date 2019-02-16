import os,sys
from PIL import Image
images = []
global k 
def evaluator(pix):
	global k
	# frome is in i, pixel is in k
	pixelx = k/400
	pixely = k%400
	print k
	k += 1
	return images[i].getpixel((pixelx, pixely))

if len(sys.argv) != 2 or (sys.argv[1] != 'XSlice' and sys.argv[1] != 'YSlice'):
	print "Usage: python slice_cube.py [XSlice|YSlice]"
	exit()

for i in range(1,401):
	j = "%03d" % (i,)
	jpgfile = Image.open("frames/filename{}.jpg".format(j))
	images.append(jpgfile.copy())
	jpgfile.close()

for i in range(0,400):
	print 'Generating frame {}'.format(i)
	img = Image.new("RGB", (400,400), "Red")
	pixelsNew = img.load()
	for ix in range(img.size[0]):
		for iy in range(img.size[1]):
			if sys.argv[1] == 'XSlice':
				pixelsNew[ix,iy] = images[ix].getpixel((i, iy))
			else:
				pixelsNew[ix,iy] = images[ix].getpixel((iy, i))

	j = "%03d" % (i+1,)
	img.save("frames/out{}.jpg".format(j))
