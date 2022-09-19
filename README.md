# Penn Labs Backend Challenge

## Documentation

Fill out this section as you complete the challenge!

## Installation

1. Click the green "use this template" button to make your own copy of this repository, and clone it. Make sure to create a **private repository**.
2. Change directory into the cloned repository.
3. Install `pipenv`
   - `pip install --user --upgrade pipenv`
4. Install packages using `pipenv install`.

## File Structure

- `app.py`: Main file. Has configuration and setup at the top. Add your [URL routes](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing) to this file!
- `models.py`: Model definitions for SQLAlchemy database models. Check out documentation on [declaring models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/) as well as the [SQLAlchemy quickstart](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart) for guidance
- `bootstrap.py`: Code for creating and populating your local database. You will be adding code in this file to load the provided `clubs.json` file into a database.
- `templates` directory with 9 HTML templates listed below.  

## Developing

0. Determine how to model the data contained within `clubs.json` and then complete `bootstrap.py`
1. Run `pipenv run python bootstrap.py` to create the database and populate it.
2. Use `pipenv run flask run` to run the project.
3. Follow the instructions [here](https://www.notion.so/pennlabs/Backend-Challenge-Fall-20-31461f3d91ad4f46adb844b1e112b100).
4. Document your work in this `README.md` file.

## Submitting

Follow the instructions on the Technical Challenge page for submission.

## Installing Additional Packages

Use any tools you think are relevant to the challenge! To install additional packages
run `pipenv install <package_name>` within the directory. Make sure to document your additions.

## Packages
0. json
1. Flask: request, jsonify, render_template, url_for, redirect

## models.py
0. `Club`: Attributes--`id` (primary key), `code`, `name`, `description`, `fav_counter` (# of user favorites a club has), `tags`. To avoid storing arrays in the database, a seperate model `Tags` was created that was linked to `Club` via a ForeignKey. 
1. `Tag`: Relationship with  `Club`. Attributes--`id` (primary key), `club_id` (ForeignKey), `tag` (name of the tag).
2.  `Users`: Attributes--`id` (primary key), `first_name`, `last_name`, `grade`, `school` (within the university), `gender`, `major`, `interests`, `favorites`. `interests` and `favorites` are arrays, so again, seperate models `Interests` and `Favorites` were created that were linked to `Users` via a ForeignKey. 
3.  `Interests`: Relationship with `Users`. Attributes--`id` (primary key), `users_id` (ForeignKey), `interest` (name of the interest). The purpose of this class is to link certain interests (ie. sports, coding etc.) with a user so in the future, we can suggest certain clubs for them through filtering. 
4.  `Favorites`: Relationship with `Users`. Attributes--`id` (primary key), `users_id` (ForeignKey), `favorite` (name of the favorite). Favorites links what clubs a user has marked as favorite to that user's profile. See `fav_club ()`.
5.  Areas to improve/didn't have time to do: Add more attributes, tailor user entries to the variable (ie. more drop downs instead of all fill in the blank). 

## bootstrap.py
0. `create_user ()`: Creates 4  `Users` objects josh, tony, jeff, avi which are associated with `User` attributes listed above. Added to database for testing. 
1. `load_data ()`: Loads the club data from `clubs.json` as `Club` objects. `Tags` objects are created seperately but they are linked to `Club` with the `club` paramter. 
2. Areas to improve/didn't have time to do: first names are lower case because I suspected case sensitivity was the root of `login ()` error mentioned below.

## app.py
0. `/api/clubs` `clubs ()`: Re-constructs `clubs.json` by starting with an empty list, and then appending a json object for every club name. 
1. `/api/finduser` `find_user ()`: Enter first name of a user registered in the database, outputs school and major.
2. `/api/findclub` `find_club ()`: Enter part of a club name, output is club code, description, and how many favorites it has
3. `/api/addclub` `add_club ()`: Enter Club attributes, new club object is added to the database. 
4. `/login/` `login ()`: Enter first name that is in the database (see `signup`), redirects to `fav_club`. This is one example of a way a user can store their personal data. However, there is a bug in the redirect call that I did not have time to fix.
5. `/favclub/<username>` `fav_club ()`: Redirects to this route once you login. Again, there is some issue with the redirect/dynamic routing that I did not have time to fix. 
6. `/api/modifyclub` `modify_club`: Enter club code that is the club to be modified. Tags are the only mutable attributes that a user can change. In the future, I will make admin roles where club leaders can change other attributes of their club.
7. `/api/filter` `filter ()`: Filters tag objects by the club they are associated with. Possible bug.
8. `/signup` `signup ()`: Feature I choose to create. It allows users to create an account that will be stored in the database. Users can type in their `interests` and `favorites` that will be associated with their profile. 
9. Areas to improve/didn't have time to do: Fix bug with login page, printing formatting is jumbled as I didn't have time to make html templates for every route, add roles so different kinds of users can access different routes, improve security with passwords.

## HTML Templates
0. `add_club.html`
1. `clubs.html`
2. `favorites.html`
3. `filter.html`
4. `find_club.html`
5. `find_user.html`
6. `login.html`
7. `modify_club.html`
8. `signup.html`

## TODO
0. Didn't have time, but for webscraping use `BeautifulSoup` to extract the HTML tags associated with the attributes of a `Club` object. 
1. Resolve `login ()` bug.
