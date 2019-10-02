import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "online_cookbook"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("SECRET_KEY")

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


@app.route("/recipes")
def recipes():
    """
    Request each unique value for the fields 'type', 'cuisine' and 'healthy' in the database. These unique values
    will then be passed to the recipes.html page to correctly display a list of options to select from when searching recipes.
    """
    cake_types = mongo.db.recipes.distinct("type")
    cuisine_types = mongo.db.recipes.distinct("cuisine")
    healthy_types = mongo.db.recipes.distinct("healthy")
    return render_template("recipes.html", recipes=mongo.db.recipes.find(), cakeTypes=cake_types, cuisineTypes=cuisine_types, healthyTypes=healthy_types)


@app.route("/search_recipes", methods=["POST"])
def search_recipes():
    """
    Function called when a user searches the database using the form on the recipes.html page.
    The values submitted on the form are stored in variables below and then passed to MongoDB
    query to find the list of recipes. These recipes are then sorted using the value in the
    sortItems variable.
    """
    cakeType = request.form.get("type")
    cuisineType = request.form.get("cuisine")
    healthyType = request.form.get("healthy")
    sortItems = request.form.get("sort")
    return render_template("selectedrecipes.html", recipes=mongo.db.recipes.find({"$and": [{"type": cakeType}, {"cuisine": cuisineType}, {"healthy": healthyType}]}).sort(
        [(sortItems, -1)]))


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


@app.route("/healthy")
def healthy():
    """
    Request a count of each health & diet type in the database and store this value
    in the respective variable. This is then passed to the render_template
    method to be used in rendering the healthy.html page.
    """
    glutenFree = mongo.db.recipes.find({"healthy": "Gluten Free"}).count()
    lowFat = mongo.db.recipes.find({"healthy": "Low Fat"}).count()
    lowCalorie = mongo.db.recipes.find({"healthy": "Low Calorie"}).count()
    return render_template("healthy.html", glutenFreeCount=glutenFree, lowFatCount=lowFat, lowCalorieCount=lowCalorie)


@app.route("/selected_recipes/<key>,<value>")
def selected_recipes(key, value):
    """
    For the selected cake collection selected i.e. Chocolate, loaf etc, send a query to the database to find a
    list of those recipes. These records are then stored in the variable recipes and passed to the render_template
    method to be used when rendering the selectedrecipes.html page.
    """
    return render_template("selectedrecipes.html", recipes=mongo.db.recipes.find({key: value}))


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """
    When selecting a recipe from the list of selected recipes send a query to the database, passing it the recipe_id
    to request this record back. Store this record in the recipe variable and pass this to the render_template method
    to render the recipe.html page.
    """
    the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=the_recipe)


@app.route("/add_recipe")
def add_recipe():
    """
    Request each unique value for the fields 'type', 'cuisine' and 'healthy' in the database. The values returned are
    stored in the recipes variable. These unique values will then be used in the addrecipe.html page to correctly
    display a list of options to select from when adding a new recipe.
    """
    cake_types = mongo.db.recipes.distinct("type")
    cuisine_types = mongo.db.recipes.distinct("cuisine")
    healthy_types = mongo.db.recipes.distinct("healthy")
    return render_template("addrecipe.html", recipes=mongo.db.recipes.find(), cakeTypes=cake_types, cuisineTypes=cuisine_types, healthyTypes=healthy_types)


@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    """
    Function called when a user submits a new recipe to the database.
    """

    # Take each line from the ingredients textarea of the addrecipe.html
    # page and split this into an array to be uploaded to the database
    ingredients_list = request.form["ingredients"].split("\n")

    # Take each line from the instructions textarea of the addrecipe.html
    # page and split this into an array to be uploaded to the database
    instructions_list = request.form["instructions"].split("\n")

    recipes = mongo.db.recipes
    # Insert the completed recipe into the database by requesting
    # each completed field from the addrecipe form
    recipes.insert_one({

        "type": request.form["type"],
        "name": request.form["name"],
        "image": request.form["image"],
        "cuisine": request.form["cuisine"],
        "author": request.form["author"],
        "rating": 0,
        "views": 0,
        "description": request.form["description"],
        "healthy": request.form["healthy"],
        "time_to_cook": {
            "prepTime": int(request.form["prepTime"]),
            "cookTime": int(request.form["cookTime"]),
            "readyIn": int(request.form["readyIn"]),
        },
        "serves": int(request.form["serves"]),
        "ingredients": ingredients_list,
        "instructions": instructions_list
    })
    return redirect(url_for("new_recipe"))


@app.route("/new_recipe")
def new_recipe():
    """
    Find the latest recipe added to the database, save this in the new_recipe
    variable and then pass this to the render_template method to be used when
    rendering the recipe.html page.
    """
    new_recipe = mongo.db.recipes.find().sort("_id", -1).limit(1)
    flash("Recipe added!")
    return render_template("recipe.html", recipe=new_recipe)


@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    """
    Function called when editing a recipe.
    """
    the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    cake_types = mongo.db.recipes.distinct("type")
    cuisine_types = mongo.db.recipes.distinct("cuisine")
    healthy_types = mongo.db.recipes.distinct("healthy")

    recipe_Lists = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})

    # Create empty strings to be populated with each ingredient/instruction from the
    # respective array in the database
    ingredientsList = ""
    instructionsList = ""

    for ingredient in recipe_Lists["ingredients"]:
        # Put each ingredient on a newline within the ingredientsList string
        ingredientsList += ingredient + "\n"
        # Delete last newline from ingredientsList string as this will be empty
        # and store result in new string variable newIngredientsList
        newIngredientsList = ingredientsList.strip()

    for instruction in recipe_Lists["instructions"]:
        # Put each instruction on a newline within the instructonsList string
        instructionsList += instruction + "\n"
        # Delete last newline from instructionsList string as this will be empty
        # and store result in new string variable newInstructionsList
        newInstructionsList = instructionsList.strip()

    return render_template("editrecipe.html", recipe=the_recipe, cakeTypes=cake_types, cuisineTypes=cuisine_types, healthyTypes=healthy_types, ingredients=newIngredientsList, instructions=newInstructionsList)


@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    """
    Function called when selecting the Update recipe button from the Edit recipe page. This function operates
    similarly to the insert recipe function, but instead of adding a new record it simply updates the fields
    for an existing record.
    """

    ingredients_list = request.form["ingredients"].split("\n")
    instructions_list = request.form["instructions"].split("\n")

    recipe = mongo.db.recipes
    recipe.update(
        {"_id": ObjectId(recipe_id)},
        {"$set": {
            "type": request.form.get("type"),
            "name": request.form.get("name"),
            "image": request.form.get("image"),
            "cuisine": request.form.get("cuisine"),
            "author": request.form.get("author"),
            "description": request.form.get("description"),
            "healthy": request.form.get("healthy"),
            "time_to_cook": {
                "prepTime": int(request.form.get("prepTime")),
                "cookTime": int(request.form.get("cookTime")),
                "readyIn": int(request.form.get("readyIn")),
            },
            "serves": int(request.form.get("serves")),
            "ingredients": ingredients_list,
            "instructions": instructions_list
        }
        })
    flash("Recipe updated!")
    return redirect(url_for('recipe', recipe_id=recipe_id))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Function called when selecting the Delete recipe option from the floating action button.
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted!")
    return redirect(url_for('recipe', recipe_id=recipe_id))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
