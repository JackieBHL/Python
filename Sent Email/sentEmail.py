#real coding 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# your info
user = '@gmail.com'
password = ''
# reciver's email
to_addr = '@gmail.com'

smtp_server = 'smtp.gmail.com'
#info to sent 
text = 'testing'
msg = MIMEText(text,'plain','utf-8')
msg['From'] = Header(user)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('Header')


# sequire sent // start server 
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
# login
server.login(user,password)
# sent
server.sendmail(user, to_addr, msg.as_string())
# close
server.quit()

#Status
    #Failed Due to Google rule