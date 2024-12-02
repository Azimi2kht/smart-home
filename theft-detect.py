from picamera2 import Picamera2, Preview
import torch
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
import ssl
import smtplib
import time


def send_email():
	email_address = "EMAIL_ADDRESS"
	email_key = "EMAIL_KEY"
	email_receiver = "RECOVER_EMAIL_ADDRESS"
	
	em = EmailMessage()	
	em['From'] = email_address
	em['To'] = email_receiver
	em['Subject'] = 'warning! Theft Detected!'
	body = """Dear, IOT
		Warning! Theft Detected!
		Out model detected a person in your house. call 110 if it is not you or your relatives!
	"""
	em.set_content(body)
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
		smtp.login(email_address, email_key)
		smtp.sendmail(email_address, email_receiver, em.as_string())


# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5s") 

picam2 = Picamera2()
picam2.start()


while True:
	img = picam2.capture_array()
	results = model(img)
	labels = results.xyxyn[0][:, -1].numpy()
	if 0 in labels:
		print("person detected")
		send_email()
		time.sleep(30)
	

