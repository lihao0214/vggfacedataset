#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-04 13:48:10
# @Author  : Raymond Wong (549425036@qq.com)
# @Link    : github/Raymond-Wong

import os
import sys

def getImgsName(path):
  for root, dirs, files in os.walk(path):
    return set(files)

if __name__ == '__main__':
  inPath = sys.argv[1]
  outPath = sys.argv[2]
  resPath = sys.argv[3]
  fileNames = []
  for root, dirs, files in os.walk(inPath):
    for fn in files:
      f = open(os.path.join(inPath, fn), 'r')
      imgsName = getImgsName(os.path.join(outPath, fn.replace('.txt', '')))
      line = f.readline()
      toWriteLines = []
      while line:
        pid = line.split()[1] + '.jpg'
        if pid not in imgsName:
          toWriteLines.append(line)
        line = f.readline()
      f.close()
      f = open(os.path.join(resPath, fn), 'w')
      for line in toWriteLines:
        f.write(line)
      f.close()


