#first text 'join relationship-dirty' to twilio
from twilio.rest import Client

account_sid = 'AC2d02634d314e11a6a0629f68d9199006'
auth_token = '1536d3c8212d741bf4533cc12a68ffc6'
client = Client(account_sid, auth_token)

#For Whatsapp
from_wa_num = 'whatsapp:+14155238886'
to_wa_num = 'whatsapp:+917507182483'

#For SMS
from_sms_num = '+18582814263'
to_sms_num = '+917507182483'

message = client.messages.create(body = 'This is from a bot', from_ = from_wa_num,
                              to = to_wa_num)

print(message.sid)
