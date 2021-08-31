import urllib.request
import requests
from bs4 import BeautifulSoup


genre = ["Action","Adventure","Animation","Biography","Comedy","Crime","Drama","Family","Fantasy","Film-Noir","History","Horror","Music","Musical","Mystery","Romance","Sci-Fi","Sport","Thriller","War","Western"]
for i in range(len(genre)):
    print(genre[i], end = "  ")
print()
name = input("請輸入查詢類型: ")
name = name.replace(" ","")

url = ""
count = 0
for i in range(len(genre)):
    if name == genre[count]:
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
for i in data:
    print(i.text.replace("\n",""))
    count += 1
    if count == 10:
        break
    print()

