# Retrieve BrewDog recipies from Punk API
# https://punkapi.com/documentation/v2
# Jeff Lung 04/08/2022

import requests

beers = None

# IBU values bitterness of a beer, under 15 means slightly bitter beers.
# Also check brewed date beofre Auguest 2013.
payload = {'ibu_lt': 15, 'brewed_before': '8-2013'}

beers_request = requests.get('https://api.punkapi.com/v2/beers', params=payload)

print("Status code: ", beers_request.status_code)

if beers_request.status_code == requests.codes.ok:
    
    beers = beers_request.json()
    for beer in beers:
        print(beer["id"], beer["name"], beer["first_brewed"])

# New search
beers = None

#  Try fuzzy match with food and matching of supplied name
payload = {'food': 'beef', 'beer_name': 'punk'}

beers_request = requests.get('https://api.punkapi.com/v2/beers', params=payload)

print("Status code: ", beers_request.status_code)

if beers_request.status_code == requests.codes.ok:
    
    beers = beers_request.json()
    for beer in beers:
        print(beer["id"], beer["name"], beer["first_brewed"])
