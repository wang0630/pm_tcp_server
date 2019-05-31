import smtplib, ssl, os

port = 465  # For SSL
password = os.getenv('PASSWORD', -1)
sender = os.getenv('SENDER', -1)
receiver1 = os.getenv('RECEIVER1', -1)
receiver2 = os.getenv('RECEIVER2', -1)
receiver_arr = [receiver1, receiver2]

def send_alarm(message):
  # Create a secure SSL context
  context = ssl.create_default_context()
  print(f'sender: {sender}')
  print(f'receiver_arr: , {receiver_arr}')
  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    # TODO: Send email here
    server.sendmail(sender, receiver_arr, message)