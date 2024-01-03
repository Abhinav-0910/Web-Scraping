import pandas as pd
import requests
from bs4 import BeautifulSoup

Pname=[]
Pdes=[]
Price=[]
Review=[]
for i in range(2,8):
    url ="https://www.flipkart.com/search?q=mobile+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobile+under+50000%7CMobiles&requestId=d1bfc86e-fc65-4ed1-a55a-4bfac96f286f&as-searchtext=mobile+under+50000&page="+str(i)
    r= requests.get(url)
    soup= BeautifulSoup(r.text, "lxml")
    s=soup.find("div",class_="_1YokD2 _3Mn1Gg")

    name= s.find_all("div", class_="_4rR01T")
    for id in name:
        n=id.text
        Pname.append(n)
    print(len(Pname))


    prices= s.find_all("div",class_="_30jeq3 _1_WHN1")
    for _ in prices:
        p=_.text
        Price.append(p)
    print(len(Price))


    d=s.find_all("ul",class_="_1xgFaf")
    for j in d:
        di=j.text
        Pdes.append(di)
    print(len(Pdes))


    re= s.find_all("div", class_="_3LWZlK")
    for oi in re:
        rev=oi.text
        Review.append(rev)
    print(len(Review))


df=pd.DataFrame({"Product Name ":Pname, "Price":Price,"Description":Pdes,"Reviews":Review})
print(df)

df.to_csv("C:/Users/DELL/Desktop/python files/flipcart_mobiles_under_50000.csv")

