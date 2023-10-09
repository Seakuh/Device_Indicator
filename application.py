import subprocess
import serial
import time

# Find the Arduino port (change this according to your setup)
arduino_port = '/dev/ttyUSB0'  # Replace with the actual port

# Initialize serial connection
ser = serial.Serial(arduino_port, 9600, timeout=1)
time.sleep(2)  # Allow time for Arduino to reset

def check_camera_status():
    try:
        # Check if the camera is active using 'lsusb' command
        subprocess.check_output(['lsusb | grep -i camera'], shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def check_mic_status():
    try:
        # Check if the microphone is active using 'arecord' command
        subprocess.check_output(['arecord -l | grep -i card'], shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

try:
    while True:
        camera_status = check_camera_status()
        mic_status = check_mic_status()

        if camera_status:
            ser.write(b'B')  # Send 'B' to Arduino for blue LED
        else:
            ser.write(b'R')  # Send 'R' to Arduino for red LED

        time.sleep(1)  # Check every second
except KeyboardInterrupt:
    ser.close()