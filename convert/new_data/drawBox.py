#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from PIL import Image, ImageDraw

def ReadTag(tag_file):
  with open(tag_file, 'r') as f:
    data = f.read()
  return eval(data)

def ListInput(input_dir):
  gstring = os.path.join(input_dir, '*.*')
  return glob.glob(gstring)

def DrawBox(draw, box):
  PALETTE = {'human': 'red', 'helmet': 'blue'}
  color = PALETTE[box['class']]

  width, height = draw.im.size
  xmin = width * box['xmin']
  ymin = height * box['ymin']
  xmax = width * box['xmax'] 
  ymax = height * box['ymax']
  
  print(xmin, ymin, xmax, ymax, color)
  draw.line([
    xmin, ymin, 
    xmin, ymax, 
    xmax, ymax, 
    xmax, ymin,
    xmin, ymin],
    color, 10)
  
  return

def DrawBoxes(image, boxes):
  image_data = Image.open(image)
  draw = ImageDraw.Draw(image_data)

  for box in boxes:
    DrawBox(draw, box)
  
  return image_data

def ConvertFiles(input_dir, output_dir, tag_file):
  tag_data = ReadTag(tag_file)
  
  for image in tag_data:
    boxes = tag_data[image]['boxes']
    image_data = DrawBoxes(
        os.path.join(input_dir, image), 
        boxes)
    image_data.save(os.path.join(output_dir, image))

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description = 
      'Draw boxes for images in a directory')

  parser.add_argument('input_dir', help='input directory')
  parser.add_argument('output_dir', help='output directory')
  parser.add_argument('tag', help='tag file')
  args = parser.parse_args()
  
  ConvertFiles(args.input_dir, args.output_dir, args.tag)
