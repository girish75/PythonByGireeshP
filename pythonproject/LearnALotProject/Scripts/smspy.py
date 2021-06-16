import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC94ae07dc2a38cfd369ebdb03f5be23fb']
auth_token = os.environ['e0a9667ad4f588301f0d71ee5952318a']

message = Client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13393375290',
                     to='+918527837191'
                 )

print(message.sid)