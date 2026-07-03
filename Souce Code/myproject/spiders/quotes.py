import scrapy
from myproject.items import MyprojectItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for sel in response.css("div.quote"):
            item = MyprojectItem(
                title=sel.css("span.text::text").get(),
                price=None,
                url=response.url
        
            yield item

        next_page = response.css("li.next > a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
