# Data Centric Development Milestone Project
<details><summary>Details</summary>
- The aim of this project is to build a data-driven web application that allows users to store and access cooking recipes.
- Users will be able to add, edit and delete recipes.
- Recipes stored will be grouped and summarised base on their attributes such as cuisines, country of origin, allergens, ingredients, etc. Such groups will be clickable to reveal recipes that fall into their respective categories. The summary will be presented graphically categories will be clickable for a filtered view base on that category.
- On top of basic grouping, users will also be able to search for recipes.
- The application will provide user registration and authentication for better security. (i.e. users can only edit or delete recipes they created)

</details>

## Change Log

### 02/08/2018
- Added pagination to custom search results, view all recipes, recipes by cuisine and recipes by origin.
- Improved Pie charts' responsiveness.

### 01/08/2018
- Added route for viewing all recipes without any filters (all_recipes.html).
- Added like(upvote) feature. This feature is limited to registered users.
- Added another default grouping: Most likes(upvote).
- Data visualization on certain groupings such as recipes by cuisine and recipes by country of origin will be shown on index.html. Individual pages of such grouping have also been added.
- Custom search implemented, allowing users to search for particular recipes base on specific requirements.

### 29/07/2018
- Added basic groupings of recipes such as showing the 5 most recently added recipe on index.html whilst giving a more detailed list (up to 20 items) in a separate page. As of now, there are 3 default groupings:
	- New Arrivals (recently added recipes)
	- Most Popular (recipes with most views)
	- Capricious Recipes (recipes created by 'guests')

### 27/07/2018
- CRUD operation implemented on recipes.
	- Though update and delete is only available to the one who created the recipe whilst creating a new recipe and viewing recipes are available to anyone event if they are not logged in (as 'guest') however, recipes created by 'guests' cannot be edited and deleted by anyone.
	- As of now, users can view recipes they created from their user page, though proper methods of viewing recipes in general has not been established yet (except for the route).

### 22/07/2018
- User login functionality implemented.
- Ability to add recipe implemented.
