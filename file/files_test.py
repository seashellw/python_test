import os
import shutil
import re


# 移动文件
class move:
	# 老目录
	PathOld = r""
	# 新目录
	PathNew = r""
	
	# 构造函数
	def __init__(self, pathold, pathnew):
		self.PathOld = str(pathold).strip().rstrip("\\")
		self.PathNew = str(pathnew).strip().rstrip("\\")
		if (not os.path.exists(self.PathOld)):
			os.makedirs(self.PathOld)
			print("原始目录不存在，已经创建一个新的原始目录")
		if (not os.path.exists(self.PathNew)):
			os.makedirs(self.PathNew)
			print("目标路径创建完成，路径为：", self.PathNew)
	
	def start(self):
		shutil.move(self.PathOld, self.PathNew)
		print('移动完成')
