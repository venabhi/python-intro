from flask import Flask

app = Flask(__name__)
print(__name__)

#  using decprator here we are def a function and retun afunction

@app.route("/")
def hello_world():
    return "Hiiiii"

#  (/) it define the root to search to go the next page /blog/dogs 

@app.route("/blog")
def hello_world():
    return "welcomr to my blog"

#  flask templates giving html file to route 

