import scrapy


class TiOsuSpider(scrapy.Spider):
    name = "TI-OSU"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://www.reddit.com/r/cybersecurity/"]

    def parse(self, response):
        pass
