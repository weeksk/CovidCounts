import scrapy
from scrapy.loader import ItemLoader
from ..items import CoviddataItem
from lxml.builder import unicode

from ..items import CoviddataItem


class WikipediaSpiderSpider(scrapy.Spider):
    name = 'wikipedia_spider'
    start_urls = [
        'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'
    ]

    def parse(self, response):


        items = CoviddataItem()

        covid_locations = response.css('#thetable i a , #thetable th > a').css('::text').extract()
        covid_cases = response.css('#thetable th+ td').css('::text').extract()
        covid_deaths = response.css('#thetable td:nth-child(4)').css('::text').extract()
        covid_recoveries = response.css('#thetable td:nth-child(5)').css('::text').extract()
        # covid_reference_links = response.css(
        #     '#thetable td:nth-child(6) , #cite_ref-24 a , #cite_ref-\:1p3a_19-0 a').css('::attr(href)').extract()

        covid_cases_test = []
        covid_deaths_test = []
        covid_recoveries_test = []
        for item in covid_cases:
            covid_cases_test.append(item[:-1])
        for item in covid_deaths:
            covid_deaths_test.append(item[:-1])
        for item in covid_recoveries:
            covid_recoveries_test.append(item[:-1])





        items['covid_locations'] = covid_locations
        items['covid_cases_test'] = covid_cases_test
        items['covid_deaths_test'] = covid_deaths_test
        items['covid_recoveries_test'] = covid_recoveries_test
        # items['covid_reference_links'] = covid_reference_links

        yield items



