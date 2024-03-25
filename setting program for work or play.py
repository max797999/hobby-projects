import subprocess
def work():
    subprocess.run (["cmd", "/c",'C:\Program Files\worksetup.bat'])


def play():
    subprocess.run (["cmd", "/c",'C:\Program Files\playsetup.bat'])
Settingmode=input ('Please choose what you want to do work or play')



if Settingmode==("work"):
    work()
    
elif Settingmode==("play"):
    play()
    