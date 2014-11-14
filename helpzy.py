#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

# helpzy.py 运行步骤：
# 原方法：
# 1.下载表格 
# 2.把所有表的数据内容（不包含表头）合入一张
# 3.通过数据透析表获取有效数据
# 4.格式调整

import IOexcel
import processJson
import walkDir
import cmdFunction
import reportData
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s",
    filename="helpzy.log",
    filemode='w'
)

#定义一个StreamHandler，将DEBUG级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)-s]:%(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def procedure():
	logging.debug("Start")
	CONF = processJson.getConf()
	TARGETNAME = CONF["targetName"]
	TARGETPATH = CONF["targetPath"]
	cmdList = walkDir.getFileListByWalkDirectory(CONF["cmdPath"])		
	dataList = walkDir.getFileListByWalkDirectory(CONF["dataPath"])
	tamplatePath = walkDir.getFileListByWalkDirectory(CONF["tamplatePath"])

	for data in dataList:
		excel = IOexcel.IOexcel(data)
		shopName = excel.getShopName()

		for cmd in cmdList:
			cmdData = processJson.getCMD(cmd)
			strlist = cmd.split('\\')
			cmdName = strlist[-1].split('.')[0]
			result = cmdFunction.doCMDFunction(
				excel,
				CONF["cmdNameListPath"],
				cmdName, 
				cmdData["cmdType"], 
				cmdData["targetY"],
				cmdData["headerName"], 
				cmdData["content"],
				cmdData["embedContent"],
				cmdData["mutexHeader"],
				cmdData["mutexContent"]
			)
			excel.win32_writeToExcel(shopName, cmdData["targetY"], result)
			print("--------------")
		excel.closeExcel()
		print("=============")
	input("Prease <enter>")

if __name__ == '__main__':
	procedure()
