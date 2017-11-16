# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from builtins import print


class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-0.html']

    visited_set = set()

    def parse(self, response):
        self.visited_set.add(response.url)
        hxs = HtmlXPathSelector(response)
        # 'http://www.xiaohuar.com/list-1-\d+.html'
        # class ="item masonry_brick masonry-brick"
        item_list = hxs.select('//div[@class="item masonry_brick"]')
        for item in item_list:
            price_text_list = item.select('.//span[@class="price"]/text()').extract()
            for price_text in price_text_list:
                print(price_text)
        # <a href = "http://www.xiaohuar.com/list-1-1.html" >
        # hxs.select('//a[@href="http://www.xiaohuar.com/list-1-1.html"]')
        page_list = hxs.select('//a[re:test(@href,"http://www.xiaohuar.com/list-1-\d+.html")]/@href').extract()
        for url in page_list:
            if url in self.visited_set:
                pass
            else:
                page = Request(url=url, method="GET", callback=self.parse)
                yield page;
