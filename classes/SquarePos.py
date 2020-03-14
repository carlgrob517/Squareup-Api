
import requests
import json

class SquarePos:

  SAND_BASE = "https://connect.squareupsandbox.com/v2"
  PROD_BASE = "https://connect.squareup.com/v2"

  def __init__(self, mode, key):   
    self.mode = mode
    self.key = key 
    self.header = {
    'Accept': "application/json",
    'Authorization': "Bearer " + key,
    'Cache-Control': "no-cache",
    'Content-Type': "application/json",    
    }

  def getLocations(self):
      url = ""
      if self.mode == 'sandbox':
        url = self.SAND_BASE  + "/locations"
      else:
        url = self.PROD_BASE  + "/locations"
      locations_res = requests.request("GET", url  ,data="",  headers=self.header)
      return  locations_res.json()    
      
  def getOrders(self, locations_ids):
      if self.mode == 'sandbox':
        url = self.SAND_BASE  + "/orders/search"
      else:
        url = self.PROD_BASE  + "/orders/search"
            
      orders_data = "{'location_ids': " + str(locations_ids) + "}" 
      response = requests.request("POST", url, data= orders_data, headers=self.header)
      return response.json()


  def getOrderByLimit(self, locations_ids, limits):
      if self.mode == 'sandbox':
        url = self.SAND_BASE  + "/orders/search"
      else:
        url = self.PROD_BASE  + "/orders/search"
            
      orders_data = "{'location_ids': " + str(locations_ids) + ",'limit': " + str(limits) +  "}" 
      response = requests.request("POST", url, data= orders_data, headers=self.header)
      return response.json()


  # limits = -1  mean get all orders 
  def getOrderByFilter(self, ids, limits, start_at, end_at, status ):
      
      if self.mode == 'sandbox':
        url = self.SAND_BASE  + "/orders/search"
      else:
        url = self.PROD_BASE  + "/orders/search"      
      filter =  "{\r\n\"filter\": {\r\n \"date_time_filter\": {\r\n\"closed_at\": {\r\n\"start_at\": "+ '"' + start_at + '"' +" ,\r\n\"end_at\": " + '"' + end_at + '"' + "}\r\n        },\r\n        \"state_filter\": {\r\n          \"states\": [\r\n " + '"' + status + '"'+ "\r\n]\r\n}\r\n},\r\n\"sort\": {\r\n\"sort_field\": \"CLOSED_AT\",\r\n\"sort_order\": \"DESC\"\r\n}\r\n}"
      if limits == -1 :
          orders_data = "{'location_ids': " + str(ids) + ",'query': " + str(filter) +  "}" 
      else :
          orders_data = "{'location_ids': " + str(ids) + ",'limit': " + str(limits) + ",'query': " + str(filter) +  "}" 
            
      response = requests.request("POST", url, data= orders_data, headers=self.header)
      return response.json()



    
  
  def checkOpenShift(self, start_date, end_date):
    if self.mode == 'sandbox':
      url = self.SAND_BASE + "/labor/shifts/search"
    else:
      url = self.PROD_BASE + "/labor/shifts/search"

    filter = '"filter": {"workday": {"date_range": {"start_date": "' + start_date + '","end_date": "' + end_date + '"},"match_shifts_by": "START_AT","default_timezone": "America/Los_Angeles"}}'
    param =  '{"query": {' + filter + '},"limit": 1}'      
    response = requests.request("POST", url, data= param, headers=self.header)
    return response.json()



  def getTimeCards(self):    
    if self.mode == 'sandbox':
      url = self.SAND_BASE + "/me/timecards"
    else:
      url = self.PROD_BASE + "/me/timecards"
    print("--------------wage --------")
    print(url)
    wage = requests.request("GET", url  ,data="",  headers=self.header)
    return wage.json()


  def searchCategory(self, location_ids ,  name, limit):
    if self.mode == 'sandbox':
      url = self.SAND_BASE + "/catalog/search"
    else:
      url = self.PROD_BASE + "/catalog/search"
    
    param = '{"location_ids": '+ str(location_ids) + ', "object_types": ["ITEM"],"query": {"prefix_query": {"attribute_name": "name","attribute_prefix": "' + name + '"}},"limit": ' +str(limit) + '}'        
    print(param)
    
    response = requests.request("POST", url, data= param, headers=self.header)
    return response.json()





