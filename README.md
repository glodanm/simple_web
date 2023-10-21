# simple_web

## Test task 
https://docs.google.com/document/d/1xnczQj3_efzOi2tuzos4ZiNzxki8JIXqqmZZ7ftKeNo/edit

Create a simple website with two pages: 1) List of Users 2) List of Groups for Users 

**Description of the first page:**

List of Users consist of: username, created, group, actions.
username – User nickname 
created – Date of creating the user
group - Group, to which the user will be added 
actions – two buttons 'Edit' and 'Delete'

Also, under the list there should be a button ‘Add User'
for editing and adding new pages with such fields: username (text input) and group(select)
Please see example below

<img width="468" alt="image" src="https://github.com/glodanm/simple_web/assets/74894897/13e205af-3765-456c-b012-684781948afd">


Description of the second page:

The list of groups should consist of: ID, Name, Description, Actions.
Actions – Edit and Delete buttons 
Also, under the list there should be a button `Add Group`
For editing and adding new pages with such fields: Name (text input) and Description (text input).
Group deletion is impossible if the user is assigned to this group. 

<img width="468" alt="image" src="https://github.com/glodanm/simple_web/assets/74894897/46a724f9-cdd4-47b6-b928-0b2e1325132f">

The images above are added for your overall understanding, do make the same is not necessary, the style is up to you.

To implement the test task, use Django for the backend and HTML, CSS(bootstrapp can be used) for the frontend, the rest technologies are up to you.
The results of your work please push to  GitHub and send us link with access to view and download. 
You have one week to perform this task. In case of any questions please let me know.  


## Installation

1) Clone my [repository](https://github.com/glodanm/simple_web.git) to install project:

```bash
git clone https://github.com/glodanm/simple_web.git
```

2) Open this project in your IDE.

3) Create virtual environment:
```bash
python3 -m venv .venv
```

4) Activate virtual environment:
```bash
source .venv/bin/activate
```

5) Install all required libraries:
```bash
pip install -r requirements.txt
```

6) To run docker:
```bash
docker-compose -d --build
```

7) To run tests:
```bash
docker-compose exec app python manage.py test
```
