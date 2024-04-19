import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_email = "bekeldor101@gmail.com"

email_message = MIMEMultipart()
email_message['From'] = from_email
email_message['To'] = "bekeldor101@gmail.com"
email_message['Subject'] = "Nma gap"
email_message.attach(MIMEText("Nma gap", "plain"))

server = smtplib.SMTP('smtp.gmail.com', 465)
server.login(from_email, '')


def send_email(to_email):
    try:
        server.sendmail(from_email, to_email, email_message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


email = "bekeldor101@gmail.com"
send_email(email)

users = [    "sanjarbeksocial@gmail.com",    "shukrullonosirov@gmail.com",
             "uzalisherov@gmail.com",    "maftuna200412@gmail.com",
             "boxodirazimov683@gmail.com",    "shohpad@gmail.com",
             "muhammadrahimiminjonov@gmail.com"]