import flask

app = flask.Flask(__name__)

@app.route("/")  # now the subdomain will be passed into the parameter 'username'
def profile():
    url=(flask.request.url).replace('.flask-render.tk/','').replace('https://','')
    return f"Hello {url}"


@app.route("/test")  # now the subdomain will be passed into the parameter 'username'
def test():
    return "Hello !"

if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0')
