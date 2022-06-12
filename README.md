# Awwwards

![Awwwards](/static/image/award.png)

## Author: [Sayia Felix](https://github.com/SayiaFelix)

## Description
In this application user/developer is able to post/upload his project and also rates other people projects depending on the userbility ,content,creativity and design.

## API
[Profile Endpoint](https://sir-awwwards.herokuapp.com/api/profile/)
[Projects Endpoint](https://sir-awwwards.herokuapp.com/api/project/)


## User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* View all projects submitted by any user.
* Click on links to visit a live site.
* Search for Project by title.
* Must be signed up to vote
* See averages for the four grading criterias
* Rates Projects.


## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Add, Edit and Delete projects
* Delete projects
* Manage the application.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display all projects with grading | **Home page** | Click links to visit site|
| To add an project  | **Through Admin dashboard and homepage** | Click on add and upload respectively|
| To edit project  | **Through Admin dashboard** | Redirected to the  project form details and editing happens|
| To delete an project  | **Through Admin dashboard** | click on project object and confirm by delete button|
| To search projects by title | **Enter text in search bar** | Users can search by Project Title|
| Comment on projects | **Add comments below respective project** | Users can add comments on any project|
| Vote on projects | **vote** | Users can review projects they like and comment|


## SetUp / Installation Requirements
### Prerequisites
* python3.9
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/SayiaFelix/Awwwards.git
        $ cd Awwwards

## Running the Application
* Creating the virtual environment

        $ python3.9 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.9 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.9 manage.py test

## Technologies Used
* Python3.9
* Django framework and postgresql database

## License

Copyright (c) 2022 Sayia Felix

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
