#Flames by aravind
from tkinter import *
import tkinter.messagebox
def flames(e1,e2):
    s1=e1.get()
    s2=e2.get()
    name1={}
    name2={}
    for i in s1:
        try:
            name1[i]+=1
        except:
            name1[i]=1
    for i in s2:
        try:
            name2[i]+=1
        except:
            name2[i]=1
    dist=list(set(s1))
    h=0
    inter=list(set(s1)&set(s2))
    for i in inter:
        h+=abs(name1[i]-name2[i])
    for i in dist:
        if i not in inter:
            h+=name1[i]
    dist=list(set(s2))
    for i in dist:
        if i not in inter:
            h+=name2[i]
    fuck="FLAMES"
    while len(fuck)!=1:
        ind=h%len(fuck)
        ind-=1
        if ind==-1:
            ind=len(fuck)-1
        temp=""
        for i in range(len(fuck)):
            if i!=ind:
                temp+=fuck[i]
        fuck=temp
    if fuck=='F':
        fuck='FRIENDS'
    elif fuck=='L':
        fuck='LOVERS'
    elif fuck=='A':
        fuck='AFFECTION'
    elif fuck=='M':
        fuck='MARRIAGE'
    elif fuck=='E':
        fuck='ENEMY'
    elif fuck=='S':
        fuck='SISTER'
    print(s1,s2,fuck)
    tkinter.messagebox.showinfo('Relation box',message=fuck)


root=Tk()

root.geometry("400x400")


l1=Label(root,text='Name1   ')
l1.grid(row=0,column=0)

e1=Entry()
e1.grid(row=0,column=1)

l1=Label(root,text='      ')
l1.grid(row=1,column=0)

l1=Label(root,text='Name2   ')
l1.grid(row=2,column=0)

e2=Entry()
e2.grid(row=2,column=1)

l1=Label(root,text='      ')
l1.grid(row=3,column=0)


l1=Label(root,text='      ')
l1.grid(row=4,column=0)


b1=Button(root,text='Calculate',command=lambda:flames(e1,e2))
b1.grid(row=4,column=1)

root.mainloop()
