import os
import zipfile

# 准备一个空的压缩文件命名为demoreport.zip
# 开启添加多个文件的模式 ‘a’
with zipfile.ZipFile(file='../demoreport.zip', mode='a') as f:
    # f.writestr(zinfo_or_arcname="dddd",data='../data',compresslevel=)
    # 添加被压缩的文件，并命名为新的文件名
    f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\demoreport.html', 'demoreport.html')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200604155806.png', '20200604155806.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200604162427.png', '20200604162427.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529122236.png', '20200529122236.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529122254.png', '20200529122254.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529122404.png', '20200529122404.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529122724.png', '20200529122724.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529122834.png', '20200529122834.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529122846.png', '20200529122846.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529135708.png', '20200529135708.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529135822.png', '20200529135822.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529135833.png', '20200529135833.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529153558.png', '20200529153558.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529153701.png','20200529153701.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529153714.png','20200529153714.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529153742.png','20200529153742.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529153847.png','20200529153847.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529153859.png','20200529153859.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529154414.png','20200529154414.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529154519.png','20200529154519.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529154533.png','20200529154533.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529155950.png','20200529155950.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529160055.png','20200529160055.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529160107.png','20200529160107.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529171102.png','20200529171102.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529171245.png','20200529171245.png')
    # f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\screenshot\20200529171258.png','20200529171258.png')


    f.close()
