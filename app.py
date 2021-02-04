from flask import Flask
import scrape_mars

app = Flask(__name__)

@app.route("/")
def welcome():
    """call scraping function"""
    return scrape_mars.scrape()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 

    
