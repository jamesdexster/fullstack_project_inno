from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template('index.html')

@my_view.route("/index")
@my_view.route("/homepage")
@my_view.route("/home")
def index_redirect():
    return redirect(url_for("my_view.index"))

@my_view.route('/updates')
def updates():
    return render_template("updates.html")

@my_view.route("/changelogs")
@my_view.route("/logs")
@my_view.route("/update")
def updates_redirect():
    return redirect(url_for("my_view.updates"))

@my_view.route('/videos')
def videos():
    return render_template("videos.html")

@my_view.route("/vids")
@my_view.route("/video")
@my_view.route("/clips")
def videos_redirect():
    return redirect(url_for("my_view.videos"))

@my_view.route('/faq')
def faq():
    return render_template("faq.html")

@my_view.route("/info")
@my_view.route("/questions")
@my_view.route("/faqs")
@my_view.route("/about")
@my_view.route("/aboutus")
def faq_redirect():
    return redirect(url_for("my_view.faq"))

@my_view.route('/contactus')
def contact():
    return render_template("contact.html")

@my_view.route("/contact")
@my_view.route("/dayz")
def contact_redirect():
    return redirect(url_for("my_view.contact"))