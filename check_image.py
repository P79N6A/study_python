#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#
"check image"

import os;
import time;
import json;

# 把list_a在list_b中去重，并返回最新的list_b
def remove_same_file(list_a,list_b):
    new_list = list_b
    for x in list_a:
        if x in list_b:
            new_list.pop(list_b.index(x))
    return new_list;

# 开始检查图片
def check_image_from_path(bundle_path):
    # property
    if len(bundle_path) == 0:
        bundle_path = "."

    if not os.path.isdir(bundle_path):
        print "改路径不是一个文件夹，请检查 :("; return;

    tail_2x, tail_3x = "@2x.png", "@3x.png"
    list_all = os.listdir(bundle_path)
    list_img_ext = ['bmp','jpeg','gif','psd','png','jpg']
    list_2x_images, list_3x_images, list_images, list_dir, list_other = [], [], [], [], []

    for x in list_all:
        if cmp(x[-len(tail_2x):], tail_2x) == 0:
            for y in list_all:
                if cmp(y[-len(tail_3x):], tail_3x) == 0 and \
                   cmp(x[:(len(x) - len(tail_2x))], y[:(len(y) - len(tail_3x))]) == 0 :
                    list_2x_images.append(x)
                    list_3x_images.append(y)

    list_strange = remove_same_file(list_3x_images[:],
                                    remove_same_file(list_2x_images[:], list_all[:]));

    for x in list_strange[:]:
        file_path = os.path.join(bundle_path, x)
        if os.path.isdir(file_path):
            list_dir.append(x)
            list_strange.pop(list_strange.index(x))
        elif os.path.isfile(file_path) and not x.split(".")[-1] in list_img_ext:
            list_other.append(x)
            list_strange.pop(list_strange.index(x))

    # ending
    print "共检查文件%s个" % len(list_all)
    print "其中包含%s个文件夹" % len(list_dir) + "=>", json.dumps(list_dir, indent=1)
    print "其他类型的文件:", json.dumps(list_other, indent=1)
    print "和可能异常的%s个图片=>" % len(list_strange), json.dumps(list_strange, indent=1)

    return


#go
print "\n" + "=" * 20 + "检查完成" + "=" * 20

start_time = time.time()
check_image_from_path("/Users/luxi/Works/DIDI/iOS Project/ditravel/DICarpool/DICarpoolRes.bundle")
end_time = time.time() - start_time

print "-", ">", "程序运行耗时:%0.8f秒" % end_time
print "=" * 20 + "have fun" + "=" * 20
