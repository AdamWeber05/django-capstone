# Tidewater App (Name Pending)

## What is this?
We are creating a Django webapp that will allow the employees of Tidewater boats to better track the progress of boats being built in their factory. This will be achieved via a QR code system, where each boat will have a unique QR code that is used to track and/or update its progress. The webapp will also provide a view of all of the boat's current progress on a graph.

## Deployment
Our website can be found at: http://tidewatercsce490.pythonanywhere.com. You must login to be able to access the boat tracking system. 
For testing purposes we recommend making a new user account. 

## Admins
Admins can access there control center at: http://tidewatercsce490.pythonanywhere.com/admin/login/?next=/admin/.
You must have a admin account to log in, you will be able to set permissions, delete users, add users, delete boats, and see all boats that have ever existed. 
Only existing admins can create new admins. Please contact us for your admin credentials. 

## Accounts
All accounts created are non-Admin/manager accounts. To create a new admin, login into the exisiting admin account and manually change them to a 'superuser'. If you have forgotten your password, contact your system admin and they can manually reset it. All passwords are hashed and not saved in plaintext by the system, therefore password recovery is impossible. 

## How to install and use:
Clone the repository to your local computer using the following command line (windows):

```bash
git clone https://github.com/SCCapstone/Tidewater.git
pip3 install -r requirements.txt
cd testsite
py manage.py migrate
py manage.py runserver
```
Clone the repository to your local computer using the following command line (Mac):
```bash
git clone https://github.com/SCCapstone/Tidewater.git
python3 -m pip install -r requirements.txt
cd testsite
python3 manage.py migrate
python3 manage.py runserver
```

  
## Running
Use the next command to run the local server

```python manage.py runserver```

Follow the link provided in the terminal to see the webapp

## Test
To use the unit test
Boat model test is in /solookup/tests.py

``` python manage.py test ```

## Behavior Test
Using Selenium IDE with a chrome extension press play on the test to run
using https://tidewatercsce490.pythonanywhere.com/solookup/
testfile in /Selenium Test

## Our team members
-Jacob Carter
-Scott Craig
-Jake Fuller
-Zachary Kilgore
-Lam Nguyen
-Thomas Scampini
-Adam Weber
