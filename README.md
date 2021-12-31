# Craigslist Scanner 

This project is used to retrieve search results from Craigslist. The user enters a city and category, then the program scans for those results and prints them to the screen. 

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes.

### Installing On Linux

A step by step series of examples that tell you how to get a development
environment running

Clone and change into directory

    git clone https://github.com/marcaur/craigslist_scanner.git && cd craigslist_scanner

Run this file 

    ./scan_craig.py

### Using 
    example = craig_model.search_craigslist("atlanta","jobs")
    example.scan_site()
    example.view_results()
    
    # if you want to scan for a specific keyword, add the following line at the end
    example.search_keyword("pizza") 


## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details


