#!/usr/bin/python3 
import craig_model

try:
    # create the object to search 
    fig = craig_model.search_craigslist("detroit metro","jobs")

    # scan the site 
    fig.scan_site()

    # view results that are printed on command line 
    fig.view_results()

    # search for a keyword that matches in the listing (OPTIONAL) 
    fig.search_keyword("driver")

except KeyError:
    fig.search_city()
    # print("Select from one of the following cities..")