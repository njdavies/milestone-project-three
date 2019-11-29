# Data Centric Development

I was given the following brief to create a data-driven web application:

> Create a web application that allows users to store and easily access cooking recipes.

> Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data.
>
> Create the backend code and frontend form to allow users to add new recipes to the site.
>
> Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category.
>
> Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable aspect (e.g. number of views or upvotes). Create a frontend page to display these.
>
> Create a detailed view for each recipe, that would just show all attributes for that recipe, and the full preparation instructions.
>
> Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages.

From a front end design perspective, I wanted to keep the site as simple as possible with the least amount of visual clutter. I went with a red, white and black main colour scheme as these colours mesh well with eachother, with the red and black standing out against a white background. I also used orange to highlight key information to the user such as the recipe rating and views. I deliberately did not take up the full width of the screen on larger viewport sizes so that the recipe information is centred and there is breathing rooom around it. Again, this is in line with wanted as little visual clutter as possible.

So that users of all different ages and web surfing competencies can use the site with the minimum of fuss the interface is self-intuitive and user-friendly. The addition of a pulsing floating action button draws attention from the user and provides a list of options available on given pages.

---

## UX

### User Stories

Using the brief given to me, I created [User Stories](https://pinup.com/rJkaXmflB "User Stories") in a tool called Pinup. This allowed
me to break down each feature required within the website.

### Mock Ups

I then used a tool called Pencil to create [wireframes](https://github.com/njdavies/milestone-project-three/tree/master/wireframes) for the site. This allowed me to plan out the content and functionality on each page, taking into account the user stories I had put together. I put together the mobile mockups first, keeping in line with a mobile first design approach. From there, very little work was required with the desktop design as the page layouts would be very similar.

### Schema

I designed a [database schema](https://github.com/njdavies/milestone-project-three/blob/master/schema.pdf) for the recipes, breaking down the attributes of each recipe into the approprate data types and making use of nesting and arrays where necessary.

---

## Features

### Existing Features

- Home Page - This displays a random 'Recipe of the day' each time the site is visited by a user.

- Recipes Page - This page contains a form that the user can complete to search through the database for a desired cake type, cuisine type and health type. The search results are sorted based on a choice of rating, views, servings or total cooking time. From the summarised recipe list returned the user can then select a recipe for full ingredient and instruction information. If there are no recipes available under the selected filters then a message is displayed to the user to confirm this.

- Cuisine Page - This page displays a link to each of the four cuisine types in the database so that users can quickly see a summarised list of recipes available. The number of recipes available for each type is also displayed.

- Cake Collections Page - This page displays a link to each of the six cake types in the database so that users can quickly see a summarised list of recipes available. The number of recipes available for each type is also displayed.

- Health & Diet Page - This page displays a link to each of the three healthy eating cake types in the database so that users can quickly see a summarised list of recipes available. The number of recipes available for each type is also displayed.

- Floating action button - This button pulses for increased visibility to users of the site. It is displayed on certain pages where CRUD operations are possible. By hovering over the button on larger viewports or selecting it on smaller viewports you are presented with a list of available options:

  1. Edit the existing recipe - By selecting this option you are taken to a page that displays the recipe in an editable form. Once you have finished editing and have selected 'Update Recipe' you are returned to the original recipe view with confirmation displayed that it has been updated.

  2. Delete the existing recipe - Upon initially selecting this option you are prompted to confirm that this is definitely the action you wish to take. This removes possible user error in deleting a recipe by mistake. Once the user confirms that they do want to delete the recipe it is deleted from the database and a page is displayed with confirmation that this has been done.

  3. Add recipe - By selecting this option you are taken to a page that displays a blank form with all of the fields required in order to add a new recipe to the database. It is not possible to submit a new recipe unless all fields are completed. In addition, certain fields can only take a specific input type, for example the 'Servings' field can only accept a number. This further reduces the a recipe being uploaded to the database with incorrect information. Once the user selects 'Add Recipe' they are taken to a page which displays the recipe in

### Features I would like to have implemented

- User authentication - Currently any user can edit and delete recipes, which could lead to the recipe information being amended/deleted maliciously. In order to remedy this I would like to have implemented a user authentication system that would mean only the original author of the recipe has the power to amend or remove it.

- The rating attribute to be fully functioning - Currently the ratings for each recipe are fabricated. I would like to have a implemented a rating feature for each recipe so that a true average rating can be displayed instead based on user feedback.

- Views against each recipe to be recorded and displayed - Currently the number of views for each recipe is fabricated. For a more authentic user experience I would like to have implemented a counting feature for the number of times a recipe has been viewed.

---

## Technologies Used

In designing and creating this website I have utilised the following tools, languages and frameworks:

- [Pinup](https://pinup.com/) - As user stories are usually written on sticky notes I decided to use this tool to replicate the
  same process digitally.
- [Pencil](https://pencil.evolus.vn/) - I wanted to put together mock-ups of the website before starting to code anything. This simple
  but effective tool let me create wireframes very quickly, and aided in visualising how the website would look from the beginning of
  development.
- [HTML5](https://en.wikipedia.org/wiki/HTML5) - I used this language to build the basic structure and elements of the website.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - This language was used to apply styling to the HTML structure, and
  described how the elements should be displayed.
- [Javascript](https://en.wikipedia.org/wiki/JavaScript) - This language allowed me to make the site interactive by incorporating buttons and applying logic depending on user choices.
- [JQuery](https://en.wikipedia.org/wiki/JQuery) - A Javascript library used to greatly simplify the finding, selecting and manipulation of DOM elements.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) - I used this language on the backend when working with the database and Flask web framework.
- [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework) - This micro web framework was used to handle the views for the different web page routes and displayed the pages using the Jinja2 template engine.
- [MongoDB](https://en.wikipedia.org/wiki/MongoDB) - The NoSQL document-oriented database program used to store all recipes used on the site.
- [Materialize](https://materializecss.com) - I utilised the Materialize framework which allowed me to quickly incorporate templates for navbars dropdown menus and floating action buttons. I also made extensive use of the framework's grid system, which allowed me to make the site fully responsive across different viewports and web browsers.
- [Google Fonts](https://fonts.google.com/specimen/Encode+Sans+Semi+Condensed) - In order to achieve a professional looking feel to the text used in the site I utilised the Google Fonts library to include the Sans Semi Condensed font.

---

## Testing

### Automated Testing

In order to rigorously test the functionality of the site I initially made use of the following automated tools:

[W3C Markup Validation Service](https://validator.w3.org/) - I used this tool to validate the HTML used within the website. To do this
I pasted the website URL (https://online-cookbook-project-three.herokuapp.com/) into the address field and hit Check. It will then advise you
of any errors within your code and make suggestions regarding how to keep this as correct as possible against the W3C standards.

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - I used this tool to validate CSS used within the website. To do
this I first selected the 'By direct input' tab and then pasted the entire CSS code from the [style.css](https://github.com/njdavies/milestone-project-three/blob/master/static/css/style.css) file into the box provided. I then hit Check. As per the HTML checker above, if there are any errors in the code these will be highlighted.

[JSHint](https://en.wikipedia.org/wiki/JSHint) - A linter for Javascript which analysed my front end code and highlighted any errors.

[Pylint](https://en.wikipedia.org/wiki/Pylint) - A linter for Python which analysed my back end code and highlighted any errors.

### Manual Testing

I tested the User Stories I had put together by conducting the following scenarios:

1. Upon the site loading, check that a random recipe is displayed. Then refresh the page so that another recipe is displayed.

2. Select the floating action button and check that the options to edit or delete the recipe and also add a new recipe are displayed.

3. Select the delete option and check that an alert is displayed which asks the user whether they wish to proceed. Select cancel to back out of this option.

4. Select the edit button, make a change to the information displayed and then select Update recipe. Check that user feedback is provided that the recipe has been updated and then ascertain if the amendment to the recipe has gone through successfully.

5. Select the Home page and check that you are directed back to this page with another random recipe displayed.

6. Select add recipe option from the floating action button and check that a page is displayed with a form to add a recipe.

Input the following recipe into the form for testing purposes:

Cake Type: Sponge
Cake Name: Basic plain sponge cake
Image: http://ukcdn.ar-cdn.com/recipes/port960/893b2533-380e-400a-a7f8-23e5d61b09da.jpg
Cuisine: British
Author: kuppet
Description: This is a simple sponge cake recipe - you can serve it plain sandwiched with jam to make a Victoria sponge cake, or fill with buttercream for a birthday cake.
Healthy: None
Preparation Time: 20
Cooking Time: 25
Total Time: 45
Servings: 8
Ingredients: 225g (8 oz) self-raising flour
225g (8 oz) butter, at room temperature
225g (8 oz) caster sugar
4 eggs
1 teaspoon baking powder
Instructions: Preheat the oven to 180 degrees C / gas mark 4.
Measure all the ingredients into a large bowl.
Mix all of the ingredients using a electric whisk.
Pour the mixture into 2 non-stick 7 inch (18cm) tins.
Place them in the oven till golden brown 15-25 minutes.
Cool on a wire rack before serving.

7. Select Add Recipe and check that a message is displayed that confirms this has been added. Also check that the page displayed is the newly added recipe and that this is formatted correctly.

8. Select the delete recipe option from the floating action button and select Ok when prompted. Check that confirmation is received that recipe has been deleted.

9. Select each of the Cuisine, Cake Collections and Health & Diet pages and perform the following tests:

   i. Check that a group of cake choices are displayed with numbers next to each option.

   ii. Select each of the options and check that a list of recipes is displayed.

   iii. Select the floating action button and check that the option to add a recipe is displayed.

   iv. Select a random recipe from the list returned and check that a full page recipe description with ingredients and instructions is displayed.

   v. Select the image of the random recipe and check that this image then is then displayed in fullscreen. Select the image again so that this reverts back to its original size.

   vi. Select the floating action button and check that the options to edit or delete the recipe are available.

During the development of the site I made extensive use of Chrome Developer Tools to view the content in different viewports and assess how it was behaving. This then led to me using multiple media queries to make subtle changes to the code so that the content was always displayed correctly.

In order to be completely satisfied that the site worked correctly across multiple browsers I completed the manual testing above after loading the site in Chrome, Internet Explorer, Edge and Firefox.

---

## Deployment

In order to deploy the site, I first created a remote Git repository on GitHub. I then committed and pushed content from my local repository to the remote repository each time I added a new piece of functionality.

Secondly, I created an new app within Heroku and linked this to my Github repository by going into the Deploy tab and selecting to deploy by Github. This then prompts you to select the appropriate repository from your GitHub account. You are then able to select from Automatic or Manual deploys. By selecting Automatic deploys it meant that whenever I pushed something to GitHub it automatically triggered a new build within Heroku. This allowed me to continually test the live version of the site in different browsers throughout development, to see how it was responding.

In the Settings tab within the app in Heroku I selected the Reveal Config Vars tab and input the following information:
IP: 0.0.0.0
Port: 5000

I also set the environment variables MONGO_URI and SECRET_KEY, whose details I will not reveal here.

Finally, I created a Procfile and requirements.txt file within my project folder and pushed these to my Git repository. The Procfile contained the following text to instruct Heroku that the application is a python web application: 'web: python app.py'. The requirements.txt file was created by running 'pip freeze > requirements.txt' within my terminal. This then created a list of the dependencies that my project utilised. Heroku also needs this so that it installs these dependencies for each build.

Heroku provided the following domain for the fully deployed site: https://online-cookbook-project-three.herokuapp.com/

To run locally, first create a new workspace in your local computer. Then use \$ git clone https://github.com/njdavies/milestone-project-three to create a local copy of the code.

Install the key project dependencies with \$ pip3 install -r requirements.txt

Set the following environment variables:

MONGO_URI
SECRET_KEY

Run the app with \$ python3 app.py

---

## Credits

### Content

1. In working with the Materialize framework I relied heavily on the official documentation found at the [following site](https://materializecss.com)

### Media

1. All recipe information and images are taken from the [following website](http://allrecipes.co.uk/)

### Acknowledgements

I received inspiration in the design of this project from the following website:

1. [Allrecipes Website](http://allrecipes.co.uk/)
