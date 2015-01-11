#!/usr/bin/env python
#coding: utf8

import sys, os
import urllib2, urllib

def curr_dir():
    return sys.path[0]

def download(url, local_file_name):
    file_name = os.path.join(curr_dir(), local_file_name)
    urllib.urlretrieve(url, file_name)
    '''
    try:
        urllib.urlretrieve(url, file_name)
    except:
        print "Downloading error!!!"
    '''

if __name__ == '__main__':
    download("http://haijia.bjxueche.net/tools/CreateCode.ashx?key=ImgCode&random=0.7518748722504824", "temp.gif")
