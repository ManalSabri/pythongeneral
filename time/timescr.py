from datetime import datetime
import pytz

def get_current_time(city, timezone):
    city_time = datetime.now(pytz.timezone(timezone))
    formatted_time = city_time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"{city}: {formatted_time}")

def main():
    print("Current time\n")
    cities_timezones = {
        'London': 'Europe/London',
        'Delhi': 'Asia/Kolkata',
        'Florida': 'US/Eastern',
        'San Diego': 'US/Pacific',
        'Singapore': 'Asia/Singapore',
        'Wuxi': 'Asia/Shanghai'
    }

    for city, timezone in cities_timezones.items():
        get_current_time(city, timezone)

if __name__ == '__main__':
    main()

