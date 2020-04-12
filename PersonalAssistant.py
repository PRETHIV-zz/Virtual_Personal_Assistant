#Project 1stUI try

#********************************************************#
#IMPORTED PACKAGES
from tkinter import *
import speech_recognition as sr
import pyautogui as pgi
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tkinter.messagebox as Mbox
from pygame import mixer
#from imageai.Detection import ObjectDetection
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
#Play Sound
def PlaySound(filename):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
#********************************************************#
def Order_Pizza(words):
    print(words)

#********************************************************#
#Order_Online
def Order_Online(words):
    search=""
    shop="amazon"
    order_found=False
    from_found=False
    try:
        for i in range(len(words)):
            if order_found:
                if words[i]=='from' or words[i]=='in' or words[i]=='In' or words[i]=='IN' or words[i]=='From' or words[i]=='FROM':
                    from_found=True
                    shop=words[i+1]
                    break
                search+=words[i]
                search+=" "
            if words[i]=='order' or words[i]=='buy' or words[i]=='Buy' or words[i]=='BUY' or words[i]=='Order' or words[i]=='ORDER':
                order_found=True
    except:
        shop='amazon'
        search=''
    if shop=='amazon' or shop=='Amazon' or shop=='AMAZON':
        if len(search)>0:
            driver=webdriver.Chrome(executable_path='D:\\SELENIUM\\chromedriver.exe')
            driver.maximize_window()
            driver.get('https://www.amazon.in/')
            elem=driver.find_element_by_name("field-keywords")
            elem.clear()
            elem.send_keys(search)
            elem.send_keys(Keys.RETURN)
        else:
            PlaySound("recognize_failed.mp3")
            Mbox.showinfo("what you are looking for?","Couldn't recognize your item")
    elif shop=='flipkart' or shop=='Flipkart' or shop=='FLIPKART':
        #Flipkart algorithm should be coded here
        pass
    elif shop=='snapdeal' or shop=='Snapdeal' or shop=='SNAPDEAL':
        #snapdeal algorithm should be coded here
        pass
    elif shop=='myntra' or shop=='Myntra' or shop=='MYNTRA':
        #myntra algorithm should be coded here
        pass


#********************************************************#
#Start Search
def Start_Search(e2,e3):
    file=e2.get()
    disk=e3.get()
    found=False
    PlaySound("start_search.mp3")
    if disk=='d' or disk=='D':
        disk='D:'
    elif disk=='e' or disk=='E':
        disk='E:'
    else:
        disk='D:'
    for r,d,f in os.walk(disk):
        file_path=r
        for files in f:
            print(files)
            if files in file:
                PlaySound("file_found.mp3")
                file_path+='\\'
                file_path+=files
                print(file_path)
                os.system('\"'+file_path+'\"')
                found=True
                break
        if found:
            break
    
#********************************************************#

#Auxillary for Search PC
def auxilary(search,disk):
    PlaySound("confirm_search.mp3")
    h1=Tk()
    h1.geometry("400x200")
    h1.title('Confirm your file and disk')
    l1a=Label(h1,text='Item to be searched ')
    l1a.config(font=("Century Gothic", 10))
    l1a.grid(row=0,column=0)
    print(search,disk)
    e2=Entry(h1)
    e2.grid(row=0,column=1)
    e2.delete(0,END)
    e2.insert(0,search)
    
    l1a=Label(h1,text='Disk to lookup for ')
    l1a.config(font=("Century Gothic", 10))
    l1a.grid(row=1,column=0)


    e3=Entry(h1)
    e3.grid(row=1,column=1)
    e3.delete(0,END)
    e3.insert(0,disk)
    
    b1a=Button(h1,text='Start Search',command=lambda:Start_Search(e2,e3))
    b1a.grid(row=2,column=0)
    
    h1.mainloop()
    print("hi")

#********************************************************#
#Search PC
def Search_Pc(words):
    cleaned=[]
    local_disk='D:'
    search=''
    search_found=False
    for i in words:
        if i=='for' or i=='FOR' or i=='For':
            continue
        elif i=='in' or i=='In' or i=='IN':
            break
        else:
            cleaned.append(i)
    if 'E' in words or 'e' in words:
        local_disk='E:'
    elif 'C' in words or 'c' in words:
        local_disk='C:'
    for i in cleaned:
        if search_found:
            search+=i
            search+=' '
        if i=='search' or i=='Search' or i=='SEARCH':
            search_found=True
    print(cleaned)
    print(search,local_disk)
    auxilary(search,local_disk)
    #print('Item to be searched ',search,local_disk)
#********************************************************#
#ShutDown PC
def Shut_PC():
    os.system("shutdown /s /t 1")
#********************************************************#
def Seperate(e1):
    exec_path=e1.get()
    cur_path=os.getcwd()
    os.chdir(exec_path)
    time.sleep(5)
    try:
        os.makedirs("images")
        os.makedirs("study_materials")
        os.makedirs("audio")
        os.makedirs("video")
    except:
        pass
    for r,d,f in os.walk(os.getcwd()):
        for file in f:
            if '.jpg' in file or '.jpeg' in file:
                o="move "+"\""+exec_path+"\\"+file+"\" "+"\""+exec_path+"\\images\""
                os.system(o)
                print(o)
            elif '.mp3' in file:
                o="move "+"\""+exec_path+"\\"+file+"\" "+"\""+exec_path+"\\audio\""
                os.system(o)
                print(o)
            elif '.mp4' in file:
                o="move "+"\""+exec_path+"\\"+file+"\" "+"\""+exec_path+"\\video\""
                os.system(o)
                print(o)
            elif '.docx' in file or '.pdf' in file:
                o="move "+"\""+exec_path+"\\"+file+"\" "+"\""+exec_path+"\\study_materials\""
                os.system(o)
                print(o)
        break
    Mbox.showinfo("Your Files have been Seperated","Task Done")
    os.chdir(cur_path)
    
#********************************************************#
def Seperatefiles():
    h1=Tk()
    h1.geometry("300x150")
    h1.title("Seperate Files")

    l1a=Label(h1,text='Execution Path')
    l1a.config(font=("Century Gothic", 10))
    l1a.grid(row=0,column=0)
    
    e2=Entry(h1)
    e2.grid(row=0,column=1)
    
    b1a=Button(h1,text='Seperate Files',command=lambda:Seperate(e2))
    b1a.grid(row=2,column=0)

    h1.mainloop()

#********************************************************#
def ObjectPicker(e2,e3):
    item=e2.get()
    cur_path=os.getcwd()
    execution_path = e3.get()
    os.chdir(execution_path)
    try:
        os.makedirs("selectedimages")
    except:
        pass
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(cur_path, "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    #iname=input("Enter the image i want to analyse :")
    #firstname=""
    #for i in iname:
    #    if i=='.':
    #        break
    #    else:
    #        firstname+=i
    #os.chdir("selectedimages")
    for r,d,f in os.walk(execution_path):
        for file in f:
            if '.jpg' in file:
                firstname=list(file.split('.'))
                firstname=firstname[0]
                detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path ,file), output_image_path=os.path.join(execution_path , firstname+"_Analysed.jpg"))
                for eachObject in detections:
                    if eachObject["name"]==item:
                        o="copy "+"\""+execution_path+"\\"+file+"\" "+"\""+execution_path+"\\selectedimages\""
                        print(o)
                        os.system(o)
        break
        #print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    #print("End _of _our _sneak Peak Coded by rocky")
    Mbox.showinfo("Info","Task Finished")
    os.chdir(cur_path)
#********************************************************#
def PickObjects():
    h1=Tk()
    h1.geometry("300x150")
    h1.title("Pick Objects")

    l1a=Label(h1,text='Object Name ')
    l1a.config(font=("Century Gothic", 10))
    l1a.grid(row=0,column=0)
    
    e2=Entry(h1)
    e2.grid(row=0,column=1)

    l1a=Label(h1,text='Execution Path ')
    l1a.config(font=("Century Gothic", 10))
    l1a.grid(row=1,column=0)

    e3=Entry(h1)
    e3.grid(row=1,column=1)
    
    b1a=Button(h1,text='Pickup Photos',command=lambda:ObjectPicker(e2,e3))
    b1a.grid(row=2,column=0)

    h1.mainloop()
#********************************************************#
def GoogleIt(words):
    search=""
    cmd="https://www.google.com/search?q="
    for_found=False
    for i in words:
        if for_found:
            search+=i
            search+='%20'
        elif i=='for' or i=='For':
            for_found=True
    os.system("start "+cmd+search)
#********************************************************#
def GoogleIt1(s):
    temp=''
    for i in s:
        if i.isspace():
            temp+='%20'
        else:
            temp+=i
    cmd="https://www.google.com/search?q="
    os.system("start "+cmd+temp)
#********************************************************#
def Youtube(words):
    temp=""
    play=False
    for i in words:
        if play:
            temp+=i
            temp+='%20'
        elif i=='play' or i=='Play':
            play=True
    cmd="https://www.youtube.com/results?search_query="
    os.system("start "+cmd+temp)
    time.sleep(5)
    pgi.moveTo(131,298,1)
    pgi.click()
#********************************************************#
def Ordered(e1):
    s=e1.get()
    words=list(s.split())
    if 'order' in words or 'Order' in words or 'ORDER' in words or 'buy' in words or 'Buy' in words or 'BUY' in words:
        if 'pizza' in words or 'Pizza' in words or 'PIZZA' in words:
            Order_Pizza(words)
        else:
            Order_Online(words)
    elif 'search' in words or 'Search' in words or 'SEARCH' in words:
        Search_Pc(words)
    elif 'shutdown' in words or 'Shutdown' in words or 'SHUTDOWN' in words:
        Shut_PC()
    elif 'seperatefiles' in words or 'seperate' in words or 'separate' in words or 'Seperatefiles' in words or 'SEPERATEFILES' in words or 'Seperate' in words or 'SEPERATE' in words:
        Seperatefiles()
    elif 'pickup' in words or 'Pickup' in words or 'PICKUP' in words or 'object' in words or 'Object' in words or 'OBJECT' in words: 
        PickObjects()
    elif 'google' in words or 'Google' in words:
        GoogleIt(words)
    elif 'play' in words or 'Play' in words:
        Youtube(words)
    else:
        GoogleIt1(s)
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
b1=Button(root,text='Order',command=lambda:Ordered(e1))
b1.grid(row=2,column=2)


root.mainloop()
