#first text 'join relationship-dirty' to twilio
from twilio.rest import Client

account_sid = 'AC2d02634d314e11a6a0629f68d9199006'
auth_token = 'your_aut_token'
client = Client(account_sid, auth_token)

#For Whatsapp
from_wa_num = 'whatsapp:+14155238886'
to_wa_num = 'whatsapp:your_whatsapp_number'

#For SMS
from_sms_num = '+18582814263'
to_sms_num = '+your_number'

message = client.messages.create(body = 'This is from a bot', from_ = from_wa_num,
                              to = to_wa_num)

print(message.sid)
