import smtplib, email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def sendMail(receiverId,recCount,senderMail,senderPass):
  receiver_email =  receiverId

  server = smtplib.SMTP_SSL("smtp.gmail.com",465)
  server.login(senderMail,senderPass)

  message = MIMEMultipart("alternative")
  message['Subject'] = str(senderCount) + ' ROHIT SINGH ' + str(recCount)
  message['From'] = senderMail
  message['To'] = receiver_email

  # Open a file: file
  file = open('mailBody.txt',mode='r')

  # read all lines at once
  text = file.read()

  # close the file
  file.close()

  part1 = MIMEText(text, "plain")
  message.attach(part1)

  f = open("attachment.txt", "w")
  f.write(str(senderCount) + ' ROHIT SINGH ' + str(recCount))
  f.close()

  part = MIMEBase('application', "octet-stream")
  part.set_payload(open("attachment.txt", "rb").read())
  encoders.encode_base64(part)
  
  part.add_header('Content-Disposition', 'attachment; filename="attachment.txt"')

  message.attach(part)
    
  server.sendmail(senderMail, receiver_email, message.as_string())
  print("Mail sent to " + receiver_email + " from  "+  senderMail)

  server.quit()
   
f = open("sender.txt", "r")
print("Starting... ");
senderCount = 1 
for x in f:
  userPass = x.split(",")
  senderMail = str(userPass[0])
  senderPass = str(userPass[1])
  f = open("receiver.txt", "r")
  recCount = 1
  for x in f:
    # Send email to each receiver
    receiverId = x
    sendMail(receiverId,recCount,senderMail,senderPass)
    recCount = recCount + 1
  senderCount = senderCount + 1


