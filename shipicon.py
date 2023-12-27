#!/usr/bin/env python3

from PIL import Image, ImageFont, ImageDraw
import argparse
import os

FONTFACE = 'Roboto-Medium.ttf'
FONTSIZE = 100
IMAGESIZE = 400, 400
ALLY_COLOR = 0, 255, 0
ENEMY_COLOR = 255, 69, 69
BACKGROUND_COLOR = 0, 0, 0, 0
VERTPATH = 'vertices/'
SCALE = 5.0

class shipicon:
    def __init__(self):
        self.classicon = {}
        for shipclass in ['submarine','destroyer',
                          'cruiser', 'battleship',
                          'aircarrier']:
            with open(f'{VERTPATH}{shipclass}.vertices', 'r') as vfile:
                verts = vfile.read().replace('\n', '')
                center, polygon = eval(verts)
                icon = {'center': center,
                        'polygon': polygon}
                self.classicon[shipclass] = icon
        self.fontface = ImageFont.truetype(FONTFACE, FONTSIZE)

    def render(self, size, shipclass, shipname, color, filename=None):
        base = Image.new('RGBA', size, color=BACKGROUND_COLOR)
        base = self.draw_classicon(size, base, shipclass, color)
        base = self.draw_shipname(size, base, shipname, color)
        if filename:
            base.save(filename)
        else:
            base.save(f'{shipname}.png')

    def draw_classicon(self, size, base, shipclass, color):
        draw = ImageDraw.Draw(base, 'RGBA')
        iwidth, iheight = size
        center = self.classicon[shipclass]['center']
        polygons = self.classicon[shipclass]['polygon']
        cy, cx = center
        for polygon in polygons:
            poly = [((x-cx)*SCALE+iwidth//2, (y-cy)*SCALE+iheight//2) for x,y in polygon]
            draw.polygon(poly, fill=color)
        return base

    def getbbox(self, string): # width, height
        left, top, right, bottom = self.fontface.getbbox(string)
        return right-left, bottom-top

    def draw_shipname(self, size, base, shipname, color):
        draw = ImageDraw.Draw(base)
        left, top, right, bottom = self.fontface.getbbox(shipname)
        iwidth, iheight = IMAGESIZE
        while self.getbbox(shipname)[0] > iwidth:
            shipname = shipname[:-1]
        while shipname and shipname[-1] == ' ':
            shipname = shipname[:-1]
        left, top, right, bottom = self.fontface.getbbox(shipname)
        width, height = right-left, bottom-top
        pos = (iwidth-width)//2, iheight-bottom
        draw.text(pos, shipname, font=self.fontface, fill=color)
        return base

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shiplist', type=str, required=True)
    parser.add_argument('--shipclass', type=str, required=True)
    parser.add_argument('--size', type=int, required=False)
    parser.add_argument('--dir', type=str, required=False)
    arg = parser.parse_args()
    filename = arg.shiplist
    shipclass = arg.shipclass
    if arg.size:
        size = arg.size, arg.size
    else:
        size = IMAGESIZE
    icongen = shipicon()
    with open(filename, 'r') as shipsfile:
        shiplist = shipsfile.read().split('\n')
        for side, color in [('enemy',ENEMY_COLOR), ('ally', ALLY_COLOR)]:
            if arg.dir:
                directory = f'{arg.dir}/{shipclass}/{side}'
            else:
                directory = f'icons/{shipclass}/{side}'
            try:
                os.makedirs(directory)
            except FileExistsError:
                pass
            icongen.render(
                size=size,
                shipclass=shipclass,
                shipname='',
                color=color,
                filename=f'{directory}/UNNAMED.png')
            print(f'{directory}/UNNAMED.png')
            for ship in shiplist:
                if ship:
                    icongen.render(
                        size=size,
                        shipclass=shipclass,
                        shipname=ship,
                        color=color,
                        filename=f'{directory}/{ship}.png')
                    print(f'{directory}/{ship}.png')

if __name__ == '__main__':
    main()
