#抓取 PTT 電影版的網頁原始碼(HTML)
import urllib.request as req
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url="https://www.ptt.cc/bbs/movie/index.html"
#print(root.title) #取得標籤：<title>看板 movie 文章列表 - 批踢踢實業坊</title>
#print(root.title.string) #取得標籤內的文字：看板 movie 文章列表 - 批踢踢實業坊
url_list = [url]
for num in range(9):  
    if len(url_list) > 1:
        url = url_list[num]
    #建立一個 Request 物件，附加 Headers 的資訊
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析原始碼，取得每篇文章的標題   
    root=bs4.BeautifulSoup(data, "html.parser")
    back_btn=root.find_all("a", class_="btn wide")[1] #尋找 class="btn wide" 的 a，並以陣列排序找出 上頁 的標籤
    next_link = "https://www.ptt.cc" +  back_btn['href']
    url_list.append(next_link)
# print(url_list)

title_list = []
for url_link in url_list:
    request=req.Request(url_link, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title") #尋找 class="title" 的 div標籤
    for title in titles:
        if title.a != None: #如果標題含 a 標籤(沒有被刪除)，印出來
            # print(title.a.string)
            title_list.append(title.a.string)

# 找出具有[好雷]、[普雷]、[負雷]的標題
good_title_list = []
normal_title_list = []
bad_title_list = []
for title in title_list:
    if title.startswith("[好雷]"):
        good_title_list.append(title)
    if title.startswith("[普雷]"):
        normal_title_list.append(title)
    if title.startswith("[負雷]"):
        bad_title_list.append(title)

with open("movie.txt", "w", encoding = "utf-8") as file:
    for title in good_title_list:
        file.write(title + '\n')
    for title in normal_title_list:
        file.write(title + '\n')
    for title in bad_title_list:
        file.write(title + '\n')