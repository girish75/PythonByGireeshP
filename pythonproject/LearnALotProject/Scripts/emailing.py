import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # OS Path
htmlobj = Template(Path('index.html').read_text())

"""
In the case that you are sending emails through GMAIL,  
just go to your account(gmail) -> Account setting -> Scroll to the bottom of the page and
you see Less Secured Apps tab ,now you just have to turn that feature ON. for more info visit this:

Links Less Secured Apps : https://support.google.com/accounts/answer/6010255
Third party sites & apps: https://support.google.com/accounts/answer/3466521

I recommend turning that feature back OFF once done experimenting with email.
"""
email = EmailMessage()
email['from'] = 'Girish Pareek'
email['To'] = 'girishpareek1@gmail.com'
email['Subject'] = 'You won 1,00,000 millor Dollars'

# email.set_content('I am a Python Master!')
email.set_content(htmlobj.substitute({'name' : 'Tintin'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login( 'zerotoheropython@gmail.com', 'hellozthp')
    smtp.send_message(email)
    print("Email sent")
