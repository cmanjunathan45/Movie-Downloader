from bs4 import BeautifulSoup 
import requests
import pyshorteners
from fake_useragent import UserAgent
query=input("Enter the Query : ")

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
url='https://google.com/search?q="intitle:""index of" '+query

response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"lxml")


scr=soup.find_all("div",class_="g")[0]
ah=scr.find("a")

print("THE SHORTENED URL is\n")
p=pyshorteners.Shortener()
print(p.tinyurl.short(ah["href"]))
