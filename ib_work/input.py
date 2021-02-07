firm_list =[]
while True:
    firm = input ('请输入公司全称：【若不再输入，请输入数字0】 ')
    if firm == str(0) :
        break
    else:
        firm_list += [firm]
print ('你要查询的公司如下 \n', firm_list)
print('查询的网站有：\n 国家应急管理部 \n 国家税务总局 \n 国家自然资源部 \n 国家海关总署 \n 国家生态环境部')

