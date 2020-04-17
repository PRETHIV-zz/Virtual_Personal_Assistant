import os
import os.path
import time


def line(c):
    i=0
    while i<56:
        print(c,end="")
        i+=1
    print()

def info(information):
    line('=')
    print(" ||   ")
    print(" ||   "+information)
    print("  o   ")
    line('=')

def qBox(msg):
    print()
    line("-")
    print(msg)
    line("-")
    print()

def MessageBox(msg):
    print(" _______________________________________________________")
    print("|                                                       |")
    print("|      "+msg+"                                                 ")
    print("|_______________________________________________________|")


def getValidChoice(choices,choicename,ismsg=False,msg=""):
    if ismsg:
        if len(msg)==0:
            pass
        else:
            print()
            line('*')
            print()
            print(msg)
            print()
            line('*')
    #Choicename is like enter your os where os is the choice name
    choice=""
    while True:
        if not ismsg:
            print("Enter Your "+choicename)
        for i in range(len(choices)):
            print(str(i+1)+"."+choices[i])
        choice=input("Enter ur choice")
        try:
            choice=int(choice)
            if choice<=len(choices) and choice>0:
                break
            else:
                MessageBox("Invalid Choice")
        except:
            MessageBox("Invalid Choice Choose 1 or 2 or 3...")
    if not ismsg:
        MessageBox("Your "+choicename+" is"+" "+choices[choice-1])
    return choice


os_name="win"
archi="32"
chrome_v=""
ischrome=False
ismscpp=False
adminerror=False

cur_dir=os.getcwd()
os.chdir("drivers")
driver_dir=os.getcwd()
os.chdir("..")
packages_to_install=["ChromeBrowser","Microsoft visual c++","Chrome Driver","speechrecognition","pyautogui","selenium","pygame","gtts","PyAudio"]
installed_packages=[]
try:
    download_dir=os.path.expanduser("~")
    download_dir+="\\Downloads"
except:
    download_dir=input("Please provide your download directory path (typically where the downloaded files will be saved)\nEg:- c:\\users\\Prethiv\\Downloads")
try:
    home_dir=os.path.expanduser("~")
except:
    home_dir=input("Please provide your user workspace .Eg: c:\\users\\prethiv")


MessageBox("Home dir "+home_dir)
MessageBox("Download dir "+download_dir)
os.chdir(home_dir)
time.sleep(3)


line('*')
print()
print("TRIANGLE VPA INITIALIZER SETUP SCRIPT ")
print()
line('*')

print()
print("Before the magic happen please give us some information regarding your pc")
print()

time.sleep(2)

qBox("Choose your OS ")

c=getValidChoice(["Windows","Mac","Linux"],"OS")

if c==1:
    info("OS is Windows")
    os_name="win"
elif c==2:
    info("OS is Macintosh")
    os_name="mac"
else:
    info("OS is Linux")
    os_name="lin"

qBox("Choose Your Architecture")

info("To view your Architecture just run python terminal in the first line itself will tell us")

time.sleep(3)

c=getValidChoice(["32bit","64bit","arm64bit"],"Architecture")

if c==1:
    info("Processor is 32-bit architecture")
    archi="32bit"
elif c==2:
    info("Processor is 64-bit architecture")
    archi="64bit"
else:
    info("Processor is arm 64 bit architecture")
    archi="arm64bit"

qBox("Is Chrome Installed")

c=getValidChoice(["Yes","No"],"",True,"")

if c==1:
    info("Chrome is installed")
    qBox("Choose your chrome Version")
    d=getValidChoice(["v79","v80","v81"],"Chrome Version")
    if d==1:
        chrome_v="79"
    elif d==2:
        chrome_v="80"
    else:
        chrome_v="81"
    ischrome=True
else:
    info("Chrome is not installed")
    ischrome=False
    chrome_v="81"


qBox("Microsoft Visual C++ V14.0+ Installed in your system?")

c=getValidChoice(["yes","No"],"",True,"")

if c==1:
    info("Microsoft Visual C++ is installed")
    ismscpp=True
else:
    info("Microsoft Visual c++ is not installed")
    ismscpp=False

line("*")

qBox("Summary of your information before doing the magic")

print("Home Dir ",home_dir)

print("\nDownload directory",download_dir)

print("\nChrome Installed ",ischrome)

print("\nOperarting system",os_name)

print("\nProcessor Architectur ",archi)

print("\n Driver Directory",driver_dir)

print("Microsoft c++ installed",ismscpp)

print("Chrome version ",chrome_v)
    
print()
line('*')

time.sleep(3)

qBox("Downloading the necessary files ")

if not ischrome:
    qBox("Downloading Chrome for you")
    if os_name=="win":
        os.system("start https://www.google.com/chrome/browser/desktop/index.html")
        info("Press any key once the chrome download finished")
        k=input()
        os.chdir(download_dir)
        chrome_v="81"
        os.system("ChromeSetup.exe")
        os.chdir(home_dir)
    else:
        info("For mac and linux we dont provide support try manual installation of chrome")
        info("Press any key once instaled the chrome")
        k=input()

installed_packages.append(packages_to_install.pop(0))
if not ismscpp:
    qBox("Downloading Microsoft Visual C++ ")
    if os_name=="win":
        if archi=="32bit":
            print("Downloading MS c++ for 32")
            os.system("start https://aka.ms/vs/16/release/VC_redist.x86.exe")
            time.sleep(20)
            info("Press any key once driver been downloaded")
            c=input()
            os.chdir(download_dir)
            os.system("VC_redist.x86.exe")
            os.chdir(home_dir)
        elif archi=="64bit":
            print("Downloading MS C++ for 64 bit")
            os.system("start https://aka.ms/vs/16/release/VC_redist.x64.exe")
            time.sleep(20)
            info("Press any key once driver downloaded")
            c=input()
            os.chdir(download_dir)
            os.system("VC_redist.x64.exe")
            os.chdir(home_dir)
        else:
            print("Downloading MS C++ for arm 64 bit")
            os.system("start https://aka.ms/vs/16/release/VC_redist.arm64.exe")
            time.sleep(20)
            info("Press any key once the download finishes")
            c=input()
            os.chdir(download_dir)
            os.system("VC_redist.arm64.exe")
            os.chdir(home_dir)
installed_packages.append(packages_to_install.pop(0))
qBox("Downloading Selenium Driver")
if chrome_v=="79":
    if os_name=="win":
        print("Downloading chrome driver 79 for win")
        time.sleep(3)
        os.system("start https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_win32.zip")
        time.sleep(20)
        info("Presss any key once the driver downloaded ")
        c=input()
        print("Driver downloaded")
        time.sleep(2)
        os.chdir(download_dir)
        os.system("move \"chromedriver_win32.zip\" \""+driver_dir+"\"")
        os.chdir(home_dir)
        print("The driver had been moved into our projects drivers folder please unzip it")
    elif os_name=="mac":
        print("Downloading chrome driver 79 for mac")
        time.sleep(2)
        os.system("start https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_mac64.zip")
        time.sleep(20)
        print("The driver had been downloaded please unzip the content into drivers folder of our project")
    else:
        print("Downloading chrome driver 79 for linux")
        time.sleep(2)
        os.system("start https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip")
        time.sleep(20)
        print("The driver had been downloaded please unzip the content into drivers folder of our project")
elif chrome_v=="80":
    if os_name=="win":
        print("Downloading chrome driver 80 for win")
        time.sleep(3)
        os.system("start https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_win32.zip")
        time.sleep(20)
        info("Press any key once the driver downloaded")
        c=input()
        print("Driver downloaded")
        os.chdir(download_dir)
        os.system("move chromedriver_win32.zip \""+driver_dir+"\"")
        os.chdir(home_dir)
        print("The driver had been moved into our projects drivers folder please unzip it")
    elif os_name=="mac":
        print("Downloading chrome driver 80 for mac")
        time.sleep(2)
        os.system("start https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_mac64.zip")
        time.sleep(20)
        print("The driver had been downloaded please unzip the content into drivers folder of our project")
    else:
        print("Downloading chrome driver 80for linux")
        time.sleep(2)
        os.system("start https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip")
        time.sleep(20)
        print("The driver had been downloaded please unzip the content into drivers folder of our project")
elif chrome_v=="81":
    if os_name=="win":
        print("Downloading chrome driver 81 for win")
        time.sleep(2)
        os.system("start https://chromedriver.storage.googleapis.com/81.0.4044.69/chromedriver_win32.zip")
        time.sleep(20)
        info("Press any key once the driver downloaded")
        c=input()
        print("Driver downloaded")
        os.chdir(download_dir)
        os.system("move chromedriver_win32.zip \""+driver_dir+"\"")
        os.chdir(cur_dir)
        print("The driver had been moved into our projects drivers folder please unzip it")
    elif os_name=="mac":
        print("Downloading chrome driver 81 for mac")
        time.sleep(3)
        os.system("start https://chromedriver.storage.googleapis.com/81.0.4044.69/chromedriver_mac64.zip")
        time.sleep(20)
        print("The driver had been downloaded please unzip the content into drivers folder of our project")
    else:
        print("Downloading chrome driver 81 for linux")
        time.sleep(3)
        os.system("start https://chromedriver.storage.googleapis.com/81.0.4044.69/chromedriver_linux64.zip")
        time.sleep(20)
        print("The driver had been downloaded please unzip the content into drivers folder of our project")
installed_packages.append(packages_to_install.pop(0))

info("The driver had been downloaded please unzip the content into drivers folder of our project")

time.sleep(3)

try:
    print("\nPlease wait for a while installing few supporting packages")
    time.sleep(1)
    print("For any propmts please allow permission")
    time.sleep(2)
    print("Packages that will be installed are:")
    print("1.Selenium           EU    Browser Automation")
    print("2.Pyautogui          EU    Mouse keyboard automation")
    print("3.SpeechRecognition  EU    for listening to voices")
    print("4.Pygame             EU    for giving voice to vpa")
    print("5.gtts               DEV   For making voices using voice maker")
    print("6.PyAudio            EU    For playing music via speaker ")
    time.sleep(3)
    try:
        status=os.system("pip install speechRecognition")
        if status==1:
            adminerror=True
            print(1//0)
        installed_packages.append(packages_to_install.pop(0))
    except:
        if os_name=="win":
            os.system("pip install --user speechRecognition")
            installed_packages.append(packages_to_install.pop(0))
        else:
            print("Your os is not supported by us try manually installing speechRecognition")
    try:
        if adminerror:
            print(1//0)
        os.system("pip install pyautogui")
        installed_packages.append(packages_to_install.pop(0))
    except:
        if os_name=="win":
            os.system("pip install --user pyautogui")
            installed_packages.append(packages_to_install.pop(0))
        else:
            print("Your os is not supported by us try manually installing pyautogui")
    try:
        if adminerror:
            print(1//0)
        os.system("pip install selenium")
        installed_packages.append(packages_to_install.pop(0))
    except:
        if os_name=="win":
            os.system("pip install --user selenium")
            installed_packages.append(packages_to_install.pop(0))
        else:
            print("Your os is not supported by us try manually installing selenium")
    try:
        if adminerror:
            print(1//0)
        os.system("pip install pygame")
        installed_packages.append(packages_to_install.pop(0))
    except:
        if os_name=="win":
            os.system("pip install --user pygame")
            installed_packages.append(packages_to_install.pop(0))
        else:
            print("Your os is not supported by us try manually installing pygame")
    try:
        if adminerror:
            print(1//0)
        os.system("pip install gtts")
        installed_packages.append(packages_to_install.pop(0))
    except:
        if os_name=="win":
            os.system("pip install --user ")
            installed_packages.append(packages_to_install.pop(0))
        else:
            print("Your os is not supported by us try manually installing gtts")
    line('*')
    print("PyAudio INSTALATION")
    os.system("start https://download.lfd.uci.edu/pythonlibs/s2jqpv5t/PyAudio-0.2.11-cp38-cp38-win32.whl")
    c=input("Press any key once download is done")
    os.chdir(download_dir)
    status=9
    if adminerror and os_name=="win":
        status=os.system("pip install -user PyAudio-0.2.11-cp38-cp38-win32.whl")
    else:
        status=os.system("pip install PyAudio-0.2.11-cp-38-cp-38-win32.whl")
    os.chdir(home_dir)
    if status==0:
        installed_packages.append(packages_to_install.pop(0))

except:
    info("Unexpected error occured please manually install the packeages left")
    qBox("Script will tell what needs to be installed")
    time.sleep(3)


line('=')

print("SUMMARY ")

line('=')

qBox("Installed Packages")

for i in installed_packages:
    print(i)

qBox("Packages to install manually")

for i in packages_to_install:
    print(i)

line('*')

qBox('The END')

info('Thank you for choosing triangle as your VPA')


c=input("press any key to quit")
