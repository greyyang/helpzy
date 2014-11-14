import os.path
from win32com.client import Dispatch  
import win32com.client  
class easyExcel:  
      """A utility to make it easier to get at Excel.    Remembering 
      to save the data is your problem, as is    error handling. 
      Operates on one workbook at a time."""  
      def __init__(self, filename=None):  #打开文件或者新建文件（如果不存在的话）
          self.xlApp = win32com.client.Dispatch('Excel.Application')  
          if filename:  
              self.filename = filename  
              self.xlBook = self.xlApp.Workbooks.Open(filename)  
          else:  
              self.xlBook = self.xlApp.Workbooks.Add()  
              self.filename = ''
      
      def save(self, newfilename=None):  #保存文件
          if newfilename:  
              self.filename = newfilename  
              self.xlBook.SaveAs(newfilename)  
          else:  
              self.xlBook.Save()      
      def close(self):  #关闭文件
          self.xlBook.Close(SaveChanges=0)  
          del self.xlApp  
      def getCell(self, sheet, row, col):  #获取单元格的数据
          "Get value of one cell"  
          sht = self.xlBook.Worksheets(sheet)  
          return sht.Cells(row, col).Value  
      def setCell(self, sheet, row, col, value):  #设置单元格的数据
          "set value of one cell"  
          sht = self.xlBook.Worksheets(sheet)
          sht.Cells(row, col).Value = value  
      def getRange(self, sheet, row1, col1, row2, col2):  #获得一块区域的数据，返回为一个二维元组
          "return a 2d array (i.e. tuple of tuples)"  
          sht = self.xlBook.Worksheets(sheet)  
          return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value  
      def addPicture(self, sheet, pictureName, Left, Top, Width, Height):  #插入图片
          "Insert a picture in sheet"  
          sht = self.xlBook.Worksheets(sheet)  
          sht.Shapes.AddPicture(pictureName, 1, 1, Left, Top, Width, Height)  
      
      def countRowsAndCols(self, sheet = 1):
          sht = self.xlBook.Worksheets(sheet)  
          return sht.UsedRange.Rows.Count, sht.UsedRange.Columns.Count
          
      def cpSheet(self, before):  #复制工作表
          "copy sheet"  
          shts = self.xlBook.Worksheets  
          shts(1).Copy(None,shts(1)) 

if __name__ == "__main__":
  xlsPath = r"tamplate\123.xlsx"
  xabsPath = os.path.abspath(xlsPath)
  print(xabsPath)
  xls = easyExcel(xabsPath)
  print(xls.getCell(1, 5, 5))
  # print(xls.countRowsAndCols())
  xls.save()  
  xls.close()  