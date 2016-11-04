# -*- coding: utf-8 -*-

import requests


def get_data_by_requests():
    url = 'http://fromleaf.tistory.com'
    result = requests.post(url)
    html = result.text

    print(html)


