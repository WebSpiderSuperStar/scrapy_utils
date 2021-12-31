# scrapy_utils

scrapy_utils is configuration template project, Contains the extraction of scrapy configuration

## requirements

python >= 3.6

## TODO

> contains the following functions

- [x] RANDOM USER-AGENT

- [x] PROXY DOCKING

- [x] CHAOTIC TLS FINGERPRINT

- [x] Conveniently configured log

- [x] Common database connection

- [x] Distributed configuration

## Note

Can't change all the time ja3_hash

**Normal Situation**

```text
2021-12-31 13:52:50 [scrapy] INFO: Spider opened
2021-12-31 13:52:51 [scrapy] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2021-12-31 13:52:51 [ja3] INFO: Spider opened: ja3
2021-12-31 13:52:53 [scrapy] DEBUG: Crawled (200) <GET https://ja3er.com/json> (referer: None)
2021-12-31 13:52:53 [ja3] INFO: {'ja3_hash': 'e6dff86c9a58dce9116eda911d246f0a', 'ja3': '771,4866-4867-4865-52394-49196-49200-49195-49199-49327-49325-49188-49192-49162-49172-157-49313-49309-156-49312-49308-61-60-53-47-52393-52392-159-49315-49311-158-49314-49310-107-103-57-51-49326-49324-49187-49191-49161-49171-255,0-11-10-22-23-13-43-45-51-21,29-23-1035-25-24,0-1-2', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
2021-12-31 13:52:54 [scrapy] DEBUG: Crawled (200) <GET https://ja3er.com/json> (referer: None)
2021-12-31 13:52:54 [ja3] INFO: {'ja3_hash': 'd1192bf72abf7d674238d296b2c61f4f', 'ja3': '771,4866-4867-4865-159-49315-49311-158-49314-49310-107-103-57-51-157-156-49196-49200-49327-49325-49188-49192-49162-49172-52393-52392-49195-49199-49326-49324-49187-49191-49161-49171-49313-49309-49312-49308-61-60-53-47-52394-255,0-11-10-22-23-13-43-45-51-21,29-23-1035-25-24,0-1-2', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
2021-12-31 13:52:56 [scrapy] DEBUG: Crawled (200) <GET https://ja3er.com/json> (referer: None)
2021-12-31 13:52:56 [ja3] INFO: {'ja3_hash': 'e6dff86c9a58dce9116eda911d246f0a', 'ja3': '771,4866-4867-4865-52394-49196-49200-49195-49199-49327-49325-49188-49192-49162-49172-157-49313-49309-156-49312-49308-61-60-53-47-52393-52392-159-49315-49311-158-49314-49310-107-103-57-51-49326-49324-49187-49191-49161-49171-255,0-11-10-22-23-13-43-45-51-21,29-23-1035-25-24,0-1-2', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
2021-12-31 13:52:58 [scrapy] DEBUG: Crawled (200) <GET https://ja3er.com/json> (referer: None)
2021-12-31 13:52:58 [ja3] INFO: {'ja3_hash': 'd1192bf72abf7d674238d296b2c61f4f', 'ja3': '771,4866-4867-4865-159-49315-49311-158-49314-49310-107-103-57-51-157-156-49196-49200-49327-49325-49188-49192-49162-49172-52393-52392-49195-49199-49326-49324-49187-49191-49161-49171-49313-49309-49312-49308-61-60-53-47-52394-255,0-11-10-22-23-13-43-45-51-21,29-23-1035-25-24,0-1-2', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'}
2021-12-31 13:53:01 [scrapy] DEBUG: Crawled (200) <GET https://ja3er.com/json> (referer: None)
2021-12-31 13:53:01 [ja3] INFO: {'ja3_hash': 'e6dff86c9a58dce9116eda911d246f0a', 'ja3': '771,4866-4867-4865-52394-49196-49200-49195-49199-49327-49325-49188-49192-49162-49172-157-49313-49309-156-49312-49308-61-60-53-47-52393-52392-159-49315-49311-158-49314-49310-107-103-57-51-49326-49324-49187-49191-49161-49171-255,0-11-10-22-23-13-43-45-51-21,29-23-1035-25-24,0-1-2', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
2021-12-31 13:53:01 [scrapy] INFO: Closing spider (finished)

```

> now, I have found can you use new terminal to change it,Please clean you ``pycache``,
>
> use `find . -type f -name "*.pyc" -delete && find . -type d -name "__pycache__" -delete`