from flask import Flask, render_template, redirect
from flask_pymongo import Pymongo
import scrape_mars

app = Flask(__name__)

mongo - PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def homepage():
  
    #Find a Record of data from the mongo db#
    mars_one_data = mongo.db.collection.find_one()

    return render_template("index.html", mars=mars_one_data)

@app.route("/scrape")
def scrape():

    #Run scraping function
    mars_data = scrape_mars.scrape()

    #Updated the mongo db using update and upsert=True#
    mongodb.collection.update({}, mars_data, upsert=True)

    #Redirect back to the home page#
    return redirect("/")
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 

