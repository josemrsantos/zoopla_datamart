import logging
import urllib
import json
import sys
import pickledb
import os.path
import time
import psycopg2
import StringIO
import datamart
from datamart.datamart import *
import settings


def set_price(str_value):
    ''' Sets the price to a range
        ex: 100 = [100, 199] range
        if invalid, return None
    '''
    try: 
        value=int(str_value)
    except:
        return None
    if value<200:
        return "100"
    elif value<300:
        return "200"
    elif value<400:
        return "300"
    elif value<500:
        return "400"
    elif value<600:
        return "500"
    elif value<700:
        return "600"
    elif value<800:
        return "700"
    elif value<900:
        return "800"
    elif value<1000:
        return "900"
    return "1000"


def main(argv):
    ''' Get all house data from zoopla and put it on the DB (DM start schema)
    '''
    
    #### EXTRACT
    print "start EXTRACT"
    page_number = "1"
    page_size = "100"
    max_page = 3
    key = settings.key
    area = "London"
    listing_status = "rent"
    property_type = "houses"
    minimum_price = "10"
    data = []
    for page_number in range(1,max_page):
        url="http://api.zoopla.co.uk/api/v1/property_listings.json?area="+area+"&api_key="+key+"&page_size="+page_size+"&page_number="+str(page_number)+"&listing_status="+listing_status+"&order_by=age&property_type="+property_type+"&minimum_price="+minimum_price
        data_url = urllib.urlopen(url)
        data_raw = data_url.read()
        json_data = json.loads(data_raw)
        if json_data.has_key('listing'):
            data += json_data['listing']

    ### TRANSFORM
    print "start TRANSFORM"
    dm_rent = DataMart(settings.connect_str)
    dim_listing_id = DegenerateDimension("listing_id")
    dim_num_floors = Dimension("dim_num_floors")
    dim_price_range = Dimension("dim_price_range")
    dim_property_type = Dimension("dim_property_type")
    dim_agent_name = Dimension("dim_agent_name")
    dim_num_bedrooms = Dimension("dim_num_bedrooms")
    dim_num_bathrooms = Dimension("dim_num_bathrooms")
    fact_rent_house = Fact("fact_rent_house")
    fact_rent_house.addDimension(dim_listing_id)
    fact_rent_house.addDimension(dim_num_floors)
    fact_rent_house.addDimension(dim_num_bathrooms)
    fact_rent_house.addDimension(dim_price_range)
    fact_rent_house.addDimension(dim_property_type)
    fact_rent_house.addDimension(dim_agent_name)
    fact_rent_house.addDimension(dim_num_bedrooms)
    dm_rent.addFact(fact_rent_house)

    for l in data:
        fact_rent_house.addFactLine((l['listing_id'], l['num_floors'], l['num_bathrooms'], set_price(l['price']), l['property_type'], l['agent_name'], l['num_bedrooms']))

    ### LOAD
    print "start LOAD"
    dm_rent.LoadDB()

# Call main if not imported
if __name__ == "__main__":
    main(sys.argv)
