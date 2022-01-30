#!/usr/bin/env python
# coding: utf-8

# ## LIBRARIES

# In[1]:


import concurrent.futures
import requests
from bs4 import BeautifulSoup
import pandas as pd


# ## FUNCTIONAL PROGRAMS

# In[2]:


def thread(function, webpage_urls):
  """
  speed up the request for html pages
  """

  with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(function, webpage_urls)

def get_tag_contents(webpage_url, tag_name, find_tag, class_selector):
    """
    requests for the html content of the web page.
    parse the requested web page content into its component parts
    for easy extraction.
    locate all the tags with the given tag name and class selector.
    extract the text, url from each tag and store it in the 
    texts, urls list.
    """
    
    thread(requests.get, webpage_url)
    soup = BeautifulSoup(requests.get(webpage_url).text, "html.parser")
    
    tags = [
        tag.find(find_tag, href=True) 
        for tag in soup.find_all(tag_name, class_=class_selector)
    ]
    
    tag_texts = [tag.text for tag in tags]
    tag_urls = [f"https://yellowpages.ca{tag['href']}" for tag in tags]
    
    return tag_texts, tag_urls


def get_tags_contents(webpage_urls, tag_name, find_tag, class_selector):
    """
    requests for the html content of the web page.
    store the webpage contents in a list.
    parse the webpage contents.
    store the parsed contents in a list.
    extract all texts, urls from the tags at once.
    """
    
    thread(requests.get, webpage_urls)
    web_contents = [
        webpage_content 
        for webpage_content in (
            requests.get(url).text for url in webpage_urls
        )
    ]
    
    parsed_contents = [
        parsed_content 
        for parsed_content in (
            BeautifulSoup(content, "html.parser")
            for content in web_contents
        )
    ]
    
    tags_texts = [
                  [
                      tag.text for tag in [
                          tag.find(find_tag, href=True)
                          for tag in parsed_content.find_all(
                              tag_name, class_=class_selector
                          )
                      ]
                  ]
        for parsed_content in parsed_contents
    ]

    tags_urls = [
                  [
                      f"https://yellowpages.ca{tag['href']}" for tag in [
                          tag.find(find_tag, href=True)
                          for tag in parsed_content.find_all(
                              tag_name, class_=class_selector
                          )
                      ]
                  ]
        for parsed_content in parsed_contents
    ]

    return tags_texts, tags_urls


def get_tags_texts(webpage_urls):
    """
    requests for the html content of the web page.
    store the webpage contents in a list.
    parse the webpage contents.
    store the parsed contents in a list.
    extract needed texts from the tags at once.
    """
    
    thread(requests.get, webpage_urls)
    web_contents = [
        webpage_content 
        for webpage_content in (
            requests.get(url).text for url in webpage_urls
        )
    ]
    
    
    parsed_contents = [
        parsed_content 
        for parsed_content in (
            BeautifulSoup(content, "html.parser")
            for content in web_contents
        )
    ]

    tags_texts_1 = [
                  [
                      tag.text for tag in [
                          tag.find("a", href=True)
                          for tag in parsed_content.find_all(
                              "h3", class_="listing__name jsMapBubbleName"
                          )
                      ]
                  ]
        for parsed_content in parsed_contents
    ]
 
     
    tags_texts_2 = [
                 [
                     tag.text for tag in [
                         tag.find("a", href=True)
                         for tag in parsed_content.find_all(
                             "div", class_="listing__headings"
                         )
                     ]
                 ]
        for parsed_content in parsed_contents
    ]

    tags_texts_3 = [
               [    
                    tag for tag in [
                        tag.find(itemprop="streetAddress")
                        for tag in parsed_content.find_all(
                            "div", class_="listing__address address mainLocal noNum"
                        )
                    ]
                ]
        for parsed_content in parsed_contents
    ]

    tags_texts_4 = [
               [    
                    tag for tag in [
                        tag.find(itemprop="addressLocality")
                        for tag in parsed_content.find_all(
                            "div", class_="listing__address address mainLocal noNum"
                        )
                    ]
                ]
        for parsed_content in parsed_contents
    ]

    tags_texts_5 = [
               [    
                    tag for tag in [
                        tag.find(itemprop="addressRegion")
                        for tag in parsed_content.find_all(
                            "div", class_="listing__address address mainLocal noNum"
                        )
                    ]
                ]
        for parsed_content in parsed_contents
    ]

    tags_texts_6 = [
               [    
                    tag for tag in [
                        tag.find(itemprop="postalCode")
                        for tag in parsed_content.find_all(
                            "div", class_="listing__address address mainLocal noNum"
                        )
                    ]
                ]
        for parsed_content in parsed_contents
    ]

    tags_texts_7 = [
               [    
                    tag for tag in [
                        tag.find(tabindex="0")
                        for tag in parsed_content.find_all(
                            "li", class_="mlr__submenu__item"
                        )
                    ]
                ]
        for parsed_content in parsed_contents
    ]
    
    tags_texts = [
        [i for texts in tags_texts_1 for i in texts],
        [i for texts in tags_texts_2 for i in texts],
        [i for texts in tags_texts_3 for i in texts],
        [i for texts in tags_texts_4 for i in texts],
        [i for texts in tags_texts_5 for i in texts],
        [i for texts in tags_texts_6 for i in texts],
        [i for texts in tags_texts_7 for i in texts]
    ]

    texts_titles = [
                   "name",
                   "type",
                   "str_addr",
                   "addr_loc",
                   "addr_reg",
                   "post_code",
                   "phone_num"
    ]
    
    titles_texts = pd.concat(
        [pd.Series(text, name=title) for title, text in zip(
            texts_titles, tags_texts)], axis=1)

    return titles_texts

def extract_bus(text, url):
  """
  extract the bus, bus_type and bus_addr of each location within a 
  province into a csv file
  """

  thread(get_tag_contents, url)
  bus_cats, bus_cat_urls = get_tag_contents(
      url, "h3", "a", "categories-title catTitle")
 
  thread(get_tags_contents, bus_cat_urls)
  subbus_cat, subbus_cat_urls = get_tags_contents(
      bus_cat_urls, "h3", "a", "categories-title catTitle")

  subbus_cat_urls = [i for url in subbus_cat_urls for i in url]
  thread(get_tags_contents, subbus_cat_urls)
  subsubbus_cat, subsubbus_urls = get_tags_contents(
      subbus_cat_urls, "li", "a", "resp-list")

  subsubbus_urls  = [i for url in subsubbus_urls for i in url]
  thread(get_tags_texts, subsubbus_urls)
  bus = get_tags_texts(subsubbus_urls)

  pd.DataFrame(bus).to_csv(f"{text.lower().replace(" ", "-")}-businesses.csv", index=False)

  return "extraction complete!"

