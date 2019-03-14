import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class msg():
    
    def generatemsg(self,name):
            return "Hi, " + name + " thanks for showing interest in my website.<br /> I'll be sure to inform you once the site is functional."
    
    
    def sendemail(self,emailrec,name):
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login('xyz05556@gmail.com','1@3$5^7*')
        msg =MIMEMultipart()
        reciever =""
        msg['From'] ='xyz05556@gmail.com'
        msg['Subject'] = 'Thanks for Showing Interest!'
        msg['To'] = emailrec
        name1 = self.generatemsg(name)
        msg.attach(MIMEText(name1, 'html'))
        s.send_message(msg)
        s.quit()

