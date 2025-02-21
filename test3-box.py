# test3-box.py
# (prototype)
# job   : testing header position with box items
# job   : testing motetkangxi box function
# git   : https://github.com/motetpaper/kangxi-mkchart
# lic   : MIT

from PIL import Image, ImageDraw, ImageFont
from motetkangxi import *
import json

with open('kangxi.json') as f:
    data = json.loads(f.read().strip())

outfilepdf = 'tests/test-kangxi-chart-boxes.pdf'
dpi = 300

# in inches
size = (17,11)
margin = 1

# in pixels
w = size[0] * dpi
h = size[1] * dpi
bx = bxdims[0]
by = bxdims[1]
dx = 20
dy = 20

# margins, offsets, initials and finals
xi = 250
yi = 250
xf = w - xi
yf = h - yi
yoffset = 100
xoffset = bx

coords = (0,0) # keeps last coordinates

with Image.new('RGB',(w,h),wht) as im:
    d = ImageDraw.Draw(im)
    i = 0
    for y in range(yi+yoffset,yf,by+dy):
        for x in range(xi+xoffset,xf-bx-500,bx+dx):
            if(i < len(data)):
                g = test_box('214', '龠', 'yuè')
                coords = (x,y)
                g.copy()
                im.paste(g,(x,y))
                i=i+1

    print(coords)
    xy = (coords[0]+bx+dx,coords[1],xf-bx-500+dx+dx,coords[1]+by)
    d.rectangle(xy,fill=(204,204,204),outline=(204,204,204),width=4)
    im.save(outfilepdf)
