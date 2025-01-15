# motetkangxi.py
# (prototype)
# job   : creates kangxi chart objects
# git   : https://github.com/motetpaper/kangxi-mkchart
# lic   : MIT

from PIL import Image, ImageDraw, ImageFont

## colors
wht = (255,255,255)
blk = (0,0,0)

## dims for each grid item
bxdims = (125,275)

## font area
nmfont=ImageFont.truetype(f'./fonts/GentiumPlus-Bold.ttf',size=48)
hzfont=ImageFont.truetype(f'./fonts/ShipporiMincho-Bold.ttf',size=100)
pyfont=ImageFont.truetype(f'./fonts/GentiumPlus-Bold.ttf',size=36)

## header fonts
strksfont=ImageFont.truetype(f'./fonts/GentiumPlus-Bold.ttf',size=80)
unitsfont=ImageFont.truetype(f'./fonts/ShipporiMincho-Bold.ttf',size=100)

def test_box(num,hz,py):
	with Image.new('RGB',bxdims,wht) as img:
		d = ImageDraw.Draw(img)
		d.rectangle((0,0)+bxdims, fill=wht, outline=blk, width=4)
		d.text((10,8),str(num).rjust(3),fill=blk,font=nmfont)
		d.text((10,80),hz,fill=blk,font=hzfont)
		d.text((10,200),py.center(7),fill=blk,font=pyfont)
		return img

def test_hdr(strks, units):
	with Image.new('RGB',bxdims,blk) as img:
		d = ImageDraw.Draw(img)
		d.rectangle((0,0)+bxdims, fill=blk, outline=blk, width=4)
		d.text((10,20),str(strks).rjust(3),fill=wht,font=strksfont)
		d.text((10,120),str(units),fill=wht,font=unitsfont)
		return img

