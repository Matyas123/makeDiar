from PIL import Image, ImageEnhance
import argparse
import os
import re

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', help='input directory containing images, jpegs',
						required=True)
	parser.add_argument('-r', help='height to weight ratio, default is 220/343',
						default=float(220) / 343)
	args = parser.parse_args()
	return args.d, args.r

def extension(s):
    ext = re.findall('\.([0-9a-zA-Z]+)',s)
    if len(ext)> 0:
        return re.findall('\.([0-9a-zA-Z]+)',s)[0]
    else:
        return None

def cut_image(im):
    width, height = im.size
    #nalezeni velikosti cutu
    if float(height)/width > RATIO:
        height_cut = width*(RATIO)
        width_cut = width
    else:
        height_cut = height
        width_cut = height*(1/RATIO)
    if height == height_cut:
        top = 0
        bottom = height
        left = int((width-width_cut)/2)
        right = int(left+width_cut)
    else:
        top = int((height-height_cut)/2)
        bottom = int(top+height_cut)
        left = 0
        right = width
    im_crop = im.crop((left,top,right,bottom))
    #im_crop.show()
    return im_crop


if __name__ == "__main__":
	path, ratio = get_arguments()
	print(path)
	print(ratio)

	ext = ['jpg','jpeg','JPG']
	files = os.listdir(path)

"""
	if not os.path.exists(path + 'upravene'):
	    os.makedirs(path + 'upravene')

	if not os.path.exists(path + 'upravene\\bw_to_edit'):
	    os.makedirs(path + 'upravene\\bw_to_edit')

	i = 0
	for item in files:
	    im_ext = extension(item)
	    if im_ext in ext :
	        im = Image.open(path + item)
	        #orizni
	        im_crop = cut_image(im)
	        im_name = (3-len(str(i)))*'0'+str(i)
	        im_crop.save(path + 'upravene\\' + im_name + '.jpg', 'JPEG', quality=90)
	        im_crop_bw = im_crop.convert('L')

	        im_crop_bw.save(path + 'upravene\\bw_to_edit\\bw_' + im_name + '.jpg', 'JPEG', quality=90)


       i += 1
"""
