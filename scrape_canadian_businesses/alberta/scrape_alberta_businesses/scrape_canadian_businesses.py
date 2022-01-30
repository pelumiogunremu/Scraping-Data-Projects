#!/usr/bin/env python
# coding: utf-8

# ## MODULE

# In[1]:


from scrape_businesses import *


# ## FUNCTIONAL PROGRAMS

# #### ALBERTA BUSINESSES

# In[2]:


def extract_alb_bus(index):
  """
  extract alberta businesses by location.
  check the location index in alberta_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[0][index], ca_loc_urls[0][index]) 


# #### BRITISH COLUMBIA BUSINESSES

# In[3]:


def extract_bc_bus(index):
  """
  extract british columbia businesses by location.
  check the location index in british_columbia_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[1][index], ca_loc_urls[1][index])
  


# #### MANITOBA BUSINESSES

# In[4]:


def extract_man_bus(index):
  """
  extract manitoba businesses by location.
  check the location index in manitoba_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[2][index], ca_loc_urls[2][index])


# #### NEW BRUNSWICK BUSINESSES

# In[5]:


def extract_newb_bus(index):
  """
  extract new brunswick businesses by location.
  check the location index in new_brunswick_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[3][index], ca_loc_urls[3][index])
  


# #### NEWFOUNDLAND AND LABRADOR BUSINESSES

# In[6]:


def extract_newfl_bus(index):
  """
  extract newfoundland & labrador businesses at once or by location.
  check the location index in newfoundland_labrador_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[4][index], ca_loc_urls[4][index])     


# #### NOVA SCOTIA BUSINESSES

# In[7]:


def extract_ns_bus(index):
  """
  extract nova scotia businesses by location.
  check the location index in nova_scotia_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[5][index], ca_loc_urls[5][index])


# #### NORTHWEST TERRITORIES BUSINESSES

# In[8]:


def extract_nw_bus(index):
  """
  extract northwest territories businesses by location.
  check the location index in northwest_territories_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  
  return extract_bus(ca_loc[6][index], ca_loc_urls[6][index])    


# #### NUNAVUT BUSINESSES

# In[9]:


def extract_nun_bus(index):
  """
  extract nunavut businesses by location.
  check the location index in nunavut_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[7][index], ca_loc_urls[7][index])


# #### ONTARIO BUSINESSES

# In[10]:


def extract_ont_bus(index):
  """
  extract ontario businesses by location.
  check the location index in ontario_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[8][index], ca_loc_urls[8][index])  


# #### PRINCE EDWARD ISLAND BUSINESSES

# In[11]:


def extract_prin_bus(index):
  """
  extract prince edward island businesses by location.
  check the location index in prince_edward_island_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[9][index], ca_loc_urls[9][index])


# #### QUEBEC BUSINESSES

# In[12]:


def extract_que_bus(index):
  """
  extract quebec businesses by location.
  check the location index in quebec_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[10][index], ca_loc_urls[10][index])


# #### SASKATCHEWAN BUSINESSES

# In[13]:


def extract_sas_bus(index):
  """
  extract saskatchewan businesses by location.
  check the location index in saskatchewan_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[11][index], ca_loc_urls[11][index])


# #### YUKON BUSINESSES

# In[14]:


def extract_yuk_bus(index):
  """
  extract yukon businesses by location.
  check the location index in yukon_locations.csv.
  """
  ca_url = "https://www.yellowpages.ca/locations/"
  ca_prov, ca_prov_urls = get_tag_contents(
      ca_url, "h3", "a", "categories-title catTitle")
  
  thread(get_tags_contents, ca_prov_urls)
  ca_loc, ca_loc_urls = get_tags_contents(
      ca_prov_urls, "li", "a", "resp-list")

  return extract_bus(ca_loc[12][index], ca_loc_urls[12][index])

