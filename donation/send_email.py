#import pandas as pd 
import smtplib
#e = pd.read_excel("email.xlsx")
#emails = e['emails'].values
def send(emails,number):
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("sanjay.p@ug.cusat.ac.in","sanju123")
    msg = 'Contact this mobile no:' + number
    subject ='Urgent!'
    body="subject:{}\n\n{}".format(subject,msg)
    for email in emails :
        server.sendmail("sanjay.p@ug.cusat.ac.in",email,body)

    server.quit()

    