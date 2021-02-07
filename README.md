# mission-to-mars

Goal: Creating an application that scrapes various websites for data related to the Mission To Mars. All results are displayed in a single HTML page.

# Process

# Web Scraping

- I created a Jupyter Notebook file (mission_to_mars.ipynb) to use and complete all of my scraping of various Mars-related websites.

- Scraped the Mars News Website and collected the latest News Title and Paragraph Text. I assigned the text to variables that you can reference later.

- The JPL Mars Featured Space Image website was inactive, so I found another NASA website with a featured image of Mars and scraped that data. 

- Visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

- Scraped the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres. 

- Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys img_url and title.

# MongoDb and Flask

- Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs.

- Converted my Jupyter notebook into a Python script called scrape_mars.py with a function called scrape intended to execute all of my scraping code to return one Python dictionary containing all of the scraped data.

- Created a route called /scrape to import my scrape_mars.py script and call my scrape function.

- Stored the return value in Mongo as a Python dictionary.

- Created a root route / to query the Mongo database and pass the mars data into an HTML template to display the data.

- Created a template HTML file called index.html intended take the mars data dictionary and display all of the data in the appropriate HTML elements.

