
# Smart Home Project
![smart-home-ahmad](https://github.com/user-attachments/assets/74f9eba9-c7b4-4e62-8434-a96f8c5deb0d)

This repository contains the code and resources for a smart home system with theft detection functionality. The system uses image processing to detect unauthorized persons and sends email notifications when an intrusion is detected.

---

## Features

- **Theft Detection**: 
  - Leverages a camera and a machine learning model to detect the presence of a person.
- **Email Alerts**:
  - Sends an email notification to a configured recipient upon detection of an intrusion.
- **Real-Time Processing**:
  - Processes images in real-time using YOLOv5 and Raspberry Pi.
- **Efficient Automated Lighting and Cooling Control**:
  - An intelligent control system for managing lighting and cooling, optimizing energy usage.
- **Controlling and Monitoring All Inputs and Actuners With Smartphone**:
  - Seamless control and real-time monitoring of inputs and actuators via a user-friendly smartphone interface, leveraging Thingsboard for data analysis.
- **Sound Control Integration**:
  - Voice-activated and deactivated room lighting for smartphone-free experiences.
---

## Prerequisites

### Hardware
- Raspberry Pi (any model supporting `picamera2`) with a connected camera module.

### Software
- Python 3.x
- [picamera2](https://github.com/raspberrypi/picamera2)
- [PyTorch](https://pytorch.org/)
- [YOLOv5](https://github.com/ultralytics/yolov5)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Azimi2kht/smart-home.git
cd smart-home
```

### 2. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```
Ensure `picamera2`, `torch`, and YOLOv5 dependencies are correctly set up.

### 3. Configure Email Settings
Update the `send_email` function in `theft-detect.py` with your email credentials:
```python
def send_email():
    # Example: Update sender_email, receiver_email, and password
    sender_email = "your_email@gmail.com"
    receiver_email = "recipient_email@gmail.com"
    password = "your_email_password"
```

---

## Usage

Run the theft detection script:
```bash
python theft-detect.py
```

- The system will start monitoring for the presence of a person.
- If a person is detected, an email alert will be sent to the configured recipient.

---

## File Structure

- `theft-detect.py`:
  - Main script for theft detection and email notification.
- `requirements.txt`:
  - List of Python dependencies to install.
- `README.md`:
  - This documentation file.
- `assets/`:
  - (Optional) Directory for storing any additional resources such as example images or videos.

---

## Contributing

Contributions are welcome! If you'd like to contribute:
1. Fork this repository.
2. Create a new branch with your feature/bugfix (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature-name"`).
4. Push to the branch (`git push origin feature-name`).
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. For more details, refer to the [LICENSE](LICENSE) file.

---

## Acknowledgements
I thank my team that made this project possible:
- Ahmad Mardani
- Arsalan Talaee
- Yosef Ghaderi

Libaried Used:
- [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5) - Used for real-time object detection.
- [picamera2 by Raspberry Pi](https://github.com/raspberrypi/picamera2) - Camera module interface for Raspberry Pi.
- The open-source community for providing tools and resources.

---

For further details or queries, feel free to raise an issue or contact the repository owner.

---
