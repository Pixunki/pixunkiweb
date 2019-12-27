import flask as fl
web_app = fl.Flask(__name__)

test = {
    "rogerio": "cool",
    "potatoes": "yummy",
    "mazunki": "hungwy",
    "teachers": "boring"
}

@web_app.route("/home.html")
@web_app.route("/")
def home(**kwargs):
    return fl.render_template('home.html', people=test, **kwargs)

@web_app.route("/neopixels.html")
def run_neopixels():
    return fl.render_template('neopixels.html')

@web_app.route("/people.html")
def people():
    return fl.render_template('people.html')

@web_app.route("/runFunction")
def button_action():
    print("We did it, cowards!")
    return ""


if __name__ == '__main__':
    web_app.run(debug=True)
