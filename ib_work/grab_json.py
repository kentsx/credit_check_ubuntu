import urllib.request, urllib.parse, urllib.error
import ssl
import json


# Ingnore SSL error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
'cookie':'yfx_c_g_u_id_10003701=_ck20020517015612731203719763145; yfx_f_l_v_t_10003701=f_t_1580893316257__r_t_1580893316257__v_t_1580893316257__r_c_0; _Jo0OQK=78F3925FC14FB53C0B17DED5B5C5BCA8115DE736F6BC4C71FA762C1BFA496E985C2B36EFF013B501FDC4273727401ADDBBC2D2013287A654D1C979D7EF5FC7AECFC1B918CCA8FE3BB9470EE0D297309F84070EE0D297309F8409CC21899663DE4F1052015BB621FE564GJ1Z1ZA==; JSESSIONID=89745EB279FEB917957DC703D724E0FA'    
}

ls = ["资本市场失信记录查询", "税务总局的重大税收违法案件信息公布栏"]
print("1、%s" % ls[0])
print("2、%s" % ls[1])
url_ls = ["http://neris.csrc.gov.cn/shixinchaxun/honestyObj/importentObj.do", "http://hd.chinatax.gov.cn/service/findMajor.do?type=1"]

url_num = int(input("Enter: "))
url = url_ls[url_num -1 ]
# html = urllib.request.urlopen(url, context = ctx, data = bytes(json.dumps(headers),encoding = "utf-8")).read()
# html = urllib.request.urlopen(url,  data = bytes(json.dumps(headers),encoding = "utf-8")).read()
req = urllib.request.Request(url = url, headers = headers)
response = urllib.request.urlopen(req)
html = response.read()

info = json.loads(html)

fname = ls[url_num -1 ] + "_dataset.json"
f = open(fname, "w", encoding = "utf-8")
f.write(json.dumps(info, ensure_ascii=False, indent =2))
f.close()