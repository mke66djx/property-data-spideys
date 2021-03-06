# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PierceCountyDescriptionItem(scrapy.Item):
    owner_name = scrapy.Field()
    owner_last_name = scrapy.Field()
    owner_first_name = scrapy.Field()
    owner_2_first = scrapy.Field()
    parcel = scrapy.Field()
    site_address = scrapy.Field()
    mailing_address = scrapy.Field()
    mail_city = scrapy.Field()
    mail_state = scrapy.Field()
    mail_zip = scrapy.Field()
    tax_year_1 = scrapy.Field()
    tax_year_2 = scrapy.Field()
    tax_year_3 = scrapy.Field()
    tax_year_1_assessed = scrapy.Field()
    tax_year_2_assessed = scrapy.Field()
    tax_year_3_assessed = scrapy.Field()
    current_balance_due = scrapy.Field()
    square_footage = scrapy.Field()
    acres = scrapy.Field()
    electric = scrapy.Field()
    sewer = scrapy.Field()
    water = scrapy.Field()
    property_type = scrapy.Field()
    occupancy = scrapy.Field()
    building_square_footage = scrapy.Field()
    lot_square_footage = scrapy.Field()
    lot_acres = scrapy.Field()
    attached_garage_footage = scrapy.Field()
    year_built = scrapy.Field()
    adj_year_built = scrapy.Field()
    stories = scrapy.Field()
    bedrooms = scrapy.Field()
    baths = scrapy.Field()
    siding_type = scrapy.Field()
    units = scrapy.Field()
    exemption = scrapy.Field()

class DuvalCountyDescriptionItem(scrapy.Item):
    parcel = scrapy.Field()
    owner_name = scrapy.Field()
    building_type = scrapy.Field()
    site_address = scrapy.Field()
    mailing_address = scrapy.Field()
    property_type = scrapy.Field()
    building_square_footage = scrapy.Field()
    year_built = scrapy.Field()
    stories = scrapy.Field()
    baths = scrapy.Field()
    bedrooms = scrapy.Field()
    siding_type = scrapy.Field()
    units = scrapy.Field()
    sale1_price = scrapy.Field()
    sale1_date = scrapy.Field()
    sale2_price = scrapy.Field()
    sale2_date = scrapy.Field()
    tax_year_1_assessed = scrapy.Field()
    tax_year_2_assessed = scrapy.Field()
    lot_square_footage = scrapy.Field()
    lot_acres = scrapy.Field()
    electric = scrapy.Field()
    sewer = scrapy.Field()
    units = scrapy.Field()
    water = scrapy.Field()
    senior_exemption = scrapy.Field()
    homestead_exemption = scrapy.Field()
    currentTaxDue = scrapy.Field()
    currentDelinquentTax = scrapy.Field()

class DuvalSalesItem(scrapy.Item):
    parcel = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()
    document = scrapy.Field()


class CookCountyDescriptionItem(scrapy.Item):
    list_pin = scrapy.Field()
    parcel = scrapy.Field()
    owner_name = scrapy.Field()
    owner_first = scrapy.Field()
    owner_2_first = scrapy.Field()
    owner_last = scrapy.Field()

    site_address = scrapy.Field()
    site_address_city = scrapy.Field()
    site_address_zip = scrapy.Field()
    site_address_township = scrapy.Field()

    mailing_address= scrapy.Field()
    mail_city = scrapy.Field()
    mail_state = scrapy.Field()
    mail_zip = scrapy.Field()

    age = scrapy.Field()
    lot_square_footage = scrapy.Field()
    building_square_footage = scrapy.Field()
    current_year_assessed_value = scrapy.Field()
    prior_year_assessed_value = scrapy.Field()
    property_use = scrapy.Field()
    residence_type = scrapy.Field()
    units = scrapy.Field()
    construction_type = scrapy.Field()
    full_bathrooms = scrapy.Field()
    half_bathrooms = scrapy.Field()
    basement = scrapy.Field()
    central_air = scrapy.Field()
    garage_type = scrapy.Field()
    home_owner_exemption = scrapy.Field()
    senior_citizen_exemption = scrapy.Field()

    taxes_sold = scrapy.Field()
    tax_paid_year0 = scrapy.Field()
    tax_paid_year1 = scrapy.Field()
    tax_paid_year0_amount = scrapy.Field()
    tax_paid_year1_amount = scrapy.Field()
    doc1_string = scrapy.Field()
    doc2_string = scrapy.Field()
    doc3_string = scrapy.Field()
    doc4_string = scrapy.Field()
    doc5_string = scrapy.Field()
    doc1_date = scrapy.Field()
    doc2_date = scrapy.Field()
    doc3_date = scrapy.Field()
    doc4_date = scrapy.Field()
    doc5_date = scrapy.Field()


class MaricopaCountyDescriptionItem(scrapy.Item):
    parcel = scrapy.Field()
    owner_name = scrapy.Field()
    owner_first = scrapy.Field()
    owner_last = scrapy.Field()
    owner_full_address = scrapy.Field()
    owner_street_address1 = scrapy.Field()
    owner_city = scrapy.Field()
    owner_state = scrapy.Field()
    owner_zip = scrapy.Field()
    full_property_address = scrapy.Field()
    site_street = scrapy.Field()
    site_city = scrapy.Field()
    site_zip = scrapy.Field()
    property_description = scrapy.Field()
    lot_size = scrapy.Field()
    property_type = scrapy.Field()
    rental = scrapy.Field()
    value_0 = scrapy.Field()
    value_1 = scrapy.Field()
    value_2 = scrapy.Field()
    last_deed_date = scrapy.Field()
    last_sale_price = scrapy.Field()



