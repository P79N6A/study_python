#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#
"check image"

import os;
import time;
import json;

def remove_common(list_a,list_b):
    new_list = list_b
    for x in list_a:
        if x in list_b:
            new_list.pop(list_b.index(x))
    return new_list;

# check image in bundle path
def check_image():
    # property
    bundle_path = "/Users/luxi/Works/DIDI/iOS Project/ditravel/DICarpool/DICarpoolRes.bundle"
    tail_2x = "@2x.png"
    tail_3x = "@3x.png"
    # list
    list_all = os.listdir(bundle_path)
    list_2x_images = [x for x in list_all if cmp(x[-len(tail_2x):], tail_2x) == 0]
    list_3x_images = [x for x in list_all if cmp(x[-len(tail_3x):], tail_3x) == 0]
    list_images = []

    for x, y in zip(list_2x_images, list_3x_images):
        # get image name
        image_dict = {}
        image_2x_name = x[:(len(x) - len(tail_2x))]
        image_3x_name = y[:(len(y) - len(tail_3x))]

        # match image
        if cmp(image_2x_name, image_3x_name) == 0:
            image_dict['2x'] = x
            image_dict['3x'] = y
            list_images.append(image_dict);

    # 检查其他文件
    list_strange = remove_common(list_3x_images[:], remove_common(list_2x_images[:], list_all[:]));

    print "文件总共有%s个" % len(list_all)
    print "异常文件有=>", json.dumps(list_strange,indent=1)

#go
print "\n" + "=" * 20 + "检查完成" + "=" * 20
start_time = time.time()
check_image()
end_time = time.time() - start_time
print "-"*5, ">", "程序运行耗时:%0.8f秒" % end_time
print "=" * 20 + "have fun" + "=" * 20
