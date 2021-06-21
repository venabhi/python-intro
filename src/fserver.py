from flask import Flask

app = Flask(__name__)
print(__name__)

#  using decprator here we are def a function and retun afunction

@app.route("/")
def hello_world():
    return "Hello World"
