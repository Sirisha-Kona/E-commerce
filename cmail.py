import smtplib
from email.message import EmailMessage  #email.message is a package,EmailMessage is a class
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)  #server object creation,to connect to a server,465 port number,ssl secure socket layer
    server.login("sirishakona245@gmail.com",'qxmx medw vfdu qgxn')
    msg=EmailMessage()
    msg["FROM"]="sirishakona245@gmail.com"
    msg["TO"]=to
    msg["SUBJECT"]=subject
    msg.set_content(body)
    server.send_message(msg)  #through server it will send mail
    server.close()