from ftplib import FTP
import os


def upload_zipfile_ftp(date, type, subtype, key):
    connect = FTP()
    connect.connect(host='10.0.64.241')
    resp = connect.login(user='autotest', passwd='LmwmlCo-0wt1')
    # connect.retrlines(cmd='LIST')
    connect.cwd(dirname=date + '/' + type + '/' + subtype + '/')

    if key == '上传压缩包':
        with open(file='../demoreport.zip', mode='rb+') as file:
            file.seek(0)
            connect.storbinary(cmd='STOR demoreport.zip', fp=file, blocksize=4096)
        connect.quit()

    elif key == '上传解压后的文件':
        for i in os.listdir('../test_result_set'):
            print('上传的文件名:', i)
            with open(file='../test_result_set/%s' % i, mode='rb+') as file:
                file.seek(0)
                connect.storbinary(cmd='STOR %s' % i, fp=file, blocksize=4096)
    elif key == '上传视频':
        for i in os.listdir('../data'):
            with open(file='../data/result.csv') as f:
                csv = f.read()
                if i in csv:
                    with open(file='../data/%s' % i, mode='rb') as vf:
                        connect.storbinary(cmd='STOR %s' % i, fp=vf, blocksize=4096)
    elif key == '上传图片':
        for i in os.listdir('../UItest/report/screenshot'):
            with open(file='../data/result.csv') as f:
                csv = f.read()
                if i in csv:
                    with open(file='../UItest/report/screenshot/%s' % i, mode='rb') as pf:
                        connect.storbinary(cmd='STOR %s' % i, fp=pf, blocksize=4096)
    elif key == '上传html':

        with open(file='../UItest/report/test_report.html', mode='rb') as hf:
            hf.seek(0)

            connect.storbinary(cmd='STOR test_report.html', fp=hf)
        print('上传成功')
            # connect.quit()


# 上传整个录频文件
def upload_Mp4(date, type, subtype):
    connect = FTP()
    connect.connect(host='10.0.64.241')
    resp = connect.login(user='autotest', passwd='LmwmlCo-0wt1')
    connect.cwd(dirname=date + '/' + type + '/' + subtype + '/')

    fpath = os.listdir(r'C:\Users\janti\video')
    path = 'C:\\Users\\janti\\video\\' + fpath[-1]
    print(path)
    with open(file=path, mode='rb') as file:
        file.seek(0)
        connect.storbinary(cmd='STOR %s' % fpath[-1], fp=file, blocksize=4096)
    connect.quit()


#
def new_dir_buid(date, type, key):
    connect = FTP()
    connect.connect(host='10.0.64.241')
    resp = connect.login(user='autotest', passwd='LmwmlCo-0wt1')
    if key == 'YY':
        dir_resp = connect.mkd(dirname=date + '/')
        dir_resp = connect.mkd(dirname=date + '/' + type + '/')
        dir_resp = connect.mkd(dirname=date + '/' + type + '/' + key + '/')
    else:
        # 同级目录
        dir_resp = connect.mkd(dirname=date + '/' + type + '/' + key + '/')
