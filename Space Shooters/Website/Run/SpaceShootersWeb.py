#pip install
import smtplib      #api module om email's te versturen
import socket       #ip achterhalen
from flask import Flask, render_template, redirect, session, g

#eigen packages
from users.Nederlands.Nederlands import Nederlands
from users.Engels.Engels import Engels
from Admin.Admin import Admin
from Error.Error import Error
from Game.Game import Game


users = []

#array word opgezet
class User:
    def __init__(self, id, username, password, email, logins):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.logins = logins

    def __repr__(self):
        return f'<User: {self.username}>'


for line in open("../accountfile.txt", "r").readlines():
    accounts = line.split()
    users.append(User(id=accounts[0], username=accounts[1], password=accounts[2], email=accounts[3], logins=accounts[4]))

def test():
    ##by start send email of connected ip
    ##enable this when deployd
    #ip word opgevraagd door de pi
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    #email sturen
    gmail_user = 'spaceshooters1@gmail.com'
    gmail_password = 'SpaceInvaders'

    sent_from = gmail_user
    to = "butrosgroot@gmail.com"
    subject = 'SpaceShooters'
    body = IPAddr

    email_text = """\
            From: %s
            To: %s
            Subject: %s
            
            %s
            """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print("Email sent!")
    except:
        print("Something went wrong...")


app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'


@app.before_request
def before_request():           #word uitgevoerd voordat je op de site komt
    g.user = None

    #maakt een session id aan als gast
    if 'user_id' in session:
        try:
            user = [x for x in users if x.id == session['user_id']][0]
            g.user = user
        except:
            g.user = users[0]


@app.route('/')
def link1():
    return redirect("/NL/Login")

app.register_blueprint(Error, url_prefix="")
app.register_blueprint(Nederlands, url_prefix="/NL")
app.register_blueprint(Engels, url_prefix="/EN")
app.register_blueprint(Admin, url_prefix="/admin")
app.register_blueprint(Game, url_prefix="/game")


@app.route("/language")
def language_selection():
    return render_template("Space_Shooter_Web_Language-Selection.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")