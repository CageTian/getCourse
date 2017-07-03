import requests
from bs4 import BeautifulSoup
import time
import datetime
id = "*********"
password = "*************"
course={
    #'rpingp(4)':'02',
    #'100001015y':'880',
    #'100001020y':'880',
    '1090340110':'01',
    #'100001002z':'880',
    #'100001004z':'880'
    }
url="http://zhjw.dlut.edu.cn"
header1 = {
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    #'Content-Length':'25',
    #'Host':'zhjw.dlut.edu.cn',
    #'Accept-Encoding':'gzip, deflate',
    #'Referer':'http://zhjw.dlut.edu.cn/',
    'Cookie':'lzstat_uv=31329816153518056971|3122532;'
    #'Connection':'keep-alive',
    #'Upgrade-Insecure-Requests':'1'
    }
header2={
    'Content-Type':'application/x-www-form-urlencoded',
    'Content-Length':'97',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    }
header3={
    'Content-Type':'application/x-www-form-urlencoded',
    'Content-Length':'47',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    }
logindata = "zjh=" + id + "&mm=" + password
s=requests.Session()
s.post(url+'/loginAction.do',data=logindata,headers=header1)
hint=s.get(url+'/xkAction.do?actionType=17')
#print hint.content.decode('gb2312').find(u'请选择方案名称后点击网上选课按钮')
while hint.content.decode('gb2312').find(u'请选择方案名称后点击网上选课按钮')<=0:
    print "continiue request..."
    #print datetime.datetime.now().second
    #if datetime.datetime.now().second<50.0:
    #    time.sleep((60-datetime.datetime.now().second)/10)
    time.sleep(2)
    hint=s.get(url+'/xkAction.do?actionType=17')

s.get(url+'/xkAction.do?actionType=5&pageNumber=-1&cx=ori')
while(1):
    for courseId in course:
        coursedata="kch="+courseId+"&cxkxh="+course[courseId]+"&kcm=&skjs=&kkxsjc=&skxq=&skjc=&pageNumber=-2&preActionType=2&actionType=5"
        coursedata2="kcId="+courseId+'_'+course[courseId]+"&preActionType=5&actionType=9"
        respon1=s.post(url+'/xkAction.do',data=coursedata,headers=header2)
        respon=s.post(url+'/xkAction.do',data=coursedata2,headers=header3)
        time.sleep(1)
        soup=BeautifulSoup(respon.text,"html.parser")
        try:
            print soup.find("font",attrs={'color':'#990000'}).string.encode('gb2312')
        except:
            print "fail to choose "+courseId+"_"+course[courseId]+" will continiue"
            continue
