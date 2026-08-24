import cv2
import time
pin=1234
attempt=0
max_attempt=3

while attempt<max_attempt:
     try:
         user_pin = int(input("Enter your pin:"))
         if pin == user_pin:
             print("Permission granted.")
             break
         else:
             print("Wrong pin, try again!")
             attempt += 1
     except ValueError:
         print("wrong!")
         attempt+=1
if attempt==max_attempt:
    print("You reached your maximum attempts")

    print("Waiting for more quarry!")
    cap=cv2.VideoCapture(0)
    quarry = input("Enter your pet name:")
    with open('karan.txt', mode='a') as file:
        file.write(quarry+"\n")
    time.sleep(5)
    for i in range(5):
        ret, frame =cap.read()
        if ret:
            cv2.imwrite("karan.jpg",frame)
            print("Your image is capture")
        else:
            print("Capturing image is failed")
    cap.release()
