import scrapy


class TiOsuSpider(scrapy.Spider):
    name = "TI-OSU"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://www.reddit.com/r/cybersecurity/comments/r0hmkc/zeroday_windows_vulnerability_enables_threat/"]

    def parse(self, response):
        pass
