import urllib.request
firm = ['哈尔滨哈投投资股份有限公司','江海证券有限公司']

for i in firm:
    pdf_url = 'https://public.creditchina.gov.cn/credit-check/pdf/download?companyName='+i+'&entityType=1&uuid=2e5f123071398db7a37078ba11efb348&tyshxydm=91230100128025258G'
    pdfname = i + '-信用中国.pdf'
    
    urllib.request.urlretrieve(pdf_url)
        
str = 'FINISHED'
print(str.center(60, '*'))