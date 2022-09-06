import json
import time
import schedule
import requests


def get_power_consumption(postal_code):
    """Function to fetch power consumption data"""
    response = requests.get(f"https://rest.fjordkraft.no/pricecalculator/priceareainfo/private/{postal_code}")
    return response.json()
    # return list(map(data.json().get, ['price', 'lastUpdatedPriceAreaDate']))
    # [806.58, '2022-08-30T13:15:00.0666449']


def store_data(data):
    try:
        with open('tmp/data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except ValueError as e:
        return e
    finally:
        print("Done")


def scheduler():
    data = get_power_consumption('4633')
    return store_data(data)


if __name__ == '__main__':
    schedule.every(10).seconds.do(scheduler)

    while True:
        schedule.run_pending()
        time.sleep(1)
