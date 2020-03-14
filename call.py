from classes.SquarePos import SquarePos
from datetime import datetime


# ----------------------------------------------- GET Location API ---------------------------------------------------------------------
squarePos = SquarePos("production", "EAAAEETPhjxWoRLi59B9gqAXQmYYBuApAb0IzFgiL5oVopPCPXSKE7mWSrB3e_KG")
res = squarePos.getLocations()

location_lists = []
location_lists_string = "["
location_id = ''
dateTimeObj = ''
index = 0
for item in res["locations"]:
  location_lists.append( '"' + item["id"] + '"')
  if index == 0:
    location_lists_string = location_lists_string +  '"' + item["id"] + '"'
  else:
    location_lists_string = location_lists_string +  ',"' + item["id"] + '"'
  location_id = item["id"]
  index = index + 1
location_lists_string  = location_lists_string + ']'
# ------------------------------------------------- Order Relative APIS ------------------------------------------------------------------
#res = squarePos.getOrders(location_lists)
#res = squarePos.getOrderByLimit(location_lists, 4)
#res = squarePos.getOrderByFilter(location_lists, -1 , "2020-01-01T20:00:00+00:00", "2020-01-06T21:54:45+00:00", "COMPLETED") #COMPLETED


# ----------------------------------------------  Employee and Shift APIS ---------------------------------------------------------------
res = squarePos.getEmployees(location_id)
employee_id = ''
for item in res["employees"]:
  employee_id = item["id"]  
#res = squarePos.getEmployeeWage(employee_id)
#res = squarePos.checkOpenShiftByEmployeeId(employee_id)
#res = squarePos.createShift(employee_id, location_id, start_at="2020-02-19T17:00:00+00:00", title="Programmer",amount=345, currency="USD")
#res = squarePos.checkOpenShift("2019-01-20", "2019-01-20")
#res = squarePos.getTimeCards()
res = squarePos.searchCategory( location_lists_string,  "Aloo", 100)

print(res)





#------------------------------------------------ Generate Json Txt File ------------------------------------------------------------------
# dateTimeObj = datetime.now()
# timestampStr = dateTimeObj.strftime("%H_%M_%S")
# name = dateTimeObj.microsecond
# file = open( "ApiCall_" +  str(timestampStr) + ".txt", "x")
# file.write(str(res))
# file.close()
#print("File Created !!! File name: " + "ApiCall_" +  str(timestampStr) + ".txt")
