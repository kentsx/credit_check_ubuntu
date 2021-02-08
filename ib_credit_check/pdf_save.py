# 非玩windows下使用
#引入模块
import pdfkit
# from makepath import mkdir
import sys , os, time
import os
from xyzg_web import xyzg_web_download
# 导入信用中国下载模块
import json


def mkdir(path):
	#去除首位空格
	path = path.strip()
	#去除尾部\符号
	path = path.rstrip('\\')
	#判断路径是否存在
	#存在    True
	#不存在  False
	isExists = os.path.exists(path)
	#判断结果
	if not isExists:
		#如果不存在则创建目录
		#创建目录操作函数
		os.makedirs(path)
		print(path+'【文件夹创建成功】')
		return True
	else:
		#如果目录存在则不创建，并提示目录已存在
		print(path+'【文件夹目录已存在】')
		return False

def helpme(ver):
	print("")
	print("历史版本：")
	for i in ver["ver"]:
		print ("版本号：%s" %i["num"])
		print ("更新日期：%s" %i["date"])
		print ("更新log：%s" %i["changelog"])
		print ("-" *60 )
	print("")
	help_info = ver["help"]
	print(help_info)

		
def screen_print(readme):
	firm_list =[]
	while True:
		firm = input ('请输入公司全称：【若不再输入，请输入数字0】 ')
		if firm == "0" :
			break
		elif firm == "help":
			helpme(readme)
		else:
			firm_list += [firm]
	if len(firm_list) > 0:
		print ('你要查询的公司如下 \n', firm_list)
	else:
		print('没有需要查询的公司，程序自动退出')
		time.sleep(3)
		sys.exit()

	txt = '现在开始查询'
	print (txt.center(60, '='))
	options = {'javascript-delay':'500','load-error-handling':'skip','margin-top':'5','default-header':'', 'header-font-size':'6', 'footer-left':'[date] [time]', \
	'footer-font-size':'6','no-outline':'', 'enable-smart-shrinking':'','disable-external-links':'', 'disable-javascript':''}
	current_path = os.getcwd()
	# 网址字典集
	wz= dict()
	for firm in firm_list:
		mkdir(firm)
		os.chdir(current_path + '/'+ firm)
		# 应急管理部
		url_yingji = 'https://www.mem.gov.cn/was5/web/sousuo/index.html?sw='+firm+'&date1=&date2=&stype=0'
		wz['应急管理部'] = url_yingji
		# 生态环境部
		url_shengtai = 'http://www.mee.gov.cn/qwjs2019/?searchword='+firm
		wz['生态环境部'] = url_shengtai
		# 工业信息部
		url_gongye = 'https://www.miit.gov.cn/search/index.html?websiteid=110000000000000&pg=&p=&tpl=&category=&q='+firm+'&jsflIndexSeleted='
		wz['工业信息部'] = url_gongye
		# 外汇管理局
		url_waihui = 'http://www.safe.gov.cn/safe/search/index.html?q='+firm+'&siteid=safe&order=releasetime'
		wz['外汇管理局'] = url_waihui
		# 银保监会
		# url_yinbaojian = 'http://www.cbirc.gov.cn/cn/view/pages/index/jiansuo.html?keyWords='+firm
		# wz['银保监会']=url_yinbaojian
		# 央行网站---有问题

		# 国家发改委
		url_fagai = 'https://so.ndrc.gov.cn/s?siteCode=bm04000007&ssl=1&token=&qt='+firm
		wz['国家发改委']=url_fagai
		# 市场监督管理局
		# url_shichang = 'http://www.samr.gov.cn/search4/s?searchWord='+firm+'&x=0&y=0&column=%E5%85%A8%E9%83%A8&siteCode=bm30000012'
		# wz['市场监管局'] = url_shichang
		# 国家统计局
		url_tongji = 'http://www.stats.gov.cn/was5/web/search?channelid=288041&andsen='+ firm
		wz['国家统计局']=url_tongji
		# 国家商务部 -- ajax

		# 国家能源局
		url_nengyuan = 'http://so.news.cn/was5/web/search?channelid=229767&searchword='+firm
		wz['国家能源局']=url_nengyuan
		# 财政部 --ajax

		# 政府采购
		url_caigou = 'http://search.ccgp.gov.cn/znzxsearch?searchtype=2&page_index=1&start_time=&end_time=&timeType=2&searchparam=&searchchannel=0&dbselect=infox&kw='+ firm
		wz['政府采购']=url_caigou
		# 农业部
		url_nongye = 'http://www.moa.gov.cn/was5/web/search?searchword='+firm+'&channelid=233424&prepage=10&orderby=-DOCRELTIME'
		wz['农业部'] =url_nongye
		# 住建部
		url_zhujian = 'http://search.mohurd.gov.cn/?tn=mohurd&lastq=%24wstquerystring%24&sort=last-modified+desc&rn=10&auth_info=&table_id=%24wsttableid%24&pn=0&query=%'+firm +'&ty=a&ukl=&uka=&ukf=&ukt=&sl=&ts=&te=&upg=0'
		wz['住建部'] = url_zhujian
		#url_guotu = 'http://s.lrn.cn/search/search.do?webid=6&pg=20&tpl=103&channelid=&searchword=&q='+firm+'&filter=001&x=6&y=21'
		# 海关总署
		# url_haiguan = 'http://www.customs.gov.cn/?ess%24ctr151088%24ListC_Info%24ctl00%24KEYWORDS='+ firm
		# wz['海关总署'] = url_haiguan
		# 自然资源部
		url_ziyuan = 'http://s.lrn.cn/jsearchfront/search.do?websiteid=110000000000000&pg=1&p=1&searchid=1&tpl=13&cateid=1&q='+firm+'&filter=001&x=0&y=0'
		wz['自然资源部'] = url_ziyuan
		# 税务总局
		url_tax = 'http://www.chinatax.gov.cn/s?siteCode=bm29000002&qt=' + firm
		wz['税务总局'] = url_tax
		# url_env = 'http://www.mee.gov.cn/qwjs2019/?searchword=' + i
		# confg = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
		# 这里指定一下wkhtmltopdf的路径，这就是我为啥在前面让记住这个路径
		# 使用的电脑上必须要安装wkhtmltopdf这个软件，安装路径要跟上面一致或调整路径
		# 保存页面。ubuntu上必须用带qt补丁的wkhtmltopdf

		num = 1
		for k,v in wz.items():
			try:
				pdfkit.from_url(v, str(num)+'-'+firm+'-'+k+'.pdf', options = options)
				num+= 1
			except (ValueError, ArithmeticError):
				num+= 1
				continue


		# try:
		# 	xyzg_web_download(frim) #保存信用中国文件
		# except:
		# 	print('信用中国网站拒绝')
		# os.chdir(current_path)
		# str = 'FINISHED 【' + frim +'】的查询，并保存' 
		# print(str.center(60, '*'))
		# print ('保存目录为： '+ current_path+ '/' + frim )
		
	print ('\n 任务已全部完成,保存地址见上面提示。\n 100秒后程序自动关闭')
	time.sleep(100)
	sys.exit()



	# from_url这个函数是从url里面获取内容
	# 这有3个参数，第一个是url，第二个是文件名，第三个就是khtmltopdf的路径
	 
	#pdfkit.from_file('my.html', 'jmeter_下载文件2.pdf',configuration=confg)
	# from_file这个函数是从文件里面获取内容
	# 这有3个参数，第一个是一个html文件，第二个是文生成的pdf的名字，第三个就是khtmltopdf的路径
	 
	#html='''
	#<div>
	#<h1>title</h1>
	#<p>content</p>
	#</div>
	'''
	#这个html是我从一个页面上拷下来的一段，也可以
	 
	#pdfkit.from_string(html, 'jmeter_下载文件3.pdf',configuration=confg)
	# from_file这个函数是从一个字符串里面获取内容
	# 这有3个参数，第一个是一个字符串，第二个是文生成的pdf的名字，第三个就是khtmltopdf的路径
	'''

	
'''
Introduction
'''
print ('\n本小程序可查询如下网站: \n     ')
func = ['国家应急管理部', '国家税务总局', '国家自然资源部' ,'国家海关总署' , '国家生态环境部','信用中国']
for i in func:
	print('     - %s' % i)

sign = ''
auther = 'by Kent'
data = open("ib_readme.json", "r", encoding = "utf")
readme = json.load(data)

current_version_num = readme["ver"][0]["num"]
current_version_date = readme["ver"][0]["date"]
current_info = current_version_num+"  "+current_version_date
print (sign.center(60, '='))
print (auther.center(60, ' '))
print (current_info.center(60, ' '))
print (sign.center(60, '='))



screen_print(readme)
