# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

class PaowangSpider(scrapy.Spider):
    name = 'paowang'
    allowed_domains = ['jcodecraeer.com']
    start_urls = ['http://www.jcodecraeer.com/plus/list.php?tid=31']

    visited_set = set()

    def parse(self, response):
        self.visited_set.add(response.url)
        hxs = HtmlXPathSelector(response)
        item_list = hxs.select('//li[@class="codeli"]')
        for item in item_list:
            price_text_list = item.select('.//div[@class="codeli-photo"]/a/img/@src').extract()
            for price_text in price_text_list:
                print(price_text)
