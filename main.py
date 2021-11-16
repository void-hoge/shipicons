#!/usr/local/bin/python3
from PIL import Image, ImageFont, ImageDraw
import sys

img_size = (400,400)
icon_size = 175
center = tuple([i//2 for i in img_size])
friend = (0,255,0)
enemy = (255, 69, 69)
base_color = (0,0,0,0)
CV = "0"
BB = "1"
CA = "2"
DD = "3"

def add_classicon(base, shipclass, color, fontsize):
	base = base.rotate(-90)
	fontpath = "./WoWsSymbol.ttf"
	font = ImageFont.truetype(fontpath, fontsize)
	draw = ImageDraw.Draw(base)
	size = draw.textsize(shipclass, font=font)
	pos = tuple([(a-b)/2 for a, b in zip(img_size, size)])
	draw.text(pos, shipclass, font=font, fill=color)
	base = base.rotate(90)
	return base

def add_shipname(base, name, color, fontsize):
	font = ImageFont.truetype("Roboto-Medium.ttf", fontsize)
	draw = ImageDraw.Draw(base)
	while draw.textsize(name, font=font)[0]>img_size[0]:
		name = name[:-1]
	size = draw.textsize(name, font=font)
	pos = tuple([(a-b)/2 for a, b in zip(img_size, size)])
	pos = (pos[0],pos[1]+125)
	draw.text(pos, name, font=font, fill=color)
	return base

argv = sys.argv
if (argv[1] == "CV") or argv[1] == "cv":
	shipclass = CV
elif (argv[1] == "BB") or (argv[1] == "bb"):
	shipclass = BB
elif (argv[1] == "CA") or (argv[1] == "CL") or (argv[1] == "ca") or (argv[1] == "cl"):
	shipclass = CA
elif (argv[1] == "DD") or (argv[1] == "dd"):
	shipclass = DD
else:
	raise Exception("invalid class name. (CV|BB|CA|CL|DD|cv|bb|ca|cl|dd)")

if (argv[2] == "enemy"):
	color = enemy
elif (argv[2] == "friend"):
	color = friend

name = argv[3]

base = Image.new("RGBA", img_size, color=base_color)
base = add_classicon(base, shipclass, color, icon_size)
base = add_shipname(base, name, color, 75)

filename = argv[4]+name+".png"

base.save(filename)
