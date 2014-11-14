# HelpZY 使用指南
------------
You can just read [Quick Start](#quickstart).

-----------
##1.获取源码
项目源代码托管在Github上.请从链接 **[HelpZY](https://github.com/greyyang/helpzy)** 下载.
也可以通过Git下载分支: **git@github.com:greyyang/helpzy.git**

-----------

##2.安装
项目运行所需要的文件在项目中的required文件夹内
>* python-3.4.2.msi
>* pywin32-219.win32-py3.4.exe
>* xlrd-0.9.3

请依次进行如下安装
### (1)python-3.4.2.msi
请执行默认安装
### (2)pywin32-219.win32-py3.4.exe
请执行默认安装
### (3)xlrd-0.9.3
请将**xlrd-0.9.3\xlrd**文件夹拷贝到python安装路径下(默认是C:\Python34)的**Lib\site-packages**文件夹下.

----------
##3.配置
项目的可配置文件如下:
>* conf.json 文件
>* cmd文件夹中的命令文件
>* configuration\cmdNames.json 文件

###(1)conf.json文件
```json
{
    "cmdPath": "cmd", 
    "dataPath": "data", 
    "targetPath": "target",
    "targetName": "report",
    "tamplatePath":"tamplate\\ReportTamplate.xlsx",
    "cmdNameListPath":"configuration\\cmdNames.json"
}
```
>* *cmdPath:*          配置存放命令文件的**文件夹路径** (默认为cmd\\*)
>* *dataPath:*         配置存放源数据的**文件夹路径** (默认为data\\*)
>* *targetPath:*       配置存放到处报表文件的**文件夹路径** (默认为target文件夹下)
>* *tamplatePath:*     配置报表模板存放的**文件路径** (默认为tamplate\\ReportTamplate.xlsx)
>* *cmdNameListPath:*  配置存放命令名和文件名的映射关系的**文件路径**(默认为configuration\\cmdNames.json)

###(2)cmd目录下的命令文件
```json
//(示例) MIFI统计操作
{
  "cmdType": "TMC",
  "headerName": "备注",
  "content": "批次:武汉高校MIFI活动, 档次:预存300送MIFI|批次:武汉高校MIFI活动, 档次:预存180送MIFI",
  "embedContent":"",
  "mutexHeader":"",
  "mutexContent":"",
  "targetY": "Y"
}
```
#### **cmdType:**
该配置用于指定该文件用于执行何种命令.
现有的命令选择有:TMC(Total Match Count)和ECC(Embed Content Count)
*TMC* : 通过完全匹配文本计算总数.例如匹配受理类型一栏中出现了多少次"补卡".
*ECC* : 通过获取嵌入内容计算数据.例如通过"批次:积分兑换通用电子券（常态化）, 档次:100积分兑换1.5元通用电子券"把文本中的100数字或1.5数字取出进行计算.(暂时废弃)
#### **headerName**:
需要统计的表头名字,例如"备注".
#### **content**:
需要匹配的字符串.
#### **embedContent**:
暂时废弃
#### **mutexHeader**:
暂时废弃
#### **metexContent**:
暂时废弃
#### **targetY**:
需要在模板表中写入列位置,例如"Y"列

--------------
##4.<div name="quickstart">使用</div>


