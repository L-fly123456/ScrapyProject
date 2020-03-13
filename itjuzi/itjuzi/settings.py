# -*- coding: utf-8 -*-

# Scrapy settings for itjuzi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'itjuzi'

# 去重类
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 持久化
SCHEDULER_PERSIST = True
REDIS_URL = "redis://127.0.0.1:6379"

SPIDER_MODULES = ['itjuzi.spiders']
NEWSPIDER_MODULE = 'itjuzi.spiders'
PROXY_URL = 'http://127.0.0.1:5000/random'
MAX_PAGE = 5
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
COOKIES = '_ga=GA1.2.1103201819.1583820115; _gid=GA1.2.970505371.1583820115; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1583820116,1583902199,1583929249; _gat_gtag_UA_59006131_1=1; juzi_user=819485; juzi_token=bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1ODM5Mzg2MjEsImV4cCI6MTU4Mzk0MjIyMSwibmJmIjoxNTgzOTM4NjIxLCJqdGkiOiIzOGI5Ujd1R3VmYnM4M29TIiwic3ViIjo4MTk0ODUsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoieG5xNnNIIn0.3qF0STRm5xeX4Ew4VHhwHhNOG_4JuezuXjGxy5ya2Q8; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1583938637'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
MONGO_URI = 'localhost'
MONGO_DB = 'ITjuzi'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://www.itjuzi.com/unicorn',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvdXNlcnNcL3VzZXJfaGVhZGVyX2luZm8iLCJpYXQiOjE1ODM5Mzg2MjEsImV4cCI6MTU4NDAyMTE1MiwibmJmIjoxNTg0MDE3NTUyLCJqdGkiOiJhTkJTNnltbElhckF0WEtJIiwic3ViIjo4MTk0ODUsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoieG5xNnNIIn0.wTtwgQueR3Qs9Ic3L6_Udl86spT5r4PSEOxuslbaL3g',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'itjuzi.middlewares.ItjuziSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'itjuzi.middlewares.ProxyMiddleware':1,
   # 'itjuzi.middlewares.ItjuziDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'itjuzi.pipelines.ITjuziPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
