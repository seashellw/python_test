import os
import shutil
import re


# 视频操作类
class Video:
	# 老目录
	PathOld = r""
	# 新目录
	PathNew = r""
	# 集合
	List0 = set()
	
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
	
	# 搜索原始目录中没有拓展名的文件，添加.mp4后缀并复制
	def tianJiaHouZhuimp4(self):
		# 提取目录中的文件名和目录名
		dirs = os.listdir(self.PathOld)
		dirs = set(dirs)
		for file in dirs:
			# 拼接成为文件全名
			file = os.path.join(self.PathOld, file)
			# 判断是否为文件
			if os.path.isfile(file):
				# 提取拓展名（带点号的拓展名）
				n = os.path.splitext(file)[1]
				if n == "":
					self.List0.add(file)
		dirs.clear()
		for file in self.List0:
			# 生成新文件全名
			newFile = os.path.join(
				self.PathNew, os.path.basename(file) + ".mp4")
			# 复制语句,当第二个参数是一个不同名称的文件时，复制文件为此新名称
			shutil.copy(file, newFile)
			print(os.path.basename(file), "已经修改为.mp4格式并复制成功")
		print("所有文件修改并复制完成")
	
	# 专用文件拼接方法
	def shipinhebing(self):
		
		def sort_key(s):
			c = re.findall('\d+', s)
			c = c[len(c) - 1]
			return int(c)
		
		dirs = os.listdir(self.PathOld)
		dirs.sort(key=sort_key)
		for i in range(len(dirs)):
			# 拼接成为文件全名
			dirs[i] = os.path.join(self.PathOld, dirs[i])
			print(dirs[i])
		endfilepath = os.path.join(self.PathNew, "end.mp4")
		with open(endfilepath, "wb") as endfile:
			for i in range(len(dirs)):
				file = open(dirs[i], "rb")
				endfile.write(file.read())
				print("剩余" + str(len(dirs) - i) + "个文件")
				file.close()
		print("所有文件处理完毕")
