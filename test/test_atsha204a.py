#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-06-15 17:32:24
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os,sys
import hashlib

#获取脚本路径
def cur_file_dir():
    pathx = sys.argv[0]
    tmppath,_file = os.path.split(pathx)
    if cmp(tmppath,'') == 0:
        tmppath = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(tmppath):
        return tmppath
    elif os.path.isfile(tmppath):
        return os.path.dirname(tmppath)

#获取父目录
def GetParentPath(strPath):
    if not strPath:
        return None;
    lsPath = os.path.split(strPath);
    if lsPath[1]:
        return lsPath[0];
    lsPath = os.path.split(lsPath[0]);
    return lsPath[0];

def getHash_SHA256(pstr):
    outstr = hashlib.sha256(pstr).hexdigest()
    print(outstr)

def getParentsPath(pth,count):
    tmppth = pth
    for i in range(count):
        tmppth = GetParentPath(tmppth)
    return tmppth



def getKeyPth():
    keyfilePth = 'code/key/hashkey.txt'
    pth = cur_file_dir()
    print(pth)
    pth = getParentsPath(pth,3)
    pth = pth + os.sep + keyfilePth
    return pth

def getKeyFromKeyPth(keypth):
    f = open(keypth,'r')
    dat = f.readlines()
    f.close()
    keysource = ''
    key1 = ''
    keytmp = ''
    for i,v in enumerate(dat):
        if i == 0:
            keysource = v.replace('\n','').replace('\t','').replace('\r','').replace(' ','')
            key1 = getHash_SHA256(keysource)
        elif i ==1:
            keytmp = v.replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    if key1 == keytmp:
        return keytmp
    else:
        print('erro')
        return None
#测试
if __name__ == '__main__':
    # args = sys.argv
    # fpth = ''
    # if len(args) == 2 :
    #     if os.path.exists(args[1]):
    #         fpth = args[1]
    #     else:
    #         print("请加上要转码的文件路径")
    # else:
    #     print("请加上要转码的文件路径")
    pth = getKeyPth()
    print(pth)
    key = getKeyFromKeyPth(pth)
    print(key)


    # f = open(name)
    # getHash_SHA256('input key in hear')
    
