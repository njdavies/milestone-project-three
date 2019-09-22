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


@app.route("/cake_collections")
def cake_collections():
    """
    Request a count of each cake type in the database and store this value
    in the respective variable. This is then passed to the render_template
    method to be used in rendering the cakecollections.html page.
    """
    chocolate = mongo.db.recipes.find({"type": "Chocolate"}).count()
    loaf = mongo.db.recipes.find({"type": "Loaf"}).count()
    sponge = mongo.db.recipes.find({"type": "Sponge"}).count()
    cheesecake = mongo.db.recipes.find({"type": "Cheesecake"}).count()
    nutAndSeed = mongo.db.recipes.find({"type": "Nut and Seed"}).count()
    traybake = mongo.db.recipes.find({"type": "Traybake"}).count()
    return render_template("cakecollections.html", chocolateCount=chocolate, loafCount=loaf, spongeCount=sponge,
                           cheesecakeCount=cheesecake, nutAndSeedCount=nutAndSeed, traybakeCount=traybake)


@app.route("/cuisine")
def cuisine():
    """
    Request a count of each cuisine type in the database and store this value
    in the respective variable. This is then passed to the render_template
    method to be used in rendering the cuisine.html page.
    """
    british = mongo.db.recipes.find({"cuisine": "British"}).count()
    american = mongo.db.recipes.find({"cuisine": "American"}).count()
    french = mongo.db.recipes.find({"cuisine": "French"}).count()
    greek = mongo.db.recipes.find({"cuisine": "Greek"}).count()
    return render_template("cuisine.html", britishCount=british, americanCount=american, frenchCount=french, greekCount=greek)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
