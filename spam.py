import pyautogui
import time

###works best with whatsapp web in full screen on 1920x1080 display###
###will need slight modifications for different resolutions###
file=open('BEEscript.txt')      #file that contains the text to be spammed
dp='jsdp.png'                   #display picture (dp) of targeted recipient, as seen on whatsapp web
                                #(do not open full image, just screenshot the small thumbnail)
                                #do not select the chat when you take a screenshot, as it would cause
                                #the chat to be highlighted and change the backgroud color around the dp


wa_x=255                #enter horizontal position of whatsapp icon in taskbar
wa_y=1058               #enter vertical position of whatsapp icon in taskbar

pyautogui.click(wa_x,wa_y,duration=0.5)         #opens whatsapp

###search chat###
pyautogui.click(300,800,duration=0.5)
pyautogui.scroll(10000)         #scroll to top of chat list
time.sleep(0.5)

timelimit=True
t1=time.time()
while timelimit is True:
    t2=time.time()
    if t2-t1>30:                #searches for the chat for 30 seconds before timing out
        timelimit=False
    time.sleep(0.5)
    try:
        p,q=pyautogui.locateCenterOnScreen(dp)      #located the chat using the dp provided
        pyautogui.moveTo(p+200,q,0.5)
        pyautogui.click()                            #opens the chat box
        timelimit=False
    except:
        pyautogui.scroll(-200)
        pyautogui.click()         #click on random chat to solve issue of required dp not being recognised due to highlighted background (if required chat is already selected)
        continue

pyautogui.click(900,1000,duration=0.1)              #navigates to the typing area

for line in file:
    line=line.rstrip()                              #splits sentences into words
    line=line.split()
    for word in line:
        pyautogui.typewrite(word+'\n',interval=0.1)


#l,t,w,h=pyautogui.locateOnScreen('test.png')
#pyautogui.moveTo(l+w/2,t+h/2,duration=1)
#OR
