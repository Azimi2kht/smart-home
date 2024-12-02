# Smart Home Project
![smart-home-ahmad](https://github.com/user-attachments/assets/74f9eba9-c7b4-4e62-8434-a96f8c5deb0d)
This repository contains code and resources for a smart home system that focuses on theft detection using image processing and notification via email.

## Features

- **Theft Detection**: Utilizes a camera to capture images and employs a machine learning model to detect the presence of a person.
- **Email Notifications**: Sends an email alert when a person is detected, indicating a potential intrusion.

## Prerequisites

### Hardware
- Raspberry Pi with a connected camera module

### Software
- Python 3.x
- [picamera2](https://github.com/raspberrypi/picamera2)
- [PyTorch](https://pytorch.org/)
- [YOLOv5](https://github.com/ultralytics/yolov5)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Azimi2kht/smart-home.git
   cd smart-home

