import os, time
import zipfile


def origin_zip():
    # 准备一个空的压缩文件命名为demoreport.zip
    # 开启添加多个文件的模式 ‘a’
    with zipfile.ZipFile(file='../demoreport.zip', mode='a') as f:
        # 添加被压缩的文件，并命名为新的文件名
        f.write(r'C:\Users\janti\PycharmProjects\autotest-android\YYandroid\UItest\report\demoreport.html',
                'demoreport11_5.html')
        f.close()


def upgrade_zipfile():
    with open('../data/result.csv',encoding='UTF-8') as f:
        text=f.read()
        # print(text)
        with zipfile.ZipFile(file='../test_result_set.zip', mode='a') as z:
            for filename in os.listdir('../UItest/report/screenshot'):
                if filename in text:
                    z.write('../UItest/report/screenshot/%s' % filename, filename)
                    z.write('../UItest/report/demoreport.html','UItestreport.html')
            for videofile in os.listdir('../data'):
                   if videofile in text:
                       print(videofile)
                       # pass
                       z.write('../data/%s'%videofile,videofile)
            z.close()




if __name__ == '__main__':
    t1 = time.time()
    upgrade_zipfile()
    t2 = time.time()
    print(t2 - t1)
