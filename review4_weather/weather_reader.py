import json
from weather import Weather

def main(city='athlone'):
    fin = open(f'review3/data/{city}_weather.json', 'r')
    w = fin.read()
    w_dict = json.loads(w)
    desc = w_dict['weather'][0]['description']
    temp = w_dict['main']['temp']
    city = w_dict['name']
    # make a Weather instance
    w = Weather(city, desc, temp)
    print(w)

def checkCity(c):
    if c.lower() in ('athlone', 'athens', 'dublin', 'kista', 'madrid', 'turin'):
        return c
    else:
        return 'athlone'

if __name__ == '__main__':
    whichCity = input('Which city? ')
    city = checkCity(whichCity)
    main(city)