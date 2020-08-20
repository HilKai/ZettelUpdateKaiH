import os, time
import smtplib
import ssl
from collections import defaultdict
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

path = './res/'

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "kaideveloperacc@gmail.com"  # Enter your address
receiver_emails = ["kaideveloperacc@gmail.com"]  # Enter receiver address
password = input("Type your password and press enter: ")


def sendMail(file, last_line):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)

        for receiver in receiver_emails:
            message = MIMEMultipart("alternative")
            message["Subject"] = last_line
            message["From"] = sender_email
            message["To"] = receiver
            message.attach(MIMEText("In {} hat sich {} eingetragen! \n Töte ihn!!".format(file, last_line), "plain"))
            try:
                server.sendmail(
                    sender_email, receiver, message.as_string()
                )
            except:
                print("Sending Mail Failed")



file_stamps = defaultdict(int)
while True:
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file_name in onlyfiles:
        last_line = ""
        with open(path + file_name, "r") as file_name:
            first_line = file_name.readline()
            for last_line in file_name:
                pass
            if not last_line:
                last_line = first_line
        file_name = file_name.name
        name, stamp = last_line.split(',')
        timehash = int(stamp.replace(':','').replace('.',''))
        if timehash > file_stamps[file_name]:
            file_stamps[file_name] = timehash
            sendMail(file_name,name)

    time.sleep(5)
