import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "online_cookbook"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    """
    Request one random record from the database and store this in the 
    recipe variable. This is then passed to the render_template method 
    to be used when rendering the index.html page.
    """
    return render_template("index.html", recipe=mongo.db.recipes.aggregate([{"$sample": {"size": 1}}]))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
