import flask

app = flask.Flask(__name__)

@app.route("/")  # now the subdomain will be passed into the parameter 'username'
def profile():
    url=flask.request.url
    return f"Hello {url}"


@app.route("/test")  # now the subdomain will be passed into the parameter 'username'
def test():
    return "Hello !"
