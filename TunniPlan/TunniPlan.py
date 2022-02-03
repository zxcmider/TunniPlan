from tkinter import *
from tkinter.messagebox import *
import time
import os
def failist_sõnastikusse():
	tund_kirjeldus={}
	file=open("Tunnid_kirjeldused.txt","r")
	for line in file:
		tund,kirjeldus=line.strip().split(":")
		tund_kirjeldus[tund.strip()]=kirjeldus.strip()
	file.close()
	print(tund_kirjeldus)
	return tund_kirjeldus

tund_kirjeldus=failist_sõnastikusse()
def kirjeldus_aknasse(t:str,tit:str):
	if (askyesno("Küsimus","Kas tahad kirjeldust näha?")):
		alam_aken=Toplevel()
		lbl_kirjeldus=Label(alam_aken,text=tund_kirjeldus[t]).pack()
		alam_aken.geometry("400x400")
		c=Canvas(alam_aken,height=500,width=500)
		file=PhotoImage(file=t)
		c.create_image(10,10,image=file,anchor=NW)
		c.pack()
		alam_aken.mainloop()
	else:
		showinfo("Vastus","Kui ei taha,siis ei taha!!!")

j=0
def veel():
	global j
	if j==0:
		aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-350))
		btn_veel.config(text="+")
		j=1
	else:
		aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+350))
		btn_veel.config(text="-")
		j=0
aken=Tk()
aken.geometry("1650x1080")
aken.title("Tunniplan")
p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
j=0
for i in range(2,11,2):
	Ep=Label(aken,text=p[j],font="Arial 20",relief="groove").grid(row=i,column=0,rowspan=2,sticky=N+S+W+E)
	j+=1
keel=["7:40-8:25","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12:40-13:25","13:30-14:15","14:20-15:05","15:10-15:55","16:00-16:45"]
k=0
for i in range(1,12,1):
	Ek=Label(aken,text=keel[k],font="Arial 6",relief="flat").grid(row=1,column=i,rowspan=2,sticky=N)
	k+=1
Rp=Label(aken,text="TARpv21",font="Arial 16",relief="flat").grid(row=0,column=0,sticky=N+S+W+E)
Ep=Label(aken,text="",relief="flat").grid(row=1,column=0,rowspan=1,sticky=N+S+W+E)
for i in range(11):
	tn="t"+str(i)
	tn=Label(aken,text=i,font="Arial 20",relief="groove").grid(row=0,column=i+1,sticky=N+S+W+E)
Ep=Label(aken,text="Esmaspäev",relief="solid",font="Arial 10",width=10,height=1).grid(row=2,column=0,rowspan=2,sticky=N+S+W+E)
Tp=Label(aken,text="Teisipäev",relief="solid",font="Arial 10",width=10,height=1).grid(row=4,column=0,rowspan=2,sticky=N+S+W+E)
Kp=Label(aken,text="Kolmapäev",relief="solid",font="Arial 10",width=10,height=1).grid(row=6,column=0,rowspan=2,sticky=N+S+W+E)
Np=Label(aken,text="Neljapäev",relief="groove",font="Arial 10",width=10,height=4).grid(row=8,column=0,rowspan=2,sticky=N+S+W+E)
Rp=Label(aken,text="Reede",relief="groove",font="Arial 10",width=10,height=1).grid(row=10,column=0,rowspan=2,sticky=N+S+W+E)

t0=Label(aken,text="0",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=1,sticky=N+S+W+E)
t1=Label(aken,text="1",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=2,sticky=N+S+W+E)
t2=Label(aken,text="2",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=3,sticky=N+S+W+E)
t3=Label(aken,text="3",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=4,sticky=N+S+W+E)
t4=Label(aken,text="4",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=5,sticky=N+S+W+E)
t5=Label(aken,text="5",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=6,sticky=N+S+W+E)
t6=Label(aken,text="6",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=7,sticky=N+S+W+E)
t7=Label(aken,text="7",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=8,sticky=N+S+W+E)
t8=Label(aken,text="8",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=9,sticky=N+S+W+E)
t9=Label(aken,text="9",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=10,sticky=N+S+W+E)
t10=Label(aken,text="10",relief="groove",font="Arial 20",width=10,height=1).grid(row=1,column=11,sticky=N+S+W+E)

k1=Button(aken,text="Multimeedia",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=2,column=2,columnspan=2,sticky=N+S+W+E)
ks=Button(aken,text="   ",relief="groove",font="Arial 20",width=10,height=4).grid(row=3,column=4,sticky=N+S+W+E)
k2=Button(aken,text="Programeerimise alused",relief="groove",font="Arial 20",bg="#1ebbd7",width=10,height=4).grid(row=2,column=5,columnspan=3,sticky=N+S+W+E)
k0=Button(aken,text="Rühmajuhataja tund",relief="groove",font="Arial 20",bg="#1ebbd7",width=10,height=4).grid(row=2,column=8,rowspan=2,sticky=N+S+W+E)
k3=Button(aken,text="Programeerimise alused",relief="groove",font="Arial 20",bg="#1ebbd7",width=10,height=4).grid(row=3,column=2,columnspan=3,sticky=N+S+W+E)
k4=Button(aken,text="Multimeedia",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=3,column=5,columnspan=2,sticky=N+S+W+E)

h1=Button(aken,text="Inglise Keel",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
h2=Button(aken,text="Inglise Keel",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=5,column=2,columnspan=2,sticky=N+S+W+E)
h3=Button(aken,text="Operatsioonisüsteemide alused",relief="groove",font="Arial 20",bg="#f603a3",width=10,height=4).grid(row=4,column=4,rowspan=2,columnspan=2,sticky=N+S+W+E)
h4=Button(aken,text="    ",relief="groove",font="Arial 20",width=10,height=4).grid(row=4,column=6,rowspan=2,sticky=N+S+W+E)
h5=Button(aken,text="Kehaline kasvatus",relief="groove",font="Arial 20",bg="#f603a3",width=10,height=4).grid(row=4,column=7,rowspan=2,columnspan=2,sticky=N+S+W+E)
h6=Button(aken,text="Eesti keel",relief="groove",font="Arial 20",bg="#8e7cc3",width=10,height=4).grid(row=4,column=9,rowspan=1,columnspan=1,sticky=N+S+W+E)
h7=Button(aken,text="Eesti keel",relief="groove",font="Arial 20",bg="#3e3530",width=10,height=4).grid(row=5,column=9,rowspan=1,columnspan=1,sticky=N+S+W+E)
h8=Button(aken,text="Geograafia",relief="groove",font="Arial 20",bg="#f8ac6a",width=10,height=4).grid(row=4,column=10,rowspan=2,sticky=N+S+W+E)

y1=Button(aken,text="Programeerimise alused",relief="groove",font="Arial 20",bg="#1ebbd7",width=10,height=4).grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
y2=Button(aken,text="Multimeedia",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=7,column=2,columnspan=3,sticky=N+S+W+E)
y3=Button(aken,text="    ",relief="groove",font="Arial 20",width=10,height=4).grid(row=6,column=5,rowspan=2,sticky=N+S+W+E)
y4=Button(aken,text="Multimeedia",relief="groove",font="Arial 20",bg="#424983",width=10,height=4).grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
y5=Button(aken,text="Programeerimise alused",relief="groove",font="Arial 20",bg="#1ebbd7",width=10,height=4).grid(row=7,column=6,columnspan=3,sticky=N+S+W+E)
y6=Button(aken,text="Multimeedia",relief="groove",font="Arial 20",width=4,height=1,bg="#424983").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
y7=Button(aken,text="Kunstiained",relief="groove",font="Arial 20",width=4,height=1,bg="#424983").grid(row=6,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)

g1=Button(aken,text="Andmebaasisüsteemide alused",relief="groove",font="Arial 20",width=10,height=4,bg="#424983").grid(row=8,column=2,columnspan=5,sticky=N+S+W+E)
g2=Button(aken,text="Geograafia",relief="groove",font="Arial 20",width=10,height=4,bg="#424983").grid(row=8,column=7,columnspan=1,rowspan=2,sticky=N+S+W+E)
g3=Button(aken,text="",relief="groove",font="Arial 20",width=10,height=4,bg="#424983").grid(row=8,column=8,columnspan=1,sticky=N+S+W+E)
g4=Button(aken,text="Eesti Keel",relief="groove",font="Arial 20",width=10,height=4,bg="#424983").grid(row=9,column=8,columnspan=1,sticky=N+S+W+E)
g5=Button(aken,text="Eesti Keel",relief="groove",font="Arial 20",width=10,height=4,bg="#424983").grid(row=9,column=8,columnspan=1,sticky=N+S+W+E)

aken.mainloop()
