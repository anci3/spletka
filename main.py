import datetime

from flask import Flask, render_template

"""
JINJA crash course

{{ variableName}} --> print out variable
{% %} --> control statement

--> for loop
{% if variable %}
{% endfor %}

--> if statement 
{% if variable %}
{% else %}
{% endif %}

--> extending temlates
{% extends "base.html %"}

--> block (content)

"""


app = Flask(__name__)

@app.route("/")
def index():
    ninja = "This will be our first JINJA text!"
    year = datetime.datetime.now().year
    todoList = [ "Buy onions", "Buy cabbages", "Buy beer", "Do homework" ]

    loggedIn = True

    return render_template(
        "index.html",
        ninja = ninja,
        year = year,
        todoList = todoList,
        loggedIn = loggedIn
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run()