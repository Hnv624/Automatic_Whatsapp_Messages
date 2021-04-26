import pyautogui
import time

file=open('BEEscript.txt')
dp='jsdp.png'
im=pyautogui.screenshot()
x=im.getpixel((255,1058))
#print(x)
#41,196,76

if pyautogui.pixelMatchesColor(255,1058,(x)) is True:
    pyautogui.click(255,1058,duration=0.5)

pyautogui.click(300,800,duration=0.5)
pyautogui.scroll(10000)
time.sleep(0.5)


timelimit=True
t1=time.time()
while timelimit is True:
    t2=time.time()
    if t2-t1>30:
        timelimit=False
    time.sleep(0.5)
    try:
        p,q=pyautogui.locateCenterOnScreen(dp)
        pyautogui.moveTo(p+200,q,0.5)
        pyautogui.click()
        print('Mila')
        timelimit=False
    except:
        pyautogui.scroll(-200)
        pyautogui.click()
        continue

pyautogui.click(900,1000,duration=0.1)

for line in file:
    line=line.rstrip()
    line=line.split()
    for word in line:
        pyautogui.typewrite(word+'\n',interval=0.1)


#l,t,w,h=pyautogui.locateOnScreen('test.png')
#pyautogui.moveTo(l+w/2,t+h/2,duration=1)
#OR
