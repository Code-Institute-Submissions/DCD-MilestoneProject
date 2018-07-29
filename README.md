# Data Centric Development Milestone Project
<details><summary>Details</summary>
- The aim of this project is to build a data-driven web application that allows users to store and access cooking recipes.
- Users will be able to add, edit and delete recipes.
- Recipes stored will be grouped base on their attributes such as cuisines, country of origin, allergens, ingredients, etc. Such groups will be clickable to reveal recipes that fall into their respective categories.
- On top of basic grouping, users will also be able to search for recipes.
- The application will provide user registeration and authentication for better security. (i.e. users can only edit or delete recipes they created)

</details>

## Change Log

### 29/07/2018
- Added basic groupings of recipes such as showing the 5 most recently added recipe on index.html whilst giving a more detailed list (up to 20 items) in a separate page. As of now, there are 3 default groupings:
	- New Arrivals (recently added recipes)
	- Most Popular (recipes with most views)
	- Capricious Recipes (recipes created by 'guests')
More groupings will be added including more advanced ones where user can adjust criteria for example, users can filter recipes that has a particular country of origin.

### 27/07/2018
- CRUD operation implemented on recipes.
	- Though update and delete is only available to the one who created the recipe whilst creating a new recipe and viewing recipes are available to anyone event if they are not logged in (as 'guest') however, recipes created by 'guests' cannot be edited and deleted by anyone.
	- As of now, users can view recipes they created from their user page, though proper methods of viewing recipes in general has not been established yet (except for the route).

### 22/07/2018
- User login functionality implemented.
- Ability to add recipe implemented.