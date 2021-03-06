from flask import Flask
import smtplib, os
from flask_mail import Mail, Message
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

app =Flask(__name__)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_USERNAME'] = 'otter.oh@gmail.com'
# app.config['MAIL_PASSWORD'] = '******'
app.config['MAIL_SERVER']='smtp.naver.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'otter35@naver.com'
app.config['MAIL_PASSWORD'] = '****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/mail_submit")
def mail_submit():
    msg = MIMEMultipart()
    msg = Message('Hello world!', sender = app.config['MAIL_USERNAME'], recipients = ['otter35@naver.com', 'otter.oh@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    files = ['static/download.jpg']
    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
#     app.run(host='172.30.1.5', port='80', debug = True)
    app.run(host='0.0.0.0', debug = True)