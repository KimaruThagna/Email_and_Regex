import smtplib
# before running the script, go to your google account settings and enable access
#  from less secure apps in order for the script to work
content="My simple mail example"
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls() # this ensures everything from here on is encrypted
username='' # enter your email account
pwd='' # enter your account's password
mail.login(username,pwd)
receiver=[] # list of email addresses to receive the mail
mail.sendmail(username,receiver,content)
mail.close()