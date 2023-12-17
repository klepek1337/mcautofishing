import pyautogui
import time
print("Skrypt na wędkę by klepek, Ultimate build 1.0")
print("GUI scale 3, Show subtitles")
def gigawedkaeng():
    try:
        return pyautogui.locateOnScreen('gigawedka.png', confidence=0.8, grayscale=True) is not None
    except pyautogui.ImageNotFoundException:
        return False
    
def main():
    print("Rightclick")
    wejscie()
    gigawedkadetector()
    main()
def wejscie():
    print("wejscie")
    time.sleep(5)
    pyautogui.rightClick()
def gigawedkadetector():
    while gigawedkaeng() is False:
        time.sleep(0.1)
    print("złapano pierwsze ")
    pyautogui.rightClick()


main()