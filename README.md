Gesture-Controlled Car

This project allows you to control a car using hand gestures captured by a webcam. The hand gestures are recognized using Python, OpenCV, and Mediapipe, and the commands are sent to an Arduino board via serial communication to control the car's movements.

Getting Started
Prerequisites
To run this project, you'll need:

Python 3.x
OpenCV (cv2)
Mediapipe
PySerial
You can install the required Python libraries using pip:


pip install opencv-python mediapipe pyserial

Hardware Setup

Connect the necessary hardware components to your Arduino, including motors, motor drivers, and any sensors (optional) you want to use for the car. Make sure your Arduino is properly programmed to respond to the commands received over serial communication.

Installing

1. Clone this repository to your local machine.


git clone https://github.com/Benitmulindwa/gesture-controlled-car.git

2. Change into the project directory.

cd gesture-controlled-car

3. Connect your Arduino to your computer and check the correct serial port (e.g., COM4 for Windows) in the serialPort variable inside the main.py file. Adjust the port name accordingly.

Running the Program

Run the main.py script to start the gesture-controlled car program.

python main.py

The webcam feed will open, and the program will start detecting hand landmarks and interpreting hand gestures.
Hand Gestures and Car Commands
The following hand gestures can be used to control the car:

- Fist: Stop the car
- Index and Pinky Fingers Up: Move the car forward
- Thumb and Pinky Fingers Up: Move the car backward
- Index Finger Up, Others Down: Turn the car left
- Pinky Finger Up, Others Down: Turn the car right

Safety Precautions

Ensure that you have set up the hardware components correctly, and test the car's movement in a safe environment to avoid any accidents.



Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to create a pull request.

License

This project is licensed under the MIT License.

Acknowledgments

The project was inspired by the work of OpenCV and Mediapipe.
Thanks to the contributors of the libraries used in this project.