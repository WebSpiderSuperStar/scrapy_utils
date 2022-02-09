from scrapy.cmdline import execute


def sign():
    execute(["scrapy", "crawl", "ja3"])


if __name__ == "__main__":
    sign()
