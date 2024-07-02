from django.utils.translation import activate, get_language
from django.shortcuts import render, redirect
from django.conf import settings


def set_language(request):
    if request.method == 'POST':
        new_language = request.POST.get('language')
        redirect_url = request.POST.get('redirect_url')
        if new_language in [lang[0] for lang in settings.LANGUAGES]:
            request.session['django_language'] = new_language
            activate(new_language)
            if redirect_url:
                return redirect(redirect_url)
            else:
                return redirect('jobs:main_page')
    return render(request, 'language_change.html', {})

def about(request):
    return render(request, 'about.html',{})



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def customerInquery(name, email, user_msg, subject):
    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Use port 465 for SSL or 587 for TLS
    sender_email = 'prodm675@gmail.com'
    receiver_email = 'messi2010arz@gmail.com'
    password = 'lmwo dwdb rqtz ruki'

    # Create a message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject


    # HTML email template with placeholders for variables
    email_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dear CEO</title>
    <style>
        /* Add your custom CSS styles here */
        body {{
            font-family: Arial, sans-serif;
            background-color: #092635;  /* Updated background color */
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        h1, p, h2 {{
            color: #333333;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #ffffff;
            text-decoration: none;
            border-radius: 5px;
        }}
    </style>
    </head>
    <body>
    <div class="container">
        <h1>Dear CEO</h1>
        <h2>Mr/Mrs. {name}</h2>
        <p>Has inquiry about {subject},</p>
        <p>{user_msg}</p>
        <p>His/Her contact details:<br>{email}</p>  <!-- Use <br> for line breaks -->
    </div>
    </body>
    </html>
    """.format(name=name, subject=subject, user_msg=user_msg, email=email)


    message.attach(MIMEText(email_template, 'html'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, password)  # Login to the SMTP server
        server.send_message(message)  # Send the email


def contact(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(name, email, subject, message)
        customerInquery(name, email, message, subject)

    return render(request, 'contact.html',{})

def custom_404(request, exception):
    return render(request, 'error_404.html', status=404)
