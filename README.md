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


[Deployment and making a clone](#Deployment-and-making-a-clone)
+ [Deployment to heroku](#Deployment-to-heroku)
+ [Forking the GitHub Respository](#forking-the-github-repository)
+ [Making a Local Clone](#making-a-local-clone)
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

#### User stories - users app

The following user stories were satisfied by creation of users app, including the features:
- user ability to register as a user for this website
- build in django feature that makes the user remained logged in, even when the website is closed and re opened again. 

[#16]() As a returning visitor I can have my own profile so that data I put in is kept private

[#20]() As a frequent visitor I can stay logged in so that I don't have to type in my login and password every time I visit the website

#### User stories - traffic app

The following user stories were satisfied by creation of traffic app, including the features:

- adding new traffic alert for other drivers
- display a list off traffic alerts to the users
- "thank you" button allowing drivers to show appreciation for the traffic alert
- "road clear" buttton allowing drivers to notify that the road has cleared (feature later removed due to testers raising concer that the use of the button is unclear and that google maps shows most up to date road cleard information)
- traffic alert list displayed on home page as well as in drive view
- pagination of traffic alerts on home page and displaying only 3 alerts on drive view limits long scrolling on mobile phone
- information label by the little tank button explaining it is a button to "thank you"

[#18]() As a drivers I can leave messages on the portal about problems on the road so that other drivers can avoid the area

[#19]() As a driver I can see if other drivers have posted any messages about traffic issues in the area so that I could avoid getting stuck

[#23]() As a driver I can say thank you in response to the message about traffic warning so that I can show my gratitude to fellow drivers

[#28]() As a driver I can thank the driver that posted the traffic alert so that the other driver feels appreciated

[#24]() As a driver I can mark traffic warning message as out of date so that other fellow drivers know that the traffic issue was resolved and the area is safe

[#29]() As a driver I can mark the traffic alert - road clear so that other drivers know that the alert doesn't apply any more

[#47]() As a driver I can see traffic alerts all the time, when I use app so that I know if there is anything new going on need to add traffic messages view to Drive view

[#88]() As a frequent user I can see which messages I thanked for so that I don't have to click again to thank them

[#106]() As a driver I can have my traffic messages signed with my first name so that my email is kept private

[#108]() As a regular driver I can have only few newest messages when I type my postcodes so that limit endless scrolling

[#64]() As a new user I can see some kind of description so that *understand the meaning of little tanks in the corner of the traffic alert

#### User stories - general features

The following user stories were satisfied, including the features:

- accessibility including aria-labels
- responsivness of all elements of the page, simple design easy to use on mobile
- page deployed to heroku so it can be browsed by members of the public
- fully responsive nav bar with hamburger button for mobile phone users
- footer with short information about site owner
- detailed readme including va


[#25]() As a visually impaired visitor I can the project to accommodate my needs so that I can use it with the help of my screen reader

[#26]() As a driver I can access the app on my phone so that I can use it while on the go

[#27]() As a first time user I can browse to find this app publicly available so that use it and share it


[#71]() As a mobile phone user I can hide nav bar in hamburger button so that the nav bar doesn't hide the website

[#72]() As a new user I can see more details about the makers of the site in the footer so that I can find out more about them


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

Navbar and footer has been copied from Bootstrap components and adjusted to the needs of the project

I have used a beautiful nav bar with icons found in bootstrap examples in headers. Unfortunately this nav bar didn't have the feature to collapse into hamburger menu. I tried adding the bootstrap's classess to create the hamburger menu but this has changed the look of the nav bar. The design was quite unique and bootstrap classes have hindered the design. I removed the nav bar classes and left the nav bar styled as oryginally copied from bootstrap examples - headers.

Since the app is designed for mobile phone users as a main group of clients - it needed a robust and well designed mobile nav bar. I decided to make a second nav bar for mobile phones only. I have used a different nav bar from bootstrap and I have used the same icons inside this design. This way the whole nav bar was collapsing into a hamburger button, which was much easier for mobile phone users. 

Footer contains only minimal information about the author of the page. It stays at the bottom of the page. It does not contain any relevant information for the user and if it was made "sticky" it would just take up valuble space on mobile devices screen.

### Home page 

Home page consists of a hero with a short message with buttons and a little image reffering to Tank

Second part of the home page is the list of traffic alerts. The list is generated dynamicly as per most current alert first. 

Traffic alert design - I've chosen a simple card design from bootstrap. Since this is an app for drivers I have taken the mobile first aproach. This app needs to be comfortable to use by someone that is using mobile phone only. This led to a decision to display only maximum of 6 alerts per page. This way the mobile phone user will not have to scroll down too much, but there is an option to go to the next page. The rest of messages is paginated and is available under a little nav menu with page numbers.


### Form validation

Forms validation:
1. HTML validation using HTML atributes
2. Javascript validation (only in Drive view)
3. Django form validation

The drive view is the most complex part of the app and the most important one. I have focused on this view to make sure I have various levels of validation to help the user to submit the data correctly. Drive view consists of 2 input fields for start and destination adress. For correct functioning of both functions that are fetching google API user needs to input data in a specific way. The form validation guides the user through the process. 

In the next release some features of this validation can be added to other forms especially the User profile view. 

**1. HTML validation**

Some input fields are given attribute "required" to prevent the user from submitting the empty form.

**2. javascript validation for Drive**
![input boxes showing javascript validation]()

I have added Javascript function detecting input on the start address and destination address fields. The function adds and removes classes showing the user in red and green if the field is filled in correctly. 

The green text explaining "ok" status for both fields is added by the function handling google places api query. Once the query is completed and data is submited to the fields this function adds and removes classes so it shows user in green that geocoodinates have been found. 

**3. Django validation for Drive (AddJourney)**
![error message displayed after validation has failed]()

If user decides to ignore the above messages from JavaScript, the form gets submitted with some missing data, but django form validation function prevents the item to be submitted to database with missing data. 

The user gets displayed a message describing the error.

The most common error will be submitting form with geocoordinates missing. I decided that I would preffer user not to see geocoordinates as it would be too much information for a little phone application. Geocoordinates would need to be inside not editable input elements anyway. 

I am adding detailed message describing what to do if the drop down input field from google places api doesn't show up. I am also clearing the form data - hopefuly when user types both addresses again, he understands how to do this correctly. 

### Day Report

Day report allows the user to see all journeys travelled in a day and it also displays the summary of the miles. The journeys are displayed in accordeon with more details available inside, as well as edit and delete button.

### Traffic Alert

The Traffic Alert app allows the users to add traffic alerts for other drivers to see. I have added a form that submits new traffic alerts to the database. The user can also interact with the traffic alerts - to add "thank you" by clicking a tank icon. 

In my current employment the office uses internal in app messages to describe issue on the road for example "by the big Mcdonadls in Kettering" This explains the location very clearly for locals and co workers. The user can type the location of the incident in such descriptive way so it is understandable. 

The traffic alerts are displayed as cards stacked in rows. The cards contain only minimal information - category and location. They need to be small to make them easy to view in a small mobile. There is availibity to see further details of the traffic alert by clicking into the card and a modal with details will show up. 

### Users App

User - build in django user model enables users to register log in and log out. 

I have added a User Profile model and form to enable user to give us more data about themselves. This data will be useful for reporting the mileage to the employer. The profile asks about their employer details and email addres.

Another idea is to add a special Drive Home button for the user - once the user has submitted their private address in their user profile. 

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

I started tidying up HTML code by searching for a beautifyier for HTML code. I tired [JS Beautifier](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify) and [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) in VS code - both have edited django templating tags in the way they were no longer working. They were also splitting the attributes of html elements to seperate lines. This was visualy helpfull with some tags with wide variety of attributes, but for most tags it was confusing. In the end I used [online HTML code Beautifier](https://htmlbeautify.com/). It has visualy fixed issues with incorrect indentation inherited from copying from various sources. 

### HTML valiation

I have right clicked on the rendered page and copied the code of each page into [HTML validator](https://validator.w3.org/nu/#textarea)


| Page  |  result
| ------ | ------ |
|  [Index]() |  No errors |
|  [Date pickeer]()|No errors|
|  [Drive]() |No errors|
|  [Day Report]() |No errors|
|  [New Traffic Alert]() |No errors|
|  [Login]() |No errors|
|  [Register]() |No errors|
|  [User Profile]() |No errors|


### CSS validation

No errors were found when passing through the official [W3C validator](https://jigsaw.w3.org/css-validator/). The copy of the CSS report can be found [here]()


### Python beautify
All pages were initialy put through [Python Formatter](https://codebeautify.org/python-formatter-beautifier) which automaticaly sorted most of the too long lines errors. Than the code was checked by pylint and problems were displayed in the console. Once the issues were cleared I have put all code though pep8 validator.

### Python validator


| App name  |  file name | result |
| ------ | ------ |------ |
| mileage-tracker |  urls.py |  [all ok]() |
| traffic |  admin.py |  [all ok]() |
| traffic |  forms.py |  [all ok]() |
| traffic |  models.py |  [all ok]() |
| traffic |  urls.py |  [all ok]() |
| traffic |  views.py |  [all ok]() |
| users |  admin.py |  [all ok]() |
| users |  forms.py |  [all ok]() |
| users |  models.py |  [all ok]() |
| users |  urls.py |  [all ok]() |
| users |  views.py |  [all ok]() |
| visits |  admin.py |  [all ok]() |
| visits |  forms.py |  [all ok]() |
| visits |  mixins.py |  [all ok]() |
| visits |  models.py |  [all ok]() |
| visits |  urls.py |  [all ok]() |
| visits |  views.py |  [all ok]() |

## Tests
------

### Automated tests

Automated tests have not been created due to time constrains of the project.

### Lighthouse

![Lighthouse general report]()
The Lighthouse in Chrome dev tools has been run. The results indicated very positive outcome of testing Accessibility, Best Practice and SEO, unfortunately the Performance has been assesed very low.  

![Lighthouse Performance report]()

It seems that perfo is hindered by the fact I have all bootstrap files in cludinary. I would normaly use cdn link provided by bootstrap. In the case of this project I used bootstwatch. This ment that I had to download all css files that bootstrap is made off and replace the main bootstrap.css with the one that is provide by bootstwatch. 

Another hiderance in performance must have been heroku - as a free user I am provided with much slower performance than commercial websites. 

The images were compressed - using [tiny.png]() to prevent any issues.

### Manual tests

#### 1. First set of manual testing on Version 1 (branch Visits)

**Relese main fetures:**

* users app - user was able to register and log in
* traffic app - user was able to add traffic alerts
* visits app - drive view: user was able to type in start and destination address, than he was automaticaly transfered to map pre view, where user could add the entry to database and click the link to go to google maps.

**Reported issues:**

  * Initial version did not have submit button, but the form has been submitted automaticaly after the user chose the destination address from dropdown box, this was assessed negatively, as the user likes to have control over when he goes to the next page. 

  I have added the button to submit the addresses

  * Initial version requred user to submit data on the address input form, than submit data on the map page. Users complained that the process is very complicated and, when user was observed interacting with the page, it became obvious that he is lost as to what to do on the Map page. 

  I have dropped the Map page and I have the one button fetching data from google directions and submitting to the database in one go. I also thought that javascript google map is not of any value to mobile phone user, as he can't use it to drive. User needs a button to click and be transfered to google maps and use it as Sat Nav. 

  User was unaware that he had the option to click into the link and be transfered to google maps. The link was white letters on dark background and didn't stand out. 

  I have added a google maps icon with geocoordinates for user to click so he can intuitivly use this option. 

  * Initial testing have revealed that google places drop down sometimes doesn't apear. It might have been caused by [Dark Raider](https://chrome.google.com/webstore/detail/dark-reader/eimadpbcbfnmbkopoojfekhnkhdbieeh/related?hl=en) chrome extension, although further tests have excluded this. 

  I have added javascript validation on input that guides the user through helpfull messages 
  - Please click into the drop down field to choose the correct address
  - This field is required
  - We have found geocoordinates
  Positive message is in green, negative are in red.

  Should the user still decide to submit the form with the red errors he gets a long message from django form validation that is customised, depending on error type. 

  * Users also noticed that new traffic alerts aren't showing on the traffic alerts list. 

  I have found the error in the code, new messages were submitted as "draft" not "published" therefore they were not shown on the list. I have made all new traffic alerts created with the status "published"

  * Users pointed out that the "month" button in nav bar isn't working

  This functionality wasn't ready for the first realease

  * Users appraised the dark theme of the website and the general design. 

  * Users didn't like the fact that nav bar wasn't folding into a button for mobile phone. The fact that the icons were dropping down in un organized way was particulary distracting. 

  Since this app is directed for mobile phone users mainly I have build special dedicated nav bar for mobile only. I have used media query to show and hyde the nav bars appropriately.



## Project Bugs and Solutions:
------

### Static files not loading
I deployed page to heroku. Page was displaying white without any css or js files loaded. 
![deployed site without static files rendering correctly]()

The below error was displaying on console:

![error message on the console]()

Tried several solutions:

Not worked:

- import mimetypes - solution found [here](https://stackoverflow.com/questions/35557129/css-not-loading-wrong-mime-type-django) 
- changes to file path in settings and / or in base.html file, which was suggested in one of the answeres [here](https://stackoverflow.com/questions/48248832/stylesheet-not-loaded-because-of-mime-type)

- assumption that the problem is caused by CSS library starting with comments - solution found [here](https://stackoverflow.com/questions/48248832/stylesheet-not-loaded-because-of-mime-type)

Worked:

- change `DEBUG = False` - solution found [here](https://stackoverflow.com/questions/35557129/css-not-loading-wrong-mime-type-django).

- make DEBUG variable dependable on development variable. If app can find development variable in enviroment - it sets the debug to the value of the variable, if no development variable found - the debug goes to False as default. Solution proposed in [this](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/00bc94313a374f519dbec8dfb7ed0fbd/) Code Institute video. 
```
development = os.environ.get('DEVELOPMENT', False)

DEBUG = development

if development:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '127.0.0.1:8000']
else:
    ALLOWED_HOSTS = ["mileage-tracker-app.herokuapp.com"]
```
`os.environ["DEVELOPMENT"] = "True"` variable needs to be added to env.py file, while in heroku - do not add this variable at all. 


### Hero image styling

The hero was copied from Bootstrap examples as a whole item with all styling already applied by bootstra's classes. I've noticed when testing responsivness on chrome dev tools that hero image on index.html is moving to the left of the screen, doesn't stay in the middle. I have tested in dev tools various different bootstrap classes and different css properties. The solution was adding some more classes in row div to control the number of columns depending on the screen size (`row row-cols-1 row-cols-sm-1 row-cols-md-1 row-cols-lg-2`), while the col divs will have only `col` class. Previously img div had set col width depending on screen size, while text col div had only settings for large screens. They did not seem to add up to 12 as per bootstrap's standard. I copied the classes from dev tools to the template, which has resolved the issue.



### Navbar Current Link

I wanted to ensure that user understands where in the structure of the page he currently is. I have added a feature that changes the color of navbar icon when the user is in the given url. I've done it with multiple `if else` statements. 

In attempt to simplyfy the template I tried to use `if .. or .. or `. The line of code became very long and unconvenient to read or modify. I tried to split `if... or` to seperate lines. This resulted in an error:
```
Error Invalid block tag on line 113: 'endif', expected 'endblock'. 
```
I decided that I preffer to have a repeated `if else` statement, rather than an extremly long line of `if or` statement. I have come back to `if else` statement for most of the navbar elements. 


### Source code

W3W validator returning errors on drive and user profile pages:

I struggled with one error and a several warnings in this view. The screenshots of the issues can be found [here](static/img/readme/HTML-validator/HTML-validator-06-drive.png) and the text with marked problematic areas can be found [here](static/img/readme/HTML-validator/HTML-validator-07-drive.png).

* The error shows up for `<meta charset="utf-8">` from the head.  w3w validator is complaining that it was found after first 1024 bytes. It seeems that w3w is expecting this to be the first tag in the head. Unfortunately javascript places seems to inject styling at the beggining of the head and pushes meta charset down below it. I found interesting article [here](https://dev.to/maggiecodes_/why-is-lt-meta-charset-utf-8-gt-important-59hl#:~:text=Furthermore%2C%20most%20browsers%20use%20UTF,There%20you%20have%20it.) why this tag is important.

I tried to reasearch about google autocomplete causing errors when validating HTML, but all results have been pointing to errors within google autocomplete, not HTML validation errors. 

* It seems that jquery cdn script is injecting the script below the title inside the head. This script contains the below expressions, which showed up as warnings in html validator: 
- charset attribute on the script being obselete 
- type attribute is unnecessary for JavaScript resources.
I tried various different cdn links for jquery, they all had same effect as this one. 

Solution was found by another student Dom Quail He has suggested to right click on the page and get to source code and copy the html from there. I was copying the HTML code from inspect the page -> edit as HTML and paste it to validator. Once I copied HTML from the source code - the validator wasn't raising the above errors.

### Form fields styling
Problem with displaying form fields using |as_bootstrap. 

Forms with added |as_bootstrap display neatly on the page, unified with the style of the app. Unfortunately displaying form|as_bootstrap causes that fields display without proper gap between each line. The fields stick too close one above another. The label is nearly touching the field above. 

First tried to loop through each field and use |as_bootstrap, but it was returning error. This ment that I had to prepare the whole html structure of label + input + help + wrapping div with bootstrap classes to acheve bootstrap styling. I added id, name, label information using `field.`. 
```
          {% for field in traffic_msg_form %}
            <div class="mb-3">

                <label for="{{ field.id_for_label }}" class="form-label">{{ field.label }}</label>
                <input type="field.widget_type" class="form-control" id="{{ field.id_for_label }}" aria-describedby="{{ field.id_for_label }}-help" name="{{ field.html_name }}">
                
                <div id="{{ field.id_for_label }}-help" class="form-text">{{field.errors}}</div>

             </div>
          {% endfor %}
```
All this seemed to work and generated all fields that were needed by django model and set by forms.py, except of input type. The fields with text area or select input type just rendered as if the input type was set to text.

I tried to loop through each field, but the input type doesn't change. Django documentation about input type field ([here](https://docs.djangoproject.com/en/3.2/ref/forms/api/#django.forms.BoundField)) mentiones that field.widget_type should return the type of input.


django documentation provides example:
```
  {% for field in form %}
      {% if field.widget_type == 'checkbox' %}
          # render one way
      {% else %}
          # render another way
      {% endif %}
    {% endfor %}
```
when I wrote `<input type="field.widget_type">` the page rendered with exactly the same `<input type="field.widget_type">`. It did not fill in the apropriate input type for each field. I might have to adjust forms.py to add widgets.

Even if the above works I would still have to loop throuogh options to display options in drop down. 

For now I decided to leave the forms |as_bootstraps - because they actualy work and display the content and input type correctly. This might need addressing in further development of the site.

### Bugs left
<!-- Out of the above list bugs that were left to be delt with in the next release:

- styling of some of the forms could be improved as default |as_bootstrap styling of the form leaves too small gap between the label and the next input field above

- traffic list pagination - not working on drive - this was changed into a feature - the list of traffic message for drive is only 3 messages long - to limit scrolling the screen on mobile phones

- link to google maps - it gives random results for some desktop computers as the google maps might struggle to obtain user's current location, as unlike mobile phones - no automatic data is provided. -->


## Deployment

**In your app** 

1. add the list of requirements by writing in the terminal "pip3 freeze --local > requirements.txt"
2. Git add and git commit the changes made

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

