# teachers-directory
Maintain a directory of teachers in a school.
Allow signup/login and allow logged in users to import teacher details into the system.

## Steps to Install:
- Clone the repo:
  - git clone https://github.com/ranjantanya/teachers-directory.git
- Create and activate virtual environment. If you have virtualenvwrapper installed, run the following command to create a virtual env called test:
  - mkvirtualenv --python=/usr/bin/python3 test
  - workon test
  - If you have multiple versions of python installed on the system, remember to include the path to python3 as shown above.
- Navigate to the directory where you cloned the repo and install requirements:
  - pip install -r requirements.txt
- Apply the migrations:
  - python manage.py migrate
- Collect the static files:
  - python manage.py collectstatic 
- Run the server:
  - python manage.py runserver
  
You should now be able to access the website at http://127.0.0.1:8000/.
Click on the 'Login' option on the top right. Click on the link to sign up once you are on the login page. After a successful registration, 
you should be able to import the teacher details by visiting the 'Import' link from the top menu bar.
