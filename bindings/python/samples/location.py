import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "city": response.get("city")
    }
    return location_data.get("city").lower()


city_from_api = get_location().get("city").lower()

print(city_from_api)
