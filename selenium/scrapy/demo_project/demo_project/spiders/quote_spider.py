import scrapy


class QuoteSpiderSpider(scrapy.Spider):
    name = "quote_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        yield {'response':response}
