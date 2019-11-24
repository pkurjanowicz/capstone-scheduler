from flask import Blueprint, jsonify, request
from db_instance import db
from models import Invites
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_api = Blueprint('email_api', __name__)
gmail_user = 'pkurjanowicz10@gmail.com'
gmail_password = 'AtYoqLFPDQpTfrpWKT.zLP*4FU'

@email_api.route('/sendinvites', methods=['POST'])
def sendinvites():
    emails = request.json["emails"]
    event_id = request.json['event_id']
    if emails != '':
        for email in emails:
            # Add to DB
            new_invite = Invites(invitee_email=email,event_id=event_id)
            db.session.add(new_invite)
            db.session.commit()
            #send emails
            msg = MIMEMultipart()
            msg['From'] = gmail_user
            msg['To'] = email
            msg['Subject'] = 'Please accept this invite to my event!'
            # Create the body of the message (a plain-text and an HTML version).
            # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
            html = """\
            <html>
            <head></head>
            <body>
                <p>Hi!<br>
                How are you?<br>
                Here is the <a href="https://www.python.org">link</a> you wanted.
                </p>
            </body>
            </html>
            """

            # Record the MIME types of both parts - text/plain and text/html.
            # part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')

            # Attach parts into message container.
            # According to RFC 2046, the last part of a multipart message, in this case
            # the HTML message, is best and preferred.
            # msg.attach(part1)
            msg.attach(part2)
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user,email,msg.as_string())
            server.close()
            print('Success!')
        return jsonify(success=True)


