# -*- coding:utf-8 -*-
import os
import os.path

def getFileListByWalkDirectory(path):
	filelist = []
	for parent, dirnames, filenames in os.walk(path):
#		for dirname in dirnames:
#			print("parent is:" +  parent)
#			print("dirname is:" + dirname)
		for filename in filenames:
			filelist.append(path + "\\" + filename)
	return filelist

if __name__ == "__main__":
	for a in getFileListByWalkDirectory("data"):
		a = (a.split('\\')[-1]).split('.')[0]
		print(a)
