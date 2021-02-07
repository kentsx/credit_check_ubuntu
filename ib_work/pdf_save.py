#引入模块
import pdfkit
# from makepath import mkdir
import sys , os, time
import os
from xyzg_web import xyzg_web_download
import json
from multiprocessing.pool import ThreadPool

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

def screen_pdf(i):
    mkdir(i)
    os.chdir(current_path+ '\\' + i)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    print(url_dict)
    for k,v in url_dict.items():
        url_temp = v % i
        filename = i + k
        # print(url_temp, filename)
        pdfkit.from_url(url_temp, filename,configuration = config, options = options)

def screen_print(i):

    mkdir(i)
    os.chdir(current_path+ '\\' + i)
    url_yingji = 'https://www.mem.gov.cn/was5/web/sousuo/index.html?sw='+i+'&date1=&date2=&stype=0'
    url_guotu = 'http://s.lrn.cn/search/search.do?webid=6&pg=20&tpl=103&channelid=&searchword=&q='+i+'&filter=001&x=6&y=21'
    url_haiguan = 'http://search.customs.gov.cn/search/pcRender?pageId=f5261418ddc74f03b27e3590c531102b&q='+i+'&ext=siteId:300632&sr=score%20desc'
    url_tax = 'http://www.chinatax.gov.cn/s?siteCode=bm29000002&qt=' + i
    url_env = 'http://www.mee.gov.cn/qwjs2019/?searchword=' + i
    confg = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    #这里指定一下wkhtmltopdf的路径，这就是我为啥在前面让记住这个路径
    #使用的电脑上必须要安装wkhtmltopdf这个软件，安装路径要跟上面一致或调整路径
    pdfkit.from_url(url_yingji, i+'-应急管理部.pdf',configuration=confg, options = options)
    pdfkit.from_url(url_tax, i+'-税务总局.pdf',configuration=confg, options = options)
    pdfkit.from_url(url_guotu, i+'-自然资源部.pdf',configuration=confg, options = options)
    pdfkit.from_url(url_haiguan, i+'-海关.pdf',configuration=confg, options = options)
    pdfkit.from_url(url_env, i+'-环境部.pdf',configuration=confg, options = options)
    try:
        xyzg_web_download(i) #保存信用中国文件
    except:
        print('信用中国网站拒绝')
    os.chdir(current_path)
    str = 'FINISHED 【' + i +'】的查询，并保存' 
    print(str.center(60, '*'))
    print ('保存目录为： '+ current_path+ '\\' + i )
        


if __name__ == '__main__':
    print ('\n本小程序可查询如下网站: \n     ')
    func = ['国家应急管理部', '国家税务总局', '国家自然资源部' ,'国家海关总署' , '国家生态环境部','信用中国']
    for i in func:
        print('     - %s' % i)
    print('如需了解版本信息及使用方法，输入help并回车！')

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



    # screen_print(readme)
    firm_list =[]
    while True:
        firm = input ('请输入公司全称：【若不再输入，请输入数字0】 >>>')
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
    options = {'default-header':'', 'header-font-size':'6', 'footer-left':'[date] [time]', 'footer-font-size':'6','no-outline':'', 'enable-smart-shrinking':'','disable-external-links':''}
    current_path = os.getcwd()

    url_dict = {}
    url_dict['-应急管理部.pdf'] = 'https://www.mem.gov.cn/was5/web/sousuo/index.html?sw=%s&date1=&date2=&stype=0'
    url_dict['-税务总局.pdf'] = 'http://www.chinatax.gov.cn/s?siteCode=bm29000002&qt=%s'
    url_dict['-自然资源部.pdf'] = 'http://s.lrn.cn/search/search.do?webid=6&pg=20&tpl=103&channelid=&searchword=&q=%s&filter=001&x=6&y=21'
    url_dict['-海关总署.pdf'] = 'http://search.customs.gov.cn/search/pcRender?pageId=f5261418ddc74f03b27e3590c531102b&q=%s&ext=siteId:300632&sr=score%20desc'
    url_dict['-环境部.pdf'] = 'http://www.mee.gov.cn/qwjs2019/?searchword=%s'

    for i in firm_list:
        screen_print(i)
    #     screen_pdf(i)
    # pool = ThreadPool(processes = 10)
    # pool.map(screen_pdf,(i for i in firm_list))
    # pool.close()


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
