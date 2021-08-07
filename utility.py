import requests
import random
from geopy.geocoders import Nominatim
class Utility:

  @staticmethod
  def getLatitudeAndLongtitude(location):
    geolocator = Nominatim(user_agent="myApp")
    location = geolocator.geocode(location)
    print(location.address)
    print(location.latitude)
    print(location.longitude)
    return location

  def getRestaurant():
    url = "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng"

    querystring = {
      "latitude":"12.91285",
      "longitude":"100.87808",
      "limit":"30",
      "currency":"USD",
      "distance":"2",
      "open_now":"true",
      "lunit":"km",
      "lang":"en_US"}

    headers = {
        'x-rapidapi-key': "83a545bc5amsh06fbcc7fa996dc6p10a7f0jsn91a017833a3b",
        'x-rapidapi-host': "travel-advisor.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    j = response.json()
    data = []

    for res in j['data']:
      data.append({
        'name' : res['name'] if "name" in res else "-",
        'photo' : res['photo']['images']['medium']['url'] if "photo" in res else "https://i.ibb.co/Lx2Njcn/Paeto-final-project.png",
        'rating' : res['rating'] if "rating" in res else "unrated",
        'description' : res['description'] if "description" in res else "-"
      })

    print(data)
    return data

  def getRestaurantsByLocation(location, radius, rating):
    url = "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng"

    address = Utility.getLatitudeAndLongtitude(location)
    latitude = address.latitude
    longitude = address.longitude


    querystring = {
      "latitude":latitude,
      "longitude":longitude,
      "limit":"30",
      "currency":"USD",
      "distance":radius,
      "open_now":"true",
      "lunit":"km",
      "lang":"en_US",
      "min_rating": rating}

    headers = {
        'x-rapidapi-key': "83a545bc5amsh06fbcc7fa996dc6p10a7f0jsn91a017833a3b",
        'x-rapidapi-host': "travel-advisor.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    j = response.json()
    data = []

    for res in j['data']:
      data.append({
        'name' : res['name'] if "name" in res else "not found",
        'photo' : res['photo']['images']['medium']['url'] if "photo" in res else "https://i.ibb.co/Lx2Njcn/Paeto-final-project.png",
        'rating' : res['rating'] if "rating" in res else "unrated",
        'description' : res['description'] if "description" in res else "please random again",
        'address' : res['address'] if "address" in res else "-",
        'distance' : res['distance_string'] if "distance_string" in res else "-"
      })

    random_number = random.choice(range(0, 29))
    
    print(data[random_number])
    return data[random_number]