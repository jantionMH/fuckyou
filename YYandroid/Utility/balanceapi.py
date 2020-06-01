import requests

session=requests.session()

auth={'dWc3VElZYkhYM1ZFaC9CRTA5WjQxV2k2RkFCUm5FVnRHR0FyeS83UHpsRzdwQU1FVTZ5UHJPOUhMRVhmeXdKSlNEczdTeC9GdXNkcldkVUFuY0gxQnhJWHRHQUNnV3NI'}
data1={"bets":[{"betContent":"9","betMode":"Y","menuStr":"整合_和值","multiple":852,"nodeCodeFirstStr":"整合","nodeCodeSecondStr":"整合","nodeCodeThirdStr":"和值","odds":8.5104,"orderMoney":852.0,"orderNum":1,"playCode":"K3HAHZ","showBetContent":"9"},{"betContent":"13","betMode":"Y","menuStr":"整合_和值","multiple":852,"nodeCodeFirstStr":"整合","nodeCodeSecondStr":"整合","nodeCodeThirdStr":"和值","odds":10.1356,"orderMoney":852.0,"orderNum":1,"playCode":"K3HAHZ","showBetContent":"13"},{"betContent":"15","betMode":"Y","menuStr":"整合_和值","multiple":852,"nodeCodeFirstStr":"整合","nodeCodeSecondStr":"整合","nodeCodeThirdStr":"和值","odds":21.276,"orderMoney":852.0,"orderNum":1,"playCode":"K3HAHZ","showBetContent":"15"},{"betContent":"18","betMode":"Y","menuStr":"整合_和值","multiple":852,"nodeCodeFirstStr":"整合","nodeCodeSecondStr":"整合","nodeCodeThirdStr":"和值","odds":212.76,"orderMoney":852.0,"orderNum":1,"playCode":"K3HAHZ","showBetContent":"18"}],"gameCode":"AHK3","numero":"20200601001","playType":"HAPPY"}
pose=session.post("http://sit-mile-h5.lottodev2020.com/wps/api/bet HTTP/1.1",data=data1,json=auth)
print(pose.text)
