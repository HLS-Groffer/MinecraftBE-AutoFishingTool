#HLS_Groffer
import pyautogui
import time
import os
import random
from ctypes import windll # 获取屏幕上某个坐标的颜色

##手动调整以适合你的垂钓环境##
sensitivity=0.8
fishingCounter=200
##########################

def get_color(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r =int( pixel & 0x0000ff)
    #print(r)
    return r

def checkb(lista,powlista,arvar):
    reseta=0
    broken=0
    for checkfish in range(100):
        reseta=reseta+1
        br=[0]
        sumbr=0
        x,y=pyautogui.position()
        #print(x,y)
        for i in lista:
                for l in lista:
                        brr=get_color(x+i,y+l)
                        br.append(brr)
        for xb in br:
                sumbr=sumbr+xb
        arvbr=sumbr/powlista      
        print(arvbr)
        #print("differ",abs(arvbr-arvar))
        if abs(arvbr-arvar)>sensitivity:
            #time.sleep(0.1)
            print("Click!")
            return pyautogui.rightClick()
        if reseta>=20:
            arvar=arvbr
            reseta=0
        if arvbr==255:
            broken=broken+1
        else:
            broken=0
        if broken==5:
            return 1
        else:
            pass

def main():
    print("Auto rightClick in 2 sec!")
    time.sleep(2)
    pyautogui.click()
    print("Auto rightClick start!")
    lista=[100,-50,0,50,100]
    time.sleep(1)
    powlista=len(lista)*len(lista)
    for fishTimeCount in range(fishingCounter):
            ar=[]
            sumar=0
            pyautogui.rightClick()
            x,y=pyautogui.position()
            time.sleep(3)
            for i in lista:
                for l in lista:
                    arr=get_color(x+i,y+l)
                    ar.append(arr)
                    #print(arr,arg,arb)
            for xa in ar:
                sumar=sumar+xa
            arvar=sumar/powlista
            if checkb(lista,powlista,arvar)==1:
                pyautogui.rightClick()
                os.system("start AutoFishing.py")
                quit()
            else:
                time.sleep(random.uniform(0.1,0.5))
    print("Fishing done 200 times. Check durableness of your rod")

main()
os.system("start 自动钓鱼优化.py")
quit()
