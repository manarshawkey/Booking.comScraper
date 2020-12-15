#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
--Project Description: 
    Create an RPA (Scrapper) using python that opens booking.com and searches for hotels in Hurghada. 
    Populate a csv file with the information below for the first 10 hotels that appear. 

        1- Hotel Name
        2- Rating Score, example 8.7 or 8
        3- Rating Value, example Excellent or Very Good
        4- Number of Reviews
        
--Date Created: Thursday, Oct 29th, 2020
--Developer: Manar Shawkey

"""
from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaEOIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4AtiH6PwFwAIB0gIkMjJmZDg3ZTUtOGY0MS00NjRjLTljZWItNjhjODk2MDE0M2M22AIE4AIB&lang=en-gb&sid=f0ca66a1c6bc3a097c0c9a7c880384e5&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaEOIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4AtiH6PwFwAIB0gIkMjJmZDg3ZTUtOGY0MS00NjRjLTljZWItNjhjODk2MDE0M2M22AIE4AIB%3Bsid%3Df0ca66a1c6bc3a097c0c9a7c880384e5%3Bsb_price_type%3Dtotal%26%3B&ss=Hurghada%2C+Red+Sea+Governorate%2C+Egypt&is_ski_area=&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=hurga&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=-290029&dest_type=city&iata=HRG&place_id_lat=27.258932&place_id_lon=33.811974&search_pageview_id=d509a7acd11b011a&search_selected=true&search_pageview_id=d509a7acd11b011a&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0').text
soup = BeautifulSoup(source, 'lxml')
output_file = open('booking_scrape.csv', 'w')
csv_writer = csv.writer(output_file)
csv_writer.writerow(['Hotel Name', 'Rating Score', 'Score Title', 'Number of Reviewers'])
hotels = soup.findAll('div','sr_property_block')
for i in range(10):
    hotel = hotels[i]
    hotel_title = hotel.find('div', class_='sr-hotel__title-wrap')
    hotel_name = hotel_title.find('span', 'sr-hotel__name').text
    hotel_review = hotel.find('div', class_='reviewFloater')
    Rating_score = hotel_review.find('div', class_='bui-review-score__badge').text
    Score_title = hotel_review.find('div', class_='bui-review-score__title').text
    number_of_reviewers = hotel_review.find('div', class_='bui-review-score__text').text
    csv_writer.writerow([hotel_name, Rating_score, Score_title, number_of_reviewers])
output_file.close()


# In[ ]:




