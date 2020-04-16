import os
import os.path
import time


os_name="win"
archi="32"
chrome_v=""
adminerror=False
cur_dir=os.getcwd()
os.chdir("drivers")
driver_dir=os.getcwd()
os.chdir("..")
packages_to_install=["speechrecognition","pyautogui","selenium","pygame","gtts","ChromeBrowser","Microsoft visual c++","PyAudio"]
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


print("Home dir ",home_dir)
print("Download dir ",download_dir)
os.chdir(home_dir)
time.sleep(3)

print("**************************************************")
print("Triangle VPA Initial Setup Script ")
print("**************************************************")

choice=""
while True:
    print()
    choice=input("Enter your os:\n1.Windows\n2.Mac\n3.Linux")
    try:
        choice=int(choice)
        if choice>=1 and choice<=3:
            if choice==1:
                os_name="win"
            elif choice==2:
                os_name="mac"
            else:
                os_name="lin"
            break
        else:
            print("\n**************************************************")
            print("Invalid choice choose between 1 ,2 and 3")
            print("**************************************************")
    except:
        print("\n**************************************************")
        print("Invalid choice type 1 or 2 or 3")
        print("**************************************************")

while True:
    print()
    choice=input("Enter your processor architecture\n1.32-bit\n2.64-bit\n3.arm64-bit")
    try:
        choice=int(choice)
        if choice>=1 and choice<=3:
            if choice==1:
                archi="32bit"
            elif choice==2:
                archi="64bit"
            else:
                archi="arm64"
            break
        else:
            print("\n**************************************************")
            print("Invalid choice choose between 1,2 and 3")
            print("**************************************************")
    except:
        print("\n**************************************************")
        print("Invalid choice type 1 or 2 or 3")
        print("**************************************************")

print("**************************************************")
print()
print("OS: ",os_name)
print("Architecture: ",archi)
print()
print("**************************************************")
time.sleep(2)
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
    print("7.Chrome Browser     EU    Preferres browser for our VPA")
    print("8.MS Visual c++      EU    Supporting driver for PyAudio")
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
    print("\n\n********************************************************")
    print("Packages installation completed next supporting drivers and applications")
    time.sleep(3)
    while True:
        print("Chrome installed in your system \n1.yes\n2.No")
        choice=input()
        try:
            choice=int(choice)
            if choice==1:
                print("Awwww....Fine chrome is already there")
                print("Please enter your chrome version \n1.79 \n2.80 \n3.81")
                while True:
                    chrome_v=input()
                    if chrome_v=="79":
                        print("Chrome version 79 is choosen")
                        break
                    elif chrome_v=="80":
                        print("Chrome version 80 is choosen")
                        break
                    elif chrome_v=="81":
                        print("Chrome version 81 is choosen")
                        break
                    else:
                        print("Invalid chrome version try updating chrome or choose again if u mistyped type (80 or 81 or 79)")
                break
            elif choice==2:
                if os_name=="win":
                    print("DOWNLOADING CHROME")
                    time.sleep(3)
                    os.system("start https://www.google.com/chrome/browser/desktop/index.html")
                    time.sleep(15)
                    c=input("Press any key once the download finished")
                    os.chdir(download_dir)
                    chrome_v="81"
                    os.system("ChromeSetup.exe")
                    os.chdir(home_dir)
                    break
                else:
                    print("We are sorry,Currently we dont have any support for mac or linux try manually installing chrome")
                    c=input("Press any key once u installed chrome")
                    break
        except:
            print("****************************************")
            print("Invalid choice please choose between 1 and 2")
    if chrome_v=="79":
        if os_name=="win":
            print("Downloading chrome driver 79 for win")
            time.sleep(3)
            os.system("start https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_win32.zip")
            time.sleep(20)
            c=input("Presss any key once the driver downloaded ")
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
            c=input("Press any key once the driver downloaded")
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
            c=input("Press any key once the driver downloaded")
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
    print("*****************************************************************")
    print("CHROME INSTALLATION FINISHED")
    time.sleep(3)
    print("*****************************************************************")
    print("\n")
    print("*****************************************************************")
    print("MICROSOFT VISUAL C++ INSTALATION")
    choice=input("Microsoft visual c++ installed in ur pc \n1.Yes\n2.No")
    while True:
        try:
            choice=int(choice)
            if choice==1:
                print("Aww u got ms visual c++")
                break
            elif choice==2:
                if archi=="32bit":
                    print("Downloading MS c++ for 32")
                    os.system("start https://aka.ms/vs/16/release/VC_redist.x86.exe")
                    time.sleep(20)
                    c=input("Press any key once driver been downloaded")
                    os.chdir(download_dir)
                    os.system("VC_redist.x86.exe")
                    os.chdir(home_dir)
                    break
                elif archi=="64bit":
                    print("Downloading MS C++ for 64 bit")
                    os.system("start https://aka.ms/vs/16/release/VC_redist.x64.exe")
                    time.sleep(20)
                    c=input("Press any key once driver downloaded")
                    os.chdir(download_dir)
                    os.system("VC_redist.x64.exe")
                    os.chdir(home_dir)
                    break
                else:
                    print("Downloading MS C++ for arm 64 bit")
                    os.system("start https://aka.ms/vs/16/release/VC_redist.arm64.exe")
                    time.sleep(20)
                    os.chdir(download_dir)
                    os.system("VC_redist.arm64.exe")
                    os.chdir(home_dir)
                    break
            else:
                print("Invalid choice choose between 1 and 2")
        except:
            print("Invalid please choose between 1 and 2")
    installed_packages.append(packages_to_install.pop(0))
    print("*****************************************************************")
    print("MICROSOFT VISUAL C++ FINISHED")
    time.sleep(3)
    print("*****************************************************************")
    print("\n")
    print("*****************************************************************")
    print("PyAudio INSTALATION")
    os.system("start https://download.lfd.uci.edu/pythonlibs/s2jqpv5t/PyAudio-0.2.11-cp38-cp38-win32.whl")
    c=input("Press any key once download is done")
    os.chdir(download_dir)
    if adminerror and os_name=="win":
        os.system("pip install -user PyAudio-0.2.11-cp38-cp38-win32.whl")
    else:
        os.system("pip install PyAudio-0.2.11-cp-38-cp-38-win32.whl")
    os.chdir(home_dir)
    print("*****************************************************************")
    installed_packages.append(packages_to_install.pop(0))
    print("PyAudio FINISHED")
    print("*****************************************************************")
    print("INSTALATION SUCCESSFULL NOW YOU CAN RUN OUR VPA")
    print("INFO INSTALLED PACKEGAES")
    for i in installed_packages:
        print(i)
    print()
    print("INFO PACKAGES YET TO BE INSTALLED")
    if len(packages_to_install)==0:
        print("Evrything is done")
    for i in packages_to_install:
        print(i)
except:
    print("InSTALLATION FAILED TRY MANUAL INSTALATION OR RETRY AGAIN")
    print("INFO INSTALLED PACKEGAES")
    for i in installed_packages:
        print(i)
    print()
    print("INFO PACKAGES YET TO BE INSTALLED")
    for i in packages_to_install:
        print(i)





print("Note:  The chrome driver u need to unzip manually we have downloaded the drover and put into drivers folder of our vpa")

print("Thank You for choosing our VPA")
c=input("The END PRESS ANY KEY TO QUIT")
