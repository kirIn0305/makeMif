# -*- coding: utf-8 -*-
from __future__ import print_function  #printを関数に変更
import imtools
from get_image import get_imageData

filelist = imtools.get_imlist('./', 'mif')
filename = "image{0:04d}.mif".format(len(filelist) + 1)

data = get_imageData("./image_Lena256.png")
width = 8
depth = len(data)

firstword = """ -- Copyright (C) 1991-2011 Altera Corporation
-- Your use of Altera Corporation's design tools, logic functions 
-- and other software and tools, and its AMPP partner logic 
-- functions, and any output files from any of the foregoing 
-- (including device programming or simulation files), and any 
-- associated documentation or information are expressly subject 
-- to the terms and conditions of the Altera Program License 
-- Subscription Agreement, Altera MegaCore Function License 
-- Agreement, or other applicable license agreement, including, 
-- without limitation, that your use is for the sole purpose of 
-- programming logic devices manufactured by Altera and sold by 
-- Altera or its authorized distributors.  Please refer to the 
-- applicable agreement for further details.

-- Quartus II generated Memory Initialization File (.mif)

WIDTH={0};
DEPTH={1};

ADDRESS_RADIX=UNS;
DATA_RADIX=UNS;

CONTENT BEGIN
""".format(width, depth)

with open(filename, 'w') as wf:

    wf.write(firstword)

    for number, line in enumerate(data):
            dataline = "{0}   :   {1};\n".format(number, line)
            wf.write(dataline)

    wf.write("END;")
