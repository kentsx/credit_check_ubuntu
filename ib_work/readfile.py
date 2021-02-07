import os


def read_file_indir( path ):

    files = os.listdir(path)
    for f in files:
        if not os.path.isdir(f):
            # fname = 
            fn = open(path+"/"+f, 'r', encoding='utf-8')
            content = fn.read().encode('gbk', errors = 'ignore').decode('gbk', errors = 'ignore')
            pos = content.find("date: ")
            dt = content[pos+11 : pos+26]
            id = dt[:2]+dt[3:5]+dt[6:8]+dt[9:11]+dt[12:14]
            rewrite = content[:pos] + "timestamp: pt=" + id +'\n' + content[pos:] 
            fn.close()
            fn = fn = open(path+"/"+f, 'w', encoding='utf-8')
            # print(rewrite)
            fn.write(rewrite)
            fn.close()
            print('finished', f) 
            # print(read, f)

if __name__ == "__main__":
    read_file_indir( path )
            # pos = content.find('date:')
        
