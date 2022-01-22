import os
import requests
import itertools
from flask import Flask, flash, json, jsonify, redirect, render_template, request, session
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


@app.route('/', methods=["GET", "POST"])
def get_title_slide_input():
    """Gets data user enters in homepage form"""
    if request.method == "POST":
        name = request.form['name']
        job_title = request.form['job-title']
        company = request.form['company']
        presentation_date = request.form['pres-date']

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')