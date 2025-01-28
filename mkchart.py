#!/usr/bin/env python3

# mkchart.py
# (prototype)
# job   : creates a PDF kangxi chart using a JSON kangxi chart
# git   : https://github.com/motetpaper/kangxi-mkchart
# lic   : MIT

from PIL import Image, ImageDraw, ImageFont
from motetkangxi import *
import json
import yaml

with open('chart.yaml') as f:
    prefs = yaml.safe_load(f)

print(prefs)

slug = prefs['chart']['slug']


with open('kangxi.json') as f:
    data = json.loads(f.read().strip())

outfilepdf = f'out/{slug}.pdf'
outfilepng = f'out/{slug}.png'
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
                item = data[i]

                ## two parallel lists
                k = list(item.keys())
                v = list(item.values())

                if 'header' in k:
                    g = test_hdr(str(v[0]), v[1])
                elif 'radical' in k:
                    g = test_box(str(v[0]), v[1], v[3])

                coords = (x,y)
                g.copy()
                im.paste(g,(x,y))
                i=i+1

    print(coords)
    xy = (coords[0]+bx+dx,coords[1],xf-bx-500+dx+dx,coords[1]+by)
    d.rectangle(xy,fill=(255,255,255),outline=(0,0,0),width=4)

    bnfont=ImageFont.truetype(f'./fonts/{chartPinyinFont}',size=85)
    btfont=ImageFont.truetype(f'./fonts/{chartPinyinFont}',size=50)
    bufont=ImageFont.truetype(f'./fonts/{chartPinyinFont}',size=36)

    brand_name = prefs['chart']['branding']['title']
    brand_tagline = prefs['chart']['branding']['tagline']
    brand_url = prefs['chart']['branding']['learnmore']
    d.text((xy[0]+dx,xy[1]),brand_name,fill=blk,font=bnfont)
    d.text((xy[0]+dx,xy[1]+dx+100),brand_tagline,fill=blk,font=btfont)
    d.text((xy[0]+dx,xy[1]+dx+175),brand_url,fill=blk,font=bufont)
    im.save(outfilepdf)
    im.save(outfilepng)
