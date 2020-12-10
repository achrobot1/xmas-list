import smtplib

EMAIL_ADDRESS = ''
EMAIL_PASS = ''

try:
    from .credentials import *
except ImportError:
    print('unable to send email: Cannot get credentials')


def send_email(msg, recipients):
    if EMAIL_ADDRESS == '':
        return
    if EMAIL_PASS == '':
        return 

    body = '\r\n'
    body += msg
    body += '\r\n\r\n'
    body += '************************************\n\n'
    body += '🎅Merry Christmas!🎅'


    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.ehlo()
    s.starttls()
    s.ehlo()

    s.login(EMAIL_ADDRESS, EMAIL_PASS)
    s.sendmail(EMAIL_ADDRESS, recipients, body.encode('utf8'))

    s.quit()

