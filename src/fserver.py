from os import name
from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

#  using decprator here we are def a function and retun afunction
#  giving html file to the route and making flask templete


@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template('firstserver.html', name= name, post_id=None)



#  (/) it define the root to search to go the next page /blog/dogs 

@app.route("/blog")
def hello_blog():
    return "welcomr to my blog"

#  flask templates giving html file to route 

