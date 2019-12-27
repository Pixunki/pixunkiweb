import flask as fl
web_app = fl.Flask(__name__)

@web_app.route("/<name>/<content>/<morecontent>")
@web_app.route("/<name>/<content>")
@web_app.route("/<name>")
@web_app.route("/")
def home(**kwargs):
    return fl.render_template('default_template.html', **kwargs)


if __name__ == '__main__':
    web_app.run(debug=True)
