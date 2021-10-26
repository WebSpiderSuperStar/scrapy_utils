# -*- coding: utf-8 -*-
import random
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory
from scrapy.core.downloader.handlers.http import HTTPDownloadHandler
ORIGIN_CIPHERS = 'TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:RSA+AESGCM:RSA+AES'


def shuffle_ciphers():
    ciphers = ORIGIN_CIPHERS.split(":")
    random.shuffle(ciphers)
    ciphers = ":".join(ciphers)
    return ciphers + ":!aNULL:!MD5:!DSS"


class HTTPDownloadHandler11(HTTPDownloadHandler):
    def download_request(self, request, spider):
        tls_cipher = shuffle_ciphers()
        self._contextFactory = ScrapyClientContextFactory(tls_ciphers=tls_cipher)
        return super().download_request(request, spider)
