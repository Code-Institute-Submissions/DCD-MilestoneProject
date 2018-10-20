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
- User registeration
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
