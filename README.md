Smart Home Project

This repository contains code and resources for a smart home system, focusing on theft detection using image processing and notification via email.

Features

	•	Theft Detection: Utilizes a camera to capture images and employs a machine learning model to detect the presence of a person.
	•	Email Notifications: Sends an email alert when a person is detected, indicating a potential intrusion.

Prerequisites

	•	Hardware: Raspberry Pi with a connected camera module.
	•	Software:
	•	Python 3.x
	•	picamera2
	•	PyTorch
	•	YOLOv5

Setup Instructions

	1.	Clone the Repository:

git clone https://github.com/Azimi2kht/smart-home.git
cd smart-home


	2.	Install Dependencies:

pip install -r requirements.txt

Note: Ensure that picamera2, torch, and YOLOv5 are properly installed.

	3.	Configure Email Settings:
	•	Update the send_email function in theft-detect.py with your email credentials and recipient information.

Usage

Run the theft detection script:

python theft-detect.py

The system will continuously monitor for the presence of a person and send an email alert if one is detected.

Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

License

This project is licensed under the MIT License.

Acknowledgements

	•	YOLOv5 by Ultralytics
	•	picamera2 by Raspberry Pi

For more information, please refer to the theft-detect.py script.
![smart-home-ahmad](https://github.com/user-attachments/assets/74f9eba9-c7b4-4e62-8434-a96f8c5deb0d)
