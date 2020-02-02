from twilio.rest import Client 
 
account_sid = 'AC9fe3d41d1f63d5e1e77c7b361347676a' 
auth_token = 'a174a22e7caf906a888370f0e11164a5' 
client = Client(account_sid, auth_token) 

def send_msg(): 
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='Your appointment is coming up on July 21 at 3PM',      
                                  to='whatsapp:+918073342037' 
                              ) 
 
    print(message.sid)