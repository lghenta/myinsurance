# My Insurance Hub

## Project Overview

My Insurance Hub is a Django-based web application developed that stores OAuth Credentials and API Logs in a database built with Postgres. This application integrates with HubSpot CRM to optimize customer retention and enhance sales strategies through personalized policy renewals and cross-selling functionalities.

## Key Features

- **OAuth Management**: Secure management of OAuth credentials via Django's admin interface. 

Admin can be accessed via http://localhost:8000/admin/ once the app is running. Credentials for accessing the admin interface: user: `newuser` and PAssword: `HubSp0t123`.

- **API Logs**: Secure storage of API request response via Django's admin interface.
- **Contact Managemnt**: Newly added contacts in HubSpot will auto-populate in the Contacts Tab. 


## Technology Stack

- **Django**: The web framework for perfectionists with deadlines.
- **Python 3**: High-level programming language known for its clear syntax and code readability.
- **PostgreSQL**: Robust, open-source object-relational database system.
- **HubSpot CRM**: For seamless customer relationship management and marketing automation.

## Prerequisites

Before you begin, ensure you have the following software installed on your machine:
- **Python 3**: [Download and install Python 3](https://www.python.org/downloads/).
- **PostgreSQL**: [Install PostgreSQL](https://www.postgresql.org/download/) and create a new database.
- **Django**: Django can be installed via pip. Ensure that Python and pip are correctly installed by running `python --version` and `pip --version`.

## Installation

Follow these steps to set up your development environment:

 **Clone the Repository**
   
   git clone https://github.com/yourusername/myinsurancehub.git
   cd myinsurancehub
   run python3 manage.py runserver
   access the application via localhost

## Resources used:

Django:

https://docs.djangoproject.com/en/5.0/intro/tutorial01/
https://docs.djangoproject.com/en/5.0/intro/tutorial01/
https://docs.djangoproject.com/en/5.0/intro/tutorial03/

Postgres:

https://www.postgresql.org/docs/current/tutorial-start.html

HubSpot:

https://developers.hubspot.com/docs/api/developer-tools-overview
https://developers.hubspot.com/docs/api/creating-an-app
https://developers.hubspot.com/docs/api/overview
https://pypi.org/project/hubspot-api-client/
https://developers.hubspot.com/docs/api/working-with-oauth
https://developers.hubspot.com/docs/api/developer-guides-resources

