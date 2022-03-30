# Diners 3Star Restaurant

<!-- [![responsive](***)](https://diners-3star-restaurant.herokuapp.com/) -->

Click [here](https://diners-3star-restaurant.herokuapp.com/) to view deployed site.  

# Contents

[Diners 3Star Restaurant](#diners-3star-restaurant)

[UX](#ux)
+ [Purpose of the site](#purpose)
+ [Project Scoping](#project-scoping-and-agile-methodology)
+ [Wireframes](#wireframes)
+ [User Stories](#user-stories)
+ [Agile Methodology](#Agile-Methodology)

# UX

## Purpose
----
This project was developed to satisfy my fourth Milestone Project for the full stack development program with [Code Institute](https://www.codeinstitute.net). For this project I have decided to create an imaginary beautiful 3star Michelin restaurant serving customers staying at the nearby beach Hotel. The restaurant allows customers to prebook meals with the added feature of allowing customers to select between three locations within the restaurant, these being outside, window seat or in the main hall areas. This current release will be restricted to a maximum of 2 tables outside sitting 2 people on each table. 2 window tables each sitting a maximum of 4 people on each and 2 hall tables each sitting a maximum of 6 people on each table.

The restaurant prides itself in providing their customers with a more inclusive experience by allowing customers to visit the kitchen area, speak to the chef and their team and be able to have a little taste of any Menu meal before ordering.


## Project Scoping and Agile Methodology

Using the Design Thinking approach to this project, some prework was carried out to bring the ideas and functionality of the project to "paper". Powerpoint slides are used to illustrate this process beggining with a problem statement
Entity Relationship diagram

The raw data can be downloaded from [here](https://github.com/RicardoIT-Web/diners-3star-restaurant/blob/main/media/agile_methodology/Diners-3Star-Restaurant_project_Scoping.pptx).


## Wireframes 
This project is created using Bootstrap and Django frameworks. The built in tools for these frameworks already assist with site responsiveness, as a result, a Desktop approach first was adopted with the aim that responsive adjustments would be minor and is applied at the end of the projects' full creation.

Wireframes are created using [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQiAubmPBhCyARIsAJWNpiMYzrk_0rLzl3vgYKRLXwnX7rpqyQiUFdyt3xHGpRiHlZlozwO_pvcaAvUFEALw_wcB). 

The project was developed from initial wireframes and some modifications were made during the development process to ensure better UX.


#### The Home page
Where some sites demontrate some django functionality on the landing page ie. the home page, for this project, the landing page shows the basic features one would expect to see for a restaurant site. The User is greeted with a main hero image, together with a Navbar and footer to guide the user to other features of the site, which covers some of the User Stories listed below.

![Home page](/media/wireframes/homepage_wf.jpg)

![Offcanvas Navbar](/media/wireframes/offcanvas_navbar_wf.jpg)


#### The Register page
The registration page a designed to be light on the eyes to the User. There are 3 cards above the registration form which aim to remind the customers of the speacial services available to them should they wish to take advantage.

![Register page](/media/wireframes/register_page_wf.jpg)


#### The Login page
The login page initially looked bare and was missing a little something with just the Login form for the User to fill in. At this point it was decided the a hero image in the background would improve this UX.

![Login page](/media/wireframes/login_page_wf.jpg)


#### The Menu page
After carrying out some research into this Menu section, it was found that a lot of restaurants actually have fixed, unchanged menus. As a result it was decided that this restaurant would have a fixed unchanged menu for this first release. In future releases of this project the administrator will have control of this functionality and will be able to make changes to the Menu of the restaurant.

![Menu page](/media/wireframes/menu_wf.jpg)


## User Stories

In order to demonstrate an Agile approach to this project, GitHub issues were used as a Kanban board to record the user stories. The user stories were categorised into different User functions between the Admin and the User and each issue would be moved from the "to-do" board to the "done" board as the project progressed.

The Project Kanban board.

![Kanban Board](/media/images/agile_kanban_img.jpg)

### User stories - Admin features
The following user stories were satisfied by the creation of the Restaurant app, which include these features:


[User Story #1](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/1) As a administrator I can click on the navbar and select "login" so that I can make a booking on behalf of a customer.

[User Story #2](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/2) As a administrator I can view pending customer bookings so that I can approve or reject reservation requests.

[User Story #3](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/3) As a administrator I can view User Contact details so that I can reach out to them regarding their booking requests.

[User Story #4](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/4) As a administrator I can access the menu section so that I can remove existing menu and replace with new menu.

[User Story #11](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/11) As a administrator I can manage the table layouts so that I can have flexibility with moving tables around to meet demand.

### User stories - User features
The following user stories were satisfied by downloading the Django Allauth application which provides the project with built in tools to manage authentication, registration and account management:

[User Story #5](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/5) As a User I can click on Menu in the navbar so that I can view the days specials.

[User Story #6](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/6) As a User I can Click on navbar and select "contacts" so that I can view the restaurants contact details.

[User Story #7](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/7) As a User I can click on navbar and select "register" so that I can create a personal account.

[User Story #8](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/8) As a User I can login by inserting my email and password so that I can create a booking.

[User Story #9](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/9) As a User I can go to the navbar and select login so that I can book a table.

[User Story #10](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/10) As an authenticated User I can click on the navbar and select "Bookings" so that I can book a table.

# Existing Features

## The Restaurant app

This project is built using Django, adopting the MVT methodology. The restaurant app which contains the MVT(Models-Views-Templates) structure to make this site an interactive has two main models:

    * The Table Model
    * The Booking Model


