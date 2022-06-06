#! /bin/python3
"""
This is a model for my Craigslist Scanner
You enter a city, category, keyword and the program scans the results to
return a link to the post with the included keyword

Create CSV sheet with data from search 
"""
import requests, bs4, sys, city_dict, pprint
from requests.exceptions import HTTPError


URL = city_dict.ALL_CITIES

CITY_LIST = city_dict.ALL_CITIES.keys()

CATEGORIES = {'community': 'd/community/search/ccc', 'services': 'd/services/search/bbb',
'discussion forums': 'https://forums.craigslist.org/?areaID=3', 'housing': 'd/housing/search/hhh',
'for sale': 'd/for-sale/search/sss', 'jobs': 'd/jobs/search/jjj',
'gigs': 'd/gigs/search/ggg', 'resumes': 'd/resumes/search/rrr'}


class search_craigslist:

    # Collect the data that is being scanned 
    TITLES = []
    LINKS  = []

    def __init__(self,city,category):
        self.self = self
        self.city = city
        self.category = category  

    # print if there is a city error 
    def search_city(self):
        if self.city not in CITY_LIST:
            # if user selects a wrong city, show the list of cities available
            # user may enter correct city, but there are two words; show a city that may match 
            print("Please search for one of the following cities..")
            pprint.pprint(CITY_LIST)
        else:
            print(f"You chose {self.city}")

    def new_page():
        global NEXT_PAGE
        page_num =  [120,240,360,580]
        # for page in page_num:
        NEXT_PAGE = f"?s={page_num[2]}"

        # retrieve the number of pages to scan 
                # loop through the list of different pages 
        print("Do you want to search another page?"); GO_NEXT = str(input()).lower()
        if GO_NEXT == 'y':
            print("ok")
            # CATEGORY_URL = CATEGORY_URL+ NEXT_PAGE
        else:
            print("ok")
            # print(f"This is the URL: {CATEGORY_URL}")
    
    # display if there is a problem with the category chosen 
    def verify_url(self):
        if self.category in CATEGORIES.keys():
            CATEGORY_URL = URL[self.city] + CATEGORIES[self.category]
            print(CATEGORY_URL)
        else:
            print('not a valid category')


    def scan_site(self):
        global res 
        CATEGORY_URL = URL[self.city] + CATEGORIES[self.category]
        
        try:
            res = requests.get(CATEGORY_URL)
            res.raise_for_status()

        except HTTPError as http_err:
            print(f'This HTTP error occured: {http_err}')
            sys.exit('Exiting Program..')
        except Exception as err:
            print(f'Another error occured: {err}')
            # sys.stdout.write('Program exiting')
            sys.exit('Exiting Progran..')
        else:
            print(f'Connecting to the site...')
            print('Successful Connection!')

        soup = bs4.BeautifulSoup(res.text, "html.parser")
        title_obj = soup.select("h3 > a")


        # GET POSTS TITLE
        for title in title_obj:
            search_craigslist.TITLES.append(title.getText())

        # Add the links for posts LINKS
        for link in title_obj:
            search_craigslist.LINKS.append(link.get("href"))


    def view_results(self):
        global LOWER_KEYS
        # Complete dictionary of scanned links
        TOTAL_LIST = dict(zip(search_craigslist.TITLES,search_craigslist.LINKS))

        # keys converted to lowercase for input validation
        LOWER_KEYS = dict((t.lower(), l) for t, l in TOTAL_LIST.items())

        pprint.pprint(f"These are the results for the whole page {TOTAL_LIST}")


    def search_keyword(self, keyword:str):
        # this checks each listing to see if the keyword is present 
        MY_URLS = []
        total_count = 1
        match = 1
        no_match = 1
        for key in LOWER_KEYS.keys():
            if keyword not in key:
                print(f"No match found for '{keyword}'")
                no_match += 1 
                total_count += 1
            elif keyword in key:
                print("Result # " + str(total_count) + " " + LOWER_KEYS[key])
                MY_URLS.append(LOWER_KEYS[key])
                total_count += 1
                match += 1
            else:
                print("Try another keyword")
        print(f"We found {match - 1} URLs that match the word: '{keyword}' and {no_match} that did not..")
        