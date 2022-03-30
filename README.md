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

## UX
------

### Purpose

This project was developed to satisfy my fourth Mileston Project to for the full stack development program with [Code Institute](https://www.codeinstitute.net). For this project I have decided to create an imaginary beautiful 3star Michelin restaurant serving customers staying at the nearby beach Hotel. The restaurant allows customers to prebook meals with the added feature of allowing customers to select between three locations within the restaurant, these being outside, window seat or in the main hall areas. This current release will be restricted to a maximum of 2 tables outside sitting 2 people on each table. 2 window tables each sitting a maximum of 4 people on each and 2 hall tables each sitting a maximum of 6 people on each table.

The restaurant prides itself in providing their customers with a more inclusive experience by allowing customers to visit the kitchen area, speak to the chef and their team and be able to have a little taste of any Menu meal before ordering.

------
### User Stories

In order to demonstrate an Agile approach to this project, GitHub issues were used to record the user stories. The user stories were categorised into different User functions between the Admin and the User.

#### User stories - Admin features

The following user stories were satisfied by the creation of the Restaurant app, which include these features:


[User Story #1](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/1) As a administrator I can click on the navbar and select "login" so that I can make a booking on behalf of a customer.

[User Story #2](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/2) As a administrator I can view pending customer bookings so that I can approve or reject reservation requests.

[User Story #3](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/3) As a Admin I can view User Contact details so that I can reach out to them regarding their booking requests.

[User Story #4](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/4) As a Admin I can access the menu section so that I can remove existing menu and replace with new menu.

[User Story #11](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/11) As a administrator I can manage the table layouts so that I can have flexibility with moving tables around to meet demand.

#### User stories - User features

The following user stories were satisfied by downloading the Django Allauth application which provides the project with built in tools to manage authentication, registration and account management:

[User Story #5](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/7) As a User I can click on Menu in the navbar so that I can view the days specials.

[User Story #7](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/7) As a User I can click on navbar and select "register" so that I can create a personal account.

[User Story #8](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/8) As a User I can login by inserting my email and password so that I can create a booking.

[User Story #9](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/9) As a User I can go to the navbar and select login so that I can book a table.

[User Story #10](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/10) As an authenticated User I can click on the navbar and select "Bookings" so that I can book a table.


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
