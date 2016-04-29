import PIL, sys
from PIL import Image

src = sys.argv[1]
target = src.split('.')
target.insert(-1,'thumb')
print src, target
target = '.'.join(target)
print src, target

basewidth = 300
img = Image.open(src)
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
img.save(target)

