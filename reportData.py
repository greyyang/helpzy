# -*- coding:utf-8 -*-

class reportData():
	"""最终报表的数据封装"""
	def __init__(self, name, *shopDataList):
		super(reportData, self).__init__()
		self.name = name
		self.shopDataList = shopDataList

class shopData():
	"""营业厅的数据封装"""
	def __init__(
		self, 
		shopname = '',
		bkhbk = -1,
		cptj = -1,
		jfq5 = -1,
		jfq10 = -1,
		jfq20 = -1,
		jfq50 = -1,
		jfq100 = -1,
		jfq200 = -1,
		jfq500 = -1,
		jff100 = -1,
		jff200 = -1,
		jff500 = -1,
		jff1000 = -1,
		jff2000 = -1,
		jff5000 = -1,
		jff10000 = -1,
		jff20000 = -1,
		kh = -1,
		sj = -1,
		mifi = -1
		):
		super(shopData, self).__init__()
		self.shopname = shopname
		self.bkhbk = bkhbk
		self.cptj = cptj
		self.jfq5 = jfq5
		self.jfq10 = jfq10
		self.jfq20 = jfq20
		self.jfq50 = jfq50
		self.jfq100 = jfq100
		self.jfq200 = jfq200
		self.jfq500 = jfq500
		self.jff100 = jff100
		self.jff200 = jff200
		self.jff500 = jff500
		self.jff1000 = jff1000 
		self.jff2000 = jff2000 
		self.jff5000 = jff5000 
		self.jff10000 = jff10000
		self.jff20000 = jff20000
		self.kh = kh
		self.sj = sj
		self.mifi = mifi
	

if __name__ == '__main__':
	pass
