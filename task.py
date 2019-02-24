# -*- coding: utf-8 -*-

import smtplib
def send_mail_from_app4hiiigmailcom(send_conf, n_try=3):
    for i in range(n_try):
        try:
            server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
            server.login(user='app4hiii@gmail.com', password='bc8yqrevyud')
            status = server.sendmail(from_addr='app4hiii@gmail.com', 
                                     to_addrs=send_conf['to_addrs'], 
                                     msg='Subject: {}\n\n{}'.format(send_conf['subject'], send_conf['msg']))
            server.close()
            if not(status):
                return True
        except:
            pass
    return False