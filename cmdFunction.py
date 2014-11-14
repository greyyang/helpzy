# -*- coding: utf-8 -*-
import IOexcel
import processJson

def doCMDFunction(excel, cmdNameListPath, cmdName,types, targetY, headerName = None, content = None, embedContent = None, mutexHeader = None, mutexContent = None):
	NAMEABB = processJson.getCMDName(cmdNameListPath)

	CMDTYPES = {
		"TMC": TMC,
		"ECC": ECC
	}

	print("Excute %s, it is a %s command"%(NAMEABB[cmdName], types))
	result = CMDTYPES[types](excel, headerName, content, embedContent, mutexHeader, mutexContent);
	return result

#计算:通过匹配文本计算数据(Total Match Count)
#传入参数:
#	excel: 			excel数据对象
#	headerName: 	需要搜寻匹配的列名
#	content: 		需要匹配的文件信息,可以传入多个以'|'符号分隔
#	preContent: 	字符串前匹配
#	backContent:	字符串后匹配
#返回值:
#	匹配到的总数
def TMC(excel, headerName, content, embedContent, mutexHeader, mutexContent):
	if not excel:
		print("TMC:Excel file object error!")
		return
	if not headerName or not content:
		print("TMC:Parameter error!");
		return

	headerList = headerName.split('$')
	headerYList = []
	for header in headerList:
		headerx, headery = excel.findValue(header)
		headerYList.append(headery)
	matchList = content.split('$')
	if not len(matchList) == len(headerYList):
		print("TMC: The length of headerName and content are not equality, please check the cmd json file!")
		return
	matchDic = {}

	for i in range(len(matchList)):
		matchDic[headerYList[i]] = matchList[i].split('|')
	return excel.countByCol(matchDic, startRow = headerx)

#计算:通过获取嵌入内容计算数据(Embed Content Count)
#传入参数:
#	excel: 			excel数据对象
#	headerName: 	需要搜寻匹配的列名
#	content: 		需要匹配的文件信息,可以传入多个以'|'符号分隔
#	preContent: 	字符串前匹配
#	backContent:	字符串后匹配
#返回值:
#	匹配到的总数
def ECC(excel, headerName, content, embedContent, mutexHeader, mutexContent):
	if not excel:
		print("ECC:Excel file object error!")
		return
	if not headerName or not embedContent:
		print("ECC:Parameter error!")
	headerx, headery = excel.findValue(headerName)
	embedList = excel.getEmbedCountByContent(headery, embedContent, startRow = headerx)
	print(embedList)

if __name__ == '__main__':
	excel = IOexcel.IOexcel(r"C:\code\pythonlearn\helpzy\data\江岸江大阳光通讯.xls");
	a = doCMDFunction(excel, r"configuration\cmdNames.json",r"kh","TMC", 5,"受理类型$备注","开户$")