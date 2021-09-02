import requests
from bs4 import BeautifulSoup


genre = ["Action","Adventure","Animation","Biography","Comedy","Crime","Drama","Family","Fantasy","Film-Noir","History","Horror","Music","Musical","Mystery","Romance","Sci-Fi","Sport","Thriller","War","Western"]
genre2 = ["1:Action","2:Adventure","3:Animation","4:Biography","5:Comedy","6:Crime","7:Drama","8:Family","9:Fantasy","10:Film-Noir","11:History","12:Horror","13:Music","14:Musical","15:Mystery","16:Romance","17:Sci-Fi","18:Sport","19:Thriller","20:War","21:Western"]
print("類型選擇:")
for i in range(len(genre2)):
    print(genre2[i])
print()
name = input("請輸入查詢類型號碼: ")
if(int(name)>21):
    print("類型不符合")
else:
    print()
    url = ""
    count = 0
    for i in range(len(genre)):
        if str(name) == str(i+1):
            url = "https://www.imdb.com/search/title?genres=" + genre[count].lower() + "&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=9RH8JQQN18JZV9QMNKGS&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_" + str(count+1)
            break
        count += 1

    #print(url)
    #browser = webdriver.Chrome("D:\google download\chromedriver_win32 (1)\chromedriver.exe")
    #browser.get(url)

    html = requests.get(url)
    html.encoding = 'utf8'
    sp = BeautifulSoup(html.text, 'lxml')

    data = sp.find_all("h3",class_ = "lister-item-header")
    count = 0
    name = []
    for i in data:
        temp = i.text.replace("\n","")
        name.append(temp)
        #print(i.text.replace("\n",""))
        count += 1
        if count == 20:
            break

    data2 = sp.find_all("span",class_ = "certificate")
    count = 0
    certificate = []
    for i in data2:
        #print(i.text.replace("\n",""))
        certificate.append(i.text.replace("\n",""))
        count += 1
        if count == 20:
            break

    data3 = sp.find_all("span",class_ = "runtime")
    count = 0
    runtime = []
    for i in data3:
        #print(i.text.replace("\n",""))
        runtime.append(i.text.replace("\n",""))
        count += 1
        if count == 20:
            break

    data4 = sp.find_all("div",class_ = "inline-block ratings-imdb-rating")
    count = 0
    rate = []
    for i in data4:
        #print(i.text.replace("\n",""))
        rate.append(i.text.replace("\n",""))
        count += 1
        if count == 20:
            break

    data5 = sp.find_all("p", class_="")
    count = 0
    dir = []
    for i in data5:
        #print(i.text.replace("\n",""))
        dir.append(i.text[5:].replace("\n","").replace("|","\n演員： ").replace("     ","").replace(":",": "))
        count += 1
        if count == 20:
            break

    data6 = sp.find_all("p",class_ = "text-muted")
    count = 0
    text = []
    for i in data6:
        if count%2!=0:
            text.append(i.text.replace("\n","").replace("    ",""))
        count += 1
        if count == 40:
            break


    data7 =  sp.select('h3.lister-item-header a')
    count = 0 
    web = [] 
    begin = "https://www.imdb.com" 
    end = "?ref_=adv_li_tt" 
    for i in data7:     
        web.append(begin + i["href"] + end)     
        count += 1     
        if count == 20:         
            break

    for i in range(20):
        print(name[i])
        print("分級：",certificate[i])
        print("長度：",runtime[i])
        print("評價：",rate[i],"⭐")
        print("導演：",dir[i])
        print("大綱：",text[i])
        print("連結：",web[i])
        print()
    
