import urllib.request, urllib.parse, urllib.error
import ssl
import json

def make_url(firm_name):
    url_firm = urllib.parse.quote(firm_name)
    url_one = "https://public.creditchina.gov.cn/private-api/getTyshxydmDetailsContent?keyword="+url_firm +"&scenes=defaultscenario&entityType=1&searchState=1&uuid=&tyshxydm="
    url_two = "https://public.creditchina.gov.cn/credit-check/pdf/download?companyName="+url_firm+"&entityType=1&uuid="
    
    return [url_one, url_two]

def xyzg_web_download(firm_name):
    # Ingnore SSL error
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    
    url = make_url(firm_name)
    
    req = urllib.request.Request(url[0], headers = headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf8')
    
    data = json.loads(html)

    is_correct = tyshdm = data["data"]["headEntity"]
    if is_correct == {}:
        print ("【%s】：该公司不存在或名称错误" % firm_name)
    else:
        uuid = data["data"]["data"]["entity"]["uuid"]
        tyshdm = data["data"]["headEntity"]["tyshxydm"]
        req_two = url[1]+uuid+"&tyshxydm="+tyshdm
        path = firm_name + "_信用中国.pdf"
        req = urllib.request.Request(url = req_two, headers = headers)
        
        response = urllib.request.urlopen(req)
        html = response.read()
        f = open(path,"wb")
        f.write(html)
        f.close()
        
        print ("finish download " + firm_name + "!")
    
    
    
    # con = json.dumps(data, ensure_ascii=False, indent =2)
    
    # f_name = firm_name + "_信用中国.json"
    
    # f = open(f_name,"w", encoding = 'utf-8')
    # f.write(con)
    # f.close()



