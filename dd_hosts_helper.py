#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#

import os
import json

def format_log(x):
    print json.dumps(x,indent=1)

#-r(1) -u(2)
def main():
    hosts_list = [{'10.10.65.14'    : 'git@xiaojukeji.com'},
                  {'10.10.65.8'     : 'wiki.intra.xiaojukeji.com'},
                  {'10.10.65.3'     : 'jenkins.intra.xiaojukeji.com'},
                  {'10.242.150.229' : 'jenkins.xiaojukeji.com'}]

    etc_hosts_file_path = "/etc/hosts"
    etc_config_header = '#==>xiaojukeji_etc_config_header'
    etc_config_footer = '#==>xiaojukeji_etc_config_footer'

    if not os.access(etc_hosts_file_path, os.W_OK):
        print '\nerror : 没有获得文件修改权限，请使用sudo命令执行\n   => : sudo python dd_hosts_helper.py\n'
    else:
        with open(etc_hosts_file_path, 'r+') as f:
            for d in hosts_list[:]:
                s = '\n' + d.keys()[0] + " " + d.values()[0]
                hosts_list[hosts_list.index(d)] = s

            #print "=" * 10 + "开始处理hosts文件：\b %s" % f.read() + '\n'
            list_originHosts = f.read().split('\n')
            format_log(list_originHosts)
            # print json.dumps(arr, indent=1)
            change_mode = 1
            if change_mode == 1:
                list_curHost = list(set(list_originHosts) ^ set(hosts_list))
            elif change_mode == 2:
                list_curHost = list(set(list_originHosts) - set(hosts_list))
            else:

            # f.write('\n' + etc_config_header)
            # f.write('\n' + etc_config_footer)

if __name__ == '__main__':
    main()
