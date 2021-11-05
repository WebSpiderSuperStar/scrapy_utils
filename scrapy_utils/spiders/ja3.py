import scrapy


class Ja3Spider(scrapy.Spider):
    name = 'ja3'
    start_urls = ['https://ja3er.com/json']

    def start_requests(self):
        for _ in range(5):
            yield scrapy.Request(url=self.start_urls[0], dont_filter=True)

    def parse(self, response, **kwargs):
        self.logger.info(response.json())
