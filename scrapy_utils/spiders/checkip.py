import scrapy

class CheckipSpider(scrapy.Spider):
    name = 'checkip'
    start_urls = [
        'http://checkip.amazonaws.com/',
        'https://cip.cc'
        'http://members.3322.org/dyndns/getip',
        'https://myip.ipip.net/',

    ]

    def start_requests(self):
        for _ in range(5):
            yield scrapy.Request(
                url=self.start_urls[-1],
                callback=self.parse,
                dont_filter=True
            )

    def parse(self, response, **kwargs):
        self.logger.info(response.text.strip())
