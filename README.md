# HANDYWOMAN

## Full Stack Frameworks with Django

![Responsive Mockup](media/mockup.png)  

---

## Project Summary

Handywoman is a site that connect handy women with other handy womens. The site contains a blog page where news, interesting articles, tips and handy trick can be read and commented on. The site also provides a contact form where users can request help / services from handy women.  

This project is my milstone project 4 for Code Institute and is for educational purposes only.

Feel Free to visit the live website: [Handywoman](https://handywoman.herokuapp.com/) 

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

The purpose of this project is to build a site where women connect and exchange knowledge and services

## Scope

Based on the requirements of achieving user's and owner's goals and stories, below is the list of required pages with the features and functions:

- Simple design landing page that the purpose of the website is obvious to anybody and even first-time users know how to navigate the website. 
- Services page where users can view all the services the site provides.
- Blog page where user can read and comment on the latest post / news.
- About page where users can get information about the site and what it provides.
- Contact page where users can contact the admin of the site or to send a quotation,
- Checkout success page where users get confirmation of purchase
- Login / register page where users can log in or register.
- Logout function that users can safely log out the website and takes users back to the home page.
- Blog page management (admin only) where admin can add, edit, approve and delete content.


### User Stories

**ID** | **As a/an** | **I want to be able to...** | **So that I can**
--- | --- | --- | ---
1 | Site User | find responsive ,rich media , with a simple navbar | have a nice user experience
2 | Site User | easily navigate through the website | understand what this website provide
3 | Site User | view a list of services | select one to that suits
4 | Site User | view services details | see description and ask for a qoute
5 | Site User | read blog post about news and tips 
6 | Site User | register an account | comment and share experience
7 | Site User | contact the aministrator of the site | get more information
8 | Site User | get a quotation for service
9 | Administrator | have access to all the functionalities available as a simple user | controll the site and its content
10 | Administrator | add new content | keep the site up to date
11 | Administrator | create, read, update and delete content | manage my site content
12 | Administrator | approve or disapprove comments| filter out objectionable comments


## Structures of the website

Website contains:
- Navigation bar is fixed and collapse to burger icon on mobile devices with essential links to navigate on the website.
- The home page first view will be simple in structure with a short text intro. 
- Below it will contain some information about services and a about snippet with a testimonial carousel. 
- The services page will contain information of what the services can be requested.
- The blog page contain a smaller blog where users can read articles and logged in user can comment.
- The about page will contain information of what the site provides and some information about the site ethos.
- The contact page / request is a clean and simple contact.
- The footer will contains social media links.


## Skeleton

### Wireframes

The website is created as a desktop-first because it is easy to picture the whole image of the website, however, it is a fully mobile responsive website as well so users using a mobile phone have no difficulties toggeling the site. Below are the wireframes of the core pages of the website.

- [Desktop](media/wireframe_desktop.png)
- [Tablet](media/wireframe_tablets.png)
- [Mobile](media/wireframe_mobile.png)


## Surface

### Design

A custom CSS file, placed within the static folder of Handywoman, was used in conjunction with Bootstrap, which serves as the main CSS library. The site is built in dark mode and where I changed the dark theme to basic black. The fonts used are from fontawsome and is built in css file. 

### Media 
Pictures used in this site are taken from:
- [Freepik](https://freepik.com/)
- [Pexels](https://www.pexels.com/)
- [Unsplash](https://unsplash.com/)


---
# Features:

## Existing Features:

### Base

![Landing Page](media/landing_page.png)

The landing page contains two background image with diffrent styles and some text and call to action buttons. 

### Navbar

![Navbar](media/navbar.png)

The navigation bar at the top of each page of the website enables the user to easily access all pages of the website. On smaller devices, the navbar transforms into a burger menu, where links are only visible in a dropdown menu.


### Services Selection

![Services](media/service_page.png)

This is where the users can read more detailed information about services that offers. The services card displays a button from where the users will have a direct access to the contact/request page.


### About Us

![About Us](media/about_page.png)

This is where the users can read more detailed information about what the site is about and who the persons behind it are. 


### Blog Page

![Blog](media/blog_page.png)

The blog page displays an overview of all published blog posts for readers to scroll through. It also has a sidebar panel with a welcome message to users to tell them more about the blog and how often to come back for new blog posts. Logged in users can also comment on posted articles. Before comments are posted on the site they have to be approved by the admin. 


### Contact Page

![Contact](media/contact_page.png)

On the contact page, a form is available for the user to send messages to the admin of the site or to send a request for service. The form contain the fields Name, email, subject, service sellection and message. 


### Sign up a new user

![Sign up](media/signup_page.png)

When accessing the sign up screen, the user must choose a username, password and fill in a email for access to the commenting on the blog-platform.


### User Login

![Login](media/signin_page.png)

On the login screen, the user is asked to fill in his/her login and password for access. 

### Blog Management

The blog management are only accessible to the admin of the website. The admin must approve comments before they are posted. The admin can edit, delete, and add blog posts. 


## Features Left to Implement:

- Register as a supplier/business for advertisment and to receive quotations.  
- Payment options (for supplier) different typ off packages.
- Search option for user so they can search directly after a Pro.
- A chat function were logged in users directly can ask questions.

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
- [Am I responsive](http://ami.responsivedesign.is/) - For mockup

---  
# Testing:

## Validator Testing:
- [W3C Markup Validation Service](https://validator.w3.org/) - For testing HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - For testing CSS code
- [PEP8 Online](http://pep8online.com/) - For checking Python PEP8 requirements. 
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - For testing, style checking and debugging


### This project was tested with the following browsers: 
- Laptop MacOS Big Sur (ver 11.4): Google Chrome


### The following steps were taken:

- Manually testing via Devtools 
- Non-logged in user attempting to access content (refused)
- All buttons and links tested
- Users availing of the like button
- Image uploads tested - large, incorrect format etc. 
- Form tested with correct and incorrect detail 
- Clear user experience & navigation
- Picture loading speed
- Login/register/logout functionalities
- Edit, add, delete items & posts functionalities
- bugs or disabled links

### Issues / Unfixed Bugs:

- Like button not working properly with hovering as well as counting likes - not fixed 
- Testimonial carousell indicators doesnt float within the testimonial card on smaller devices - not fixed
- When running CSS validator there is alot of warnings depending on the full bootstrap theme choosen.
- I had issues with making the contact post - fixed.
- All through I had many issues to make it work as I planned for in the beginning. The main reason for that depends on that I choosed to go with a template instead of doing it all by my self from scratch. I discoverd during the way that it took me much more time to try to change the prewritten scripts then it would have done if I just started from scratch. Al though it has been a good experience with alot of lessons.


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

## Code:
- [Code Institute](https://codeinstitute.net/) - Inspiration of blog layout were taken from tutorial.
- [Youtube](https://www.youtube.com/results?search_query=python+django+dentist+website+%237) - Tutorial used for setting up sending email .  
- [Startbootstrap](https://startbootstrap.com/) - Core template layout contact form taken from this site.
- [Stack Overflow](https://stackoverflow.com/) - Was used to find solutions and debugging.
- [GitHub](https://github.com/Toto-Kotaro-Tanaka/ms4-eagle-golf) - Inspiration of structure for this README file were adapted from this site. 
- [GitHub](https://github.com/rodrigoneumann/photographer-ms4) - Inspiration of structure and contactforms were adapted from this site. 
- [GitHub](https://github.com/ZahraSadiq/Milestone4-PosterBay) - Inspiration of layout for main site were adapted from this site.
 

## Acknowledgments:

- Nishant Kumar: My Code Institute mentor who guided me through this process and shared a lot of valuable knowledge.


[Back to Table of contents](#table-of-contents)

