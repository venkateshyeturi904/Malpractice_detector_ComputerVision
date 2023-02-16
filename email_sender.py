import smtplib, ssl


def send_email(recipient, email):    
    recipient = "<" + recipient + ">"
    port = 465  
    smtp_server = "smtp.gmail.com"
    sender = "assyyy47@gmail.com"
    password = "txswtcafbqltlyvq"
    #password = "yash_1234"


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, email)