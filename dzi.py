#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, deepzoom

# Specify your source image
SOURCE = sys.argv[1]
TARGET = ''.join(SOURCE.split('.')[:-1] + ['.dzi'])

# Create Deep Zoom Image creator with weird parameters
creator = deepzoom.ImageCreator(tile_size=128, tile_overlap=2, tile_format="png", image_quality=0.8, resize_filter="bicubic")

# Create Deep Zoom image pyramid from source
creator.create(SOURCE, TARGET)
