# Smile Door

### This project detects a persons smile and opens the door for him. In this case we have used OpenCV in Raspberry Pi and used a SG90 servo motor with Arduino.Serial communication has been made between Raspberry Pi and Arduino.

## 💻 Tech Spec

![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)

[Watch the Video](https://youtu.be/4RrMKNeumP0)

[Smile Door](smiledoor.png)

## 🛠 Components Used

- Arduino Uno
- Raspberry Pi
- SG90 Servo Motor
- Webcam

## 🚀 How to Start

- Boot Raspbian OS Buster Desktop in Raspberry Pi and install OpenCV and Arduino Editor in Raspberry Pi. Thonny Editor for python is already installed on Raspbian OS.
- Plug in the Webcam with Raspberry Pi and attach Arduino Uno with Raspberry Pi using Arduino Cable.
- Set Up Servo motor with below schematics.
- First upload `smile_door.ino` to Arduino Uno from Arduino editor.
- Then Run `smile_detection.py` using Thonny Editor ( you can use your fav editor in this case)
- Finally just smile :) 

## 🖍📐 Schematics


![Schematic](circuit_diagram.jpg)
