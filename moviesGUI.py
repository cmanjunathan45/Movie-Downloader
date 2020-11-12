from tkinter import *
import pyshorteners
import requests
from bs4 import BeautifulSoup
import tkinter as tk
import webbrowser
from tkinter import messagebox

root=tk.Tk()
root.geometry("500x500")
root.title("Movie Searcher | Manjunathan c")
ico=PhotoImage(file="icon.png")
root.iconphoto(True,ico)
root.config(bg="#ffa40b")
label1=Label(root,text="Type The Name Of the Movie ",font=("font awesome",15,"bold italic"),bg="#ffa40b",fg="green")
label1.place(x=85,y=20)
entry=Entry(root,width=28,borderwidth=6,font=("fontawesome",15,"bold italic"),bg="green",fg="#ffa40b")
entry.place(x=40,y=60)

def search():
	result.delete("1.0",END)
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
	url='https://google.com/search?q="intitle:""index of" '+entry.get()
	if entry.get() != '':
		response=requests.get(url,headers=headers)
		soup=BeautifulSoup(response.text,"lxml")

		scr=soup.find_all("div",class_="g")[0]
		ah=scr.find("a")
		
		p=pyshorteners.Shortener()
		result.insert(tk.END,p.tinyurl.short(ah["href"]))
		result.config(state="disabled")
		def web():
			webbrowser.open(p.tinyurl.short(ah["href"]))
		def copy():
			root.clipboard_clear()
			root.clipboard_append(p.tinyurl.short(ah["href"]))
		buttonCopy=Button(root,text="COPY",font=("font awesome",15,"bold italic"),bg="green",fg="#ffa40b",borderwidth=5,command=copy)
		buttonCopy.place(x=90,y=440)

		buttonOpen=Button(root,text="OPEN",font=("font awesome",15,"bold italic"),bg="green",fg="#ffa40b",borderwidth=5,command=web)
		buttonOpen.place(x=300,y=440)
	else:
		messagebox.showerror("Empty","Empty Values can't be Processed")

buttonSearch=Button(root,text="SEARCH",font=("font awesome",15,"bold italic"),bg="green",fg="#ffa40b",borderwidth=5,command=search)
buttonSearch.place(x=190,y=130)

buttonClear=Button(root,text="CLEAR",font=("font awesome",15,"bold italic"),bg="green",fg="#ffa40b",borderwidth=5,command=lambda: entry.delete(0,END))
buttonClear.place(x=200,y=190)

buttonExit=Button(root,text="EXIT",font=("font awesome",15,"bold italic"),bg="green",fg="#ffa40b",borderwidth=5,command=root.destroy)
buttonExit.place(x=212,y=250)

buttonContact=Button(root,text="CONTACT",font=("font awesome",15,"bold italic"),bg="green",fg="#ffa40b",borderwidth=5,command=lambda:webbrowser.open("https://github.com/cmanjunathan45/"))
buttonContact.place(x=182,y=310)

result=Text(root,font=("fontawesome",15,"bold italic"),bg="green",fg="#ffa40b",height=2,width=30,borderwidth=5)
result.place(x=30,y=370)

root.mainloop()
