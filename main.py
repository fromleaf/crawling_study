# -*- coding: utf-8 -*-

from crawling import collect

if __name__ == '__main__':
    # collect.by_requests('http://fromleaf.tistory.com')
    # collect.by_robobrowser('http://fromleaf.tistory.com')
    # collect.by_feedparser()
    collect.get_news_by_feedparser(
        'http://imnews.imbc.com/news/2016/politic/article/4155019_19803.html'
    )