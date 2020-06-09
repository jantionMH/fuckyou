import random, time

from interface.fast3gametown import *

# text='福彩3D第 20204362 期'
# if '3D' in text:
#     print('在')
# else:
#     print('不在')
# listmodel=[1,2]
# for i in range(10):
#   r=random.choice(["com.yy.sport:id/tv_menu_all","com.yy.sport:id/tv_menu_da","com.yy.sport:id/tv_menu_xiao","com.yy.sport:id/tv_menu_ji","com.yy.sport:id/tv_menu_ou"])
#
#
#   print(r)
# # print(random.choice(listmodel))
# a=5
# b=6
# c=1
# print(type(True))
# f="8,345.94"
# newf=f.replace(",","")
# print(newf)
#
#
# newbefore='7055.276'
# newbefore=newbefore[:-1]
# print(newbefore)
# listrule = ['和值', '三同号通选', '三同号单选', '三不同号', '三连号通选', '二同号复选', '二同号单选', '二不同号']
# for i in listrule:
#     print(type(i))

# print(listrule)
#
# for i in range(5):
#   r=random.randint(0,5)
#   # r = random.choices([0, 2, 4, 7, 9, 11])
#   # r=random.randrange(6)
#   # r = random.choice([0, 1, 2, 3, 4, 5])
#   print(r)
# try:
#   d=6
# except:
#   print('try的内容为Flase')
# else:
#   c=d
#   print(c)
# r = int(44444 / int(54))
# l=len(str(r))
# for i in range(l):
#   print(str(r)[i])
#  # print(str(r)[0:l])


# print(list(page1.keys())[0])
# print(list(page1['和值'].keys())[0])
# print(type(page1['和值']['3']))
# print(list(page2.keys())[0])
# print(list(page2['两连'].keys())[0])
# print(page2['两连']['12'])
# d1={'play_name_1': [3, 4, 7, 9, 12, 15]}
# # d2={ 'play_name_2': ['大', '单']}
# listbaozi = []
# listduizi = []
# listdudan = []
# listhezhidanxiaodanshuang = []
# listhezhi = []
# dict_v = {"豹子": listbaozi, '对子': listduizi, '两连': listdudan, '独胆': listdudan, '和值大小单双': listhezhidanxiaodanshuang,
#           '和值': listhezhi}
# list_dic = [{'豹子': '任意豹子'}, {'豹子': '3'}, {'豹子': '2'}, {'豹子': '1'}, {'对子': '6'}, {'对子': '5'}, {'对子': '2'}, {'对子': '1'},
#             {'独胆': '4'}, {'独胆': '3'}, {'独胆': '1'}, {'两连': '26'}, {'两连': '23'}, {'两连': '16'}, {'两连': '12'},
#             {'和值大小单双': '单'}, {'和值大小单双': '大'}, {'和值': '15'}, {'和值': '12'}, {'和值': '9'}, {'和值': '7'}, {'和值': '4'},
#             {'和值': '3'}]
# for i in list_dic:
#     if list(i.keys())[0] == '豹子':
#
#         listbaozi.append(i['豹子'])
#     elif list(i.keys())[0] == '对子':
#         listduizi.append((i['对子']))
#     elif list(i.keys())[0] == "独胆":
#         listdudan.append((i['独胆']))
#     elif list(i.keys())[0] == '两连':
#         listdudan.append(i['两连'])
#     elif list(i.keys())[0] == '和值大小单双':
#         listhezhidanxiaodanshuang.append(i['和值大小单双'])
#     elif list(i.keys())[0] == '和值':
#         listhezhi.append(i['和值'])
#
# # print(dict_v)
#
#
# p1 = {'和值': ['3', '4', '7', '9', '12', '15'], '和值大小单双': ['大', '单']}
# p2 = {'两连': ['12', '16', '23', '26'], '独胆': ['1', '3', '4']}
# p3 = {'对子': ['1', '2', '5', '6'], '豹子': ['1', '2', '3', '任意豹子']}
# d = {'豹子': ['任意豹子', '3', '2', '1'], '对子': ['6', '5', '2', '1'], '两连': ['4', '3', '1', '26', '23', '16', '12'],
#      '独胆': ['4', '3', '1', '26', '23', '16', '12'], '和值大小单双': ['单', '大'], '和值': ['15', '12', '9', '7', '4', '3']}
# # 在d中寻找键：
# # for i in d:
# #     #如果键刚好在p1中
# #     if i in p1:
# #          for j in p1[i]:
# #               if j in d[i] and len(d[i])==len(p1[i]):
# #                   print("内同和数量相等",j)
# #               else:
# #                   print('不相等',j)
# #
# #
# #     if i in p2:
# #          for j in p2[i]:
# #               if j in d[i] and len(d[i])==len(p2[i]):
# #                   print("内同和数量相等",j)
# #               else:
# #                   print('不相等',j)
# #
# #
# #     if i in p3:
# #          for j in p3[i]:
# #               if j in d[i] and len(d[i])==len(p3[i]):
# #                   print("内同和数量相等",j)
# #               else:
# #                   print('不相等',j)
# l = []
# if l:
#     print(l)
#
#
# def assert_equal_el(expect, actual, case, scenes):
#     now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
#     if expect == actual:
#         result = '成功'
#
#         with open('../data/result.csv', mode='a+') as f:
#             f.write(now + ',' + scenes + ',' + case + ',' + result + ',' + '无' + ',' + '无' + '\n')
#     else:
#         result = '失败'
#         filename = '%s.png' % now
#         # driver.get_screenshot_as_file("../UItest/report/screenshot/%s" % filename)
#         with open('../data/result.csv', mode="a+") as f:
#             f.write(
#                 now + ',' + scenes + ',' + case + ',' + result + ',' + filename + ',' + "期望:%s,type%s,实际:%s,type%s" % (
#                     expect, type(expect), actual, type(actual)) + '\n')
#
#
# list_except = [1]
#
#
# def assert_not_null(actual, case, scenes):
#     now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
#     if len(actual) != 0:
#
#         filename = '%s.png' % now
#         # driver.get_screenshot_as_file("../UItest/report/screenshot/%s" % filename)
#         with open('../data/result.csv', mode="a+") as f:
#             f.write(
#                 now + ',' + scenes + ',' + case + ',' + '失败' + ',' + filename + ',' + "期望:失败列表为空,实际:%s,type%s" % (
#                      actual, type(actual)) + '\n')
#
#
#     elif len(actual) == 0:
#
#         with open('../data/result.csv', mode='a+') as f:
#             f.write(now + ',' + scenes + ',' + case + ',' + '成功' + ',' + '无' + ',' + '无' + '\n')
#
# # assert_not_null(actual=list_except, scenes='投注记录', case='投注次数和投注内容')
# list = ['龙,0', '虎,1']
# print(type(random.choice(list).split(',')[0]))
# for i in range(20):
#  ra=random.randrange(0,10)
#  print(ra)

listname = [{'平特一肖':['鼠','虎','牛','蛇','狗']}, {'平特尾数':['0尾','2尾','5尾','7尾','9尾']}]

print(list(listname[0].values())[0])