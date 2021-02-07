import json


x =dict(num = "Ver 1.1", date = "06-02-2020", changelog ="1、增加了信用中国网站的下载功能；2、一些小的改进")
y =dict(num = "Ver 1.0", date ="22-01-2020", changelog="原始版，加入了5个网站：国家应急管理部、国家税务总局、国家自然资源部、国家海关总署、国家生态环境部")
data = dict(help = "使用指南：", ver = [x,y])
con = json.dumps(data, indent =2, ensure_ascii =False)

f_name ="ib_readme.json"

f = open(f_name,"w", encoding = 'utf-8')
f.write(con)
f.close()