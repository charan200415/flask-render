from flask import Flask
app = Flask(__name__)

@app.route("/", subdomain="<username>")  # now the subdomain will be passed into the parameter 'username'
def profile(username):
    return "Hello " + username + "!"
