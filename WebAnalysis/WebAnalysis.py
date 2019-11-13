import urllib.request
from bs4 import BeautifulSoup
import threading

class WebAlalysis:
    def __init__(self,url):
        self.url = url

    def ReadContent(self):
        return urllib.request.urlopen(self.url).read()
#########################################################################################
# def GetMsg(begin,End,fileName):
#     # f = open(fileName+'.txt', "a+")
#     # with open(fileName+'.txt', 'w') as f
#     for i in range(begin,End+1):
#         url = r'http://ask.39.net/news/237-'+str(i)+'.html'
#         print(url)
#         try:
#             wa = WebAlalysis(url)
#             rt = wa.ReadContent()
#             # print (rt.decode('utf-8')
#             soup = BeautifulSoup(rt,"html.parser")
#             for item in soup.find_all("a"):
#                 try:
#                     link = item.get("href")
#                     if 0 == link.find('/question'):
#                         AnswerLink = r'http://ask.39.net'+link
#                         tempwa = WebAlalysis(AnswerLink)
#                         AnswerContent = tempwa.ReadContent()
#                         subSoup = BeautifulSoup(AnswerContent, "html.parser")
#                         rt = subSoup.find_all('p', attrs={"class": ["txt_ms", "sele_txt"]})
#                         problem = '问题:'+rt[0].get_text().strip()
#                         answer = '回答:'+rt[1].get_text()
#                         with open(fileName+'.txt', 'a+') as f:
#                             f.write(problem+'\n'+answer+'\n')
#                             # f.write(answer)
#                         # print(problem)
#                         # print(answer)
#                 except:
#                     pass
#         except:
#             pass
#########################################################################################
def getHtml(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    page1=urllib.request.Request(url,headers=headers)
    page=urllib.request.urlopen(page1)
    html=page.read()
    return html


def GetMsg(begin,End,fileName):
    # f = open(fileName+'.txt', "a+")
    # with open(fileName+'.txt', 'w') as f
    for i in range(begin,End+1):
        url = r'http://www.120ask.com/list/xxgnk/over/'+str(i)+'/'
        print(url)
        try:
            # wa = WebAlalysis(url)
            rt = getHtml(url)
            # print (rt.decode('utf-8')
            soup = BeautifulSoup(rt,"html.parser")
            # print(soup)
            for item in soup.find_all(class_="q-quename", href=True):
                # print('http:'+item['href'])
                try:
                    link = 'http:'+item['href']
                    rt = getHtml(link)
                    subsoup = BeautifulSoup(rt, "html.parser")
                    rt = subsoup.find_all(class_="crazy_new")
                    print("问题：",rt[0].get_text().strip('\n').strip())
                    print("答案：", rt[1].get_text().strip())
                except:
                    pass
        except:
            pass

class myThread (threading.Thread):
    def __init__(self, threadID,Begin,End,fileName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        # self.name = name
        # self.counter = counter
        self.Begin = Begin
        self.End = End
        self.fileName = fileName
    def run(self):
        GetMsg(self.Begin,self.End,self.fileName)
        print ("开始线程：" + self.threadID)

ThreadNum=1
PageNum = 200
threadList = []
for i in range(1,ThreadNum+1):
    begin = int((PageNum/ThreadNum)*(i-1))
    end = int((PageNum/ThreadNum)*i)
    ThreadName = "Thread-"+str(i)
    threadList.append(myThread(i, begin,end,ThreadName))
    print(i)

for item in threadList:
    item.start()

for item in threadList:
    item.join()



