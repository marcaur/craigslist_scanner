#! /bin/python3
"""

This is a model for my Craigslist Scanner
You enter a city, category, keyword and the program scans the results to
return a link to the post with the included keyword 

"""
import requests, bs4, sys
import city_dict
from requests.exceptions import HTTPError


URL = city_dict.ALL_CITIES

CITY_LIST = city_dict.ALL_CITIES.keys()

CATEGORIES = {'community': '/d/community/search/ccc', 'services': '/d/services/search/bbb',
'discussion forums': 'https://forums.craigslist.org/?areaID=3', 'housing': '/d/housing/search/hhh',
'for sale': '/d/for-sale/search/sss', 'jobs': '/d/jobs/search/jjj',
'gigs': '/d/gigs/search/ggg', 'resumes': '/d/resumes/search/rrr'}


class search_craigslist:
    def city_search():
        global city
        while True:
            print("What city do you want to search? "); city = str(input()).lower()
            if city not in CITY_LIST:
                print("Please select one of the following cities..")
                # sort cities by alphabet and let user select
                print(CITY_LIST)
                continue
            else:
                print(f"You chose {city}")
                break

    def new_page():
        global NEXT_PAGE
        page_num =  [120,240,360,580]
        # for page in page_num:
        NEXT_PAGE = f"?s={page_num[2]}"

    def connect_to_site():
        page_num =  [120,240,360,580]
        # for page in page_num:
        NEXT_PAGE = f"?s={page_num[2]}"
        global res
        # what category does the user want to search?
        print(CATEGORIES.keys())
        while  True:
            # keep asking the user which category until a match is made
            print("Which category do you want to search?");option = str(input()).lower()
            if option in CATEGORIES.keys():
                CATEGORY_URL = URL[city] + CATEGORIES[option]
                print("Do you want to search another page?"); GO_NEXT = str(input()).lower()
                if GO_NEXT == 'y':
                    CATEGORY_URL = CATEGORY_URL+ NEXT_PAGE
                else:
                    break
                # print(f"This is the URL: {CATEGORY_URL}")
            else:
                print('not a valid category')
                continue
            break

        try:
            res = requests.get(CATEGORY_URL)
            res.raise_for_status()

        except HTTPError as http_err:
            print(f'This HTTP error occured: {http_err}')
            # sys.stdout.write('Program exiting')
            sys.exit('Exiting Progran..')

        except Exception as err:
            print(f'Another error occured: {err}')
            # sys.stdout.write('Program exiting')
            sys.exit('Exiting Progran..')
        else:
            print(f'Connecting to the site...')
            print('Successful Connection!')



    def all_search_results():
        global LOWER_KEYS
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        title_obj = soup.select("h3 > a")

        TITLES = []
        LINKS  = []

        # GET POSTS TITLE
        for title in title_obj:
            TITLES.append(title.getText())
        # GET LINKS FOR POSTS
        for link in title_obj:
            LINKS.append(link.get("href"))
        # dictionary of cities and links
        TOTAL_LIST = dict(zip(TITLES,LINKS))
        # keys converted to lowercase for input validation
        LOWER_KEYS = dict((t.lower(), l) for t, l in TOTAL_LIST.items())
        print(f"These are the results for the whole page \n{TOTAL_LIST}")

    def search_results():
        global LOWER_KEYS
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        title_obj = soup.select("h3 > a")

        TITLES = []
        LINKS  = []

        # GET POSTS TITLE
        for title in title_obj:
            TITLES.append(title.getText())
        # GET LINKS FOR POSTS
        for link in title_obj:
            LINKS.append(link.get("href"))
        # dictionary of cities and links
        TOTAL_LIST = dict(zip(TITLES,LINKS))
        # keys converted to lowercase for input validation
        LOWER_KEYS = dict((t.lower(), l) for t, l in TOTAL_LIST.items())

    def search_keyword():
        while True:
            print("What keyword are you searching for? ")
            keyword = str(input())

            MY_URLS = []

            count = 1
            for key in LOWER_KEYS.keys():
                if keyword not in key:
                    continue
                elif keyword in key:
                    print("Result # " + str(count) + " " + LOWER_KEYS[key])
                    MY_URLS.append(LOWER_KEYS[key])
                    count += 1
                else:
                   break
            break
        print(f"We found {count - 1} URLs that match the word: {keyword}..")

        while True:
            print("Do you want to find another keyword?(Y/N)"); new_word = str(input()).lower()
            if new_word == 'n':
                break
            elif new_word == 'y':
                search_craigslist.search_keyword()
            else:
                print("Please enter Y or N")
                continue
