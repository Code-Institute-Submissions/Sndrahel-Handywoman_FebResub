# HANDYWOMAN

## Full Stack Frameworks with Django

![Responsive Mockup]()  

---

## Project Summary

Handywoman is a website that provides....

This project is my milstone project 4 for Code Institute and is for educational purposes only.

Feel Free to visit the live website: [Handywoman]() 

---
# Table of contents

- [UX](#ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
        - [User stories](#user-stories)
    - [Structure of the website](#structure-of-the-website)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
- [Features](#features)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

---
# UX

## Strategy

The purpose of this project is to build..
This website can be easily changed for different type of businesses.

## Scope

A MVP (minimum viable product) includes:

- landing page..
- services page..
- about page..
- blog page..
- contact page
- login and register pages

### User Stories

**ID** | **As a/an** | **I want to be able to...** | **So that I can**
--- | --- | --- | ---
1 | Site User | find responsive ,rich media , with a simple navbar | have a nice user experience
2 | Site User | easily navigate through the website | understand what this website provide
3 | Site User | view a list of services | select one to that suits
4 | Site User | view services details | see description and ask for a qoute
5 | Site User | register an account | comment and share experience
6 | Site User | contact the aministrator of the site | get more information
7 | Administrator | have access to all the functionalities available as a simple user | controll the site and its content
8 | Administrator | add new content | keep the site up to date
9 | Administrator | verify registration for new account | prevent bots and fake account
10 | Administrator | create, read, update and delete content | manage my site content
11 | Administrator | approve or disapprove comments| filter out objectionable comments


## Structures of the website

Website contains:
- fixed navigation bar or burger icon on mobile devices with essential links to navigate on the website.
- 
-


## Skeleton

### Wireframes

The website is created as a desktop-first because it is easy to picture the whole image of the website, however, it is a fully mobile responsive website as well so users using a mobile phone have no difficulties toggeling the site. Below are the wireframes of the core pages of the website.

- [Wireframes]()

### Database Schema

Database schema contains:


## Surface


---
# Features:

## Existing Features:

### Base

![Landing Page]()

All pages have the sidebar with the logo with links and footer.


### Navbar

![Navbar]()

After logging into the system, the user can access the profile screen via the MY ACCOUNT button on the sidebar.
There are three buttons, one that takes you to the page to change the profile, one to reset the password, and other to return to the main page.


### Sign up a new user

![Sign up]()

When accessing the sign up screen, the user must choose a username, password and fill in a email for access to the commenting on the blog-platform.

When a character is correctly guessed, the user will get feedback that correct character has been picked. The correct character will be added to the current team as well to a line were all "used characters" is shown.


### User Login

![Login]()

On the login screen, the user is asked to fill in his/her login and password for access. If the user does not remember the password, he/she can request a password reset at the FORGOT PASSWORD link. A link to access the registration page is provided above if the user does not already have it.


### Services Selection

![Services]()

This is where the users can read more detailed information about services that offers. The services card displays a button from where the users will have a direct access to the contact/request page.


### About Us

![About Us]()


### Blog Page

![Blog]()


### Contact Page

![Contact]()

On the contact page, a form is available for the user to send messages to the admin of the site containing the fields Name, email, subject, service sellection and message. 


## Features Left to Implement:
- 
-
-

----
# Technologies Used:

## Languages, framework libraries and programs:
- [HTML5](https://en.wikipedia.org/wiki/HTML) - For markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) - For style
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - For interaction
- [Python3](https://www.python.org/) - As a backend programming language
- [Django](https://www.djangoproject.com/) - As the main framework of Python
- [SQLite](https://www.sqlite.org/index.html) - As a database in development mode
- [PostgreSQL](https://landing.aiven.io/en/aiven-for-postgresql/) - As a database in production mode
- [Startbootstrap](https://startbootstrap.com/) - For the mainframe of the website
- [Getbootstrap](https://getbootstrap.com/) - For containers and layout
- [MDBootstrap](https://mdbootstrap.com/) - For card snippets
- [Cloudinary](https://cloudinary.com/) - For storage of media and images
- [Google Fonts](https://fonts.google.com/) - For fonts
- [Font Awesome](https://fontawesome.com/) - For icons
- [Gitpod](https://www.gitpod.io/) - As Integrated Development Environment (IDE)
- [Git](https://git-scm.com/) - For local version control, keeping the files & documents
- [GitHub](https://github.com/) - For online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) - For deploying the website
- [Balsamiq](https://balsamiq.com/) - For wireframes

---  
# Testing:

## Manual Testing:
- 
- 
- 

## Validator Testing:
- [W3C Markup Validation Service](https://validator.w3.org/) - For testing HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - For testing CSS code
- [PEP8 Online](http://pep8online.com/) - For checking Python PEP8 requirements. 
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - For testing, style checking and debugging

### This project was tested with the following browsers: 
- Laptop MacOS Big Sur (ver 11.4): Google Chrome

### The following steps were taken:
- 
-
- 
- 
-  
- 


### Issues / Unfixed Bugs:

- 
- 
- 



---
# Deployment

## Setting up
---
The website of this project requires back-end technologies such as server, application, and database so the website is deployed in [Heroku](https://www.heroku.com/), which is a cloud platform with a service supporting several programming languages, because GitHub can only host a static website. Heroku Postgres is used for the database, which is also a cloud-based platform, is used to store static files and images as Heroku has [no files system to store new files


## Setting up Heroku App
---
- Create an app in Heroku. Click *New*, put App name and select region.
- Add Heroku Postgres for the database.
- Install `gunicorn`, `dj_database_url` and `psycopg2-binary` to use Heroku Postgres, and run `pip3 freeze > requirements.txt` command to add them on requirments.txt.
- Update `settings.py` of the app. Import `dj_database_url`, comment out sqlite databases and add dj databases variable temporary while the database is transferred to Heroku Postgres.
- Run `python3 manage.py showmigrations` command to see the status of migrations (Currently not migrated). Run `python3 manage.py migrate` command to migrate.
- Create a super user with `python3 manage.py createsuperuser` command for product admin.
- Create a **Procfile** which specifies the commands that are executed by the app on startup.
- Temporary disable collectstatic by setting `heroku config:set DISABLE_COLLECTSTATIC = 1` and host name of Heroku to allowed hosts in `settings.py`.
- Generate a new secret key, set it up in Heroku and update `settings.py`. Change the setting of Debug mode that only True in Development mode.


## Deployment through Heroku
---
- Navigate to the "Deploy" section.
- Scroll down to "Deployment Method" and select "GitHub".
- Authorize the connection of Heroku to GitHub.
- Search for your GitHub repository name, and select the correct repository.
- For Deployment there are two options, Automatic Deployments or Manual.
- Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
- Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so.
- Ensure the correct branch is selected "master/Main", and select a deployment method. For this project I chose Manual Deployment.


## How to Fork the respository
---
- Log into GitHub.
- In Github go to (https://github.com/Sndrahel/Handywoman.git).
- In the top right hand corner click "Fork".
- A copy of the repository will then be added to your repositories page.

## How to clone the repository
---
- Go to the GitHub repository.
- Locate the Code button which is to the left of the green gitpod button and click it.
- Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard.
- Open Git Bash.
- Change the current working directory to the one where you want the cloned directory.
- Type git clone and paste the URL from the clipboard.
- Press Enter to create your local clone.

 
---
# Credits

## Content:
- [Code Institute](https://codeinstitute.net/) - Inspiration of blog layout were taken from tutorial.
- [Youtube](https://www.youtube.com/results?search_query=python+django+dentist+website+%237) - Tutorial used for setting up sending email .  
- [Startbootstrap](https://startbootstrap.com/) - Core template and contacform taken from this site.
- [Stack Overflow](https://stackoverflow.com/) - Was used to find solutions and debugging.
- [GitHub](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf) - Inspiration of structure for this README file were adapted from this site. 
- [GitHub](https://github.com/rodrigoneumann/photographer-ms4) - Inspiration of structure and contactforms were adapted from this site. 
- [GitHub](https://github.com/ZahraSadiq/Milestone4-PosterBay) - Inspiration of layout for main site were adapted from this site.
 

## Acknowledgments:

- Nishant Kumar: My Code Institute mentor who guided me through this process and shared a lot of valuable knowledge.


[Back to Table of contents](#table-of-contents)

