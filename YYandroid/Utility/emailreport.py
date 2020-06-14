import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def textemail():
    fromaddr = 'jantion1110@gmail.com'
    toaddrs = ['jantion1110@aol.com', ]
    subject = '这是一封python发来的邮件'
    MIMEMultipart(open(r"../UItest/report\report.html").read())
    msg = '这是正文'

    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header(fromaddr, 'utf-8')
    message['To'] = Header(','.join(toaddrs), 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    username = 'jantion1110@gmail.com'
    password = 'melanie@12345'
    try:
        server = smtplib.SMTP('smtp.gmail.com', '587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, message.as_string())
        server.quit()
        print('Send Email Successful.')
    except:
        print('Send Email Failed.')


def public_htmlemail(content):
    # 一封邮件所需要的要素
    # 发送者
    fromaddr = 'jantion1110@gmail.com'
    # 接收者
    toaddrs = ['jantion1110@aol.com', 'frankc@seektopser.com', 'sven@seektopser.com','manda@seektopser.com']


    # 邮件标题
    subject = 'python自动化测试 '
    # 邮件的正文
    maintext = MIMEText('%s'%content, 'plain', 'utf-8')

    # 登录邮箱服务器
    username = 'jantion1110@gmail.com'
    password = 'melanie@12345'

    # 对python说的话
    # 实例化一个带附件的类
    message = MIMEMultipart()
    # 加入邮件的标题
    message['Subject'] = Header(subject, 'utf-8')
    # 加入邮件的正文
    message.attach(maintext)

    # 加入附件
    if content=='测试完成':
        attr1=MIMEText(open(r"../UItest/report/test_report.html", 'r').read(), _subtype='plain', _charset='utf-8')
        # attr1 = MIMEText(open(r"C:\Users\janti\PycharmProjects\autotest-android\YYandroid\demoreport.zip", 'rb').read(),
        #                  _subtype='base64',
        #                  _charset='utf-8')
        # 加入附件的格式描述/包括打包后附件的名字
        attr1["Content-Type"] = 'application/octet-stream'
        # attr1["Content-Disposition"] = 'attachment; filename="demoreport.zip"'
        attr1["Content-Disposition"] = 'attachment; filename="demoreport.html"'
        # 正式加入附件的所有内容
        message.attach(attr1)

        # attr2=MIMEText(open(r"C:\Users\janti\PycharmProjects\YYandroid\UItest\report\screenshot\20200521022514.png",'rb').read(),'basse64','gb2312')
        # attr2["Content-Type"] = 'application/octet-stream'
        # attr2["Content-Disposition"] = 'attachment; filename="20200521022514.png'
        # message.attach(attr2)

    # python.smtp对邮箱服务器说的话
    try:
        # 连接邮箱服务器的域名和端口
        smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', '465')  # 谷歌服务器邮箱
        # smtpobj=smtplib.SMTP_SSL('secure.emailsrvr.com','465')#公司的邮箱服务器
        # 发起登录
        smtpobj.login(username, password)
        # 发起写信
        smtpobj.sendmail(fromaddr, toaddrs, message.as_string())
        print('send email successful')
    except:
        print('send email fail')





def htmlemail(content):
    # 一封邮件所需要的要素
    # 发送者
    fromaddr = 'jantion1110@gmail.com'
    # 接收者

    toaddrs =['jantion1110@aol.com','jantion@seektopser.com']
    # 邮件标题
    subject = 'python自动化测试 '
    # 邮件的正文
    maintext = MIMEText('%s'%content, 'plain', 'utf-8')

    # 登录邮箱服务器
    username = 'jantion1110@gmail.com'
    password = 'melanie@12345'

    # 对python说的话
    # 实例化一个带附件的类
    message = MIMEMultipart()
    # 加入邮件的标题
    message['Subject'] = Header(subject, 'utf-8')
    # 加入邮件的正文
    message.attach(maintext)

    # 加入附件
    if content=='测试完成':
        attr1=MIMEText(open(r"../UItest/report/test_report.html", 'r').read(), _subtype='plain', _charset='utf-8')
        # attr1 = MIMEText(open(r"C:\Users\janti\PycharmProjects\autotest-android\YYandroid\demoreport.zip", 'rb').read(),
        #                  _subtype='base64',
        #                  _charset='utf-8')
        # 加入附件的格式描述/包括打包后附件的名字
        attr1["Content-Type"] = 'application/octet-stream'
        # attr1["Content-Disposition"] = 'attachment; filename="demoreport.zip"'
        attr1["Content-Disposition"] = 'attachment; filename="demoreport.html"'
        # 正式加入附件的所有内容
        message.attach(attr1)

        # attr2=MIMEText(open(r"C:\Users\janti\PycharmProjects\YYandroid\UItest\report\screenshot\20200521022514.png",'rb').read(),'basse64','gb2312')
        # attr2["Content-Type"] = 'application/octet-stream'
        # attr2["Content-Disposition"] = 'attachment; filename="20200521022514.png'
        # message.attach(attr2)

    # python.smtp对邮箱服务器说的话
    try:
        # 连接邮箱服务器的域名和端口
        smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', '465')  # 谷歌服务器邮箱
        # smtpobj=smtplib.SMTP_SSL('secure.emailsrvr.com','465')#公司的邮箱服务器
        # 发起登录
        smtpobj.login(username, password)
        # 发起写信
        smtpobj.sendmail(fromaddr, toaddrs, message.as_string())
        print('send email successful')
    except:
        print('send email fail')

if __name__ == '__main__':
  pass
