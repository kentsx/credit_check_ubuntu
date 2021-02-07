import requests
import json
from shutil import copyfile
from PyPDF
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',\
'Cookie':'yfx_c_g_u_id_10003701=_ck20022416221810606143785711150; _Jo0OQK=3E065868666A49CF3E9F78D3519B8D4B1FF4C348F179A9125502AF4BB5A3D7E4EC3864BE5C4AA7A29D489A04A72816A29CC0D9E22D2DEA2FBBD24DE2E7E50EFEE711B918CCA8FE3BB9470EE0D297309F84070EE0D297309F84004497FC31EF50CA18BAF82A12F05C904GJ1Z1cQ==; yfx_f_l_v_t_10003701=f_t_1582532538053__r_t_1582532538053__v_t_1582534524296__r_c_0; JSESSIONID=4A519A12DD018B7901BEC5509A99CBAB'}
base_url = 'http://hd.chinatax.gov.cn/service/findMajor.do?caseNature=&publish=&page=0&categeryid=1&querystring1=name&querystring0=name&queryvalue='
firm_name = '江海证券有限公司'
r = requests.get(base_url+firm_name,\
    headers = headers)
data = json.loads(r.text)
file_name = '税务总局的重大税收违法案件信息公布栏_'+firm_name+'.pdf'
if data["content"] == []:
    copyfile('origin.pdf', file_name)
else:
    print('获取失败')



print(data["content"])