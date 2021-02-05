from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    #Visit Mars News Site#
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    #Get First News Title$
    title_test = soup.find_all('div', class_='bottom_gradient')
    title_f = title_test[0]
    news_title = title_f.find('h3').text.strip()
    #Get Paragraph Description of the Article#
    para_test = soup.find_all('div', class_='rollover_description_inner')
    para_title = para_test[6].text.strip()
    
    #Get Featured Image URL#
    feat_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(feat_url)
    browser.links.find_by_partial_text('FULL IMAGE')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('img', class_="headerimage fade-in")
    feat_img_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/" + "image/featured/mars3.jpg"
    
    #Get Mars Facts Table#
    table_url ="https://space-facts.com/mars/"
    tables = pd.read_html(table_url)
    df = tables[0]
    mars_table_html = [df.to_html(classes='data table table-borderless', index=False, header=False, border=0)]

    #Get Mars Hemisphere Info: Creating a List of Hemisphere Names#
    url_hem = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hem)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='collapsible results')
    
    #Find the Name of the Hemispheres#
    hems = results[0].find_all('h3')

    hem_names = []

    for hem in hems:
        hem_names.append(hem.text)
    
    thumb_results = results[0].find_all('a')
    thumb_links = []

    #Find the thumbnail links to click through#
    for thumb in thumb_results:
        if (thumb.img):
            thumb_url = "https://astrogeology.usgs.gov/" + thumb['href']
        
        thumb_links.append(thumb_url)
    
    #Clicking through thumbnail links to find full-size images#
    full_img = []

    for link in thumb_links:
        browser.visit(link)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        results2 = soup.find_all('img', class_='wide-image')
        img_path = results2[0]['src']
        img_link = "https://astrogeology.usgs.gov/" + img_path
    
        full_img.append(img_link)
    
    #Creating the Mars Dictionary#
    hem_zip = zip(hem_names, full_img)

    hem_img_url_list = []

    for title, img in hem_zip:
        hem_dic = {}
        hem_dic['title'] = title
        hem_dic['img_url'] = img
        hem_img_url_list.append(hem_dic)
    
    #Create Your Return Dictionary#
    mars_dict = {
        "news_title": news_title,
        "news_paragraph": para_title,
        "featured_image": feat_img_url,
        "mars_facts": mars_table_html,
        "hemispheres": hem_img_url_list
    }

    #Close the Browser after scraping
    browser.quit()

    #Return Results#
    return mars_dict