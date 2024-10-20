import requests
import pandas as pd
from bs4 import BeautifulSoup
#website url we need to exytract data is assigned to variable url
url = "https://www.rbi.org.in/Scripts/ATMView.aspx?atmid="
#initialise url_id
url_id = 134
#for getting each data set a for loop with 12 iteration
for each_url in range(1, 13):
    url_new = url + str(url_id)# Construct the complete URL with the current URL ID
    response = requests.get(url_new) # Send a GET request to the URL

    soup = BeautifulSoup(response.text, "html.parser") # Create a BeautifulSoup object to parse the HTML content
    table = soup.find("table", class_="tablebg") # Find the table element with the specified class

    # Find all the anchor tags within the table
    links = table.find_all("a")

    # Extract and print the link addresses
    for link in links:
        address = link["href"]
        print(address)

    url_id = int(url_id) + 1 # Increment the URL ID for the next iteration
