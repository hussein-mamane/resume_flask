from flask import Flask, request, render_template, flash, redirect, url_for
# from flask_wtf import StringField, EmailField
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
from pymongo import MongoClient
from forms import FeedBackForm


load_dotenv()

app = Flask(__name__)
csrf = CSRFProtect(app)
# the default prefix FLASK_
app.config.from_prefixed_env()

client = MongoClient()
db = client.reviews
feedback_coll = db.feedback


@app.route("/")
def root():
    return render_template('home.html')


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "GET":
        form = FeedBackForm()
        return render_template("feedback.html", form=form)
    elif request.method == "POST":
        form = FeedBackForm(request.form)
        if form.validate():

            full_name_from_data = form.full_name.data
            full_name = request.form['full_name']
            feedback = request.form['feedback']
            # found_password = users_coll.find_one({"username": login})
            return redirect(url_for("thanks", name=full_name))


@app.route("/thanks/<name>")
def thanks(name):
    return render_template("thanks.html", name=name)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
