import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


# Gets the location data from the IP fetched.
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "city": response.get("city")
    }
    return location_data.get("city").lower()


city_from_api = get_location()

# Formats the location data to the values recognized by the Nordpool API.
def format_city(city):
    cities = {"oslo": "oslo", "kristiansand": "kr.sand", "bergen": "bergen", "trondheim": "tr.heim", "tromsø": "tromsø",
              "molde": "molde"}
    return cities.get(city)

