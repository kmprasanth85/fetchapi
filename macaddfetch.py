import requests # extra pacakge to install to run this code 
import json
mac = raw_input("Enter the MAC address: ") # To enter the mac address
data = requests.get("https://api.macaddress.io/v1?apiKey=at_AUdP6j6DdX7I2i0RfWjW0WUrVdmso&output=json&search="+mac) #To fetch all the data retrived using mac address and apikey  

#print(data.text)

details = json.loads(data.text)
print "The Company name is: ", details['vendorDetails']['companyName']
print "The MAC Address is: ", details['macAddressDetails']['searchTerm']
