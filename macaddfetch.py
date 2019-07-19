import requests # extra pacakge to install to run this code 
import json
mac = raw_input("Enter the MAC address: ") # To enter the mac address
apikey = raw_input("Enter the API key: ") # Enter API Key
data = requests.get("https://api.macaddress.io/v1?apiKey="+apikey+"&output=json&search="+mac) #To fetch all the data retrived using mac address and apikey

#print(data.text)

details = json.loads(data.text)
print "The Company name is: ", details['vendorDetails']['companyName']
print "The MAC Address is: ", details['macAddressDetails']['searchTerm']
