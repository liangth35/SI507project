# SI507project  
## Required packages:   
bs4   
flask   
requests   
pandas   
plotly   

## To run the code:   
If you want to rerun the whole crawling process: delete gamelist.csv and gameData.json, then
run all the cells in Project_retrieve_data.ipynb. It will take roughly an hour to crawl and scrap 6544 games from steam.   

Then, run Project.py in command line, a link will be generated (http://127.0.0.1:5001), the flask app will be available in that address. 
On the homepage, you can type in the range of price, release date, rating, and number of reviews of games you would like to search for, 
you can also choose to search for discounted games only. After the ranges have been set, click on "Search" button and the results 
will show up. On the result page, you can choose to sort the games by price, release date, rating, and number of reviews in both 
descending and ascending order. You can also select an attribute and plot its distribution by clicking on "Plot" button. When in the 
plot page, clicking "Return" button will take you back to results page.   

## Data structure
The data structure I use in this project is a kd-tree. It is a variant of binary search tree, in which nodes are partitioned in 4 dimensions in turn as depth grows. I organize the game data into classes named Node. Other than the game data, each node has left and right child, which are set to None by default. I use 4 numeric attributes in game data: release date, original price, discounted price, and rating, as the 4 dimensions of this kd-tree. 