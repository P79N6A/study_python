#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#
"check image"

import os;
import time;
import json;

def check_image_from_path(bundle_path):

    if len(bundle_path) == 0 or cmp(bundle_path, '.') == 0:
        bundle_path = os.path.join(".")

    if not os.path.isdir(bundle_path):
        print "Error:\n%s, 该路径不是一个文件夹，请检查 :(" % bundle_path;
        return;

    tail_2x, tail_3x = "@2x.png", "@3x.png"
    list_all = os.listdir(bundle_path)
    list_img_ext = ['bmp','jpeg','gif','psd','png','jpg']
    list_images, list_dir, list_other = [], [], [];

    # 应该还可以优化
    for x in list_all:
        if cmp(x[-len(tail_2x):], tail_2x) == 0:
            for y in list_all:
                if cmp(y[-len(tail_3x):], tail_3x) == 0 and \
                   cmp(x[:(len(x) - len(tail_2x))],
                       y[:(len(y) - len(tail_3x))]) == 0 :
                    list_images.append(x)
                    list_images.append(y)

    list_strange = list(set(list_all) - set(list_images))

    for x in list_strange[:]:
        file_path = os.path.join(bundle_path, x)
        if os.path.isdir(file_path):
            list_dir.append(x)
            list_strange.pop(list_strange.index(x))
        elif os.path.isfile(file_path) and not x.split(".")[-1] in list_img_ext:
            list_other.append(x)
            list_strange.pop(list_strange.index(x))

    # ending
    print "1.检查路径:%s" % bundle_path
    print "2.共检查文件%s个" % len(list_all)
    print "3.其中包含%s个文件夹" % len(list_dir) + "=>", json.dumps(list_dir, indent=1)
    print "4.其他类型的文件:", json.dumps(list_other, indent=1)
    print "5.可能异常的%s个图片=>" % len(list_strange), json.dumps(list_strange, indent=1)

    return

if __name__ == '__main__':
    print "\n" + "=" * 20 + "检查完成" + "=" * 20
    start_time = time.time()
    input_path = raw_input("请输入检查目录:\n")
    # input_path = '/Users/Risy/Works/DDI/iOS Project/ditravel/DICarpool/DICarpoolRes.bundle'
    check_image_from_path(input_path)
    end_time = time.time() - start_time

    print "\n->", "程序运行耗时:%0.8f秒" % end_time
    print "=" * 20 + "have fun" + "=" * 20

    raw_input('\nPress Enter to exit')
