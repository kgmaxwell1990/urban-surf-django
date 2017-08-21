# Urban Surf 
**Ecommerce & Blog Web Application with User Authentication and Stripe Payments**

This Web App was built as a final project for the Code Institute's classroom bootcamp. It is a **fictional** Ecommerce site built with Python's *Django* framework - no template was used.

## Live Demo

Follow this link to view deployed version of the web app https://katie-dev-urban-surf.herokuapp.com/ 

## Built with 
1. Django framework
2. Python
2. HTML
3. CSS
4. Javascript

## URL's

urls.py at the project level (urbanSurf) gives the url patterns routes to views, either directly:

 `from search.views import do_search`

 `urlpatterns = [url(r'^search/', do_search, name='search')]`

Or for the Apps that have their own urls, via the 'include' function:

 `from accounts import urls as accounts_urls`

 `urlpatterns = [url(r'^accounts/', include(accounts_urls))]`

## Views

Views called via URLs are Python functions that perform the different actions required to make the Website function e.g. render a template, log someone in, log them out etc.

## Templates

The base.html page in the top-level templates folder is the base template used for all pages and includes all the links CSS/Bootstrap/Javascript etc. and the fully responsive navbar and footer that appears on all pages of the Website. 
It also contains:
```
{% block content %}
{% endblock content %}
```
Which allows other templates to be inserted in to that section (between the navbar & footer). Linking the base.html to templates within Apps:
```
{% extends 'base.html' %}

{% block content %}

All code for the app goes in here & will appear between the navbar & footer from base.html

{% endblock content %}
```

## Apps

#### Home

The Home App renders the index.html template, which in turn calls the base.html template to present a full webpage with navbar, content and footer.

#### Accounts

The Accounts App is used for full user authentication. When users first visit the website they have two options under 'My Account' - Register if they have no account or Log In if they do. Once Registered/Logged in they can view their own profile that will display their username and email address they used to register with. The two options under 'My Account will then change to Profile or Log Out. It is possible for users to Subscribe to a monthly magazine - once clicked the subscribe function is called within the views.py in the Accounts App which connects with Stripe payments and if the card details are entered correctly into the form it will take a monthly payment from the user.

#### Products/Categories

These Apps display the Products that have been added via Django's admin panel

#### Search

The Search App uses a simple Python function to search through all the products & render the results.html page which displays them

#### Payments/Cart

The Cart App stores the size, quantity and price of all products selected and disaplays a basket total. The Payments App then renders a form for a one-off Stripe payment.

#### Contact

The Contact App is used when the 'Contact Us' link is clicked. The anchor link's href attribute points to the URL 'contact'. From the top level urls.py the 'contact' function is called from the views.py in the Contacts App. This renders the contact.html page which displays the form which has been defined in forms.py within the Contact App. Once the user fills the form in, the 'contact' function is called which checks if the form is valid. If the form is valid, an automatic email is sent to the user acknowledging reciept of the enquiry and a copy of the enquiry is emailed to the website owner. 

#### Blog

blogposts.html displays all blog posts that have been created, either via Django's admin panel or via the form in blogpostform.html. A post consists of a title, content image and tag. The words are truncated to show only 30 words on the main screen so users must click into the blog post to read the entire thing (postdetail.html) Users must be logged in to create or edit posts.
django-disqus must be pip-installed to manage comments on blogposts as well as Pillow, which facilitates upload of images. 

The home page also updates automatically when a new post is added - showing only the 3 newest posts.

## Hosting

This App is hosted on Heroku with automatic deploys from GitHub

## Databases / Static Files

When running locally, SQLite database was used & static and media files were stored locally.
When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. settings.py file was amended for the database & static files to point to the online resources.


## Installation

Follow the below instructions to clone this project for Mac (commands will be slightly different for Windows)

1. Go to folder you want to put the cloned project in your terminal & type:
    `$ git clone https://github.com/kgmaxwell1990/urban-surf.git`
2. Create & Activate a new Virtual Environment:
    Create: `$ python3 -m venv ~/virtualenvs/name_of_environment`
    Activate: `$ source ~/virtualenvs/name_of_environment/bin/activate`
3. Install the project dependancies:
    `$ pip install -r requirements.txt`
4. Create env.sh file at the top level (this will contain all sensitive information)
    **MAKE SURE IT IS IN THE .gitignore FILE**
5. Copy the following into the env.sh file:
```
#!/bin/sh

export SECRET_KEY=''
export DEBUG='True'

export STRIPE_PUBLISHABLE_KEY=''
export STRIPE_SECRET_KEY=''

export EMAIL_HOST_USER='your@gmail.com'    
export EMAIL_HOST_PASSWORD='yourPassword'
```

* A new SECRET_KEY can be generated [here](https://www.miniwebtool.com/django-secret-key-generator/)
* Set up an account with Stripe [here](https://stripe.com/gb) & input STRIPE_PUBLISHABLE_KEY & STRIPE_SECRET_KEY 
* Create email address with gmail & input your credentials

6. Go to settings.py, change the following(lines 177-205):

```
# TO RUN LOCALLY HAVE THESE TWO UNCOMMENTED #

# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'


# TO RUN ON HEROKU HAVE THESE UNCOMMENTED #

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }


AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
```

To this:

```
# TO RUN LOCALLY HAVE THESE TWO UNCOMMENTED #

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# TO RUN ON HEROKU HAVE THESE UNCOMMENTED #

# AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
#         'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#         'Cache-Control': 'max-age=94608000',
#     }


# AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# MEDIAFILES_LOCATION = 'media'
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
```

7. Also in settings.py change the following(lines 112-119):
```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
```

To this:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
```
8. In the terminal:
    `$ python manage.py migrate` - this will apply migrations to your local sqlite database
    `$ python manage.py createsuperuser` - this will create admin support
    `$ python manage.py runserver` - should say starting development server..
9. Go to your browser & type '127.0.0.1:8000' in the address bar
10. The App should run on your browser - note that there will be no products/blog posts as you are running off your own blank database
11. Log in to the admin panel by going to '127.0.0.1:8000/admin' & log in using the credentials you created for the superuser
12. You can add products/categories & blog posts from here

## Running the tests

Automated tests can be viewed in the tests.py file within the separate Apps. 
To run the tests, in your terminal navigate to the folder with your project in, activate your virtual environment and type:

`$ python manage.py test <app name>`

* `$ python manage.py test accounts` - These will all PASS
    tests.py n the Accounts App:
    1. Tests that the UserRegistrationForm validates properly when the correct information is supplied
    2. Tests that the form fails when one of the passwords has not been entered
    3. Tests that the form fails when the passwords to not match

* `$ python manage.py test cart` - This will PASS
    tests.py in the Cart App:
    1. Tests that the url for '/cart/' resolves to the 'cart' function in views.py

* `$ python manage.py test contact` - These will both PASS
    tests.py in the Contact App:
    1. Tests that the url for '/contact/' resolves to the 'contact' function in views.py
    2. Tests that the view returns the correct status code 

etc. etc.






