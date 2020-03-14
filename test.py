import requests

url = "https://tripadvisor1.p.rapidapi.com/restaurants/list-by-latlng"

querystring = {"limit":"30","latitude":"54.34663399999999","longitude":"-7.641581","units":"km"}

headers = {
    'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
    'x-rapidapi-key': "6f44686b06mshc39b79231f8e93dp138755jsnda2781dd3234"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
placeid= "1509068"
#url = "https://tripadvisor1.p.rapidapi.com/reviews/list?location_id=" + placeid
#params = "{'location_id': " + str(location_id) + "}"
#response = requests.request("GET", url  ,data="",  headers= headers)


print(response.text)