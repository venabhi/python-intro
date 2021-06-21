from os import name
from flask import Flask, render_template, url_for, request, redirect
from werkzeug.utils import redirect

import csv

app = Flask(__name__)
print(__name__)

#  using decprator here we are def a function and retun afunction
#  giving html file to the route and making flask templete


@app.route('/')
def my_home():
    return render_template('index.html')



#  (/) it define the root to search to go the next page /blog/dogs 

# @app.route("/blog")
# def hello_blog():
#     return "welcomr to my blog"

#  flask templates giving html file to route fserver.py

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

#  instead of using multiple pages routes we can use variable page_name to route multiple pages
@app.route('/page_name')
def html_page (page_name):
    return render_template('page_name')

#  cerete own database of user information
def write_to_file(data):
    with open ('database.txt' ,  mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email}, {subject}, {message}')

#  write all the data in database.csv
def write_to_csv(data):
    with open('database.csv', newline='',  mode='a') as database2:

        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_writer = csv.writer(database2, delimiter=' ', newline ='',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv.writeheader()
        csv.writerow(['email', 'subject', 'message'])
        

#  request accesing data usng methods post ,get on submit form 

@app.route('/submit_fom', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict
        # print(data)
        # write_to_file(data)
        write_to_csv
        return redirect('./thankyou.html')
    else: 
        return "something error"

    
    
