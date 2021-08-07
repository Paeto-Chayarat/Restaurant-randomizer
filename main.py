from flask import Flask, render_template, request
from utility import Utility

web_site = Flask(__name__)

@web_site.route('/')
def index():
  restaurant = Utility.getRestaurant()
  return render_template('index.html', restaurant = restaurant)

@web_site.route('/search', methods=['POST'])
def getRestaurantsByLocation():
    location = request.form['location']
    radius = request.form['radius']
    rating = request.form['rating']
    restaurants = Utility.getRestaurantsByLocation(location, radius, rating)
    return render_template('restaurants.html', restaurants=restaurants)

web_site.run(host='0.0.0.0', port=8080)