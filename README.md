# Diners 3Star Restaurant

[![responsive](***)](https://diners-3star-restaurant.herokuapp.com/)

Click [here](https://diners-3star-restaurant.herokuapp.com/) to view deployed site.  

# Contents

[Diners 3Star Restaurant](#diners-3star-restaurant)

[UX](#ux)
+ [Purpose of the site](#purpose)
+ [User Stories](#user-stories)
+ [Wireframes](#wireframes)
+ [Agile Methodology](#Agile-Methodology)

[Existing Features](#existing-features)
+ [Navbar and Footer](#Navbar-and-Footer)
+ [Home Page](#home-page)
+ [Date Picker](#Date-Picker)
+ [Form validation](#Form-validation)

[Future Features](#future-features)
+ [SMS communication app](#SMS-communication-app)

[Technologies Used](#technologies-used)
+ [Languages Used](#languages-used)
+ [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

[Code Validation](#code-validation)
+ [HTML beautify](#HTML-beautify)
+ [HTML valiation](#HTML-valiation)
+ [CSS validation](#CSS-validation)
+ [JavaScript validation](#JavaScript-validation)
+ [Python beautify](#Python-beautify)
+ [Python validator](#Python-validator)

[Tests](#tests)
+ [Automated Tests](#automated-tests)
+ [Lighthouse](#Lighthouse)
+ [Manual tests](#Manual-tests)

[Project Bugs and Solutions](#project-bugs-and-solutions)
+ [Link to Google Maps](#link-to-google-maps)
+ [Static files not loading](#static-files-not-loading)
+ [Styling map template](#styling-map-template)
+ [Hero image styling](#hero-image-styling)
+ [Navbar Current Link](#navbar-current-link)
+ [Form Fields Styling](#form-fields-styling)
+ [Bugs left](#Bugs-left)


[Deployment and making a clone](#Deployment)
+ [Deployment to heroku](#Deployment-to-heroku)
+ [Setting up your local enviroment](#Setting-up-your-local-enviroment)


[Credits](#credits)
+ [Online resources](#Online-resources)
+ [Tutorials and inspiration](#Tutorials-and-inspiration)
+ [People](#People)



## UX
------

### Purpose

This project was developed to satisfy my fourth Mileston Project to for the full stack development program with [Code Institute](https://www.codeinstitute.net). For this project I have decided to create an imaginary beautiful 3star Michelin restaurant serving customers staying at the nearby beach Hotel. The restaurant allows customers to prebook meals with the added feature of allowing customers to select between three locations within the restaurant, these being outside, window seat or in the main hall areas. This current release will be restricted to a maximum of 2 tables outside sitting 2 people on each table. 2 window tables each sitting a maximum of 4 people on each and 2 hall tables each sitting a maximum of 6 people on each table.

The restaurant prides itself in providing their customers with a more inclusive experience by allowing customers to visit the kitchen area, speak to the chef and their team and be able to have a little taste of any Menu meal before ordering.

------
### User Stories

In order to demonstrate an Agile approach to this project, GitHub issues were used to record the user stories. The user stories were categorised into different User functions between the Admin and the User.

#### User stories - Admin features

The following user stories were satisfied by creation of the Restaurant app, which including these features:
- adding and removing a table from the usual layout, enabling for flexibility in the day to day management depending on customer demands.
- manually adding a booking to the system on behalf of a customer if customers book via a phone call, email or via the contact form.
- View User contact details
- approving pending bookings created by admin and/or User.
- making changes to the Menu as and when required.



[User Story #1](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/1) As a administrator I can click on the navbar and select "login" so that I can make a booking on behalf of a customer.

[User Story #2](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/2) As a administrator I can view pending customer bookings so that I can approve or reject reservation requests.

[User Story #3](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/3) As a Admin I can View User Contact details so that I can reach out to them regarding their booking requests.

[User Story #4](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/4) As a Admin I can access the menu section so that I can remove existing menu and replace with new menu.

[User Story #11](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/11) As a administrator I can manage the table layouts so that I can have flexibility with moving tables around to meet demand.


### Wireframes 
However I have designed both desktop and mobile wireframes in the same time, but I have taken mobile first approach. This is an app for drivers and it has to look good and work well on a small mobile. 

Wireframes created with [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQiAubmPBhCyARIsAJWNpiMYzrk_0rLzl3vgYKRLXwnX7rpqyQiUFdyt3xHGpRiHlZlozwO_pvcaAvUFEALw_wcB). The project was developed from initial wireframes and some modifications were made during the development process to assure better usability. 

[Wireframes initial project]()
Initial design was focused on monthly reporting. I decided to change this do daily reporting and put monthly reporting on the list for the next relese.

The design included a long form for user to type addresses in, one after another. This idea was dropped, as it could run into a danger of loosing the data half way through the journey. I thought it is important that user saves data immediately after he types it in. 

[Wireframes final version]()

The new design includes only one pair of start and destination address. After typing them in, the user saves them and can continue typing next address. In the new design uer can look up a day report that gives him a list of his visits for the day. 

### Agile Methodology

![Screenshot of the Kanban board]()

Github issues were used to create the User stories and group them according to MoSCoW prioritization technique. Link to the project with live issues can be found [here](). The issues are currently in two categories - done or for the next relese. 

The issues were than closed automaticaly when the pull request was linked to the issue. 

## Existing Features
------

### Navbar and Footer


### Home page 



### Form validation

Forms validation:
1. HTML validation using HTML atributes
2. Javascript validation (only in Drive view)
3. Django form validation

The drive view is the most complex part of the app and the most important one. I have focused on this view to make sure I have various levels of validation to help the user to submit the data correctly. Drive view consists of 2 input fields for start and destination adress. For correct functioning of both functions that are fetching google API user needs to input data in a specific way. The form validation guides the user through the process. 

In the next release some features of this validation can be added to other forms especially the User profile view. 

**1. HTML validation**

Some input fields are given attribute "required" to prevent the user from submitting the empty form.


**3. Django validation for Drive (AddJourney)**
![error message displayed after validation has failed]()

If user decides to ignore the above messages from JavaScript, the form gets submitted with some missing data, but django form validation function prevents the item to be submitted to database with missing data. 

The user gets displayed a message describing the error.

The most common error will be submitting form with geocoordinates missing. I decided that I would preffer user not to see geocoordinates as it would be too much information for a little phone application. Geocoordinates would need to be inside not editable input elements anyway. 

I am adding detailed message describing what to do if the drop down input field from google places api doesn't show up. I am also clearing the form data - hopefuly when user types both addresses again, he understands how to do this correctly. 


## Future Features 
------


## Technologies Used
------

### Languages Used

   + HTML5
   + CSS3
   + Python
   + Django

### Technologies and Programs Used:
+ GitHub
    The Git was used for version control
    Git issues were used for user stories
    GitPod was used as IDE to write the code and push to GitHub
+ Heroku 
    The page was deployed to Heroku
+ PostgreSQL
    PostgreSQL was used as database for this project
+ cloudinary storage
    for storing static files

 ### Frameworks Libraries and Programs Used

+ Balsamiq:
    Balsamiq was used to create the wireframes during the design process.
+ Bootstrap 5:
    Bootstrap was used to add style to the website.
+ Fontawesome icons
+ Django

## Code Validation
------

### HTML beautify


### HTML valiation


### CSS validation

### Python beautify

### Python validator


## Tests
------

### Automated tests

Automated tests have not been created due to time constrains of the project.

### Lighthouse


### Manual tests

#### 1. First set of manual testing on Version 1 (branch Visits)

**Relese main fetures:**


**Reported issues:**


## Project Bugs and Solutions:
------

### Static files not loading

### Hero image styling


### Navbar Current Link



### Source code



### Form fields styling


### Bugs left


## Deployment

**In your app** 


**Log into heroku**

3. Log into [Heroku](https://dashboard.heroku.com/apps) or create a new account and log in

4. top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

5. Write app name - it has to be unique, it cannot be the same as this app
6. Choose Region - I am in Europe
7. Click "Create App"

**The page of your project opens.**

8. Go to Resources Tab, Add-ons, search and add Heroku Postgres

9. Choose "settings" from the menu on the top of the page

10. Go to section "Config Vars" and click button "Reveal Config Vars". 

11. Add the below variables to the list

    * Database URL will be added automaticaly
    * Secret_key - is the djnago secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 
    * Cloudinary URL can be obtained from [cloudinary](https://cloudinary.com/) follow the steps on the website to register. 

**Go back to your code**

12. Procfile needs to be created in your app
```
web: gunicorn PROJ_NAME.wsgi
```

13. In settings in your app add Heroku to ALLOWED_HOSTS

14. Add and commit the changes in your code and push to github

**Final step - deployment**

15. Next go to "Deploy" in the menu bar on the top 

16. Go to section "deployment method", choose "GitHub"

17. New section will appear "Connect to GitHub" - Search for the repository to connect to

18. type the name of your repository and click "search"

19. once Heroku finds your repository - click "connect"

20. Scroll down to the section "Automatic Deploys"

21. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy

22. Click "Deploy branch"

Once the program runs:
you should see the message "the app was sussesfully deployed"

23. Click the button "View"

The live link can be found [here]().


### Setting up your local enviroment

1. Create Virtual enviroment on your computer or use gitpod built in virtual enviroment feature.

2. Create env.py file. It needs to contain those 5 variables.

* Database URL can be obtained from [heroku](https://dashboard.heroku.com/), add PostgreSQL as an add on when creating an app. 
* Secret_key - is the djnago secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 
* Cloudinary URL can be obtained from [cloudinary](https://cloudinary.com/) follow the steps on the website to register. 

```
os.environ["DATABASE_URL"] = "..."
os.environ["SECRET_KEY"] = "..."
os.environ["CLOUDINARY_URL"] = "..."
os.environ["GOOGLE_API_KEY"] = "..."
os.environ["DEVELOPMENT"] = "True"
```

3. Run command 
```
pip3 install -r requirements.txt
```

## Credits 
### Online resources
* [Icons8](https://icons8.com/)
* [unsplash](https://unsplash.com/)
* [Fontawsome](https://fontawesome.com/)
* [Bootstrap 5]()
* [Markdown best practices](https://www.markdownguide.org/basic-syntax/)

### Tutorials and inspiration

* The project walkthrough I Think Therefore I Blog tutorial provided instpiration for traffic alerts the repository can be found [here](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/12_final_deployment/blog/views.py)

* Django Google API by Bobby did coding [tutorial](https://www.youtube.com/watch?v=_vCT42vDfgw&t=962s) provided clear guidance how to use google API in a django project, how to fetch data and how to use them within the project. 

* Django Google API tutorial repository can be found [here](https://github.com/bobby-didcoding/did_django_google_api_tutorial)

* Hello Django tutorial by Mr Zielinski. Link to repository can be found [here](https://github.com/ckz8780/ci-fsf-hello-django/tree/c13b414fd2e87a54b4f2788ceffec55be4ade925) This helped me to understand various Django errors.

### People

* Igor_ci for explaining how to do django forms styled by bootstrap

* Mr Zielinski for creating tutorial and showing bugs on the way

* Dave Horrocks, Kamil Kwiatkowski, Daisy Gunn - for intense testing of the App and valuble suggestions for improvement

* Felipe Souza Alarcon - for mentoring, suggestions and encouragement

