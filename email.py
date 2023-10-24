import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and recipient email addresses
sender_email = 'your@gmail.com'
recipient_email = 'recipient@example.com'
password = 'your_password'  # Use an App Password for Gmail

# Create a message object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = 'Automated Email'

# Email body
body = "This is an automated email sent from Python."
msg.attach(MIMEText(body, 'plain'))

# SMTP server setup (Gmail)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  # Use TLS (Transport Layer Security)

# Log in to the email account
server.login(sender_email, password)

# Send the email
text = msg.as_string()
server.sendmail(sender_email, recipient_email, text)

# Close the SMTP server
server.quit()

print('Email sent successfully!')
