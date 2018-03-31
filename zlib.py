# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:42:06 2018

@author: Administrator
"""

import zlib


string =  b"""   Lorem ipsum dolor sit amet, consectetur

                adipiscing elit. Nunc ut elit id mi ultricies

                adipiscing. Nulla facilisi. Praesent pulvinar,

                sapien vel feugiat vestibulum, nulla dui pretium orci,

                non ultricies elit lacus quis ante. Lorem ipsum dolor

                sit amet, consectetur adipiscing elit. Aliquam

                pretium ullamcorper urna quis iaculis. Etiam ac massa

                sed turpis tempor luctus. Curabitur sed nibh eu elit

                mollis congue. Praesent ipsum diam, consectetur vitae

                ornare a, aliquam a nunc. In id magna pellentesque

                tellus posuere adipiscing. Sed non mi metus, at lacinia

                augue. Sed magna nisi, ornare in mollis in, mollis

                sed nunc. Etiam at justo in leo congue mollis.

                Nullam in neque eget metus hendrerit scelerisque

                eu non enim. Ut malesuada lacus eu nulla bibendum

                id euismod urna sodales. """

 
print("Original Size: {0}".format(len(string)))

compressed = zlib.compress(string)
print("Compressed Size: {0}".format(len(compressed)))

decompressed = zlib.decompress(compressed)
print("Decompressed Size: {0}".format(len(decompressed)))