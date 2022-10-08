import urllib.request as request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)
    #print(data)
attractions = data["result"]["results"]
#print(attractions)
with open("data.csv", "w", encoding = "utf-8") as file:
    for x in attractions: #逐一取得列表中的資料
        #print(x["xpostDate"]) #找出各景點中的日期
        if x["xpostDate"] > "2014/12/31" and ".jpg" in x["file"].lower():
            #print(x['address'][5:8])
            area = x['address'][5:8] #篩選後的區域
            # 如果不確定資料是否含.jpg，建議多加if判斷，有含.jpg再進行篩選
            index = x["file"].lower().index(".jpg") #篩選網址(轉換小寫) 含.jpg的位置
            first_image = x["file"][:index+4]
            #print (x['stitle'], ' - ', first_image)
            longitude = x['longitude']
            latitude = x['latitude']
            title = x['stitle']
            file.write(title + "," + area + "," + longitude + "," + latitude + "," + first_image + "," + "\n")


    