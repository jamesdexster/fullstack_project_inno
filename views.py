from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template('index.html')

@my_view.route('/updates')
def updates():
    return render_template("updates.html")

@my_view.route('/videos')
def trailers():
    return render_template("videos.html")

@my_view.route('/faq')
def faq():
    return render_template("faq.html")

@my_view.route('/contactus')
def contact():
    return render_template("contact.html")