# Computer-Vision-Work-Package
1. Instructions

1.1. Operating system installation on Raspberry Pi
1) Operation system “Raspbian Stretch with desktop” was downloaded on laptop from https://www.raspberrypi.org/downloads/raspbian/ in ZIP format and unzipped
2) MicroSD card was inserted in laptop through adapter
3) A graphical SD card writing tool was downloaded from https://www.balena.io/etcher/ and installed
4) Using Etcher, image from ZIP file was copied to MicroSD
5) MicroSD was inserted in Raspberry Pi at the back side
6) Finally, Raspberry Pi was powered with 2.5A, 5V power supply and booted up
In case of any problems, more details for installation can be found here https://www.techrepublic.com/article/how-to-set-up-your-raspberry-pi-3-model-b/

1.2. OpenCV installation on Raspberry Pi
1) Filesystem was expanded to include all available space by “sudo raspi-config” command run in terminal
2) After reboot, existing packages were updated by “sudo apt-get update && sudo apt-get upgrade”
3) Then all necessary dependencies for images and video were installed by “sudo apt-get install”
4) Python was installed by “sudo apt-get install python3-dev”
5) OpenCV and OpenCV_contrib were downloaded from official repositories
6) Numpy was installed by “sudo pip3 install numpy scipy”
7) OpenCV was compiled and built (careful with path to directories) with “cmake” and “make -j4”
8) Computer was rebooted and it was checked whether OpenCV works by “import cv2” and “cv2.__version__” run in Python
In case of any problems, more details for installation can be found here  https://www.alatortsev.com/2018/09/05/installing-opencv-3-4-3-on-raspberry-pi-3-b/. For installation of OpenCV on laptop use https://opencv.org/releases.html and for Python https://www.python.org/downloads/.

1.3. Training model 
1) Video with and without target was recorded on USB camera
2) 200 positive and 1000 negative sample frames were extracted from video by VLC player as described here https://www.raymond.cc/blog/extract-video-frames-to-images-using-vlc-media-player/. 
3) Images were massively resized to 100x100 pixels with software downloaded from https://www.bricelam.net/ImageResizer/
4) Folders were created and labeled “p” and “n” respectively
5) Cascade Trainer GUI was downloaded from http://amin-ahmadi.com/cascade-trainer-gui/ and installed
6) Path to folder with samples was given in Input section, all other parameters can be kept default, otherwise experiment with Number of stages for accuracy of model, Buffer size to make training process faster, Feature Type to choose suitable method for specific application
7) The training process was started and lasted for more than 10 hours, to give .xml output file
In case of any problems, more details on Cascade Trainer GUI can be found on http://amin-ahmadi.com/cascade-trainer-gui/. For more details about meaning of parameters used in this software please visit https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html. For understanding theory behind the LBP and HAAR recognition methods, please refer to explanation prepared for in Section 3.2. and 3.3.

1.4. Running the code
1) Folder "dataset-test” was created to store pictures of target captured when it’s close to the center
2) “cascade-new.xml” file, which is HAAR trained model, was placed in the same folder where Python code is located
3) USB camera was connected to Raspberry Pi and put in “PC Camera” mode
4) Code was run in Python by clicking on logo of Raspberry, then Programming, then Python 3 (IDLE)
5) Target was detected and following commands given by programme, the center of the screen was reached
Explanation of code can be found in comments given after “#”. Tutorial on recognition can be found here https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826 . Tutorial for threading can be found here https://www.pyimagesearch.com/2015/12/28/increasing-raspberry-pi-fps-with-python-and-opencv/ .

Hardware: Akaso Brave 4 camera, Raspberry Pi 3 Model B, Scutes Deluxe USB Power Bank, Raspberry Pi 7” Touchscreen Display, USB cable
