#import packages
from threading import Thread, Lock #threading
import cv2 #opencv
import math #mathematical operations

targetCascade = cv2.CascadeClassifier('cascade-new.xml') #trained model

winw = 640 #set width
winh = 480 #set height 

#multithreading process
class WebcamVideoStream :
    def __init__(self, src = 0, width = 320, height = 240) :
        self.stream = cv2.VideoCapture(src) #start capturing video
        self.stream.set(3,winw) # set width
        self.stream.set(4,winh) # set height
        (self.grabbed, self.frame) = self.stream.read()
        self.started = False
        self.read_lock = Lock()

    def start(self) :
        if self.started :
            print ("already started!!")
            return None
        self.started = True
        self.thread = Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self) :
        while self.started :
            (grabbed, frame) = self.stream.read()
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, frame
            self.read_lock.release()

    def read(self) :
        self.read_lock.acquire()
        frame = self.frame.copy()
        self.read_lock.release()
        return frame

    def stop(self) :
        self.started = False
        self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback) :
        self.stream.release()

if __name__ == "__main__" :
    vs = WebcamVideoStream().start()
    count = 0 #start counting detections
    while True :
        frame = vs.read() #read frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert image to gray
        droneeye = targetCascade.detectMultiScale(
            gray,     
            scaleFactor=1.2,
            minNeighbors=5,     
            minSize=(20, 20) #detect target, specify parameters: step for scaling, reliability, min target size
        )

        for (x,y,w,h) in droneeye:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle around target

            #Transformation of pixels to real-world distance
            FOVdeg = 170 #const, field of view of camera
            FOVrad = math.radians(FOVdeg) #deg to rad
            hreal = 2 #comes from altitude measurements {external input}
            wreal = 2*math.tan(FOVrad/2)*hreal #diamaeter of circle captured by camera
            windiagonal = math.sqrt(math.pow(winw, 2)+math.pow(winh, 2)) #diagonal of rectangle of window
            #Rule: diameter of circle=diameter of diagonal of rectangle when rectangle is drown in circle
            oneunit = wreal/windiagonal #m/px, ration distance:pixel
            xpx = x+w/2-winw/2 #px coordinate system with 0,0 at center
            ypy = abs(y-winh+h)+h/2-winh/2 #px coordinate system with 0,0 at center
            dx = xpx*oneunit #real distance of target relative to center
            dy = ypy*oneunit #real distance of target relative to center
            

            #give commands how to move to get to the center in x and y directions
            if -1 <= dx <= 1:
                print("Close x")
            elif dx>0:
                print("go right: " + str(abs(dx)))
            else:
                print("go left: " + str(abs(dx)))
            
            if -1 <= dy <= 1:
                print("Close y")
            elif dy>0:
                print ("go up: " + str(abs(dy)))
            else:
                print ("go down: " + str(abs(dy)))
            
            #start capturing pictures if close to the center
            if -3 <= dx <= 3:
                if -3 <= dy <= 3:
                    cv2.imwrite("dataset-test/User." + '.' + str(count) + ".jpg", frame)

            #increase number of detections when detected
            count += 1
            
            print("Detection:" + str(count))
           
        cv2.imshow('img',frame) #show video of detection process
  
        if cv2.waitKey(1) == 27 : #press Esc to stop
            break

    vs.stop()
    cv2.destroyAllWindows()
