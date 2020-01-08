import flask as fl

web_app = fl.Flask(__name__)
colours = ["GREEN", "DARKGREEN", "BLUE", "BLACK", "RED", "WHITE", "DARKWHITE"]
seq_n = 0

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
    global seq_n
    HOST_PORT = HOST, PORT = "127.0.0.1", 4343
    new_status = colours[seq_n%len(colours)]
    seq_n += 1
    print("We did it, cowards")
    try:
        with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:
            sock.connect(HOST_PORT)
            sock.sendall(new_status.encode("utf-8"))
    except ConnectionRefusedError:
        print("Warning: Couldn't connect with local listener.")

    return ""


if __name__ == '__main__':
    web_app.run(debug=True, host="0.0.0.0")
