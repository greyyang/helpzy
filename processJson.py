# -*- coding:utf-8 -*-
import json

CONF_PATH = "conf.json"

def _getJsonData(path):
	fdata = open(path,'r',encoding='utf-8')
	jsonstr = ''
	for line in fdata:
		line = line.strip();
		if not line[:2] == r"//":
			jsonstr += line
	return json.loads(jsonstr)

def getConf():
	return _getJsonData(CONF_PATH)

def getCMD(path):
	return _getJsonData(path)

def getCMDName(path):
	return _getJsonData(path)

if __name__ == '__main__':
	print(getCMDName("configuration/cmdNames.json"))