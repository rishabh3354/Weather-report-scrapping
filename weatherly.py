import requests
from bs4 import BeautifulSoup
import re

def get_temp(data):
    temp_list=re.findall('[0-9]{2}',data)
    print("Current Temperature= "+"MAX= "+temp_list[0]+"°C"+" "+"MIN= "+temp_list[1]+"°C")

def get_Latitude_longitude(data):
    ll = re.findall('[0-9]{2}[.][0-9]{2}[°][" "][A-Z][" "][0-9]{2}[.][0-9]{2}[°][" "][A-Z]', data2)
    print("Location= "+ll[0])


def get_population(data):
    pp = re.findall(r'\d+', data2)
    print("Population= "+pp[-1])

def get_distance_from_sea_level(data):
    t1=[s for s in data.split() if s.isdigit()]
    res="".join(t1)
    print("Distance from SeaLevel= "+res+" Meters")


location=input("Enter City\n")
try:

    url = "https://www.weather-forecast.com/locations/" + location + "/forecasts/latest"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "lxml")
    data = soup.findAll("span", {"class": "phrase"})[0].text

    data2=soup.find_all("p",{"class": "large-loc"})[0].text

except Exception as err:
    print("This is not a city name")
else:

    while True:
        print("\nWhat Information you need about "+location+"\n(T)emperature\n(P)opulation\n(L)ocation\n(S)ea_Level\n(Q)uit")
        choice = input(">>>").lower().rstrip()
        if choice=="q":
            break
        elif choice=="t":
            get_temp(data)
        elif choice=="p":
            get_population(data2)
        elif choice=="l":
            get_Latitude_longitude(data2)
        elif choice=="s":
            get_distance_from_sea_level(data2)
        else:
            print("Invalid choice, please choose again\n")

print("Thank you!\n")
print("Developed by Rishabh Bhardwaj")
