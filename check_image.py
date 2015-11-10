#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#

"check image"

import os
import time

def remove_common(list_a,list_b):
    new_list = list_b
    for x in list_a:
        if x in list_b:

            new_list.pop()

# check image in bundle path
def check_image():
    # property
    bundle_path = "/Users/luxi/Works/DIDI/iOS Project/ditravel/DICarpool/DICarpoolRes.bundle"
    tail_2x = "@2x.png"
    tail_3x = "@3x.png"
    # list
    list_all = os.listdir(bundle_path)
    list_2x_images = [x for x in list_all if cmp(x[-len(tail_2x):], tail_2x) == 0]
    list_3x_iamges = [x for x in list_all if cmp(x[-len(tail_3x):], tail_3x) == 0]
    list_images = []

    for x, y in zip(list_2x_images, list_3x_iamges):
        # get image name
        image_dict = {}
        image_2x_name = x[:(len(x) - len(tail_2x))]
        image_3x_name = y[:(len(y) - len(tail_3x))]




        # match image
        if cmp(image_2x_name, image_3x_name) == 0:
            image_dict['2x'] = x
            image_dict['3x'] = y
            list_images.append(image_dict)

    #print list_images

    #get the other file


#go
start_time = time.time()
check_image()
end_time = time.time() - start_time
print "================>>程序运行耗时:%0.8f秒" % end_time
