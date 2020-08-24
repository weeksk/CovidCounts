# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst
from lxml.builder import unicode


class CoviddataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    covid_locations = scrapy.Field()
    covid_cases = scrapy.Field()
    covid_deaths = scrapy.Field()
    covid_recoveries = scrapy.Field()
    covid_reference_links = scrapy.Field()

# class ScrapingTestingLoader(ItemLoader):
#     default_input_processor = MapCompose(unicode.strip)
#     default_output_processor = TakeFirst()
