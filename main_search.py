#!/bin/python3
"""

[x] enter city into command https://[city].craigslist.org/d/jobs/search/jjj
- there are no spaces between cities with two names e.g new york is newyork

[x] check for cities with two words

[x] create new link according to category

[x] keep cities in list to loop through on schedule


STATIC VARIABLES:

TITLES

LINKS

CITY_LIST

TOTAL_LIST

res

LOWER_KEYS

"""
import requests, bs4, sys
import city_dict, craig_model
from requests.exceptions import HTTPError

CITY_LIST = city_dict.ALL_CITIES.keys()

# this returns the home page for the city
URL = city_dict.ALL_CITIES

CATEGORIES = {'community': '/d/community/search/ccc', 'services': '/d/services/search/bbb',
'discussion forums': 'https://forums.craigslist.org/?areaID=3', 'housing': '/d/housing/search/hhh',
'for sale': '/d/for-sale/search/sss', 'jobs': '/d/jobs/search/jjj',
'gigs': '/d/gigs/search/ggg', 'resumes': '/d/resumes/search/rrr'}



# main activty
while True:
    # ALL OF THE REQUIRED METHODS ARE EXECUTED IN SEQUENCE

    fig = craig_model.search_craigslist  # create the craigslist object
    fig.city_search() # REQUIRED: select which city ou want to search
    fig.connect_to_site() # REQUIRED: after city is selected, run this method
    fig.search_results() # REQUIRED: You have to return some type of results; you can print diff pages or save results to search for keywords
    fig.search_keyword() # OPTIONAL: returns results that include keyword

    print("Do you want to perform another search?(y/n)"); new_search = str(input()).lower()

    if new_search == 'y':
        continue
    elif new_search == 'n':
        sys.exit('Goodbye for now!')
