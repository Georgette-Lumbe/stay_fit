# Stay Fit

<img src="" width="100%" alt="responsive_image">

The live website can be viewed [here](https://stayfit2022.herokuapp.com/)

# Table of contents
1. [Introduction](#introduction)
2. [UX](#UX)
    * [User Stories](#User-Stories)
    * [Development Planes](#development-planes)
        * [Strategy](#Strategy)
         * [Skeleton](#Skeleton)
            * [Wireframes](#Wireframes)
            * [Database Schema](#Database-Schema)
        * [Structure](#Structure)
            * [Existing Features](#Existing-Features) 
            * [Features Left To Implement](Feature-Left-To-Implement)
    * [Design](#Design)
        * [Typography](#Imagery)
        * [Imagery](#Imagery)

3. [Technolgies Used](#Technologies-Used)        
4. [Testing](#Testing)
5. [Web Marketing](#web-Marketing)
6. [Issues and bugs](#issues-and-bugs)
7. [Deployment](#Deployment)
    * [Deployment Steps](#Deployment-Steps) 
    * [Making a clone to run locally](#Making-a-clone-to-run-locally)
    * [How to Fork the respository](#How-to-Fork-the-Respository)
8. [Languages Used](#languages-used)
9. [Credits](#Credits)
    * [Media](#Media)
    * [Content](#Content)
    * [Code](#Code)
10. [Acknowledgements](#Acknowledgements)

---

# INTRODUCTION

Stay Fit is a eCommerce website where can be find some of materials and clothing for fitness lovers. Users can views all products and all special offers that the website provides. They can view in detail the product that they're interested, add multiple time products in their basket, see the total before the checkout, enter their personnal information. Users can create an account and see their profile with all personal information.

There are many other site features which will be discussed in depth later on in this document.

This is the last of five milestone projects that the developer is required to complete as part of their full web development course at the Code Institute.

# UX

## User Stories

## Development Planes

### Strategy

### Skeleton

#### Wireframes

#### Database Schema

### Structure

#### Existing Features

#### Features Left To Implement

## Design

1. Typography

2. Colour Scheme

3. Imagery

[Go to top](#introduction)

# Testing

Testing information can be found in a separate [testing file]().

# Web Marketing

* Facebook Page

# Issues and bugs

The developper met some issues during the development of the website, below are the issues, bugs and solutions that the developer has encountered:

1. Heroku Login

    * When trying to login to heroku via the workspace, the developper get this error on the window `IP Address Mismatch on signing into Heroku CLI` and find solution on [this post](https://stackoverflow.com/questions/63363085/ip-address-mismatch-on-signing-into-heroku-cli) in stack Overflow. The developer typed `heroku login -i` to the workspace and then logged in.

2. Deployed to Heroku

    * When trying to push the code to Heroku master, the developper get this error `error: src refspec master does not match any`, the developper find the solution to [this post](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1629563663371100?thread_ts=1629559227.368300&cid=C7HS3U3AP) on Slack. 
    * When the site was deployed, the developper get this error `An error occurred in the application and your page could not be served. If you are the application owner, check your logs for details. You can do this from the Heroku CLI with the command heroku logs --tail`, for resolving this, the developper deplaced the Procfile to the root and updated the Procfile content which had a spelling mistake.

3. 

# Deployment

This project was developed using [Gitpod IDE](https://gitpod.io) and pushed to Github using the in-built terminal. However, because Github can only host static websites it was necessary to deploy this project to Heroku because it is a compatible hosting platform for a back-end focused site like Trainees Portal.

This project was deployed using Heroku and stored in GitHub.

## Repository Creation

1. Navigate to [Github](https://github.com/).
2. Create a new repository by first clicking the green button labeled new on the top left of the screen.
3. Select the [Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) in the templates section.
4. Give the repository a name, in this case Trainees Portal.
5. Click the green 'Create Repository' button at the bottom of the page.
6. Inside the repository click the green 'gitpod' button to initialize your repository.
8. Future access to this workspace must be gained through gitpod workspaces, clicking the green button in gitpod again 
will initialize a new workspace.
9. Use the `git add .` command to add all modified and new files to the staging area.
10. Use the `git commit -m` command to commit a change to the local repository.
11. Use the `git push` command to push all committed changes to github.   

Before deploying the website to Heroku, the following five must be followed to allow the app to work in Heroku:

1.  Install `django-gunicorn`, `psycopg2` and `dj_database_url`, `cloudinary` in your workspace cli.

2. Create requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or modules are installed during project development by using the following command:

    - pip freeze --local > requirements.txt

3. Create Procfile that contains the name of the application file so that Heroku knows what to run. If the Procfile has a blank line when it is created remove this as this may cause problems.

4. Create env.py that conrtains all secret variables as DATABASE_URL, SECRET_KEY and CLOUDINARY_URL, this file is hidden.

5. Push these files to GitHub.

## Deployment Steps

Once the above steps are done, the website can be deployed in Heroku using the steps listed below:

1. Log into Heroku .
2. Click the New button.
3. Click the option to create a new app.
4. Enter the app name in lowercase letters.
5. Select the correct geographical region.
6. Click to create

## Add Heroku Postgres Database
1. Click the resources tab in heroku.
2. Under Add-ons search for heroku postgres.
3. Click on heroku postgres when it appears. 
4. Select the Hobby Dev-Free option in plans. 
5. Click submit order form.

## Manipulate the Workspace

1. 
2. 

## Setting up environment variables

1. 
2. 

## Connect Heroku app to Github repository

1. In heroku select the deploy tab.
2. Click github button.
3. Enter the repository name and click search.
4. Select the relevant repository and click connect
5. Select Main branch
6. Click on deploy branch 

## Enable automatic deployment:

1. Click the Deploy tab
2. In the Automatic deploys section, the main branch is enabled to deploy then click Enable Automation Deploys.

## Making a clone to run locally

It is important to note that this project will not run locally unless an env.py file has been set up by the user which contains the DATABASE_URL, SECRET_KEY and CLOUDINARY_URL which have all been kept secret in keeping with best security practices. 

1. Log into GitHub.
2. Select the [respository](https://github.com/Georgette-Lumbe/stay_fit).
3. Click the Code dropdown button next to the green Gitpod button.
4. Download ZIP file and unpackage locally and open with IDE. Alternatively copy the URL in the HTTPS box.
5. Open the alternative editor and terminal window.
6. Type 'git clone' and paste the copied URL.
7. Press Enter. A local clone will be created.

Once the project been loaded into the IDE it is necessary to install the necessary requirements which can be done by typing the following command.

    -pip install -r requirements.txt

## How to Fork the respository.

1. Log into GitHub.
2. In Github go to the [respository](https://github.com/Georgette-Lumbe/stay_fit).
3. In the top right hand corner click "Fork".

---

[Go to top](#introduction)



# Technolgies Used

1. [Python](https://www.python.org/) 
    The following Python modules were used on this project:
    - asgiref==3.4.1
    - backports.zoneinfo==0.2.1
    - dj-database-url==0.5.0
    - Django==3.2.11
    - django-allauth==0.41.0
    - django-countries==7.2.1
    - django-crispy-forms==1.14.0
    - gunicorn==20.1.0
    - oauthlib==3.1.1
    - Pillow==9.0.0
    - psycopg2-binary==2.9.3
    - python3-openid==3.2.0
    - pytz==2021.3
    - requests-oauthlib==1.3.0
    - sqlparse==0.4.2
    - stripe==2.65.0
2. [Django](https://docs.djangoproject.com/en/3.1/)
    - Django was used as the main python framework in the building of this project.
3. [jQuery](https://jquery.com/)
    - This framework was used to create some of the site's interactive functions.
4. [Gitpod](https://gitpod.io)
    - This project was built using Gitpod as the IDE.
5. [Github](https://github.com/)
    - Github was used for online version control and storing files and documents.
6. [Heroku](https://id.heroku.com/)
    - Heroku was used as a cloud-based platform to deploy this site.
7. [Google fonts](https://fonts.google.com/) 
    - The font styles used on this website were chosen from Google fonts.
8. [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Various aspects of this website were structured using Materialize.
    - Bootstrap was used to make this website responsive
9. [Fontawesome](https://fontawesome.com/)
    - The icons used on this page were found in Fontawesome.
10. [Heroku Postgres](https://www.heroku.com/postgres)
    - Heroku was used as the database for this project in production mode after deployment to Heroku.
11. [Django Secret Key Generator](https://djecrety.ir/)
    - Djecrety was used to generate the secrect key for this app.   
12. [Balsamiq](https://balsamiq.com/)
    - The wireframes for this project were created using Balsamiq.
13. [Freeformatter- CSS beautifier](https://www.freeformatter.com/css-beautifier.html)
    - This was used to format the CSS stylesheet.
14. [Freeformatter- HTML formatter](https://www.freeformatter.com/html-formatter.html)
    - This was used to format each HTML page
15. [PEP8online](http://pep8online.com/)
    - PEP8 online was used to make sure all python code was pep8 compliant.
16. [Google DevTools](https://developers.google.com/web/tools/chrome-devtools) 
    - Google Dev Tools was extensively used throughout the project for various styling and testing purposes. Its lighthouse feature was used as one of the main testing tools for this project.
17. [Favicon.io](https://favicon.io/) 
    - This was used to create the site's favicon.
18. [Am I Responsive](http://ami.responsivedesign.is/)
    - This was used to test the responsiveness of the site and also to create the mock-up image presented at the start of this document.
19. - [Dbdiagram.io](https://dbdiagram.io/home)
    - Dbdiagram.io was used to create the Database Schema presented in this document.
20. [StackOverflow](https://stackoverflow.com/)
    - Stack Overflow was used as a general reference resource.
21. 

---

# Languages used

This project is primarily built using:

1. HTML5 semantic markup
2. CSS stylesheets
3. Javascript
4. Python
5. Django
6. Heroku Postgres.
7. 

# Credits

## Media

* All images used in this site was originally obtained from [unsplash](https://unsplash.com/) and [pexels]()

## Content

* 

## Code

* A large portion of this project's code was inspired by Boutique Ado walkthrough. This Code Institute tutorial was instrumental in the creation of this site.
* [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/) : Bootstrap library was used throughout the project mainly to make site responsive.

# Acknowledgements

* I would like to thank the entire slack community for being a source of support, knowledge and positive feedback throughout this project.

* I would like to thank the tutor support for their patience and guidance throughout the development of this project. In particular, I would like to thank scott_ci, Igor_ci, Ed_ci, and Kasia. I really am immensely grateful and cannot thank each of them enough. 

* I would like to thank my own class cohorts for being supportive and helpful throughout the duration of the course. This particular channel provided a great deal of respite and also necessary feedback throughout the course which has proven invaluable for maintaining motivation. 

* Finally I would like to thank my fiance Jimmy for constantly helping to test the project throughout its development, providing insightful suggestions. I would also like to thank Jimmy for his constant love, his ear to listen my ideas and his support throughout this course and for never allowing me to give up, this would not have been possible without him and I will always been grateful for everything he has done to make this possible.
---
[Go to top](#introduction)

