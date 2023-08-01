import os
import cv2 as cv
import mediapipe as mp
import serial

serialPort='COM4'

connect=serial.Serial(serialPort,9600)

image=cv.VideoCapture(0) #Access to the webcam

mpHands=mp.solutions.hands
hands=mpHands.Hands(min_detection_confidence=0.8)
mpDraw=mp.solutions.drawing_utils


while True:
    
    _, frame=image.read()
    img=cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results=hands.process(img)
    img=cv.cvtColor(img, cv.COLOR_RGB2BGR)
    
    mylist=[]
    liste=[4,8,12,16,20]
    
    cv.rectangle(img,(40,325),(300,125),(0,0,255)) 
    cv.rectangle(img, (400,125), (600,325), (255,0,0))
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                
                new=[]
               
                h,w,c=img.shape
                cx,cy=int(lm.x*w), int(lm.y*h)
                mylist.append([id,cx,cy])
                
               
                if len(mylist)>4:
                    
                    if mylist[liste[0]][2] > mylist[liste[0]-1][2]:
                        
                        new.append(1)
                        
                    else:
                        
                        new.append(0)
                
                for a in range(1,5):
                
                    if len(mylist)>20:
                        
                            if mylist[liste[a]][2] < mylist[liste[a]-2][2]:
                        
                                new.append(1)
                                
                            else:
                                
                                new.append(0)
                                
                            total=new.count(1) #count the number of up fingers
                            
                            #If the hand is within the  square, the hand gestures can now be considered
                            
                            if 300 > mylist[liste[a]][1]>40 and 325 > mylist[liste[a]][2]>125 :
                            
                                if len(new) >= 5:
                                
                                    
                                    if new[0]==1 & new[3]==1:
                                          cv.rectangle(img,(40,325),(300,125),(200,200,0),2)
                                          cv.putText(img,"FORWARD",(90,360),
                                                      cv.FONT_HERSHEY_PLAIN,3,(200,200,0),5)
                                          connect.write('1'.encode("utf-8"))
                                          
                                          
                                    elif new[0]==1 & new[4]==1:
                                          cv.rectangle(img,(40,325),(300,125),(0,200,200),2)
                                          cv.putText(img,"LEFT",(90,360),
                                                    cv.FONT_HERSHEY_PLAIN,3,(0,200,200),5) 
                                         
                                          connect.write('4'.encode("utf-8"))
                                         
                                         
                                    elif new[0]==1 & new[1]==1:
                                        cv.rectangle(img,(40,325),(300,125),(250,0,50),2)
                                        cv.putText(img,"RIGHT",(90,360),
                                                    cv.FONT_HERSHEY_PLAIN,3,(250,0,50),5)
                                        
                                        connect.write('3'.encode("utf-8"))
                                        
                                    
                                    elif new[0]==0 and new[1]==1 and new[2]==0 and new[3]==0 and new[4]==1:
                                        cv.rectangle(img,(40,325),(300,125),(0,0,0),2)
                                        cv.putText(img,"BACKWARD",(70,360),
                                                    cv.FONT_HERSHEY_PLAIN,3,(0,0,0),5)
                                        
                                        connect.write('2'.encode("utf-8"))
                                        
                                        
                                    elif new[0]==0 and new[1]==0 and new[2]==0 and new[3]==0 and new[4]==0:
                                        cv.rectangle(img,(40,325),(300,125),(0,0,255),2)
                                        cv.putText(img,"STOP",(120,360),     
                                                    cv.FONT_HERSHEY_PLAIN,3,(0,0,255),5)  
                                        
                                        connect.write('0'.encode("utf-8"))
                                        
                           
                        
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
   
    cv.imshow("Captor", img)
    cv.waitKey(1)
    
os.system('pause')