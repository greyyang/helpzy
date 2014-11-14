# -*- coding: utf-8 -*-
import xlrd
import processJson
import os.path
import easyExcel
import logging

class IOexcel():
	"""this is a class to package the functions for handle the excel files"""
	def __init__(self, path, pageNumb = 0):
		super(IOexcel, self).__init__()
		self.path = path
		self.data = None
		self.pageNumb = pageNumb
		self.table = None
		self._openxls();
		self._openSheet();
		self.nrows = self.table.nrows
		self.ncols = self.table.ncols
		CONF = processJson.getConf()
		self.tamplatePath = CONF["tamplatePath"]
		self.xls = self._openExcelForWrite(self.tamplatePath)
	# 功能：    打开一个Excel文件
	# 传入参数：无
	# 返回值：  无 
	def _openxls(self):
		print("Open file %s now"%(self.path))
		logging.debug("Open file %s now"%(self.path))
		self.data = xlrd.open_workbook(self.path, 'r', encoding_override="cp1252")

	# 功能:     通过索引顺序获取一个工作表
	# 传入参数: 无
	# 返回值:   无 
	def _openSheet(self, pageNumb = 0):
		self.pageNumb = pageNumb
		self.table = self.data.sheet_by_index(pageNumb)

	# 功能:     通过坐标获取一个单元格的值
	# 传入参数: 无
	# 返回值:   无 
	def getDataByXY(self, row, col):
		return self.table.cell(row, col).value;

	# 功能:通过列名获取到列数据的启示坐标位置
	# 传入参数:
	# 	表头名称
	# 返回值:坐标位置(X,Y)
	def findValue(self, value):
		print("Now find value %s ......"%(value))
		for i in range(self.nrows):
			for j in range(self.ncols):
				# print(self.getDataByXY(i, j),":::",i,j)
				if value == self.getDataByXY(i, j):
					print("Find value's XY:" + str(i) + "," + str(j))
					return i, j
		print("Can not find value \"%s\", please check the configuration file."%(value))

	def countByCol(self, matchDic, startRow = 0, endRow = -1):
		if -1 == endRow:
			endRow = self.nrows
		print("countByCol:Now count match number...")
		count = 0
		for row in range(startRow, endRow):
			flag = True
			for (k, v) in matchDic.items():
				if not self.getDataByXY(row, k).strip() in v:
					flag = False
			if flag:
				count += 1
		print("Count result is %d"%(count))
		return count

	def getEmbedCountByContent(self, col, econtent, startRow = 0, endRow = -1):
		if -1 == endRow:
			endRow = self.nrows
		print("getEmbedCountByContent:Now count \"%s\" in column %d from %s row to %s row"%(econtent, col, startRow, endRow))
		print(econtent.find(r'%xxx%'))
		temp = econtent.split(r'%xxx%')
		for row in range(startRow, endRow):
			value = self.getDataByXY(row, col).strip()
			if value.find(temp[0]) >= 0 and value.find(temp[1]) >= 0:
				# print(value)
				# print(temp[0])
				# print(value.split(temp[0]))
				# print(value.split(temp[0])[1].split(temp[1])[0])
				embedCount += int(value.split(temp[0])[1].split(temp[1])[0])
		return embedCount

	#  通过受理单位获得店铺名称
	def getShopName(self):
		headerx, headery = self.findValue("受理单位")
		name = self.getDataByXY(headerx + 1, headery)
		index = name.find("店")
		if not -1 == index:
			name = name[:index + 1]
		index = name.find("（")
		if not -1 == index:
			name = name[:index]
		index = name.find("(")
		if not -1 ==index:
			name = name[:index]
		print("getShopName: get shop name is %s"%(name))
		return name

	def _openExcelForWrite(self, targetPath):
		absTargetPath = os.path.abspath(targetPath)
		return easyExcel.easyExcel(absTargetPath)
		
	def win32_findShopName(self, shopName, sheet = 1):
		countRow, countCol = self.xls.countRowsAndCols()
		for col in range(countCol):
			for row in range(countRow):
				value = self.xls.getCell(sheet, row + 1, col + 1)
				if value:
					if isinstance(value, str):
						if shopName == value.strip():
							print("win32_findShopName: Find shop name at %d, %d" % (row, col))
							return row, col
		print("win32_findShopName: Can not find shop name %s! Please Check!"%(shopName))
		return -1, -1

	def win32_writeToExcel(self, shopName, targetY, value, sheet = 1):
		shopX, shopY = self.win32_findShopName(shopName)
		# 程序正常运行时应当把此判断开启以规避问题,调试时注释
		if -1 == shopX and -1 == shopY:
			print("win32_writeToExcel error: Can not find shop %s! Please check!"%(shopName))

			return
		targetY = ord(targetY) - 64
		print("put %d in Cell(%d, %d)..."%(value, shopX +1, targetY))
		self.xls.setCell(sheet, shopX + 1, targetY, value)
		return

	def closeExcel(self):
		self.xls.save()
		self.xls.close()
		return

if __name__ == '__main__':
	excel = IOexcel(r"C:\code\pythonlearn\helpzy\data\陈胜军-4星-江岸区欣佳瑞通讯指定专营店.xls");
	# excel.countByCol(4,*["补卡", "备卡购买"])
	excel.win32_findShopName("江岸全福指定专营店")