from twilio.rest import Client

account_sid = '**********************************'
auth_token = '*******************************'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18182938877',
    body='Hell yeah',
    to='+54**********'
)

print(message.sid)
