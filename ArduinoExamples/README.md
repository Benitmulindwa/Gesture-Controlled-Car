This provides Arduino codes(`master.ino` and `slave.ino`) for controlling a car using the HC-12 wireless communication module. 
The code receives commands from a remote computer(connected via HC-12) and uses those commands to control the car's movement using two DC motors.

### Obstacle Avoidance:

There are some lines of code for obstacle avoidance using ultrasonic sensors. If you want to enable this functionality, you can uncomment these lines and connect the ultrasonic sensor accordingly.

### How it works:

The `master.ino` file is uploaded to an Arduino board which is connected to the computer using the serial port,
the commands received are sent remotely( via the HC-12 module) to the other Arduino board containing the `slave.ino` file. 
The commands received will be used to control the car's movements.

### A litle scheme:

`main.py -> master.ino -> slave.ino -> car's motors`
