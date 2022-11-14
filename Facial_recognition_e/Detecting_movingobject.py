import cv2, time
import pandas 
from datetime import datetime

video_detect = cv2.VideoCapture(0)
import cv2,time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
first_frame = None 
last_background_capture_time =-2.5
status_list = [None,None]
time_s = []

while True:
    check, frame = video.read()
    status=0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(25,25),0)
    #time.sleep(3)
    #back_ground_frame updates every 2.5 sec
    if time.time() - last_background_capture_time >= 2.5:
        first_frame = gray
        last_background_capture_time = time.time()
        #continue
    delta_frame= cv2.absdiff(first_frame,gray)
    Threshold_Delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    Threshold_Delta = cv2.dilate(Threshold_Delta, None, iterations=2)

    (cnts,_) = cv2.findContours(Threshold_Delta.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0),3) #color of the rectangle

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[-1]== 1 and status_list[-2]== 0:
        time_s.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]== 1:
         time_s.append(datetime.now())
    #cv2.imshow("Gray Frame", gray)
    #cv2.imshow("Capturing", delta_frame)
   # cv2.imshow("Threshold Frame", Threshold_Delta)
    cv2.imshow("Capture Frame", frame)

    
    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            time_s.append(datetime.now())
        break

#print(status_list)
#print(time)
df = pandas.DataFrame(columns = ["start","end"])
for i in range(0, len(time_s), 2):
    df=df.append({"Start": [time_s[i]], "End": [time_s[i+1]]},ignore_index =True)
    #df2 = df.concat([df,df1], ignore_index =True)

df.to_csv("Time.csv")
video.release()
cv2.destroyAllWindows