#This example still uses gmail but this time includes an attachment
import os,smtplib
from email.mime.text import MIMEText
from email.encoders import encode_base64
from email.mime.multipart import MIMEMultipart
from tkinter.filedialog import askopenfilename
from email.mime.base import MIMEBase
# function that sends the email. Feed it with relevant parameters
def sendMail(sender,pwd,subject,body,receiver,q):
    message=MIMEMultipart() # define the whole message as a mimemultipart and add releven
    #metadata
    message['Subject']=subject
    message['From']=sender
    message['To']=receiver
    text=MIMEText(body)
    message.attach(text)# attach the body or actual message to the message object
    if q=='y':
        file=askopenfilename()# create window which allows you to browse file system\
        #and select file
        data=open(file,'rb').read() # read file in binary mode
        part=MIMEBase('application','octet-stream')
        part.set_payload(data) # set the payload as the file read in binary mode
        encode_base64(part) #encode the attachment to base64
        part.add_header('Content-disposition','attachment; filename='+os.path.basename(file))
        message.attach(part)


    print('Connecting ...')
    server=smtplib.SMTP('smtp.gmail.com',587) # setup email server
    server.ehlo() # identify yourself to gmail client
    server.starttls() # start transport layer security
    server.ehlo() #re-identify yourself after encryption
    server.login(sender,pwd) # login to sender account
    print('Connected')
    server.sendmail(sender,receiver,message.as_string()) # perform actual sending of mail
    print('Mail Sent.')
    server.quit()
    #prompts
sender=input('Input Your email ')
receiver=input('Provide Recepient ')
pwd=input('Provide password ' )
subject=input('Mail Subject ')
body=input('Type your message ')
con=input('Do you want to send an attachment? Enter y for YES ')
#call method
sendMail(sender,pwd,subject,body,receiver,con)


