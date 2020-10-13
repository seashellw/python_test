import os
import shutil


# 图片操作类
class Picture:
	# 老目录
	PathOld = r""
	# 新目录
	PathNew = r""
	# 要移动的图片的拓展名
	TuoZhanMing = {
		".png",
		".jpg",
		".webp"
	}
	PicList = set()
	
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
	
	# 从原始目录中提取图片，并移动到新目录中，顺便把.webp格式转换成.png
	def tiQuYiDong(self):
		
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
				if n in self.TuoZhanMing:
					if n == ".webp":
						file = file + ".png"
					# 加入到集合PicList之中
					self.PicList.add(file)
		# 清除占用的内存
		dirs.clear()
		for file in self.PicList:
			# 生成新文件全名
			newFile = os.path.join(self.PathNew, os.path.basename(file))
			# 判断新文件是否已经存在，若存在，则删除
			if os.path.isfile(newFile):
				# 删除语句
				os.remove(newFile)
			# 移动语句，注意新文件不能存在，否则会报错
			shutil.move(file, self.PathNew)
			print(os.path.basename(file), "移动成功")
		print("所有图片移动完成")
	
	# 搜索原始目录中没有拓展名的文件，添加.png后缀并复制
	def tianJiaHouZhuipng(self):
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
					self.PicList.add(file)
		dirs.clear()
		for file in self.PicList:
			# 生成新文件全名
			newFile = os.path.join(
				self.PathNew, os.path.basename(file) + ".png")
			# 复制语句,当第二个参数是一个不同名称的文件时，复制文件为此新名称
			shutil.copy(file, newFile)
			print(os.path.basename(file), "已经修改为.png格式并复制成功")
		print("所有文件修改并复制完成")
