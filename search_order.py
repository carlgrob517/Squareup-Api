
import requests
import json
from datetime import datetime

sandbox_order_url = "https://connect.squareupsandbox.com/v2/orders/search"
sandbox_location_url = "https://connect.squareupsandbox.com/v2/locations"

production_location_url = "https://connect.squareup.com/v2/locations"
production_order_url = "https://connect.squareup.com/v2/orders/search"

payload = ""
#EAAAEETPhjxWoRLi59B9gqAXQmYYBuApAb0IzFgiL5oVopPCPXSKE7mWSrB3e_KG  // client's product account
headers = {
    'Accept': "application/json",
    'Authorization': "Bearer EAAAEETPhjxWoRLi59B9gqAXQmYYBuApAb0IzFgiL5oVopPCPXSKE7mWSrB3e_KG",
    'Cache-Control': "no-cache",
    'Content-Type': "application/json",    
    }
#EAAAEEE1dvPti_XlTNZiNrDQlIRIgE8lUhoo3M3DoLGk7BD4k7o3IfC7nj9ZkcLM   my sandbox account

# get location ids
locations_res = requests.request("GET", production_location_url ,data=payload,  headers=headers)
data1 = locations_res.json()

# parse ids  from response
location_lists = []
for item in data1["locations"]:
  location_lists.append(item["id"])

# generage parameter and call search order api for search order api
orders_data = "{'location_ids': " + str(location_lists) + "}" #,'limit': 10
response = requests.request("POST", production_order_url, data= orders_data, headers=headers)

# create file and save json result
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%H_%M_%S")
name = dateTimeObj.microsecond
file = open( "ApiCall_" +  str(timestampStr) + ".txt", "x")
file.write(response.text)
file.close()
print("File Created !!! File name: " + "ApiCall_" +  str(timestampStr) + ".txt")



