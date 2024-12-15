from flask import current_app
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from app.models.document import VehicleDocument

def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = current_app.config['MAIL_USERNAME']
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'html'))
    
    try:
        server = smtplib.SMTP(current_app.config['MAIL_SERVER'], current_app.config['MAIL_PORT'])
        server.starttls()
        server.login(current_app.config['MAIL_USERNAME'], current_app.config['MAIL_PASSWORD'])
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

def send_welcome_email(email, name, password):
    subject = "Welcome to VehicleComply"
    body = f"""
    <h2>Welcome to VehicleComply, {name}!</h2>
    <p>Your account has been created successfully.</p>
    <p>Your login credentials:</p>
    <ul>
        <li>Email: {email}</li>
        <li>Password: {password}</li>
    </ul>
    <p>Please change your password after first login.</p>
    """
    send_email(email, subject, body)

def send_expiry_notification():
    # Get documents expiring in the next 30 days
    thirty_days = datetime.now().date() + timedelta(days=30)
    expiring_docs = VehicleDocument.query.filter(
        VehicleDocument.expiry_date <= thirty_days,
        VehicleDocument.status == 'active'
    ).all()
    
    for doc in expiring_docs:
        subject = f"Document Expiry Notification - {doc.type.upper()}"
        body = f"""
        <h2>Document Expiry Notification</h2>
        <p>Your {doc.type} for vehicle {doc.vehicle.registration_number} is expiring on {doc.expiry_date}.</p>
        <p>Please renew it before expiry to maintain compliance.</p>
        """
        send_email(doc.vehicle.user.email, subject, body)