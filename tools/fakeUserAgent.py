#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File         : fakeUserAgent.py
# @Date         : 13-04-2021
# @Software     : PyCharm
# @Author       : Payne
# @Email        : wuzhipeng1289690157@gmail.com

from random import choice

systemMark = [
    'Macintosh; Intel Mac OS X 10_10',
    'Windows NT 10.0',
    'Windows NT 5.1',
    'Windows NT 6.1; WOW64',
    'Windows NT 6.1; Win64; x64',
    'X11; Linux x86_64',
]
firefoxVersions = [
    35.0,
    40.0,
    41.0,
    44.0,
    45.0,
    48.0,
    48.0,
    49.0,
    50.0,
    52.0,
    52.0,
    53.0,
    54.0,
    56.0,
    57.0,
    57.0,
    58.0,
    58.0,
    59.0,
    6.0,
    60.0,
    61.0,
    63.0,
]
chromeVersions = [
    '37.0.2062.124',
    '40.0.2214.93',
    '41.0.2228.0',
    '49.0.2623.112',
    '55.0.2883.87',
    '56.0.2924.87',
    '57.0.2987.133',
    '61.0.3163.100',
    '63.0.3239.132',
    '64.0.3282.0',
    '65.0.3325.146',
    '68.0.3440.106',
    '69.0.3497.100',
    '70.0.3538.102',
    '74.0.3729.169',
]
operaVersions = [
    '2.7.62 Version / 11.00',
    '2.2.15 Version / 10.10',
    '2.9.168 Version / 11.50',
    '2.2.15 Version / 10.00',
    '2.8.131 Version / 11.11',
    '2.5.24 Version / 10.54',
]


def fakeUserAgent():
    """
    constructionChromeUA
    :return: str
    """
    randomSystemMark = choice(systemMark)
    return choice([
        f"Mozilla/5.0 ({randomSystemMark}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{choice(chromeVersions)} Safari/537.36",
        f"Opera/9.80 ({randomSystemMark}; U; en) Presto{choice(operaVersions)}",
        f"Mozilla/5.0 ({randomSystemMark}; rv:{choice(firefoxVersions)}) Gecko/20100101 Firefox/{choice(firefoxVersions)}"
    ])


if __name__ == '__main__':
    for _ in range(100):
        print(fakeUserAgent())
