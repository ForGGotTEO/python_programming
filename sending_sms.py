from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "" #insert your twilio account_sid
auth_token  = "" #insert your twilio auth_token
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="Random text message.",
    to="",    # Replace with your phone number(with the country code infront)
    from_="") # Replace with your Twilio number(with the country code infront)
print message.sid
