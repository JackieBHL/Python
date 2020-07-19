#import smtplib

#server = smtplib.SMTP()#set up server

    #find your email host
    
    #find your email port  common port == 25
    
#server.connect(host,port)

    #if error == UnicodeDecodeError server.connect(host,port,'utf-8')
    
#server.login(username, password)

    #username and password requied to access the account
    
#server.sendmail(from_addr, to_addr, msg.as_string()) 

    #from_addr：the username// address of the email
    
    #to_addr：to the person who recieve it 
    
    #msg.as_string()：message to a string 
    
#server.quit()

    #exit the server 

#from email.mime.text import MIMEText

    #new libiary
    
#MIMEText('send by python','plain','utf-8')

    #sent message info 
    
    
# server you can google it 
    # Gmail:        smtp.gmail.com         port 465
    # Yahoo:        smtp.mail.yahoo.com    port 465 or 587
    # Microsoft:    smtp-mail.outlook.com  Port Number 587
    # QQ:           smtp.qq.com            Port 465    
