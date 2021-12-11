from flask import Flask, render_template
from flask_mail import Mail, Message


config = {
    'MAIL_SERVER': 'smtp.ethereal.email',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_DEBUG': True,
    'MAIL_USERNAME': 'casimer.wiza11@ethereal.email',
    'MAIL_PASSWORD': 'kpNtvemDMrnt1eqV8K',
    'MAIL_DEFAULT_SENDER': 'Spacedevs <oi@spacedevs.com.br>'
}

app = Flask(__name__)
app.config.update(config)
mail = Mail(app)


@app.route('/sendmail')
def sendmail():
    msg = Message(subject="Bem-vindo(a)",
                  sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=['rogerio@gmail.com'],
                  html=render_template('mail.html', name='Rogerio')
    )
    mail.send(msg)
    return "E-mail enviado com sucesso!"


if __name__ == "__main__":
    app.run(debug=True)
