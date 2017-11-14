#!/usr/bin/python

from PIL import Image
import os
import sys

if __name__ == "__main__":
    paths = sys.argv[1:]
    for img_path in paths:
        print img_path
        out_path = os.path.join('output', os.path.basename(img_path))
        img = Image.open(img_path)
        result = img.resize([500, 300], Image.BILINEAR)
        result.save(out_path)
