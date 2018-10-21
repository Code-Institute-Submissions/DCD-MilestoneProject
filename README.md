# Data Centric Development Milestone Project
The aim of this project is to build a data-driven web application that allows users to store and access cooking recipes. Users will be able to carry out basic CRUD (Create, Read, Update, Delete) operations without having to interact directly with the backend database through a intuitive user interface. Data will be categorised for better organisation and data visualization whilst a simple search function is also provided when users want to search for recipes with particular criteria. Furthermore, a pseudo user authentication feature will be included in order to provide some basic security.

## UX
This project provides users with a intuitive platform to store and share cooking recipes with fellow users who are interested in cooking.

- As a first time user, they will be able to view recipes that can be filtered using predefined groupings or search for particular recipes using a more specified search function.
- They will also be able to add recipes to the site by filling out a structured form. The said recipe will be stored under the name of 'guest'.
- Should the user wish, they can register to the website and become a named user by filling out the registration form.
- In addition to features provided to a anonymous user, a named user can also EDIT and DELETE recipes they have created.
- Furthermore, in order to let users shows their support for recipes, there is a like button on each recipe page. This feature is limited to registered users.
- Recipes added will be rounded up for data visualisation which in turn will be displayed as pie charts.

## Features
### Existing Features
- View recipes in detail
- View recipes list with predefined filter
- Add new recipes to website
- User registration
- User login
- Custom search
- Data visualisation of recipes
- Registered users only: update recipes
- Registered users only: delete recipes
- Registered users only: like recipes

## Technologies Used
- [HTML](https://www.w3.org/html/), [CSS](https://www.w3.org/Style/CSS/), [JavaScript](https://www.javascript.com/), [Python](https://www.python.org/)
	- Languages used for this project.
	- In particular Python has been used exclusively for most of the logic in this project.
- [Materialize CSS](https://materializecss.com/)
	- Frontend language used to standardize layout and design throughout different pages of the website.
- [d3](https://d3js.org/)
	- Library used for data visualization. For this project it is used in conjunction with d3pie mentioned below.
- [d3pie](http://d3pie.org/)
	- An extended library of d3 which focuses on pie charts. This is used for visualizing distribution of recipes' cuisine type and their origin.
- [JQuery](https://jquery.com)
	- For simplifying DOM manipulation. It is also used in conjunction with [Materialize CSS](https://materializecss.com/) for initializing certain components.
- [Bootstrap-select](https://silviomoreto.github.io/bootstrap-select/)
	- Used to aid users in selecting options from dropdown lists as some of them have a vast amount of options such as country of origin.
- [Flask](http://flask.pocoo.org/)
	- Framework used for this project. It is used to handle routing and logic behind the project.

## Testing
Testing for this project has been automated using unittest package from Python. In addition to that coverage.py has been used to ensure a high coverage of code tested. The coverage report has been hosted on [GitHub Pages](https://comacoma.github.io/DCD-MilestoneProject/). Tests are mainly broken in 3 categories:
- Route: to test whether all routes can be reached without raising any problems.
- CRUD operations: to test if the application can carry out CRUD operations as expected.
- Miscellaneous: to test if supplementary features such as custom search and upvote behaves as expected.
One thing to note is that a separate Mongo database, which is a duplicate of the database used for deployment model has been used solely for testing.

During testing, the following points were discovered; some of them have not been addressed in the final build yet.
- Some pages have paginations available to reduce scrolling needed however when users attempt to enter invalid page number for example, 5 when there are only 2 pages available, the application shows some unintended behaviour such as showing one of the available pages or nothing at all. Though this does not cause the application to crash it might confuse users.
- Some features, mainly CRUD operations, rely on a valid recipe id and a username from session (i.e. a logged in user). Verification for said values was not available in earlier builds, causing the application to crash in certain scenarios and it was not notified until testing stage. Regardless, they have been addressed in the final build.

### Responsive design
Another thing to take note of is the responsive design of this project. Using a mobile-first approach, the web app has different layout depending on screen size. To be specific:
- A 1 column layout is used on small screens whilst a 2 column design with roughly 1:2 ratio is used on large screens.
- As provided by [Materialize CSS](https://materializecss.com/), navigation bar automatically collapses into slide-out menu on the side when screen size drops below a certain breakpoint.

## Deployment
This project has been deployed on [Heroku](https://dcd-milestone-colman.herokuapp.com/). As mentioned in Testing section there are in total two Mongo databases prepared for this project, one for deployment and the other for testing. Depending on whether environment variables are provided the application will choose which database to use, as well as whether or not to use debug mode. Basically, if no environment variables are provided (i.e. running the application locally), test database will be used and application will run in debug mode. On the other hand if variables are provided (i.e. on Heroku) the deployment database will be used and application will run with debug mode turned off. Because of this decision, there was no need to write separate settings for testing and deployment.
