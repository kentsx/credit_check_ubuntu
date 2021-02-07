import pdfkit
# from makepath import mkdir
import sys , os, time
from caipan_pgid import uuid
import os
from requests_html import HTMLSession

pageId = uuid()
firm = "工商银行"

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
# firm_name = "江海证券有限公司"

url_caipan = "http://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId="
#这里指定一下wkhtmltopdf的路径，这就是我为啥在前面让记住这个路径
#使用的电脑上必须要安装wkhtmltopdf这个软件，安装路径要跟上面一致或调整路径
url_caipan += pageId + "&s21="+firm
# confg = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
# pdfkit.from_url(url_caipan, firm+'-裁判.pdf',configuration=confg, headers = headers)
# str = 'FINISHED 【' + firm +'】的查询，并保存' 
# print(str.center(60, '*'))
session = HTMLSession()

r = session.get(url_caipan)

r.html.render()
print(r.html.html)


# print ('\n 任务已全部完成,保存地址见上面提示。\n 100秒后程序自动关闭')