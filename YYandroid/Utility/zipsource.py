import os
import zipfile

# 准备一个空的压缩文件命名为demoreport.zip
# 开启添加多个文件的模式 ‘a’
with zipfile.ZipFile(file='../demoreport.zip', mode='a') as f:
    # f.writestr(zinfo_or_arcname="dddd",data='../data',compresslevel=)
    # 添加被压缩的文件，并命名为新的文件名
    f.write(r'C:\Users\janti\PycharmProjects\YYandroid\UItest\report\demoreport.html', 'demoreport.html')
    f.write(r'C:\Users\janti\PycharmProjects\YYandroid\UItest\report\screenshot\20200527181421.png', '20200527181421.png')
    f.write(r'C:\Users\janti\PycharmProjects\YYandroid\UItest\report\screenshot\20200527182031.png', '20200527182031.png')
    f.write(r'C:\Users\janti\PycharmProjects\YYandroid\UItest\report\screenshot\20200527182219.png', '20200527182219.png')

    f.close()
