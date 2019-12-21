#Project 1stUI try


from tkinter import *
import speech_recognition as sr
import os
#********************************************************#
#Recognize function
def Recognize():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything")
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            e1s.set(text)
            print(text)
        except:
            print("Speak Clearly")
    #os.system("welcome.mp3")
#End of Recognize Function
#********************************************************#

#********************************************************#
def Ordered():
    pass
#********************************************************#

root=Tk()
root.geometry("400x400")
root.title("Intelligent Personal Assistant")

#Dummy label
dummy_label=Label(root,text='          ')
dummy_label.grid(row=0,column=0)

#Title Label for our project
l1=Label(root,text='Intelligent Personal Assistant')
l1.config(font=("Century Gothic", 14))
l1.grid(row=0,column=1)

#Dummy label
dummy_label=Label(root,text='          ')
dummy_label.grid(row=1,column=0)


b1=Button(root,text='Speak',command=Recognize)
b1.grid(row=1,column=1)

#You Said Label
l1=Label(root,text='You Said   =>')
l1.config(font=("Century Gothic", 10))
l1.grid(row=2,column=0)

#Text will be displayed whatever the user is said
e1s=StringVar()
e1=Entry(root,textvariable=e1s)
e1.grid(row=2,column=1)

#Order Button
b1=Button(root,text='Order',command=Ordered)
b1.grid(row=2,column=2)


root.mainloop()
