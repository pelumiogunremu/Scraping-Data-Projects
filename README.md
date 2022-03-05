# Scraping-Data-Projects
This respository contains my scraping data projects using the scraping tools such as BeautifulSoup, Scrapy, Selenium etc. 

## Project 1 - Canada Businesses Data Extraction using BeautifulSoup

This project involves the extraction of business data such as business name, type and address based on the provinces, cities and landmarks in Canada from the popular business repository - YELLOW PAGES.
The idea that inspired this project is the problem of inadequate tool for the prediction of the fertile location for a particular business type.

### Project Outline
    - https://www.yellowpages.ca/locations/ was the scraped website
    - Request for the webpage content using the requests library
    - Parse the webpage content using the BeautifulSoup from the bs4 library
    - Get the tags using the tag name and class selector
    - Grab all the information needed from the tags and store each in a separate list
    - Import them into the dataframe and export them as a csv file
