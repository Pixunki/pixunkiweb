import flask
web_app = flask.Flask(__name__)

@web_app.route("/<name>/<content>")
@web_app.route("/<name>")
@web_app.route("/")
def home(name=None, content=None):
    return flask.render_template('default_template.html', name=name, content=content)


if __name__ == '__main__':
    web_app.run(debug=True)
