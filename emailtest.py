from flask import Flask, redirect, url_for
from flask_mail import Mail
from flask_mail import Message
app = Flask(__name__)


app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER='smtp.163.com',
    MAIL_PORT=25,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='tsqpython@163.com',
    MAIL_PASSWORD='tsq1234321',#网易邮箱授权码
))

mail = Mail(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/send_mail')
def send_mail():
    # print(app.config)
    msg = Message("hello", sender=app.config["MAIL_USERNAME"], recipients=["1106142424@qq.com"])
    msg.body = '网址：‘www.tsq.red’,这是我的个人主页请查看'
    print(msg)
    mail.send(msg)
    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run()
