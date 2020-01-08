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
    import socket as s
    HOST_PORT = HOST, PORT = "127.0.0.1", 4343
    new_status = b"busy"
    print("We did it, cowards")
    with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:
        sock.connect(HOST_PORT)
        sock.sendall(new_status)

    return ""


if __name__ == '__main__':
    web_app.run(debug=True)
