import os
import shutil
import re

def Break_up (site='./',word='整合',houzui = '.*'):
	# print(word)
	a = os.listdir(site)
	if site == './' and a:
		rmfiles = ['ttt.py','test.py','整合','文件整合.exe','python文件整合.exe','Python文件整合.exe','test.exe']
		for key in rmfiles:
			if key in a:
				a.remove(key)
	if a:
		b,c =[],[]
		for file in a:
			if re.search('.*\.'+houzui,file) is not None:
				b.append(file)
			else:
				c.append(file)
		for files in b:
			way = str(site)+'/'+str(files)
			try:
				shutil.copy(way,word)	
			except shutil.SameFileError:
				pass
		if c:
			for dirs in c:
				way1 = str(site)+'/'+str(dirs)
				Break_up(way1,word)	
	else:
		return [],[]

def zenghe(str = '整合',_houzui = '.*'):
	if str in os.listdir():
		print('该目录下已有整合包，请查看文件夹“##整合包##”，或删除对应文件夹并重新整合')
	else:
		os.mkdir(str)
		print('开始整合，文件将拷贝到文件夹“##整合包##”')
		Break_up(word=str,houzui=_houzui)
		print('*************************************\n整合完毕，文件现已位于文件夹“##整合包##”')

def waiyi(site='./',word='整合'):
	a = os.listdir(site)
	if site == './' and a:
		rmfiles = ['ttt.py','test.py','整合','文件整合.exe','python文件整合.exe','Python文件整合.exe','test.exe']
		for key in rmfiles:
			if key in a:
				a.remove(key)
	if a:
		b,c =[],[]
		for file in a:
			if re.search('.*\..*',file) is not None:
				b.append(file)  # 文件
			else:
				c.append(file)  # 文件夹
		if c:
			for dirs in c:
				way1 = str(site)+str(dirs)
				new_a = os.listdir(way1)
				if new_a:
					# print('小丑''是我自己')
					nb,nc =[],[]
					for file in new_a:
						if re.search('.*\..*',file) is not None:
							nb.append(file)  # 文件
							# print('小丑')
						else:
							nc.append(file)  # 文件夹
							# print('小丑哈哈哈')
							# way2 = str(way1)+'/'+str(dirs)
							way2 = str(way1)+'/'+str(file)
							try:
								# print(way2)
								# print(way1+'_new')
								shutil.copytree(way2,'./___'+str(file)+'_new')	
								# print('成功')
								
							except FileExistsError:
								print('文件夹已存在，请删除后重试')
								pass
		print('文件夹外移完成，文件现已位于文件夹“__xxx_new中”')
	else:
		return [],[]

# a = input('请输入模式，1为整合，2为文件夹外移，3为同时执行，4为退出\n')
# print('a =',a)
a = 2
if a == 1:
	zenghe('##整合包##')
if a == 2:
	waiyi()
if a == 3:
	zenghe('##整合包##')
	waiyi()
ab = input('\n输入任何字段以结束:')