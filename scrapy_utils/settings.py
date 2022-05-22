# Scrapy settings for scrapy_utils project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import datetime
import random
from os.path import dirname, abspath, join, exists
from fake_headers import Headers
from environs import Env
from redis import StrictRedis

today = datetime.datetime.now()

ROOT_DIR = dirname(dirname(abspath(__file__)))

# Environment configuration
env = Env()
env.read_env()
LOG_DIR = join(ROOT_DIR, env.str("LOG_DIR", "Logs"))
DEV_MODE, TEST_MODE, PROD_MODE = "dev", "test", "prod"
APP_ENV = env.str("APP_ENV", DEV_MODE).lower()
APP_DEBUG = env.bool("APP_DEBUG", APP_ENV == DEV_MODE)
APP_DEV = IS_DEV = APP_ENV == DEV_MODE
APP_PROD = IS_PROD = APP_ENV == PROD_MODE
APP_TEST = IS_TEST = APP_ENV == TEST_MODE

BOT_NAME = "scrapy_utils"

SPIDER_MODULES = ["scrapy_utils.spiders"]
NEWSPIDER_MODULE = "scrapy_utils.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapy_utils (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = env.int("CONCURRENT_REQUESTS", 16)

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = random.uniform(0, 3)
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = env.int("CONCURRENT_REQUESTS_PER_DOMAIN", 60)
CONCURRENT_REQUESTS_PER_IP = env.int("CONCURRENT_REQUESTS_PER_IP", 60)

REACTOR_THREADPOOL_MAXSIZE = env.int("REACTOR_THREADPOOL_MAXSIZE", 30)

# Disable cookies (enabled by default)
COOKIES_ENABLED = env.bool("COOKIES_ENABLED", True)

# disable retry (enabled by default)
RETRY_ENABLED = env.bool("RETRY_ENABLED", True)

# Configure timeout
DOWNLOAD_TIMEOUT = env.int("DOWNLOAD_TIMEOUT", 30)

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = Headers(headers=True).generate()

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapy_utils.middlewares.ScrapyUtilsSpiderMiddleware': 543,
    # 'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "scrapy_utils.middlewares.ScrapyUtilsDownloaderMiddleware": 543,
    # "scrapy_utils.middlewares.RandomUserAgentMiddleware": 400,
    # 'scrapy_utils.middlewares.MyHttpProxyMiddleware': 750,
    # 'scrapy_splash.SplashCookiesMiddleware': 723,
    # 'scrapy_splash.SplashMiddleware': 725,
    # 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'scrapy_utils.pipelines.ScrapyUtilsPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# The cipher of the docking agent
proxyAuth = env.list("proxyAuth", [])
# @Custom handlers
DOWNLOAD_HANDLERS = {
    "http": "scrapy_utils.handler.HTTPDownloadHandler11",
    "https": "scrapy_utils.handler.HTTPDownloadHandler11",
}

LOG_LEVEL_MAP = {DEV_MODE: "DEBUG", TEST_MODE: "INFO", PROD_MODE: "ERROR"}

# LOGGING Configuration
None if exists(LOG_DIR) else os.mkdir(LOG_DIR)
LOG_ENABLED = env.bool("LOG_ENABLED", True)
LOG_ENCODING = "utf-8"
LOG_FORMATTER = "scrapy.logformatter.LogFormatter"
LOG_FORMAT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"
LOG_LEVEL = LOG_LEVEL_MAP.get(APP_ENV)
LOG_SHORT_NAMES = env.bool("LOG_SHORT_NAMES", True)
LOG_FILE_ENABLED = env.bool('LOG_FILE_ENABLED', False)
LOG_FILE = f"{LOG_DIR}/{today.year}-{today.month}-{today.day}.log" if LOG_FILE_ENABLED else None

# Database link

# @MySQL
MYSQL_PORT = env.int("MYSQL_PORT", 3306)
MYSQL_CHARSET = "utf8mb4"
MYSQL_HOST = env.str("MYSQL_HOST", "127.0.0.1")
MYSQL_DATABASE = env.str("MYSQL_DATABASE", None)
MYSQL_USER = env.str("MYSQL_USER", "root")
MYSQL_PASSWORD = env.str("MYSQL_PASSWORD", "123456")
MYSQL_CONN_MAX = env.int("MYSQL_ConnectionPool_MAX", 16)

# @MongoDB
MONGO_USER = env.str("AUTH_DB", "admin")
MONGO_PASSWORD = env.str("MONGO_PASSWORD", "admin")
AUTH_DB = env.str("AUTH_DB", "admin")
MONGO_HOST = env.str("MONGO_HOST", "127.0.0.1")
MONGO_PORT = env.int("MYSQL_PORT", 27017)
MONGO_DB = env.str("MONGO_DB", "test")
MONGO_COL = env.str("MONGO_COL", "test")

# MONGO_URI=f"mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]"
MONGO_URI = (
    f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}/{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
)

# @REDIS

# # Distributed configuration
# redis host
REDIS_HOST = env.str("REDIS_HOST", "127.0.0.1")
# redis port
REDIS_PORT = env.int("REDIS_PORT", 6379)
# redis password, if no password, set it to None
REDIS_PASSWORD = env.str("REDIS_PASSWORD", None)
# redis db, if no choice, set it to 0
REDIS_DB = env.int("REDIS_DB", 0)
# redis connection string, like
# redis://[password]@host:port or redis://[password]@host:port/0,
REDIS_CONNECTION_STRING = env.str(
    "REDIS_CONNECTION_STRING", "redis://default:passwd@127.0.0.1:6379/0"
)
#
# # scrapy_redis Distributed configuration
# """
# Settings
# --------
# SCHEDULER_PERSIST : bool (default: False)
#     Whether to persist or clear redis queue.
# SCHEDULER_FLUSH_ON_START : bool (default: False)
#     Whether to flush redis queue on start.
# SCHEDULER_IDLE_BEFORE_CLOSE : int (default: 0)
#     How many seconds to wait before closing if no message is received.
# SCHEDULER_QUEUE_KEY : str
#     Scheduler redis key.
# SCHEDULER_QUEUE_CLASS : str
#     Scheduler queue class.
# SCHEDULER_DUPEFILTER_KEY : str
#     Scheduler dupefilter redis key.
# SCHEDULER_DUPEFILTER_CLASS : str
#     Scheduler dupefilter class.
# SCHEDULER_SERIALIZER : str
#     Scheduler serializer.
# """
#
# REDIS_URL = REDIS_CONNECTION_STRING
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# REDIS_START_URLS_AS_SET = True
# # Whether to clear the queue after crawling（default: True）
# SCHEDULER_PERSIST = True
#
# # SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# # SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'
#
# SCHEDULER_FLUSH_ON_START = False
#
# STATS_CLASS = "scrapy_redis.stats.RedisStatsCollector"
#
# # FILTER
# # DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
# BLOOMFILTER_HASH_NUMBER = 6
# BLOOMFILTER_BIT = 30


# SPLASH_URL = 'http://localhost:8050'
#
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
