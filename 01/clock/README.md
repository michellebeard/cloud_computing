Author: Michelle Beard

StudentID: 1178110

Clock Web Application
=====================
Goal is to create a simple clock application using Google APP Engine 
and Python. 

Setup Environment
-----------------

1. Create virtual environment:
   ```
   $ virtualenv env
   $ source env/bin/activate
   ```
1. Add Google SDK to environment:
   ```
   $ source ~/Applications/google-cloud-sdk/completion.bash.inc
   $ source ~/Applications/google-cloud-sdk/path.bash.inc
   $ gcloud components install app-engine-python
   ```

Run Application
---------------
1. Install Dependencies:
   ```
   $ pip install -r requirements.txt
   $ pip install -t lib WTForms WTForms-Appengine
   ```
1. Run development server:
   ```
   $ dev_appserver.py .
   ```

Deploy Application
------------------
1. To Deploy:
   ```
   $ gcloud app deploy
   ```
2. Visit page [Clock](https://stone-door-180117.appspot.com/).