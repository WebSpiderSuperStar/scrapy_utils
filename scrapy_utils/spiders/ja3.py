import scrapy


class Ja3Spider(scrapy.Spider):
    name = "ja3"
    start_urls = ["https://ja3er.com/json"]

    def start_requests(self):
        """start request
        :return:
        """
        # for _ in range(5):
        #     yield scrapy.Request(url=self.start_urls[0], dont_filter=True)
        yield from [
            scrapy.Request(url=self.start_urls[0], dont_filter=True) for _ in range(10)
        ]

    def parse(self, response, **kwargs):
        """parse response
        :param response:
        :param kwargs:
        :return:
        """
        self.logger.info(response.json())
