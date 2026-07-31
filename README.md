# Trading_Chart_Alert_API

Environment & Installation: Installed using uv.  

Run commands: uv sync, uv run python manage.py migrate, uv run python manage.py test, uv run python manage.py runserver.  

Architecture Rationale: Used Django REST Framework and explicit config/ module split for production extensibility.  
Utilized IsOwner permissions and restricted get_queryset() to guarantee object isolation. 

Resource Disclosure: 
List used references: Django REST Framework Docs, Django Official Documentation, and uv Documentation.  

Follow these guidelines to test locally
1. Start the local server:
    uv run python manage.py runserver

2. Create a superuser/test user (if you haven't yet):
    Open a separate terminal window and run: uv run python manage.py createsuperuser

3. Follow the prompts to enter a username, email, and password.

Log in via browser:

Open [http://127.0.0.1:8000/api-auth/login/](http://127.0.0.1:8000/api-auth/login/) in your browser.

Log in with the superuser credentials you just created.

Test the Alert Endpoints:

Navigate to [http://127.0.0.1:8000/api/alerts/](http://127.0.0.1:8000/api/alerts/)

GET (List): You will see an HTML interface showing your current list of alerts (initially empty).

POST (Create): At the bottom of the page, DRF renders an HTML form generated from your AlertSerializer. Fill in the fields (symbol, target_price, condition, is_active) and click POST.

GET (Detail): Go to [http://127.0.0.1:8000/api/alerts/1/](http://127.0.0.1:8000/api/alerts/1/) to view a single alert.

PUT / PATCH / DELETE (Update/Delete): Use the buttons at the top of the detail page to test updating or removing the record.

Test Authorization Isolation (Crucial):

Open an Incognito Window (or log out and create/log in as a second user).

Go to [http://127.0.0.1:8000/api/alerts/](http://127.0.0.1:8000/api/alerts/).

Verify that User B cannot see User A's alerts in the list, and trying to open [http://127.0.0.1:8000/api/alerts/1/](http://127.0.0.1:8000/api/alerts/1/) returns a 404 Not Found or 403 Forbidden response.